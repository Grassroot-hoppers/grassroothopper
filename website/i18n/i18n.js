(function () {
  var COOKIE = 'lang';
  var DAYS = 365;

  function getCookie(name) {
    var match = document.cookie.match(new RegExp('(^| )' + name + '=([^;]+)'));
    return match ? match[2] : null;
  }

  function setCookie(name, value, days) {
    var expires = new Date(Date.now() + days * 864e5).toUTCString();
    document.cookie = name + '=' + value + '; expires=' + expires + '; path=/; SameSite=Lax';
  }

  function detectFrench() {
    if (navigator.languages) {
      return navigator.languages.some(function (l) { return l.startsWith('fr'); });
    }
    return (navigator.language || '').startsWith('fr');
  }

  function resolveJsonUrl() {
    var scripts = document.querySelectorAll('script[src*="i18n"]');
    var src = scripts[scripts.length - 1].getAttribute('src');
    return src.replace('i18n.js', 'fr.json');
  }

  function applyTranslations(translations) {
    document.querySelectorAll('[data-i18n]').forEach(function (el) {
      var key = el.getAttribute('data-i18n');
      if (translations[key] != null) {
        if (el.tagName === 'INPUT' || el.tagName === 'TEXTAREA') {
          el.placeholder = translations[key];
        } else {
          el.innerHTML = translations[key];
        }
      }
    });
    document.documentElement.lang = 'fr';
    updateToggle('fr');
  }

  function updateToggle(lang) {
    var toggle = document.querySelector('[data-i18n-toggle]');
    if (!toggle) return;
    toggle.textContent = lang === 'fr' ? 'EN' : 'FR';
  }

  function showToast() {
    var toast = document.createElement('div');
    toast.id = 'i18n-toast';
    toast.innerHTML =
      '<span>Ce site est aussi disponible en fran\u00e7ais</span>' +
      '<button id="i18n-accept">Passer en fran\u00e7ais</button>' +
      '<button id="i18n-dismiss">Non merci</button>';

    var s = toast.style;
    s.position = 'fixed';
    s.bottom = '1.5rem';
    s.left = '50%';
    s.transform = 'translateX(-50%)';
    s.background = '#1a1714';
    s.color = '#f5f0e6';
    s.padding = '1rem 1.5rem';
    s.borderRadius = '0.75rem';
    s.display = 'flex';
    s.alignItems = 'center';
    s.gap = '1rem';
    s.zIndex = '9999';
    s.fontFamily = "'DM Sans', sans-serif";
    s.fontSize = '0.95rem';
    s.boxShadow = '0 4px 24px rgba(0,0,0,0.4)';
    s.flexWrap = 'wrap';
    s.justifyContent = 'center';
    s.maxWidth = 'calc(100vw - 2rem)';

    function styleBtn(btn, bg, color) {
      var b = btn.style;
      b.padding = '0.5rem 1.2rem';
      b.border = 'none';
      b.borderRadius = '0.5rem';
      b.cursor = 'pointer';
      b.fontFamily = "'DM Sans', sans-serif";
      b.fontSize = '0.85rem';
      b.fontWeight = '600';
      b.background = bg;
      b.color = color;
    }

    document.body.appendChild(toast);

    var accept = document.getElementById('i18n-accept');
    var dismiss = document.getElementById('i18n-dismiss');
    styleBtn(accept, '#e8a830', '#0f0e0c');
    styleBtn(dismiss, 'transparent', '#7a756c');
    dismiss.style.border = '1px solid #7a756c';

    accept.addEventListener('click', function () {
      setCookie(COOKIE, 'fr', DAYS);
      toast.remove();
      loadAndApply();
    });

    dismiss.addEventListener('click', function () {
      setCookie(COOKIE, 'en', DAYS);
      toast.remove();
    });
  }

  function loadAndApply() {
    var url = resolveJsonUrl();
    fetch(url)
      .then(function (r) { return r.json(); })
      .then(applyTranslations)
      .catch(function (e) { console.warn('i18n: could not load translations', e); });
  }

  function setupToggle() {
    var toggle = document.querySelector('[data-i18n-toggle]');
    if (!toggle) return;
    toggle.addEventListener('click', function (e) {
      e.preventDefault();
      var current = getCookie(COOKIE) || 'en';
      if (current === 'fr') {
        setCookie(COOKIE, 'en', DAYS);
        window.location.reload();
      } else {
        setCookie(COOKIE, 'fr', DAYS);
        loadAndApply();
      }
    });
  }

  function init() {
    var saved = getCookie(COOKIE);
    if (saved === 'fr') {
      loadAndApply();
    } else if (!saved && detectFrench()) {
      showToast();
    }
    setupToggle();
    updateToggle(getCookie(COOKIE) || 'en');
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
