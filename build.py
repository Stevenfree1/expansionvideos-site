#!/usr/bin/env python3
"""ExpansionVideos.com — Premium Build"""
import os
SITE = os.path.join(os.path.dirname(__file__), 'site')

HEAD = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="stylesheet" href="/css/style.css">
<link rel="icon" href="/img/favicon.png" type="image/png">
</head>
<body>
<header class="hdr"><div class="wrap">
<a href="/" class="hdr-logo"><img src="/img/logo.png" alt="ExpansionVideos" class="hdr-logo-img"></a>
<button class="hdr-toggle" onclick="document.querySelector('.hdr-nav').classList.toggle('open')" aria-label="Menu">☰</button>
<nav class="hdr-nav"><a href="/services/">Services</a><a href="/ai-video/">AI Video</a><a href="/pricing/">Pricing</a><a href="/contact/">Contact</a><a href="https://calendly.com/mikael-hamrin/30min" class="btn btn-fill btn-sm">Book a Call →</a></nav>
</div></header>
'''

FOOT = '''
<footer class="ftr"><div class="wrap">
<div class="ftr-grid">
<div class="ftr-col"><h4>ExpansionVideos</h4><p>Since 2015, we've helped 500+ businesses worldwide tell their stories through professional animated video. Trusted by brands across 56+ industries.</p><p style="margin-top:16px"><a href="mailto:studio@expansionvideos.com">studio@expansionvideos.com</a></p></div>
<div class="ftr-col"><h4>Navigation</h4><p><a href="/services/">Services</a></p><p><a href="/ai-video/">AI Video</a></p><p><a href="/pricing/">Pricing</a></p><p><a href="/contact/">Contact</a></p></div>
<div class="ftr-col"><h4>Get Started</h4><p><a href="https://calendly.com/mikael-hamrin/30min">Book a Free Call →</a></p><p style="margin-top:16px">Villadose LLC<br>Sheridan, Wyoming</p></div>
</div>
<div class="ftr-bottom">&copy; 2015–2026 ExpansionVideos — Villadose LLC</div>
</div></footer>
</body></html>'''

P = {}

P['index.html'] = {
'title': '2D Animation, AI Video & Premium — ExpansionVideos',
'desc': 'Professional animated explainer videos — 2D Animation, AI Video & Premium. From $197. 500+ videos for 56+ industries since 2015. Money-back guarantee.',
'body': '''
<section class="hero">
<div class="wrap">
<div class="hero-text">
    <p class="label">Explainer Video Production</p>
    <h1 class="h1">Videos that <span class="blue">explain, engage</span> & convert</h1>
    <p class="sub">Professional animated explainer videos that simplify your message, captivate your audience, and drive results. From concept to final video.</p>
    <div class="hero-btns">
        <a href="/pricing/" class="btn btn-fill btn-lg">See Pricing →</a>
        <a href="https://calendly.com/mikael-hamrin/30min" class="btn btn-outline btn-lg">Book Free Call</a>
    </div>
</div>
<div class="hero-video">
    <div class="hero-video-inner">
        <iframe src="https://www.youtube.com/embed/-ls8HYBvVw8?rel=0" title="ExpansionVideos" allow="accelerometer;autoplay;clipboard-write;encrypted-media;gyroscope;picture-in-picture" allowfullscreen></iframe>
    </div>
</div>
</div>
</section>

<section class="stats"><div class="wrap">
<div class="stats-item"><h3>500+</h3><p>Videos Produced</p></div>
<div class="stats-item"><h3>56+</h3><p>Industries Served</p></div>
<div class="stats-item"><h3>5.0 ★</h3><p>Client Rating</p></div>
<div class="stats-item"><h3>10+ yrs</h3><p>Experience</p></div>
</div></section>

<section class="logos"><div class="wrap">
<p>Trusted by leading brands</p>
<div class="logos-row">
<img src="/img/clients/toyota.png" alt="Toyota"><img src="/img/clients/deloitte.png" alt="Deloitte"><img src="/img/clients/aigo.png" alt="Aigo"><img src="/img/clients/ridian.jpg" alt="Ridian"><span>MAPS</span><img src="/img/clients/veritas.png" alt="Veritas"><span>Pacific West</span><img src="/img/clients/metaforce.png" alt="Metaforce">
</div>
</div></section>

