/**
 * Cookie Consent — ExpansionVideos
 * GDPR-friendly consent manager for expansionvideos.com
 * GA4: G-X9ZQR20QNZ (loaded only after analytics consent)
 */
(function () {
  'use strict';

  var STORAGE_KEY = 'ev_cookie_consent';
  var GA_ID = 'G-X9ZQR20QNZ';

  function getPrefs() {
    try {
      var raw = localStorage.getItem(STORAGE_KEY);
      return raw ? JSON.parse(raw) : null;
    } catch (e) { return null; }
  }

  function savePrefs(prefs) {
    try { localStorage.setItem(STORAGE_KEY, JSON.stringify(prefs)); } catch (e) {}
  }

  function loadGA() {
    if (window.__gaLoaded) return;
    window.__gaLoaded = true;
    window.dataLayer = window.dataLayer || [];
    window.gtag = function () { window.dataLayer.push(arguments); };
    window.gtag('js', new Date());
    window.gtag('config', GA_ID);
    var g = document.createElement('script');
    g.async = true;
    g.src = 'https://www.googletagmanager.com/gtag/js?id=' + GA_ID;
    var f = document.getElementsByTagName('script')[0];
    f.parentNode.insertBefore(g, f);
  }

  function applyPrefs(prefs) {
    if (prefs.analytics) loadGA();
  }

  var existing = getPrefs();
  if (existing && existing.decided) { applyPrefs(existing); return; }

  var styles = [
    '#ev-cc-banner{position:fixed;bottom:0;left:0;right:0;z-index:99999;background:rgba(15,23,42,0.97);border-top:1px solid rgba(255,255,255,0.08);padding:20px 24px;display:flex;align-items:center;flex-wrap:wrap;gap:16px;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;font-size:14px;color:#cbd5e1;line-height:1.5;}',
    '#ev-cc-banner a{color:#60a5fa;text-decoration:none;}',
    '#ev-cc-banner a:hover{text-decoration:underline;}',
    '#ev-cc-text{flex:1;min-width:200px;}',
    '#ev-cc-btns{display:flex;gap:10px;flex-shrink:0;}',
    '#ev-cc-accept{background:#2563eb;color:#fff;border:none;border-radius:6px;padding:10px 22px;font-size:14px;font-weight:700;cursor:pointer;}',
    '#ev-cc-accept:hover{background:#1d4ed8;}',
    '#ev-cc-reject{background:transparent;color:#cbd5e1;border:1px solid rgba(255,255,255,0.25);border-radius:6px;padding:10px 18px;font-size:14px;cursor:pointer;}',
    '#ev-cc-reject:hover{border-color:#fff;color:#fff;}'
  ].join('\n');
  var styleEl = document.createElement('style');
  styleEl.textContent = styles;
  document.head.appendChild(styleEl);

  var banner = document.createElement('div');
  banner.id = 'ev-cc-banner';
  banner.innerHTML = [
    '<div id="ev-cc-text">We use cookies to understand how the site is used. Analytics loads only if you accept. See our <a href="/cookie-policy/">cookie policy</a>.</div>',
    '<div id="ev-cc-btns">',
    '  <button id="ev-cc-accept">Accept</button>',
    '  <button id="ev-cc-reject">Only necessary</button>',
    '</div>'
  ].join('');

  function hide() { if (banner && banner.parentNode) banner.parentNode.removeChild(banner); }

  function mount() {
    document.body.appendChild(banner);
    document.getElementById('ev-cc-accept').addEventListener('click', function () {
      var prefs = { decided: true, analytics: true };
      savePrefs(prefs); hide(); applyPrefs(prefs);
    });
    document.getElementById('ev-cc-reject').addEventListener('click', function () {
      savePrefs({ decided: true, analytics: false }); hide();
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', mount);
  } else { mount(); }
})();
