/**
 * Portfolio — main.js
 * Handles: mobile nav, nav scroll state, reveal-on-scroll animations.
 */

(function () {
    'use strict';

    // ---------------------------------------------
    // 1. Mobile nav toggle
    // ---------------------------------------------
    const navToggle = document.getElementById('navToggle');
    const navLinks = document.getElementById('navLinks');

    if (navToggle && navLinks) {
        navToggle.addEventListener('click', function () {
            navToggle.classList.toggle('active');
            navLinks.classList.toggle('open');
        });

        // Close menu when a link is clicked
        navLinks.querySelectorAll('a').forEach(function (link) {
            link.addEventListener('click', function () {
                navToggle.classList.remove('active');
                navLinks.classList.remove('open');
            });
        });
    }

    // ---------------------------------------------
    // 2. Nav background on scroll
    // ---------------------------------------------
    const nav = document.getElementById('mainNav');

    function updateNav() {
        if (!nav) return;
        if (window.scrollY > 20) {
            nav.classList.add('scrolled');
        } else {
            nav.classList.remove('scrolled');
        }
    }

    window.addEventListener('scroll', updateNav, { passive: true });
    updateNav();

    // ---------------------------------------------
    // 3. Reveal on scroll
    // ---------------------------------------------
    const revealTargets = document.querySelectorAll(
        '.section, .preview-card, .stat-card, .service-card, .project-card, .skills-category, .info-card, .contact-form'
    );

    revealTargets.forEach(function (el) {
        el.classList.add('reveal');
    });

    if ('IntersectionObserver' in window) {
        const observer = new IntersectionObserver(
            function (entries) {
                entries.forEach(function (entry) {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('visible');
                        observer.unobserve(entry.target);
                    }
                });
            },
            { threshold: 0.12, rootMargin: '0px 0px -40px 0px' }
        );

        revealTargets.forEach(function (el) {
            observer.observe(el);
        });
    } else {
        // Fallback for very old browsers
        revealTargets.forEach(function (el) {
            el.classList.add('visible');
        });
    }

    // ---------------------------------------------
    // 4. Profile Picture Lightbox Popup
    // ---------------------------------------------
    const lightbox = document.getElementById('profileLightbox');
    const lightboxBackdrop = document.getElementById('lightboxBackdrop');
    const lightboxClose = document.getElementById('lightboxClose');
    const avatarButtons = document.querySelectorAll('.brand-avatar-btn');

    function openLightbox() {
        if (!lightbox) return;
        lightbox.classList.add('active');
        document.body.style.overflow = 'hidden';
    }

    function closeLightbox() {
        if (!lightbox) return;
        lightbox.classList.remove('active');
        document.body.style.overflow = '';
    }

    avatarButtons.forEach(function (btn) {
        btn.addEventListener('click', function (e) {
            e.preventDefault();
            e.stopPropagation();
            openLightbox();
        });
    });

    if (lightboxBackdrop) {
        lightboxBackdrop.addEventListener('click', closeLightbox);
    }

    if (lightboxClose) {
        lightboxClose.addEventListener('click', closeLightbox);
    }

    document.addEventListener('keydown', function (e) {
        if (e.key === 'Escape' && lightbox && lightbox.classList.contains('active')) {
            closeLightbox();
        }
    });
})();