<section class="sec">
<div class="wrap">
<div class="sec-hdr tc"><p class="label">Services</p><h2 class="h2">The right video for every need</h2><p class="sub mx-a" style="margin-top:16px">Professional video production for every budget and timeline.</p></div>
<div class="svc-grid">
    <div class="svc-card new"><span class="svc-badge">NEW</span><div class="svc-icon">🤖</div><h3>AI Video</h3><p>Professional videos powered by AI. Delivered in days, not weeks. Perfect for social media campaigns, ads, and volume production at a fraction of the cost.</p><div class="svc-price">from $197 <small>/ 30 sec</small></div></div>
    <div class="svc-card"><div class="svc-icon">🎬</div><h3>2D Animation</h3><p>Our most popular service since 2015. Hand-crafted custom 2D animation with professional scriptwriting, voiceover, and unlimited revisions. The standard choice.</p><div class="svc-price">from $797 <small>/ 30 sec</small></div></div>
    <div class="svc-card"><div class="svc-icon">🏆</div><h3>Premium / Custom</h3><p>Exclusive production for demanding clients. Senior team, cinematic quality, fully customized. The same level we've created for Fortune 500 companies and agencies.</p><div class="svc-price">Quote on Request</div></div>
</div>
</div></section>

<section class="sec sec-gray">
<div class="wrap">
<div class="sec-hdr tc"><p class="label">Our Promise</p><h2 class="h2">Zero risk. Guaranteed.</h2><p class="sub mx-a" style="margin-top:16px">We want you to feel completely confident working with us.</p></div>
<div class="guar-grid">
    <div class="guar-card"><div class="g-icon">💰</div><h4>Money-Back Guarantee</h4><p>Not satisfied? We offer a full money-back guarantee. Your investment is protected.</p></div>
    <div class="guar-card"><div class="g-icon">🔄</div><h4>Unlimited Revisions</h4><p>We work until you're 100% happy. No extra charges for changes.</p></div>
    <div class="guar-card"><div class="g-icon">📅</div><h4>Fixed Deadlines</h4><p>You know exactly when your video will be ready. No vague "coming soon" promises.</p></div>
</div>
</div></section>

<section class="sec">
<div class="wrap">
<div class="sec-hdr tc">
    <p class="label">Portfolio</p>
    <h2 class="h2">See our work in action</h2>
    <p class="sub mx-a" style="margin-top:16px">Examples from each format — AI Video, 2D Animation and Premium.</p>
</div>
<div class="port-grid">
    <div class="port-card"><div class="port-video"><iframe src="https://www.youtube.com/embed/-ls8HYBvVw8?rel=0" title="AI Video Example" allow="accelerometer;autoplay;clipboard-write;encrypted-media;gyroscope;picture-in-picture" allowfullscreen></iframe></div><div class="port-info"><span class="port-badge ai">🤖 AI Video</span><h4>ExpansionVideos</h4><p>Fast, cost-effective AI production. Perfect for ads and social media campaigns.</p></div></div>
    <div class="port-card"><div class="port-video"><iframe src="https://www.youtube.com/embed/MbDgRyaIUwc?rel=0" title="Toyota" allow="accelerometer;autoplay;clipboard-write;encrypted-media;gyroscope;picture-in-picture" allowfullscreen></iframe></div><div class="port-info"><span class="port-badge d2">🎬 2D Animation</span><h4>Toyota</h4><p>Hand-crafted 2D explainer for Toyota's electric hybrid cars.</p></div></div>
    <div class="port-card"><div class="port-video"><iframe src="https://www.youtube.com/embed/3jhOxZUxheY?rel=0" title="Veritas" allow="accelerometer;autoplay;clipboard-write;encrypted-media;gyroscope;picture-in-picture" allowfullscreen></iframe></div><div class="port-info"><span class="port-badge prem">🏆 Premium</span><h4>Veritas</h4><p>Premium animated production for global data management leader.</p></div></div>
</div>
</div>
</section>

