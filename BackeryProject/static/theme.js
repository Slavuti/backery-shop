// theme.js — Unified theme switcher for 3 themes
(function() {
  const STORAGE_KEY = 'maison-brulee-theme';
  const THEMES = ['theme-cream', 'theme-dark', 'theme-terracotta'];

  function getCurrentTheme() {
    const bodyClass = document.body.className;
    for (let theme of THEMES) {
      if (bodyClass.includes(theme)) return theme;
    }
    return 'theme-cream';
  }

  function setActiveButton(theme) {
    const btns = document.querySelectorAll('.theme-btn');
    btns.forEach(btn => {
      const btnTheme = btn.getAttribute('data-theme');
      if (btnTheme === theme) {
        btn.classList.add('active');
      } else {
        btn.classList.remove('active');
      }
    });
  }

  function applyTheme(theme) {
    // remove any existing theme class
    THEMES.forEach(t => {
      document.body.classList.remove(t);
    });
    document.body.classList.add(theme);
    localStorage.setItem(STORAGE_KEY, theme);
    setActiveButton(theme);
  }

  function initTheme() {
    const savedTheme = localStorage.getItem(STORAGE_KEY);
    let initialTheme = 'theme-cream';
    if (savedTheme && THEMES.includes(savedTheme)) {
      initialTheme = savedTheme;
    }
    applyTheme(initialTheme);

    // attach event listeners to theme buttons (delegation)
    document.addEventListener('click', (e) => {
      const btn = e.target.closest('.theme-btn');
      if (!btn) return;
      const theme = btn.getAttribute('data-theme');
      if (theme && THEMES.includes(theme)) {
        applyTheme(theme);
      }
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initTheme);
  } else {
    initTheme();
  }
})();