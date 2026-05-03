// ========== FROST PARTICLES ==========
(function() {
  const particlesContainer = document.getElementById('frostParticles');
  if (particlesContainer) {
    for (let i = 0; i < 25; i++) {
      const particle = document.createElement('div');
      particle.classList.add('particle');
      const size = Math.random() * 8 + 3;
      particle.style.width = size + 'px';
      particle.style.height = size + 'px';
      particle.style.left = Math.random() * 100 + '%';
      particle.style.top = Math.random() * 100 + '%';
      particle.style.animationDuration = (Math.random() * 12 + 10) + 's';
      particle.style.animationDelay = Math.random() * 8 + 's';
      particle.style.opacity = Math.random() * 0.4 + 0.1;
      particlesContainer.appendChild(particle);
    }
  }
})();

// ========== PARALLAX EFFECT ==========
(function() {
  const bgImage = document.querySelector('.bg-image');
  let ticking = false;
  
  window.addEventListener('scroll', () => {
    if (!ticking) {
      window.requestAnimationFrame(() => {
        if (bgImage) {
          const scrollY = window.scrollY || window.pageYOffset;
          const maxScroll = document.documentElement.scrollHeight - window.innerHeight;
          const scrollPercent = Math.min(scrollY / Math.max(maxScroll, 1), 1);
          const offset = scrollPercent * 60;
          bgImage.style.transform = `scale(1.1) translateY(${offset}px)`;
        }
        ticking = false;
      });
      ticking = true;
    }
  }, { passive: true });
})();

// ========== SCROLL REVEAL ==========
(function() {
  const revealCallback = (entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        if (entry.target.classList.contains('project-tile')) {
          const tiles = document.querySelectorAll('.project-tile');
          const index = Array.from(tiles).indexOf(entry.target);
          setTimeout(() => {
            entry.target.classList.add('reveal');
          }, index * 100);
        } else if (entry.target.id === 'projectsLabel') {
          entry.target.classList.add('revealed');
        } else if (entry.target.id === 'footerTile') {
          entry.target.classList.add('reveal');
        }
        observer.unobserve(entry.target);
      }
    });
  };

  const observerOptions = {
    root: null,
    rootMargin: '0px 0px -50px 0px',
    threshold: 0.15
  };

  const observer = new IntersectionObserver(revealCallback, observerOptions);

  document.querySelectorAll('.project-tile').forEach(tile => observer.observe(tile));
  
  const projectsLabel = document.getElementById('projectsLabel');
  if (projectsLabel) observer.observe(projectsLabel);
  
  const footerTile = document.getElementById('footerTile');
  if (footerTile) observer.observe(footerTile);
})();

// ========== SCROLL INDICATOR ==========
(function() {
  const scrollIndicator = document.querySelector('.scroll-indicator');
  if (scrollIndicator) {
    scrollIndicator.addEventListener('click', function(e) {
      e.preventDefault();
      const projectsSection = document.getElementById('projectsSection');
      if (projectsSection) {
        projectsSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  }
})();