<section class="sec">
<div class="wrap">
<div class="sec-hdr tc"><p class="label">Process</p><h2 class="h2">From idea to finished video</h2></div>
<div class="proc-grid">
    <div class="proc-card"><div class="proc-num">1</div><h4>Brief & Script</h4><p>Tell us your goals. We craft a compelling script tailored to your audience.</p></div>
    <div class="proc-card"><div class="proc-num">2</div><h4>Voiceover</h4><p>Professional voice artist brings your script to life in any language.</p></div>
    <div class="proc-card"><div class="proc-num">3</div><h4>Storyboard</h4><p>We design every scene so you see your video before animation begins.</p></div>
    <div class="proc-card"><div class="proc-num">4</div><h4>Delivery</h4><p>We animate and deliver in HD. Ready for your website, ads, and socials.</p></div>
</div>
</div></section>

<section class="sec sec-dark">
<div class="wrap">
<div class="sec-hdr tc"><p class="label">Testimonials</p><h2 class="h2">Trusted by 500+ businesses</h2></div>
<div class="test-grid">
    <div class="test-card"><div class="test-stars">★★★★★</div><div class="test-quote">"ExpansionVideos delivered an outstanding explainer video that perfectly captured our brand message. Professional, responsive, and creative."</div><div class="test-author">Marketing Director</div><div class="test-role">Toyota</div></div>
    <div class="test-card"><div class="test-stars">★★★★★</div><div class="test-quote">"Working with ExpansionVideos was seamless from start to finish. They understood our complex product and made it simple and engaging."</div><div class="test-author">Project Manager</div><div class="test-role">Deloitte</div></div>
    <div class="test-card"><div class="test-stars">★★★★★</div><div class="test-quote">"Incredible value for money. The AI video option gave us a professional result at a price point we didn't think was possible."</div><div class="test-author">Head of Digital</div><div class="test-role">WSO2</div></div>
</div>
</div></section>

<section class="cta">
<div class="wrap">
    <p class="label">Get Started</p>
    <h2 class="h2">Ready to create your video?</h2>
    <p class="sub">Book a free consultation. We'll discuss your project and give you a quote — no obligations.</p>
    <div class="cta-btns">
        <a href="https://calendly.com/mikael-hamrin/30min" class="btn btn-fill btn-lg">Book Free Call →</a>
        <a href="/pricing/" class="btn btn-outline btn-lg">See Pricing</a>
    </div>
</div></section>
'''}

P['pricing/index.html'] = {
'title': 'Pricing | ExpansionVideos — Simple, Transparent Pricing',
'desc': 'Simple pricing for animated explainer videos. From $197. Everything included: script, voiceover, music, animation. No hidden fees.',
'body': '''
<section class="hero" style="min-height:auto;padding:140px 32px 80px">
<div class="wrap"><div class="hero-text" style="max-width:100%">
    <p class="label">Pricing</p>
    <h1 class="h1">Simple, <span class="blue">transparent</span> pricing</h1>
    <p class="sub">Everything included. No hidden fees. Money-back guarantee.</p>
</div></div></section>

<section class="sec" style="padding-top:80px">
<div class="wrap">
<div class="price-grid">
    <div class="price-card"><div class="price-dur">🤖 AI Video</div><div class="price-amt">$197 <small>/30s</small></div><div class="price-desc">Fast, budget-friendly. Perfect for social media, ads, and volume.</div><ul class="price-list"><li>AI-generated animation</li><li>Professional voiceover</li><li>Background music</li><li>1 revision round</li><li>5–7 business days</li><li>HD delivery</li></ul><a href="/contact/" class="btn btn-ghost btn-w100 btn-sm">Get Started →</a></div>
    <div class="price-card pop"><div class="price-dur">🎬 2D Animation</div><div class="price-amt">$797 <small>/30s</small></div><div class="price-desc">Our most popular. Hand-crafted custom design for most businesses.</div><ul class="price-list"><li>Custom 2D animation</li><li>Professional scriptwriter</li><li>Premium voiceover</li><li>Unlimited revisions</li><li>3–4 weeks delivery</li><li>All formats included</li></ul><a href="/contact/" class="btn btn-fill btn-w100 btn-sm">Get Started →</a></div>
    <div class="price-card"><div class="price-dur">🏆 Premium / Custom</div><div class="price-amt">Request Quote</div><div class="price-desc">Exclusive quality for demanding projects. Senior team. Cinematic.</div><ul class="price-list"><li>Fully custom production</li><li>Senior animator & team</li><li>Premium voiceover & music</li><li>Unlimited revisions</li><li>Priority delivery</li><li>Dedicated project lead</li></ul><a href="/contact/" class="btn btn-ghost btn-w100 btn-sm">Request Quote →</a></div>
