'use strict';

/* ─── Smooth scroll for anchor links ─────────────────────────────────────── */
document.addEventListener('click', function (e) {
  const link = e.target.closest('a[href^="#"]');
  if (!link) return;
  const target = document.querySelector(link.getAttribute('href'));
  if (!target) return;
  e.preventDefault();
  target.scrollIntoView({ behavior: 'smooth', block: 'start' });
});

/* ─── Modal ───────────────────────────────────────────────────────────────── */
(function () {
  var dialog = document.getElementById('modal-dialog');
  var closeBtn = document.getElementById('modal-close');
  var modalBody = document.getElementById('modal-body');
  if (!dialog || !closeBtn) return;

  function openModal() {
    if (!dialog.open) dialog.showModal();
  }

  function closeModal() {
    dialog.close();
    if (modalBody) modalBody.innerHTML = '';
    document.querySelectorAll('.btn--active').forEach(function (btn) {
      btn.classList.remove('btn--active');
    });
  }

  closeBtn.addEventListener('click', closeModal);

  dialog.addEventListener('click', function (e) {
    if (e.target === dialog) closeModal();
  });

  document.body.addEventListener('htmx:afterSwap', function (e) {
    if (e.detail.target.id === 'modal-body') openModal();
  });
}());

/* ─── Mobile nav hamburger ────────────────────────────────────────────────── */
(function () {
  var burger = document.getElementById('header-burger');
  var nav = document.getElementById('header-nav');
  if (!burger || !nav) return;

  burger.addEventListener('click', function () {
    var isOpen = nav.classList.toggle('nav--open');
    burger.setAttribute('aria-expanded', String(isOpen));
    burger.setAttribute('aria-label', isOpen ? 'Закрити меню' : 'Відкрити меню');
  });

  nav.addEventListener('click', function (e) {
    if (!e.target.classList.contains('nav-link')) return;
    nav.classList.remove('nav--open');
    burger.setAttribute('aria-expanded', 'false');
    burger.setAttribute('aria-label', 'Відкрити меню');
  });

  document.addEventListener('click', function (e) {
    if (burger.contains(e.target) || nav.contains(e.target)) return;
    nav.classList.remove('nav--open');
    burger.setAttribute('aria-expanded', 'false');
  });
}());

/* ─── Gallery lightbox ────────────────────────────────────────────────────── */
(function () {
  var lightbox   = document.getElementById('gallery-lightbox');
  var closeBtn   = document.getElementById('lightbox-close');
  var lbImg      = document.getElementById('lightbox-img');
  var lbCaption  = document.getElementById('lightbox-caption');
  if (!lightbox || !lbImg) return;

  function openLightbox(src, caption, alt) {
    lbImg.src = src;
    lbImg.alt = alt || caption || '';
    lbCaption.textContent = caption || '';
    lightbox.showModal();
  }

  function closeLightbox() {
    lightbox.close();
    lbImg.src = '';
  }

  closeBtn.addEventListener('click', closeLightbox);

  lightbox.addEventListener('click', function (e) {
    if (e.target === lightbox) closeLightbox();
  });

  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && lightbox.open) closeLightbox();
  });

  document.addEventListener('click', function (e) {
    var item = e.target.closest('.gallery-item[data-src]');
    if (!item) return;
    openLightbox(
      item.dataset.src,
      item.dataset.caption,
      item.querySelector('img') ? item.querySelector('img').alt : ''
    );
  });

  document.addEventListener('keydown', function (e) {
    if (e.key !== 'Enter' && e.key !== ' ') return;
    var item = e.target.closest('.gallery-item[data-src]');
    if (!item) return;
    e.preventDefault();
    openLightbox(
      item.dataset.src,
      item.dataset.caption,
      item.querySelector('img') ? item.querySelector('img').alt : ''
    );
  });
}());

/* ─── Active nav link via IntersectionObserver ───────────────────────────── */
(function () {
  var sections = document.querySelectorAll('#about, #products, #gallery, #contacts');
  var navLinks = document.querySelectorAll('.header-nav .nav-link');
  if (!sections.length || !navLinks.length) return;

  var observer = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (!entry.isIntersecting) return;
      var targetHref = '#' + entry.target.id;
      navLinks.forEach(function (link) {
        link.classList.toggle('nav-link--active', link.getAttribute('href') === targetHref);
      });
    });
  }, { rootMargin: '-25% 0px -65% 0px', threshold: 0 });

  sections.forEach(function (section) { observer.observe(section); });
}());
