document.addEventListener('DOMContentLoaded', function () {
  // Mobile nav toggle
  var toggle = document.querySelector('.menu-toggle');
  var nav = document.querySelector('.primary-nav');
  var scrim = document.querySelector('.nav-scrim');
  function closeNav() {
    nav && nav.classList.remove('open');
    scrim && scrim.classList.remove('open');
  }
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      nav.classList.toggle('open');
      scrim && scrim.classList.toggle('open');
    });
  }
  scrim && scrim.addEventListener('click', closeNav);

  // Mobile dropdown accordions (tap to open submenu instead of hover)
  document.querySelectorAll('nav.primary-nav > ul > li').forEach(function (li) {
    var link = li.querySelector(':scope > button.nav-toggle');
    if (!link) return;
    link.addEventListener('click', function (e) {
      e.preventDefault();
      li.classList.toggle('open');
    });
  });

  // FAQ accordion
  document.querySelectorAll('.faq-item').forEach(function (item) {
    var q = item.querySelector('.faq-q');
    q && q.addEventListener('click', function () {
      item.classList.toggle('open');
    });
  });
});