</div>
</div></section>

<section class="sec sec-gray">
<div class="wrap">
<div class="sec-hdr tc"><p class="label">FAQ</p><h2 class="h2">Common questions</h2></div>
<div class="faq-grid">
    <div class="faq-card"><h4>What's included?</h4><p>Everything: script, voiceover, music, animation, HD delivery, and revisions.</p></div>
    <div class="faq-card"><h4>How long does it take?</h4><p>AI Video: 5–7 days. Animated: 3–4 weeks. Premium: priority delivery.</p></div>
    <div class="faq-card"><h4>Money-back guarantee?</h4><p>Yes — if you're not satisfied after revisions, we offer a full refund.</p></div>
    <div class="faq-card"><h4>What languages?</h4><p>English, Spanish, French, German, Swedish, and 20+ more languages.</p></div>
</div>
</div></section>

<section class="cta">
<div class="wrap"><h2 class="h2">Ready to get started?</h2><p class="sub">Book a free call or contact us directly.</p>
<div class="cta-btns"><a href="https://calendly.com/mikael-hamrin/30min" class="btn btn-fill btn-lg">Book Free Call →</a><a href="/contact/" class="btn btn-outline btn-lg">Contact Us</a></div>
</div></section>
'''}

P['services/index.html'] = {
'title': 'Services | 2D Animation, AI Video & Premium — ExpansionVideos',
'desc': '2D Animation, AI Video and Premium/Custom video production. From $197. Professional explainer video production since 2015.',
'body': '''
<section class="hero" style="min-height:auto;padding:140px 32px 80px">
<div class="wrap"><div class="hero-text" style="max-width:100%">
    <p class="label">Services</p>
    <h1 class="h1">The right video for <span class="blue">every need</span></h1>
    <p class="sub">From hand-crafted animation to AI-powered video — we have a solution for every budget and timeline.</p>
</div></div></section>

<section class="sec" style="padding-top:80px">
<div class="wrap">
<div class="svc-grid">
    <div class="svc-card new"><span class="svc-badge">NEW</span><div class="svc-icon">🤖</div><h3>AI Video</h3><p>Professional videos powered by cutting-edge AI. Delivered in days. Perfect for social media, ad campaigns, and volume production. Cost-effective and flexible.</p><div class="svc-price">from $197 <small>· 5–7 days</small></div></div>
    <div class="svc-card"><div class="svc-icon">🎬</div><h3>2D Animation</h3><p>Our flagship since 2015. Custom 2D animation with professional scriptwriting, voiceover, and unlimited revisions. Perfect for product launches, SaaS demos, and brand stories.</p><div class="svc-price">from $797 <small>· 3–4 weeks</small></div></div>
    <div class="svc-card"><div class="svc-icon">🏆</div><h3>Premium / Custom</h3><p>Exclusive cinematic production for demanding clients. Senior team, fully customized, unlimited revisions. For Fortune 500 companies, agencies, and complex projects.</p><div class="svc-price">Quote on Request</div></div>
</div>
</div></section>

<section class="cta">
<div class="wrap"><h2 class="h2">Not sure which service?</h2><p class="sub">Book a free call and we'll help you choose.</p>
<div class="cta-btns"><a href="https://calendly.com/mikael-hamrin/30min" class="btn btn-fill btn-lg">Book Free Call →</a><a href="/pricing/" class="btn btn-outline btn-lg">See Pricing</a></div>
</div></section>
'''}

P['ai-video/index.html'] = {
'title': 'AI Video Production | Professional Videos from $197',
'desc': 'AI-powered video production from $197/30 seconds. Professional quality in 5-7 days. Perfect for social media, ads, and explainers.',
'body': '''
<section class="hero" style="min-height:auto;padding:140px 32px 80px">
<div class="wrap"><div class="hero-text" style="max-width:100%">
    <p class="label">AI Video Production</p>
    <h1 class="h1">Professional videos at a <span class="blue">fraction</span> of the cost</h1>
    <p class="sub">AI-powered video production. Stunning quality, delivered in days. Starting at just $197.</p>
    <div class="hero-btns"><a href="https://calendly.com/mikael-hamrin/30min" class="btn btn-fill btn-lg">Book Free Call →</a><a href="/pricing/" class="btn btn-outline btn-lg">See Pricing</a></div>
