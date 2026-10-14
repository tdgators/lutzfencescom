// Builds a seamless hero-banner loop from short clips: each clip plays forward once, clips
// are joined with crossfades, and the end crossfades back into the start so the loop has no
// visible jump. Six 5s clips make a ~28s loop.
//
// Usage: swift tools/hero_loop.swift out.mp4 clipA.mp4 [clipB.mp4 ...]
// Output plays at 0.9x speed, H.264 at the first clip's size (use the 960x540 compressed clips), ~1.0 Mbps, no audio.
import AVFoundation
import CoreImage

let args = CommandLine.arguments
guard args.count >= 3 else { print("usage: hero_loop out.mp4 clip1.mp4 [clip2.mp4 ...]"); exit(1) }
let outURL = URL(fileURLWithPath: args[1])
let clipURLs = args.dropFirst(2).map { URL(fileURLWithPath: $0) }
let fadeFrames = 18  // ~0.8s at 24fps
let speed = 0.9     // play slightly slower: calmer motion, and a longer loop
let ctx = CIContext()

func readFrames(_ url: URL) -> ([CGImage], CMTime, CGSize) {
    let asset = AVURLAsset(url: url)
    let track = asset.tracks(withMediaType: .video)[0]
    let reader = try! AVAssetReader(asset: asset)
    let out = AVAssetReaderTrackOutput(track: track, outputSettings: [kCVPixelBufferPixelFormatTypeKey as String: kCVPixelFormatType_32BGRA])
    reader.add(out)
    reader.startReading()
    var frames: [CGImage] = []
    while let sb = out.copyNextSampleBuffer(), let pb = CMSampleBufferGetImageBuffer(sb) {
        let img = CIImage(cvPixelBuffer: pb)
        frames.append(ctx.createCGImage(img, from: img.extent)!)
    }
    let fps = track.nominalFrameRate > 0 ? track.nominalFrameRate : 24
    return (frames, CMTime(value: 1000, timescale: CMTimeScale(fps * 1000)), track.naturalSize)
}

// Clips can come back in a different aspect (e.g. 21:9 from a wide still). Scale each frame to
// cover the output size and center-crop, so every clip fills the frame.
func cover(_ frames: [CGImage], _ size: CGSize) -> [CGImage] {
    guard let f0 = frames.first, CGFloat(f0.width) != size.width || CGFloat(f0.height) != size.height else { return frames }
    let scale = max(size.width / CGFloat(f0.width), size.height / CGFloat(f0.height))
    let dx = (CGFloat(f0.width) * scale - size.width) / 2, dy = (CGFloat(f0.height) * scale - size.height) / 2
    let t = CGAffineTransform(scaleX: scale, y: scale).concatenating(CGAffineTransform(translationX: -dx, y: -dy))
    return frames.map { ctx.createCGImage(CIImage(cgImage: $0).transformed(by: t), from: CGRect(origin: .zero, size: size))! }
}

func blend(_ a: CGImage, _ b: CGImage, _ t: Double) -> CGImage {
    let f = CIFilter(name: "CIDissolveTransition")!
    f.setValue(CIImage(cgImage: a), forKey: kCIInputImageKey)
    f.setValue(CIImage(cgImage: b), forKey: kCIInputTargetImageKey)
    f.setValue(t, forKey: kCIInputTimeKey)
    let o = f.outputImage!
    return ctx.createCGImage(o, from: CGRect(x: 0, y: 0, width: a.width, height: a.height))!
}

// Join the clips, crossfading each scene change.
var seq: [CGImage] = []
var frameDur = CMTime(value: 1, timescale: 24)
var size = CGSize.zero
for (i, url) in clipURLs.enumerated() {
    let (f, d, s) = readFrames(url)
    if i == 0 { frameDur = CMTimeMultiplyByFloat64(d, multiplier: 1 / speed); size = s }
    let fit = cover(f, size)
    if seq.isEmpty { seq = fit; continue }
    let k = min(fadeFrames, seq.count, fit.count)
    let tail = seq.count - k
    for j in 0..<k { seq[tail + j] = blend(seq[tail + j], fit[j], Double(j + 1) / Double(k + 1)) }
    seq += fit.dropFirst(k)
}
// Close the loop: fade the last frames into the opening frames, then start after them.
let k = min(fadeFrames, seq.count / 4)
let n = seq.count
for j in 0..<k { seq[n - k + j] = blend(seq[n - k + j], seq[j], Double(j + 1) / Double(k + 1)) }
let frames = Array(seq[k...])

try? FileManager.default.removeItem(at: outURL)
let writer = try! AVAssetWriter(outputURL: outURL, fileType: .mp4)
let w = Int(size.width), h = Int(size.height)
let input = AVAssetWriterInput(mediaType: .video, outputSettings: [
    AVVideoCodecKey: AVVideoCodecType.h264, AVVideoWidthKey: w, AVVideoHeightKey: h,
    AVVideoCompressionPropertiesKey: [AVVideoAverageBitRateKey: 1_000_000, AVVideoProfileLevelKey: AVVideoProfileLevelH264HighAutoLevel],
])
let adaptor = AVAssetWriterInputPixelBufferAdaptor(assetWriterInput: input, sourcePixelBufferAttributes: [
    kCVPixelBufferPixelFormatTypeKey as String: kCVPixelFormatType_32BGRA, kCVPixelBufferWidthKey as String: w, kCVPixelBufferHeightKey as String: h,
])
writer.add(input)
writer.shouldOptimizeForNetworkUse = true
writer.startWriting()
writer.startSession(atSourceTime: .zero)
for (i, img) in frames.enumerated() {
    while !input.isReadyForMoreMediaData { usleep(2000) }
    var pb: CVPixelBuffer?
    CVPixelBufferPoolCreatePixelBuffer(nil, adaptor.pixelBufferPool!, &pb)
    ctx.render(CIImage(cgImage: img), to: pb!)
    adaptor.append(pb!, withPresentationTime: CMTimeMultiplyByFloat64(frameDur, multiplier: Float64(i)))
}
input.markAsFinished()
let done = DispatchSemaphore(value: 0)
writer.finishWriting { done.signal() }
done.wait()
print(String(format: "%@: %d frames, %.1fs", outURL.lastPathComponent, frames.count, Double(frames.count) * frameDur.seconds))
