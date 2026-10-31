/*
 * chat-widget.js — on-site AI sales assistant for Animerad Reklamfilm (AR) + Expansionvideos (EV).
 * Self-contained, no dependencies. Streams answers from the chat-api Worker.
 *
 * Usage (add before </body>):
 *   <script src="/js/chat-widget.js" data-brand="ar" defer></script>   // AR sites
 *   <script src="/js/chat-widget.js" data-brand="ev" defer></script>   // EV site
 * Optional: data-accent="#1b3a5b" to match the site's accent color.
 */
(function () {
  "use strict";
  if (window.__sfChatLoaded) return;
  window.__sfChatLoaded = true;

  var script = document.currentScript || (function () {
    var s = document.getElementsByTagName("script");
    return s[s.length - 1];
  })();

  var ENDPOINT = "https://chat.mikaelhamrin.com/chat";

  var CONFIG = {
    ar: {
      lang: "sv",
      accent: "#1b3a5b",
      title: "Animerad Reklamfilm",
      launcher: "Fråga oss",
      greeting: "Hej! Jag kan svara på frågor om priser, format och hur en beställning går till. Vad undrar du över?",
      placeholder: "Skriv din fråga...",
      send: "Skicka",
      human: "Prata med en människa",
      humanUrl: "https://calendly.com/animeradreklamfilm/intromote",
      error: "Något gick fel. Prova igen, eller boka ett samtal med oss.",
      chips: ["Vad kostar en film?", "Hur lång tid tar det?", "Hur beställer jag?"],
      disclaimer: "AI-assistent. Kan ha fel, dubbelkolla viktiga detaljer."
    },
    ev: {
      lang: "en",
      accent: "#1b3a5b",
      title: "Expansionvideos",
      launcher: "Ask us",
      greeting: "Hi! I can answer questions about pricing, formats, and how ordering works. What would you like to know?",
      placeholder: "Type your question...",
      send: "Send",
      human: "Talk to a human",
      humanUrl: "https://calendly.com/mikael-hamrin/30min",
      error: "Something went wrong. Please try again, or book a call with us.",
      chips: ["How much is a video?", "How long does it take?", "How do I order?"],
      disclaimer: "AI assistant. May be wrong, double-check important details."
    }
  };

  var brand = (script && script.getAttribute("data-brand")) || "ev";
  if (!CONFIG[brand]) brand = "ev";
  var C = CONFIG[brand];
  var accent = (script && script.getAttribute("data-accent")) || C.accent;
  var side = (script && script.getAttribute("data-side")) === "left" ? "left" : "right";

  var history = [];      // {role, content}
  var busy = false;
  var opened = false;

  // ---- styles ----
  var css = [
    ".sfc-btn{position:fixed;bottom:20px;right:20px;z-index:2147483000;display:flex;align-items:center;gap:8px;",
    "background:" + accent + ";color:#fff;border:none;border-radius:999px;padding:12px 18px;font:600 15px/1 system-ui,-apple-system,Segoe UI,Roboto,sans-serif;",
    "box-shadow:0 6px 24px rgba(0,0,0,.22);cursor:pointer;transition:transform .15s ease}",
    ".sfc-btn:hover{transform:translateY(-2px)}",
    ".sfc-btn svg{width:20px;height:20px;flex:none}",
    ".sfc-panel{position:fixed;bottom:20px;right:20px;z-index:2147483001;width:370px;max-width:calc(100vw - 32px);height:560px;max-height:calc(100vh - 40px);",
    "display:none;flex-direction:column;background:#fff;border-radius:16px;overflow:hidden;box-shadow:0 12px 48px rgba(0,0,0,.28);",
    "font:14px/1.5 system-ui,-apple-system,Segoe UI,Roboto,sans-serif;color:#1a1a1a}",
    ".sfc-panel.open{display:flex}",
    ".sfc-head{background:" + accent + ";color:#fff;padding:14px 16px;display:flex;align-items:center;justify-content:space-between}",
    ".sfc-head strong{font-size:15px;font-weight:600}",
    ".sfc-head button{background:transparent;border:none;color:#fff;font-size:22px;line-height:1;cursor:pointer;padding:0 4px}",
    ".sfc-body{flex:1;overflow-y:auto;padding:16px;background:#f7f8fa;display:flex;flex-direction:column;gap:10px}",
    ".sfc-msg{max-width:84%;padding:9px 12px;border-radius:14px;white-space:pre-wrap;word-wrap:break-word}",
    ".sfc-bot{align-self:flex-start;background:#fff;border:1px solid #e6e8ec;border-bottom-left-radius:4px}",
    ".sfc-user{align-self:flex-end;background:" + accent + ";color:#fff;border-bottom-right-radius:4px}",
    ".sfc-chips{display:flex;flex-wrap:wrap;gap:6px;margin-top:2px}",
    ".sfc-chip{border:1px solid " + accent + ";color:" + accent + ";background:#fff;border-radius:999px;padding:6px 11px;font-size:12.5px;cursor:pointer}",
    ".sfc-chip:hover{background:" + accent + ";color:#fff}",
    ".sfc-foot{border-top:1px solid #eceef1;background:#fff;padding:10px}",
    ".sfc-row{display:flex;gap:8px;align-items:flex-end}",
    ".sfc-row textarea{flex:1;resize:none;border:1px solid #d7dbe0;border-radius:10px;padding:9px 11px;font:14px/1.4 inherit;max-height:96px;outline:none}",
    ".sfc-row textarea:focus{border-color:" + accent + "}",
    ".sfc-row button{background:" + accent + ";color:#fff;border:none;border-radius:10px;padding:0 14px;height:38px;font-weight:600;cursor:pointer}",
    ".sfc-row button:disabled{opacity:.5;cursor:default}",
    ".sfc-meta{display:flex;justify-content:space-between;align-items:center;margin-top:7px;font-size:11.5px}",
    ".sfc-meta a{color:" + accent + ";font-weight:600;text-decoration:none}",
    ".sfc-meta a:hover{text-decoration:underline}",
    ".sfc-meta span{color:#8a9099}",
    ".sfc-dots{display:inline-block}",
    ".sfc-dots i{display:inline-block;width:6px;height:6px;margin:0 1px;background:#9aa0a8;border-radius:50%;animation:sfc-b 1.2s infinite}",
    ".sfc-dots i:nth-child(2){animation-delay:.2s}.sfc-dots i:nth-child(3){animation-delay:.4s}",
    "@keyframes sfc-b{0%,60%,100%{opacity:.3}30%{opacity:1}}",
    ".sfc-btn.sfc-left,.sfc-panel.sfc-left{right:auto;left:20px}",
    "@media(max-width:480px){.sfc-panel,.sfc-panel.sfc-left{bottom:0;right:0;left:0;width:100vw;height:100vh;max-height:100vh;border-radius:0}}"
  ].join("");

  var style = document.createElement("style");
  style.textContent = css;
  document.head.appendChild(style);

  // ---- markup ----
  var sideCls = side === "left" ? " sfc-left" : "";
  var launcher = document.createElement("button");
  launcher.className = "sfc-btn" + sideCls;
  launcher.setAttribute("aria-label", C.launcher);
  launcher.innerHTML =
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.38 8.38 0 0 1-8.5 8.5 8.4 8.4 0 0 1-3.8-.9L3 21l1.9-5.7A8.38 8.38 0 0 1 4 11.5 8.5 8.5 0 0 1 12.5 3 8.38 8.38 0 0 1 21 11.5z"/></svg>' +
    "<span>" + C.launcher + "</span>";

  var panel = document.createElement("div");
  panel.className = "sfc-panel" + sideCls;
  panel.innerHTML =
    '<div class="sfc-head"><strong>' + esc(C.title) + "</strong>" +
    '<button type="button" class="sfc-close" aria-label="Close">&times;</button></div>' +
    '<div class="sfc-body" role="log" aria-live="polite"></div>' +
    '<div class="sfc-foot">' +
      '<div class="sfc-row">' +
        '<textarea rows="1" placeholder="' + esc(C.placeholder) + '"></textarea>' +
        "<button type=\"button\" class=\"sfc-send\">" + esc(C.send) + "</button>" +
      "</div>" +
      '<div class="sfc-meta"><a href="' + C.humanUrl + '" target="_blank" rel="noopener">' + esc(C.human) + "</a>" +
      "<span>" + esc(C.disclaimer) + "</span></div>" +
    "</div>";

  document.body.appendChild(launcher);
  document.body.appendChild(panel);

  var body = panel.querySelector(".sfc-body");
  var ta = panel.querySelector("textarea");
  var sendBtn = panel.querySelector(".sfc-send");

  launcher.addEventListener("click", open);
  panel.querySelector(".sfc-close").addEventListener("click", close);
  sendBtn.addEventListener("click", submit);
  ta.addEventListener("input", function () { ta.style.height = "auto"; ta.style.height = Math.min(ta.scrollHeight, 96) + "px"; });
  ta.addEventListener("keydown", function (e) {
    if (e.key === "Enter" && !e.shiftKey) { e.preventDefault(); submit(); }
  });

  function open() {
    panel.classList.add("open");
    launcher.style.display = "none";
    if (!opened) { opened = true; botSay(C.greeting); renderChips(); }
    setTimeout(function () { ta.focus(); }, 50);
  }
  function close() { panel.classList.remove("open"); launcher.style.display = "flex"; }

  function renderChips() {
    var wrap = document.createElement("div");
    wrap.className = "sfc-chips";
    C.chips.forEach(function (text) {
      var b = document.createElement("button");
      b.className = "sfc-chip";
      b.type = "button";
      b.textContent = text;
      b.addEventListener("click", function () { wrap.remove(); ask(text); });
      wrap.appendChild(b);
    });
    body.appendChild(wrap);
    scroll();
  }

  function submit() {
    var v = ta.value.trim();
    if (!v || busy) return;
    ta.value = ""; ta.style.height = "auto";
    var chips = body.querySelector(".sfc-chips");
    if (chips) chips.remove();
    ask(v);
  }

  function ask(text) {
    userSay(text);
    history.push({ role: "user", content: text });
    stream();
  }

  function userSay(t) { addMsg("sfc-user", t); }
  function botSay(t) { return addMsg("sfc-bot", t); }

  function addMsg(cls, text) {
    var el = document.createElement("div");
    el.className = "sfc-msg " + cls;
    el.textContent = text;
    body.appendChild(el);
    scroll();
    return el;
  }

  function scroll() { body.scrollTop = body.scrollHeight; }

  function stream() {
    busy = true; sendBtn.disabled = true;
    var el = botSay("");
    el.innerHTML = '<span class="sfc-dots"><i></i><i></i><i></i></span>';
    var acc = "";

    fetch(ENDPOINT, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ brand: brand, messages: history })
    }).then(function (res) {
      if (!res.ok || !res.body) throw new Error("http " + res.status);
      var reader = res.body.getReader();
      var dec = new TextDecoder();
      var buf = "";

      function pump() {
        return reader.read().then(function (r) {
          if (r.done) { finish(); return; }
          buf += dec.decode(r.value, { stream: true });
          var lines = buf.split("\n");
          buf = lines.pop();
          for (var i = 0; i < lines.length; i++) {
            var line = lines[i];
            if (line.indexOf("data:") !== 0) continue;
            var data = line.slice(5).trim();
            if (!data || data === "[DONE]") continue;
            try {
              var ev = JSON.parse(data);
              if (ev.type === "content_block_delta" && ev.delta && ev.delta.type === "text_delta") {
                acc += ev.delta.text;
                el.textContent = acc;
                scroll();
              }
            } catch (_) { /* skip keepalive / non-JSON */ }
          }
          return pump();
        });
      }

      function finish() {
        if (!acc) { el.textContent = C.error; }
        else { history.push({ role: "assistant", content: acc }); }
        busy = false; sendBtn.disabled = false; ta.focus();
      }

      return pump();
    }).catch(function () {
      el.textContent = C.error;
      busy = false; sendBtn.disabled = false;
    });
  }

  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) {
    return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c];
  }); }
})();