</div></div></section>

<section class="sec" style="padding-top:80px">
<div class="wrap">
<div class="sec-hdr tc"><h2 class="h2">Why AI Video?</h2></div>
<div class="guar-grid">
    <div class="guar-card"><div class="g-icon">⚡</div><h4>Lightning Fast</h4><p>Delivered in 5–7 business days. Perfect for tight deadlines and urgent campaigns.</p></div>
    <div class="guar-card"><div class="g-icon">💰</div><h4>Budget-Friendly</h4><p>Starting at $197/30s — up to 75% less than traditional animation.</p></div>
    <div class="guar-card"><div class="g-icon">📈</div><h4>Scales Easily</h4><p>Need 10 videos for different products? AI makes volume production affordable.</p></div>
</div>
</div></section>

<section class="sec sec-gray">
<div class="wrap">
<div class="price-grid">
    <div class="price-card"><div class="price-dur">Basic</div><div class="price-amt">$197 <small>/30s</small></div><div class="price-desc">Template AI visuals. Perfect for ads and social media.</div><ul class="price-list"><li>AI-generated scenes</li><li>Professional voiceover</li><li>Background music</li><li>1 revision round</li><li>5–7 business days</li><li>HD delivery</li></ul><a href="/contact/" class="btn btn-ghost btn-w100 btn-sm">Get Started →</a></div>
    <div class="price-card pop"><div class="price-dur">Professional</div><div class="price-amt">$397 <small>/30s</small></div><div class="price-desc">Custom AI animation. Best value for most projects.</div><ul class="price-list"><li>Custom AI animation</li><li>Professional scriptwriter</li><li>Premium voiceover</li><li>Custom music</li><li>2 revision rounds</li><li>7 business days</li></ul><a href="/contact/" class="btn btn-fill btn-w100 btn-sm">Get Started →</a></div>
    <div class="price-card"><div class="price-dur">Premium</div><div class="price-amt">$597 <small>/30s</small></div><div class="price-desc">Cinematic AI. Unlimited revisions. Priority delivery.</div><ul class="price-list"><li>Cinematic AI animation</li><li>Senior scriptwriter</li><li>Celebrity-style voiceover</li><li>Original music</li><li>Unlimited revisions</li><li>5 day priority</li></ul><a href="/contact/" class="btn btn-ghost btn-w100 btn-sm">Get Started →</a></div>
</div>
</div></section>

<section class="cta">
<div class="wrap"><h2 class="h2">Ready to try AI video?</h2><p class="sub">Book a free call and get a quote in 24 hours.</p>
<a href="https://calendly.com/mikael-hamrin/30min" class="btn btn-fill btn-lg">Book Free Call →</a>
</div></section>
'''}

P['contact/index.html'] = {
'title': 'Contact | ExpansionVideos — Get In Touch',
'desc': 'Contact ExpansionVideos: studio@expansionvideos.com. Book a free consultation via Calendly. We reply within 24 hours.',
'body': '''
<section class="hero" style="min-height:auto;padding:140px 32px 80px">
<div class="wrap"><div class="hero-text" style="max-width:100%">
    <p class="label">Contact</p>
    <h1 class="h1">Let's <span class="blue">talk</span></h1>
    <p class="sub">We reply to all inquiries within 24 hours. Or book a free call right now.</p>
</div></div></section>

