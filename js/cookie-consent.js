/**
 * Cookie Consent — ExpansionVideos
 * GDPR-friendly consent manager for expansionvideos.com
 * GTM: GTM-T3SQ6XD (Villadose-owned) — holds the GA4 Google tag (G-X9ZQR20QNZ) + generate_lead
 */
(function () {
  'use strict';

  var STORAGE_KEY = 'ev_cookie_consent';
  var GTM_ID = 'GTM-T3SQ6XD';

  // ── Consent Mode v2 ────────────────────────────────────────────────────────
  // Defaults denied, load GTM for everyone. Google tags send cookieless modeling
  // pings while denied and go full on consent. The Meta Pixel is gated inside GTM
  // (requires ad_storage), so it stays off until the visitor accepts.
  window.dataLayer = window.dataLayer || [];
  function gtag() { window.dataLayer.push(arguments); }
  window.gtag = gtag;
  gtag('consent', 'default', {
    ad_storage: 'denied',
    ad_user_data: 'denied',
    ad_personalization: 'denied',
    analytics_storage: 'denied',
    personalization_storage: 'denied',
    functionality_storage: 'granted',
    security_storage: 'granted',
    wait_for_update: 500
  });
  gtag('set', 'ads_data_redaction', true);
  gtag('set', 'url_passthrough', true);
  loadGTM();

  function grantConsent() {
    gtag('consent', 'update', {
      ad_storage: 'granted',
      ad_user_data: 'granted',
      ad_personalization: 'granted',
      analytics_storage: 'granted',
      personalization_storage: 'granted'
    });
  }

  function getPrefs() {
    try {
      var raw = localStorage.getItem(STORAGE_KEY);
      return raw ? JSON.parse(raw) : null;
    } catch (e) { return null; }
  }

  function savePrefs(prefs) {
    try { localStorage.setItem(STORAGE_KEY, JSON.stringify(prefs)); } catch (e) {}
  }

  function loadGTM() {
    if (window.__gtmLoaded) return;
    window.__gtmLoaded = true;
    window.dataLayer = window.dataLayer || [];
    window.dataLayer.push({ 'gtm.start': new Date().getTime(), event: 'gtm.js' });
    var j = document.createElement('script');
    j.async = true;
    j.src = 'https://www.googletagmanager.com/gtm.js?id=' + GTM_ID;
    var f = document.getElementsByTagName('script')[0];
    f.parentNode.insertBefore(j, f);
  }

  function applyPrefs(prefs) {
    // GTM is already loaded for everyone (Consent Mode). Accepting upgrades consent.
    if (prefs.analytics) grantConsent();
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
    '<div id="ev-cc-text">We use cookies for analytics and marketing (Google, Meta) to understand how the site is used and measure our ads. These load only if you accept. See our <a href="/cookie-policy/">cookie policy</a>.</div>',
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
