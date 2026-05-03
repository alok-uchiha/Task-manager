// ========== STICKY NAVIGATION ==========
(function() {
  const capsuleNav = document.getElementById('capsuleNav');
  const navLinks = document.querySelectorAll('.nav-links a');
  const sections = document.querySelectorAll('.full-section');
  
  function updateNavOnScroll() {
    if (!capsuleNav) return;
    const scrollY = window.scrollY || window.pageYOffset;
    
    // Shrink effect
    if (scrollY > 80) {
      capsuleNav.classList.add('shrink');
    } else {
      capsuleNav.classList.remove('shrink');
    }

    // Active link detection
    let currentSection = '';
    sections.forEach(section => {
      const sectionTop = section.offsetTop - 250;
      const sectionHeight = section.offsetHeight;
      if (scrollY >= sectionTop && scrollY < sectionTop + sectionHeight) {
        currentSection = section.getAttribute('id');
      }
    });

    navLinks.forEach(link => {
      link.classList.remove('active');
      const href = link.getAttribute('href').substring(1);
      if (href === currentSection) {
        link.classList.add('active');
      }
    });

    if (scrollY < 150) {
      navLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href') === '#heroSection') {
          link.classList.add('active');
        }
      });
    }
  }

  window.addEventListener('scroll', updateNavOnScroll, { passive: true });
  updateNavOnScroll();

  // Smooth scroll
  navLinks.forEach(link => {
    link.addEventListener('click', function(e) {
      e.preventDefault();
      const targetId = this.getAttribute('href').substring(1);
      const targetEl = document.getElementById(targetId);
      if (targetEl) {
        targetEl.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  });
})();