<section class="sec" style="padding-top:80px">
<div class="wrap">
<div class="ct-grid">
    <div class="ct-info">
        <h2>Get in touch</h2>
        <div class="ct-block"><div class="ic">📧</div><h4>Email</h4><p><a href="mailto:studio@expansionvideos.com">studio@expansionvideos.com</a></p></div>
        <div class="ct-block"><div class="ic">🗓️</div><h4>Book a Call</h4><p><a href="https://calendly.com/mikael-hamrin/30min">Pick a time that works →</a></p></div>
        <div class="ct-block"><div class="ic">💬</div><h4>Live Chat</h4><p>Chat with us at the bottom of the page</p></div>
        <div class="ct-block"><div class="ic">🏢</div><h4>Company</h4><p>Villadose LLC<br>30N Gould St, 82801<br>Sheridan, Wyoming</p></div>
    </div>
    <div class="ct-form">
        <h3>Send us a message</h3>
        <p id="ct-status" style="display:none;margin-bottom:12px"></p>
        <div class="fg"><label>Name</label><input type="text" id="ct-name" placeholder="Your name" required></div>
        <div class="fg"><label>Email</label><input type="email" id="ct-email" placeholder="you@company.com" required></div>
        <div class="fg"><label>Company</label><input type="text" id="ct-company" placeholder="Optional"></div>
        <div class="fg"><label>Message</label><textarea id="ct-message" placeholder="Tell us about your project..." required></textarea></div>
        <button id="ct-btn" onclick="evSubmit()" class="btn btn-fill btn-w100 btn-lg">Send Message →</button>
        <script>
        async function evSubmit() {
            const btn = document.getElementById('ct-btn');
            const status = document.getElementById('ct-status');
            const name = document.getElementById('ct-name').value.trim();
            const email = document.getElementById('ct-email').value.trim();
            const company = document.getElementById('ct-company').value.trim();
            const message = document.getElementById('ct-message').value.trim();
            if (!name || !email || !message) { status.textContent = 'Please fill in all required fields.'; status.style.display='block'; status.style.color='red'; return; }
            btn.disabled = true; btn.textContent = 'Sending...';
            try {
                const res = await fetch('https://leads.mikaelhamrin.com/leads', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json', 'Authorization': 'Bearer mikael-leads-2026' },
                    body: JSON.stringify({ name, email, company, message, source: 'ev-contact-form', brand: 'ev' })
                });
                const data = await res.json();
                if (data.success) { window.location.href = '/thank-you/'; }
                else { throw new Error('Failed'); }
            } catch(e) {
                status.textContent = 'Something went wrong. Please email us directly at studio@expansionvideos.com';
                status.style.display='block'; status.style.color='red';
                btn.disabled = false; btn.textContent = 'Send Message →';
            }
        }
        </script>
    </div>
</div>
</div></section>

<section class="cta">
<div class="wrap"><h2 class="h2">Prefer to talk?</h2><p class="sub">Book a free 30-minute consultation.</p>
<a href="https://calendly.com/mikael-hamrin/30min" class="btn btn-fill btn-lg">Book Free Call →</a>
</div></section>
'''}


P['thank-you/index.html'] = {
'title': 'Thank You | ExpansionVideos',
'desc': 'Your request has been received. We will get back to you within 24 hours.',
'body': '''
<section class="hero" style="min-height:70vh;display:flex;align-items:center;justify-content:center;text-align:center;">
<div class="wrap">
    <p class="label">Thank you</p>
    <h1 class="h1">Request received!</h1>
    <p class="sub" style="max-width:520px;margin:1rem auto 2rem;">We have got your message and will get back to you within 24 hours. Feel free to book a free call directly.</p>
    <div class="hero-btns" style="justify-content:center;">
        <a href="https://calendly.com/mikael-hamrin/30min" class="btn btn-fill btn-lg">Book a call</a>
        <a href="/" class="btn btn-outline btn-lg">Back to home</a>
    </div>
</div>
</section>
'''}

for fn, pg in P.items():
    fp = os.path.join(SITE, fn)
    os.makedirs(os.path.dirname(fp), exist_ok=True)
    html = HEAD.format(title=pg['title'], desc=pg['desc']) + pg['body'] + FOOT
    with open(fp, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'✅ {fn} ({len(html):,} bytes)')
print(f'\n🚀 {len(P)} pages built!')

P['thank-you/index.html'] = {
'title': 'Thank You | ExpansionVideos',
'desc': 'Your request has been received. We will get back to you within 24 hours.',
'body': '''
<section class="hero" style="min-height:70vh;display:flex;align-items:center;justify-content:center;text-align:center;">
<div class="wrap">
    <p class="label">Thank you</p>
    <h1 class="h1">Request received! ✅</h1>
    <p class="sub" style="max-width:520px;margin:1rem auto 2rem;">We've got your message and will get back to you within 24 hours. In the meantime, feel free to book a free call directly.</p>
    <div class="hero-btns" style="justify-content:center;">
        <a href="https://calendly.com/mikael-hamrin/30min" class="btn btn-fill btn-lg">Book a call →</a>
        <a href="/" class="btn btn-outline btn-lg">Back to home</a>
    </div>
</div>
</section>
'''}
