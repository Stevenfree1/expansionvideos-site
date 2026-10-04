#!/usr/bin/env python3
"""ExpansionVideos.com, Premium Build"""
import os
import time
SITE = os.path.join(os.path.dirname(__file__), 'site')

HEAD = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"><link rel="canonical" href="{url}"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="stylesheet" href="/css/style.css">
<link rel="icon" href="/img/favicon.png" type="image/png">
<meta property="og:type" content="website">
<meta property="og:site_name" content="ExpansionVideos">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="https://expansionvideos.com/img/logo.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="https://expansionvideos.com/img/logo.png">
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"Organization","@id":"https://expansionvideos.com/#org","name":"Expansion Videos","alternateName":"ExpansionVideos","url":"https://expansionvideos.com","logo":"https://expansionvideos.com/img/logo.png","image":"https://expansionvideos.com/img/logo.png","description":"Animated explainer video production: 2D Animation, AI-Video and Premium. 500+ videos for 56+ industries since 2015.","foundingDate":"2015","email":"studio@expansionvideos.com","address":{{"@type":"PostalAddress","addressLocality":"Sheridan","addressRegion":"WY","addressCountry":"US"}},"areaServed":"Worldwide","knowsLanguage":["en","es","fr","de","sv"],"sameAs":["https://www.instagram.com/expansionvideos/","https://www.linkedin.com/company/expansionvideos/","https://www.tiktok.com/@expansionvideos","https://www.youtube.com/@expansionvideosofficial"]}}</script>
{schema}
<script src="/js/cookie-consent.js" defer></script>
</head>
<body>
<header class="hdr"><div class="wrap">
<a href="/" class="hdr-logo"><img src="/img/logo.png" alt="ExpansionVideos" class="hdr-logo-img"></a>
<button class="hdr-toggle" onclick="document.querySelector('.hdr-nav').classList.toggle('open')" aria-label="Menu">☰</button>
<nav class="hdr-nav"><a href="/services/">Services</a><a href="/ai-video/">AI Video</a><a href="/case-studies/">Case Studies</a><a href="/portfolio/">Portfolio</a><a href="/blog/">Blog</a><a href="/pricing/">Pricing</a><a href="/contact/">Contact</a><a href="https://calendly.com/mikael-hamrin/30min" class="btn btn-fill btn-sm">Book a Call →</a></nav>
</div></header>
'''

FOOT = '''
<footer class="ftr"><div class="wrap">
<div class="ftr-grid">
<div class="ftr-col"><h4>ExpansionVideos</h4><p>Since 2015, we've helped 500+ businesses worldwide tell their stories through professional animated video. Trusted by brands across 56+ industries.</p><p style="margin-top:16px"><a href="mailto:studio@expansionvideos.com">studio@expansionvideos.com</a></p></div>
<div class="ftr-col"><h4>Navigation</h4><p><a href="/services/">Services</a></p><p><a href="/ai-video/">AI Video</a></p><p><a href="/case-studies/">Case Studies</a></p><p><a href="/portfolio/">Portfolio</a></p><p><a href="/blog/">Blog</a></p><p><a href="/pricing/">Pricing</a></p><p><a href="/contact/">Contact</a></p></div>
<div class="ftr-col"><h4>Get Started</h4><p><a href="https://calendly.com/mikael-hamrin/30min">Book a Free Call →</a></p><p style="margin-top:16px">Villadose LLC<br>Sheridan, Wyoming</p></div>
</div>
<div class="ftr-bottom">&copy; 2015–2026 ExpansionVideos, part of Villadose LLC &nbsp;·&nbsp; Sheridan, Wyoming, USA &nbsp;·&nbsp; <a href="/privacy-policy/">Privacy</a> &nbsp;·&nbsp; <a href="/terms-of-service/">Terms</a> &nbsp;·&nbsp; <a href="/cookie-policy/">Cookies</a></div>
</div></footer>
</body></html>'''

P = {}

P['index.html'] = {
'title': '2D Animation, AI Video & Premium | ExpansionVideos',
'desc': 'Professional animated explainer videos, 2D Animation, AI Video & Premium. From $497. 500+ videos for 56+ industries since 2015. Money-back guarantee.',
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
        <div class="yt-facade" data-id="-ls8HYBvVw8" onclick="this.outerHTML='<iframe src=\'https://www.youtube.com/embed/-ls8HYBvVw8?rel=0&autoplay=1\' title=\'ExpansionVideos\' allow=\'accelerometer;autoplay;clipboard-write;encrypted-media;gyroscope;picture-in-picture\' allowfullscreen style=\'position:absolute;inset:0;width:100%;height:100%;border:none\'></iframe>'" style="position:absolute;inset:0;width:100%;height:100%;background:url(https://i.ytimg.com/vi/-ls8HYBvVw8/hqdefault.jpg) center/cover no-repeat;cursor:pointer"><div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center"><div style="width:68px;height:48px;background:#ff0000;border-radius:12px;display:flex;align-items:center;justify-content:center"><svg viewBox='0 0 24 24' width='32' height='32' fill='white'><path d='M8 5v14l11-7z'/></svg></div></div></div>
    </div>
</div>
</div>
</section>

<section class="stats"><div class="wrap">
<div class="stats-item"><h3>500+</h3><p>Videos Produced</p></div>
<div class="stats-item"><h3>56+</h3><p>Industries Served</p></div>
<div class="stats-item"><h3>4.9 ★</h3><p>Client Rating</p></div>
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
    <div class="svc-card new"><span class="svc-badge">NEW</span><div class="svc-icon">🤖</div><h3>AI Video</h3><p>Professional videos powered by AI. Delivered in days, not weeks. Perfect for social media campaigns, ads, and volume production at a fraction of the cost.</p><div class="svc-price">from $497 <small>/ 30 sec</small></div></div>
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
    <p class="sub mx-a" style="margin-top:16px">Examples from each format, AI Video, 2D Animation and Premium.</p>
</div>
<div class="port-grid">
    <div class="port-card"><div class="port-video"><div class="yt-facade" onclick="this.outerHTML='<iframe src=\'https://www.youtube.com/embed/JC82Il2cjqA?rel=0&autoplay=1\' title=\'AI Video Example\' allow=\'accelerometer;autoplay;clipboard-write;encrypted-media;gyroscope;picture-in-picture\' allowfullscreen style=\'position:absolute;inset:0;width:100%;height:100%;border:none\'></iframe>'" style="position:absolute;inset:0;width:100%;height:100%;background:url(https://i.ytimg.com/vi/JC82Il2cjqA/hqdefault.jpg) center/cover no-repeat;cursor:pointer"><div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center"><div style="width:68px;height:48px;background:#ff0000;border-radius:12px;display:flex;align-items:center;justify-content:center"><svg viewBox='0 0 24 24' width='32' height='32' fill='white'><path d='M8 5v14l11-7z'/></svg></div></div></div></div><div class="port-info"><span class="port-badge ai">🤖 AI Video</span><h4>Khan Academy</h4><p>AI-generated explainer in a clean animated style. Ideal for ads and social campaigns.</p></div></div>
    <div class="port-card"><div class="port-video"><div class="yt-facade" onclick="this.outerHTML='<iframe src=\'https://www.youtube.com/embed/MbDgRyaIUwc?rel=0&autoplay=1\' title=\'Toyota\' allow=\'accelerometer;autoplay;clipboard-write;encrypted-media;gyroscope;picture-in-picture\' allowfullscreen style=\'position:absolute;inset:0;width:100%;height:100%;border:none\'></iframe>'" style="position:absolute;inset:0;width:100%;height:100%;background:url(https://i.ytimg.com/vi/MbDgRyaIUwc/hqdefault.jpg) center/cover no-repeat;cursor:pointer"><div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center"><div style="width:68px;height:48px;background:#ff0000;border-radius:12px;display:flex;align-items:center;justify-content:center"><svg viewBox='0 0 24 24' width='32' height='32' fill='white'><path d='M8 5v14l11-7z'/></svg></div></div></div></div><div class="port-info"><span class="port-badge d2">🎬 2D Animation</span><h4>Toyota</h4><p>Hand-crafted 2D explainer for Toyota's electric hybrid cars.</p></div></div>
    <div class="port-card"><div class="port-video"><div class="yt-facade" onclick="this.outerHTML='<iframe src=\'https://www.youtube.com/embed/3jhOxZUxheY?rel=0&autoplay=1\' title=\'Veritas\' allow=\'accelerometer;autoplay;clipboard-write;encrypted-media;gyroscope;picture-in-picture\' allowfullscreen style=\'position:absolute;inset:0;width:100%;height:100%;border:none\'></iframe>'" style="position:absolute;inset:0;width:100%;height:100%;background:url(https://i.ytimg.com/vi/3jhOxZUxheY/hqdefault.jpg) center/cover no-repeat;cursor:pointer"><div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center"><div style="width:68px;height:48px;background:#ff0000;border-radius:12px;display:flex;align-items:center;justify-content:center"><svg viewBox='0 0 24 24' width='32' height='32' fill='white'><path d='M8 5v14l11-7z'/></svg></div></div></div></div><div class="port-info"><span class="port-badge prem">🏆 Premium</span><h4>Veritas</h4><p>Premium animated production for global data management leader.</p></div></div>
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
<div class="sec-hdr tc"><p class="label">Testimonials</p><h2 class="h2">Trusted by 500+ businesses</h2><p class="sub mx-a" style="margin-top:12px">4.9 out of 5 from 44 verified client reviews.</p></div>
<div class="port-grid" style="margin-bottom:36px">
    <div class="port-card"><div class="port-video"><div class="yt-facade" onclick="this.outerHTML='<iframe src=\'https://www.youtube.com/embed/bGZQOh2397g?rel=0&autoplay=1\' title=\'Moran Pober testimonial\' allow=\'accelerometer;autoplay;clipboard-write;encrypted-media;gyroscope;picture-in-picture\' allowfullscreen style=\'position:absolute;inset:0;width:100%;height:100%;border:none\'></iframe>'" style="position:absolute;inset:0;width:100%;height:100%;background:url(https://i.ytimg.com/vi/bGZQOh2397g/hqdefault.jpg) center/cover no-repeat;cursor:pointer"><div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center"><div style="width:68px;height:48px;background:#ff0000;border-radius:12px;display:flex;align-items:center;justify-content:center"><svg viewBox='0 0 24 24' width='32' height='32' fill='white'><path d='M8 5v14l11-7z'/></svg></div></div></div></div><div class="port-info"><span class="port-badge prem">▶ Video review</span><h4>Moran Pober</h4><p>Founder, Acquisitions.com</p><p style="margin-top:8px;font-style:italic">"Video is converting the best of any sales process I've tried. Working with Expansionvideos was a pleasure, smooth process, amazing quality, and the results we wanted. Compared to the results you get, you don't even need to think about the price."</p></div></div>
    <div class="port-card"><div class="port-video"><div class="yt-facade" onclick="this.outerHTML='<iframe src=\'https://www.youtube.com/embed/42EJQ_4LkmI?rel=0&autoplay=1\' title=\'Gun Hudson testimonial\' allow=\'accelerometer;autoplay;clipboard-write;encrypted-media;gyroscope;picture-in-picture\' allowfullscreen style=\'position:absolute;inset:0;width:100%;height:100%;border:none\'></iframe>'" style="position:absolute;inset:0;width:100%;height:100%;background:url(https://i.ytimg.com/vi/42EJQ_4LkmI/hqdefault.jpg) center/cover no-repeat;cursor:pointer"><div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center"><div style="width:68px;height:48px;background:#ff0000;border-radius:12px;display:flex;align-items:center;justify-content:center"><svg viewBox='0 0 24 24' width='32' height='32' fill='white'><path d='M8 5v14l11-7z'/></svg></div></div></div></div><div class="port-info"><span class="port-badge prem">▶ Video review</span><h4>Gun Hudson</h4><p>Founder, Global Tax Freedom</p><p style="margin-top:8px;font-style:italic">"I had concepts my clients needed to understand or they wouldn't buy. Expansionvideos guided me through the whole process and even helped shape what to say. Since using the video, our customer support time has gone down and our sales have gone up. It was a no-brainer."</p></div></div>
</div>
<div class="test-grid">
    <div class="test-card"><div class="test-stars">★★★★★</div><div class="test-quote">"Together with Expansionvideos, we managed to package a complex topic into a great video."</div><div class="test-author">Maren Buchmüller</div><div class="test-role">COS Systems</div></div>
    <div class="test-card"><div class="test-stars">★★★★★</div><div class="test-quote">"The team at Expansionvideos were fast, efficient and gave me advice throughout."</div><div class="test-author">Amit Joshi</div><div class="test-role">Mighty CRM</div></div>
    <div class="test-card"><div class="test-stars">★★★★★</div><div class="test-quote">"Communication was smooth, with a proper understanding of our needs and good execution."</div><div class="test-author">Vidyas</div><div class="test-role">WSO2</div></div>
    <div class="test-card"><div class="test-stars">★★★★★</div><div class="test-quote">"Simple and smooth process. Responsive to changes. Highly recommend."</div><div class="test-author">Stefan Konyi</div><div class="test-role">Ahlsell</div></div>
    <div class="test-card"><div class="test-stars">★★★★★</div><div class="test-quote">"Incredibly easy to work with, even with considerable input. Easy all the way!"</div><div class="test-author">Caroline Lindblad</div><div class="test-role">Offerta Group</div></div>
    <div class="test-card"><div class="test-stars">★★★★★</div><div class="test-quote">"Impressed by the result. Good service, fast delivery, excellent outcome."</div><div class="test-author">Peter Ahlgren</div><div class="test-role">Active Solution</div></div>
</div>
</div></section>

<section class="cta">
<div class="wrap">
    <p class="label">Get Started</p>
    <h2 class="h2">Ready to create your video?</h2>
    <p class="sub">Book a free consultation. We'll discuss your project and give you a quote, no obligations.</p>
    <div class="cta-btns">
        <a href="https://calendly.com/mikael-hamrin/30min" class="btn btn-fill btn-lg">Book Free Call →</a>
        <a href="/pricing/" class="btn btn-outline btn-lg">See Pricing</a>
    </div>
</div></section>
'''}

P['pricing/index.html'] = {
'title': 'Pricing | Simple, Transparent Pricing | ExpansionVideos',
'desc': 'Simple pricing for animated explainer videos. From $497. Everything included: script, voiceover, music, animation. No hidden fees.',
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
    <div class="price-card"><div class="price-dur">🤖 AI Video</div><div class="price-amt">$497 <small>/30s</small></div><div class="price-desc">Fast, budget-friendly. Perfect for social media, ads, and volume.</div><ul class="price-list"><li>AI-generated animation</li><li>Professional voiceover</li><li>Background music</li><li>1 revision round</li><li>5–7 business days</li><li>HD delivery</li></ul><a href="/order/ai-video/" class="btn btn-ghost btn-w100 btn-sm">Get Started →</a></div>
    <div class="price-card pop"><div class="price-dur">🎬 2D Animation</div><div class="price-amt">$797 <small>/30s</small></div><div class="price-desc">Our most popular. Hand-crafted custom design for most businesses.</div><ul class="price-list"><li>Custom 2D animation</li><li>Professional scriptwriter</li><li>Premium voiceover</li><li>Unlimited revisions</li><li>3–4 weeks delivery</li><li>All formats included</li></ul><a href="/order/2d-animation/" class="btn btn-fill btn-w100 btn-sm">Get Started →</a></div>
    <div class="price-card"><div class="price-dur">🏆 Premium / Custom</div><div class="price-amt">Request Quote</div><div class="price-desc">Exclusive quality for demanding projects. Senior team. Cinematic.</div><ul class="price-list"><li>Fully custom production</li><li>Senior animator & team</li><li>Premium voiceover & music</li><li>Unlimited revisions</li><li>Priority delivery</li><li>Dedicated project lead</li></ul><a href="/contact/" class="btn btn-ghost btn-w100 btn-sm">Request Quote →</a></div>
</div>

<div style="margin-top:64px">
<h2 class="h2 tc" style="margin-bottom:8px">Detailed Pricing by Length</h2>
<p class="sub tc mx-a" style="max-width:560px;margin-bottom:48px">All prices include script, voiceover, music, animation and revisions. No hidden fees.</p>
<div style="overflow-x:auto">
<table style="width:100%;border-collapse:collapse;font-size:15px">
<thead>
<tr style="background:#0B0B0B;color:#fff">
<th style="padding:16px 24px;text-align:left;font-family:var(--font-h);font-weight:700">Video Length</th>
<th style="padding:16px 24px;text-align:center;font-family:var(--font-h);font-weight:700">🤖 AI Video</th>
<th style="padding:16px 24px;text-align:center;font-family:var(--font-h);font-weight:700;background:#1a3a6b">🎬 2D Animation</th>
<th style="padding:16px 24px;text-align:center;font-family:var(--font-h);font-weight:700">🏆 Premium</th>
</tr>
</thead>
<tbody>
<tr style="border-bottom:1px solid #e5e5e5">
<td style="padding:16px 24px;font-weight:600">30 seconds</td>
<td style="padding:16px 24px;text-align:center;color:#0057b8;font-weight:700">$497</td>
<td style="padding:16px 24px;text-align:center;color:#0057b8;font-weight:700;background:#f0f5ff">$797</td>
<td style="padding:16px 24px;text-align:center;color:#525252">Quote</td>
</tr>
<tr style="border-bottom:1px solid #e5e5e5;background:#fafafa">
<td style="padding:16px 24px;font-weight:600">60 seconds</td>
<td style="padding:16px 24px;text-align:center;color:#0057b8;font-weight:700">$697</td>
<td style="padding:16px 24px;text-align:center;color:#0057b8;font-weight:700;background:#f0f5ff">$1,397</td>
<td style="padding:16px 24px;text-align:center;color:#525252">Quote</td>
</tr>
<tr style="border-bottom:1px solid #e5e5e5">
<td style="padding:16px 24px;font-weight:600">90 seconds</td>
<td style="padding:16px 24px;text-align:center;color:#0057b8;font-weight:700">$897</td>
<td style="padding:16px 24px;text-align:center;color:#0057b8;font-weight:700;background:#f0f5ff">$1,997</td>
<td style="padding:16px 24px;text-align:center;color:#525252">Quote</td>
</tr>
<tr style="border-bottom:1px solid #e5e5e5;background:#fafafa">
<td style="padding:16px 24px;font-weight:600">2 minutes</td>
<td style="padding:16px 24px;text-align:center;color:#0057b8;font-weight:700">$1,197</td>
<td style="padding:16px 24px;text-align:center;color:#0057b8;font-weight:700;background:#f0f5ff">$2,597</td>
<td style="padding:16px 24px;text-align:center;color:#525252">Quote</td>
</tr>
<tr style="border-bottom:1px solid #e5e5e5">
<td style="padding:16px 24px;font-weight:600">3 minutes</td>
<td style="padding:16px 24px;text-align:center;color:#0057b8;font-weight:700">$1,697</td>
<td style="padding:16px 24px;text-align:center;color:#0057b8;font-weight:700;background:#f0f5ff">$3,797</td>
<td style="padding:16px 24px;text-align:center;color:#525252">Quote</td>
</tr>
<tr style="background:#fafafa">
<td style="padding:16px 24px;font-weight:600">Custom length</td>
<td style="padding:16px 24px;text-align:center;color:#525252">Contact us</td>
<td style="padding:16px 24px;text-align:center;color:#525252;background:#f0f5ff">Contact us</td>
<td style="padding:16px 24px;text-align:center;color:#525252">Contact us</td>
</tr>
</tbody>
</table>
</div>
<p style="text-align:center;margin-top:24px;font-size:14px;color:#737373">All prices in USD. <a href="/contact/" style="color:#0057b8;font-weight:600">Contact us</a> for volume discounts or custom requirements.</p>
</div>
</div></section>

<section class="sec sec-gray">
<div class="wrap">
<div class="sec-hdr tc"><p class="label">FAQ</p><h2 class="h2">Common questions</h2></div>
<div class="faq-grid">
    <div class="faq-card"><h4>What's included?</h4><p>Everything: script, voiceover, music, animation, HD delivery, and revisions.</p></div>
    <div class="faq-card"><h4>How long does it take?</h4><p>AI Video: 5–7 days. Animated: 3–4 weeks. Premium: priority delivery.</p></div>
    <div class="faq-card"><h4>Money-back guarantee?</h4><p>Yes, if you're not satisfied after revisions, we offer a full refund.</p></div>
    <div class="faq-card"><h4>What languages?</h4><p>English, Spanish, French, German, Swedish, and 20+ more languages.</p></div>
</div>
</div></section>

<section class="cta">
<div class="wrap"><h2 class="h2">Ready to get started?</h2><p class="sub">Book a free call or contact us directly.</p>
<div class="cta-btns"><a href="https://calendly.com/mikael-hamrin/30min" class="btn btn-fill btn-lg">Book Free Call →</a><a href="/contact/" class="btn btn-outline btn-lg">Contact Us</a></div>
</div></section>
'''}

P['services/index.html'] = {
'title': 'Services | 2D Animation, AI Video & Premium | ExpansionVideos',
'desc': '2D Animation, AI Video and Premium/Custom video production. From $497. Professional explainer video production since 2015.',
'body': '''
<section class="hero" style="min-height:auto;padding:140px 32px 80px">
<div class="wrap"><div class="hero-text" style="max-width:100%">
    <p class="label">Services</p>
    <h1 class="h1">The right video for <span class="blue">every need</span></h1>
    <p class="sub">From hand-crafted animation to AI-powered video, we have a solution for every budget and timeline.</p>
</div></div></section>

<section class="sec" style="padding-top:80px">
<div class="wrap">
<div class="svc-grid">
    <div class="svc-card new"><span class="svc-badge">NEW</span><div class="svc-icon">🤖</div><h3>AI Video</h3><p>Professional videos powered by cutting-edge AI. Delivered in days. Perfect for social media, ad campaigns, and volume production. Cost-effective and flexible.</p><div class="svc-price">from $497 <small>· 5–7 days</small></div></div>
    <div class="svc-card"><div class="svc-icon">🎬</div><h3>2D Animation</h3><p>Our flagship since 2015. Custom 2D animation with professional scriptwriting, voiceover, and unlimited revisions. Perfect for product launches, SaaS demos, and brand stories.</p><div class="svc-price">from $797 <small>· 3–4 weeks</small></div></div>
    <div class="svc-card"><div class="svc-icon">🏆</div><h3>Premium / Custom</h3><p>Exclusive cinematic production for demanding clients. Senior team, fully customized, unlimited revisions. For Fortune 500 companies, agencies, and complex projects.</p><div class="svc-price">Quote on Request</div></div>
</div>
</div></section>

<section class="sec sec-gray">
<div class="wrap"><div class="sec-hdr tc"><p class="label">Video types</p><h2 class="h2">Explore every format</h2><p class="sub mx-a" style="margin-top:16px">Dedicated pages for each type of video we produce.</p></div>
<div class="svc-grid" style="margin-top:48px">
    <div class="svc-card"><div class="svc-icon">💡</div><h3><a href="/explainer-video/" style="color:inherit;text-decoration:none">Explainer Video</a></h3><p>Explain your product clearly in about 60 seconds.</p><a href="/explainer-video/" class="btn btn-outline" style="margin-top:16px">Learn more →</a></div>
    <div class="svc-card"><div class="svc-icon">🎬</div><h3><a href="/2d-animation/" style="color:inherit;text-decoration:none">2D Animation</a></h3><p>Custom hand-crafted 2D animation, our flagship since 2015.</p><a href="/2d-animation/" class="btn btn-outline" style="margin-top:16px">Learn more →</a></div>
    <div class="svc-card"><div class="svc-icon">📐</div><h3><a href="/motion-graphics/" style="color:inherit;text-decoration:none">Motion Graphics</a></h3><p>Animated graphics, data and text that make information move.</p><a href="/motion-graphics/" class="btn btn-outline" style="margin-top:16px">Learn more →</a></div>
    <div class="svc-card"><div class="svc-icon">📦</div><h3><a href="/product-video/" style="color:inherit;text-decoration:none">Product & SaaS Video</a></h3><p>Show what your product does and why it is worth buying.</p><a href="/product-video/" class="btn btn-outline" style="margin-top:16px">Learn more →</a></div>
    <div class="svc-card"><div class="svc-icon">✍️</div><h3><a href="/whiteboard-animation/" style="color:inherit;text-decoration:none">Whiteboard Animation</a></h3><p>Clean hand-drawn style for education and complex topics.</p><a href="/whiteboard-animation/" class="btn btn-outline" style="margin-top:16px">Learn more →</a></div>
    <div class="svc-card"><div class="svc-icon">👥</div><h3><a href="/recruitment-video/" style="color:inherit;text-decoration:none">Recruitment Video</a></h3><p>Employer branding video that shows your culture and attracts talent.</p><a href="/recruitment-video/" class="btn btn-outline" style="margin-top:16px">Learn more →</a></div>
    <div class="svc-card"><div class="svc-icon">🤖</div><h3><a href="/ai-video/" style="color:inherit;text-decoration:none">AI Video</a></h3><p>Faster, lower-cost video powered by AI, from $497.</p><a href="/ai-video/" class="btn btn-outline" style="margin-top:16px">Learn more →</a></div>
</div>
</div></section>

<section class="cta">
<div class="wrap"><h2 class="h2">Not sure which service?</h2><p class="sub">Book a free call and we'll help you choose.</p>
<div class="cta-btns"><a href="https://calendly.com/mikael-hamrin/30min" class="btn btn-fill btn-lg">Book Free Call →</a><a href="/pricing/" class="btn btn-outline btn-lg">See Pricing</a></div>
</div></section>
'''}

P['ai-video/index.html'] = {
'title': 'AI Video Production | Professional Videos from $497',
'desc': 'AI-powered video production from $497/30 seconds. Professional quality in 5-7 days. Perfect for social media, ads, and explainers.',
'body': '''
<section class="hero" style="min-height:auto;padding:140px 32px 80px">
<div class="wrap"><div class="hero-text" style="max-width:100%">
    <p class="label">AI Video Production</p>
    <h1 class="h1">Professional videos at a <span class="blue">fraction</span> of the cost</h1>
    <p class="sub">AI-powered video production. Stunning quality, delivered in days. Starting at just $497.</p>
    <div class="hero-btns"><a href="https://calendly.com/mikael-hamrin/30min" class="btn btn-fill btn-lg">Book Free Call →</a><a href="/pricing/" class="btn btn-outline btn-lg">See Pricing</a></div>
</div></div></section>

<section class="sec" style="padding-top:80px">
<div class="wrap">
<div class="sec-hdr tc"><h2 class="h2">Why AI Video?</h2></div>
<div class="guar-grid">
    <div class="guar-card"><div class="g-icon">⚡</div><h4>Lightning Fast</h4><p>Delivered in 5–7 business days. Perfect for tight deadlines and urgent campaigns.</p></div>
    <div class="guar-card"><div class="g-icon">💰</div><h4>Budget-Friendly</h4><p>Starting at $497/30s, up to 75% less than traditional animation.</p></div>
    <div class="guar-card"><div class="g-icon">📈</div><h4>Scales Easily</h4><p>Need 10 videos for different products? AI makes volume production affordable.</p></div>
</div>
</div></section>

<section class="sec sec-gray">
<div class="wrap">
<div class="price-grid">
    <div class="price-card"><div class="price-dur">Basic</div><div class="price-amt">$497 <small>/30s</small></div><div class="price-desc">Template AI visuals. Perfect for ads and social media.</div><ul class="price-list"><li>AI-generated scenes</li><li>Professional voiceover</li><li>Background music</li><li>1 revision round</li><li>5–7 business days</li><li>HD delivery</li></ul><a href="/order/ai-video/" class="btn btn-ghost btn-w100 btn-sm">Get Started →</a></div>
    <div class="price-card pop"><div class="price-dur">Professional</div><div class="price-amt">$697 <small>/30s</small></div><div class="price-desc">Custom AI animation. Best value for most projects.</div><ul class="price-list"><li>Custom AI animation</li><li>Professional scriptwriter</li><li>Premium voiceover</li><li>Custom music</li><li>2 revision rounds</li><li>7 business days</li></ul><a href="/order/2d-animation/" class="btn btn-fill btn-w100 btn-sm">Get Started →</a></div>
    <div class="price-card"><div class="price-dur">Premium</div><div class="price-amt">$897 <small>/30s</small></div><div class="price-desc">Cinematic AI. Unlimited revisions. Priority delivery.</div><ul class="price-list"><li>Cinematic AI animation</li><li>Senior scriptwriter</li><li>Celebrity-style voiceover</li><li>Original music</li><li>Unlimited revisions</li><li>5 day priority</li></ul><a href="/contact/" class="btn btn-ghost btn-w100 btn-sm">Get Started →</a></div>
</div>
</div></section>

<section class="cta">
<div class="wrap"><h2 class="h2">Ready to try AI video?</h2><p class="sub">Book a free call and get a quote in 24 hours.</p>
<a href="https://calendly.com/mikael-hamrin/30min" class="btn btn-fill btn-lg">Book Free Call →</a>
</div></section>
'''}

P['contact/index.html'] = {
'title': 'Contact | Get In Touch | ExpansionVideos',
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


# ── Order pages ────────────────────────────────────────────────
P['order/ai-video/index.html'] = {
'title': 'Order AI Video | From $497 | ExpansionVideos',
'desc': 'Order your AI Video. Choose your length and get started.',
'body': """
<section class="hero" style="padding-top:120px;padding-bottom:40px">
<div class="wrap-sm">
<p style="margin-bottom:8px"><a href="/pricing/" style="color:var(--blue);font-weight:600">← Back to Pricing</a></p>
<p class="label">ORDER AI-VIDEO</p>
<h1 class="h2">Order your <span class="blue">AI-<br>Video</span></h1>
<p class="sub" style="max-width:480px">Fill in the form below and we'll get back to you within 24 hours with next steps. Money-back guarantee.</p>
</div>
</section>
<section class="sec" style="padding-top:0">
<div class="wrap-sm">
<div style="display:grid;grid-template-columns:1fr 2fr;gap:64px;align-items:start" class="order-layout">
<div>
<h3 style="font-family:var(--font-h);font-weight:800;margin-bottom:24px">Pricing summary</h3>
<div style="background:var(--gray-50);border:1px solid var(--gray-200);border-radius:16px;overflow:hidden">
<div style="padding:20px 24px;border-bottom:1px solid var(--gray-200)"><div style="font-weight:700;margin-bottom:4px">30 seconds</div><div style="color:var(--blue);font-size:1.4rem;font-weight:800">$497</div></div>
<div style="padding:20px 24px;border-bottom:1px solid var(--gray-200);background:rgba(37,99,235,0.04)"><div style="font-weight:700;margin-bottom:4px">60 seconds <span style="background:var(--blue);color:white;padding:2px 10px;border-radius:100px;font-size:11px;margin-left:8px">POPULAR</span></div><div style="color:var(--blue);font-size:1.4rem;font-weight:800">$697</div></div>
<div style="padding:20px 24px;border-bottom:1px solid var(--gray-200)"><div style="font-weight:700;margin-bottom:4px">90 seconds</div><div style="color:var(--blue);font-size:1.4rem;font-weight:800">$897</div></div>
<div style="padding:20px 24px"><div style="font-weight:700;margin-bottom:4px">2 minutes</div><div style="color:var(--blue);font-size:1.4rem;font-weight:800">$1,197</div></div>
</div>
<div style="margin-top:24px;background:rgba(37,99,235,0.04);border:1px solid rgba(37,99,235,0.15);border-radius:12px;padding:20px">
<h4 style="font-family:var(--font-h);font-weight:700;margin-bottom:12px">All packages include:</h4>
<ul style="list-style:none;padding:0;margin:0;font-size:14px;line-height:2">
<li>✓ AI-generated animation</li><li>✓ Professional voiceover</li><li>✓ Background music</li><li>✓ 1 revision round</li><li>✓ 5-7 business days</li><li>✓ HD delivery</li>
</ul></div>
</div>
<div>
<h3 style="font-family:var(--font-h);font-weight:800;margin-bottom:24px">Order form</h3>
<form id="orderForm" style="display:flex;flex-direction:column;gap:20px">
<div class="fg"><label>YOUR NAME</label><input type="text" name="name" placeholder="Full name" required></div>
<div class="fg"><label>EMAIL</label><input type="email" name="email" placeholder="your@email.com" required></div>
<div class="fg"><label>COMPANY / BRAND</label><input type="text" name="company" placeholder="Optional"></div>
<div class="fg"><label>VIDEO LENGTH</label><select name="length" style="width:100%;padding:14px 18px;border:2px solid var(--gray-200);border-radius:12px;font-size:15px;background:white"><option>30 seconds &mdash; $497</option><option selected>60 seconds &mdash; $697 (most popular)</option><option>90 seconds &mdash; $897</option><option>2 minutes &mdash; $1,197</option><option>3 minutes &mdash; $1,697</option></select></div>
<div class="fg"><label>VIDEO LANGUAGE</label><input type="text" name="language" placeholder="English" value="English"></div>
<div class="fg"><label>YOUR WEBSITE (OPTIONAL)</label><input type="text" name="website" placeholder="https://yoursite.com"></div>
<div class="fg"><label>TELL US ABOUT YOUR PRODUCT/SERVICE</label><textarea name="message" placeholder="What does your company do? Who is your target audience? What is the goal of the video?" required></textarea></div>
<button type="submit" class="btn btn-fill btn-lg">Submit Order →</button>
</form>
<script>
document.getElementById('orderForm').addEventListener('submit',function(e){
e.preventDefault();
var btn=this.querySelector('button[type=submit]');
btn.disabled=true;btn.textContent='Sending...';
var d=new FormData(this);
fetch('https://leads.mikaelhamrin.com/leads',{method:'POST',headers:{'Content-Type':'application/json','Authorization':'Bearer mikael-leads-2026'},body:JSON.stringify({name:d.get('name'),email:d.get('email'),message:'AI Video Order - Length: '+d.get('length')+'\\nCompany: '+d.get('company')+'\\nLanguage: '+d.get('language')+'\\nWebsite: '+d.get('website')+'\\nMessage: '+d.get('message'),source:'expansionvideos-order',service:'AI Video'})}).then(function(){try{sessionStorage.setItem('ev_order',JSON.stringify({name:d.get('name'),email:d.get('email'),company:d.get('company'),website:d.get('website')}));}catch(_){}window.location='/order/ai-video/brief/';}).catch(function(){window.location='/order/ai-video/brief/';});
});
</script>
</div>
</div>
<style>@media(max-width:768px){.order-layout{grid-template-columns:1fr !important;gap:32px !important;}}</style>
</div>
</section>"""}

# SEED:jagnneqmpuogtycwqauitcyfqqiznozgvjfrwhjtzcwkelyhdyuzaxhvmbxwltng
P['order/2d-animation/index.html'] = {
'title': 'Order 2D Animation | From $797 | ExpansionVideos',
'desc': 'Order your 2D Animation. Choose your length and get started.',
'body': """
<section class="hero" style="padding-top:120px;padding-bottom:40px">
<div class="wrap-sm">
<p style="margin-bottom:8px"><a href="/pricing/" style="color:var(--blue);font-weight:600">← Back to Pricing</a></p>
<p class="label">ORDER 2D ANIMATION</p>
<h1 class="h2">Order your <span class="blue">2D<br>Animation</span></h1>
<p class="sub" style="max-width:480px">Fill in the form below and we'll get back to you within 24 hours with next steps. Money-back guarantee.</p>
</div>
</section>
<section class="sec" style="padding-top:0">
<div class="wrap-sm">
<div style="display:grid;grid-template-columns:1fr 2fr;gap:64px;align-items:start" class="order-layout">
<div>
<h3 style="font-family:var(--font-h);font-weight:800;margin-bottom:24px">Pricing summary</h3>
<div style="background:var(--gray-50);border:1px solid var(--gray-200);border-radius:16px;overflow:hidden">
<div style="padding:20px 24px;border-bottom:1px solid var(--gray-200)"><div style="font-weight:700;margin-bottom:4px">30 seconds</div><div style="color:var(--blue);font-size:1.4rem;font-weight:800">$797</div></div>
<div style="padding:20px 24px;border-bottom:1px solid var(--gray-200);background:rgba(37,99,235,0.04)"><div style="font-weight:700;margin-bottom:4px">60 seconds <span style="background:var(--blue);color:white;padding:2px 10px;border-radius:100px;font-size:11px;margin-left:8px">POPULAR</span></div><div style="color:var(--blue);font-size:1.4rem;font-weight:800">$1,397</div></div>
<div style="padding:20px 24px;border-bottom:1px solid var(--gray-200)"><div style="font-weight:700;margin-bottom:4px">90 seconds</div><div style="color:var(--blue);font-size:1.4rem;font-weight:800">$1,997</div></div>
<div style="padding:20px 24px"><div style="font-weight:700;margin-bottom:4px">2 minutes</div><div style="color:var(--blue);font-size:1.4rem;font-weight:800">$2,597</div></div>
</div>
<div style="margin-top:24px;background:rgba(37,99,235,0.04);border:1px solid rgba(37,99,235,0.15);border-radius:12px;padding:20px">
<h4 style="font-family:var(--font-h);font-weight:700;margin-bottom:12px">All packages include:</h4>
<ul style="list-style:none;padding:0;margin:0;font-size:14px;line-height:2">
<li>✓ Custom 2D animation</li><li>✓ Professional scriptwriter</li><li>✓ Premium voiceover</li><li>✓ Unlimited revisions</li><li>✓ 3-4 weeks delivery</li><li>✓ All formats included</li>
</ul></div>
</div>
<div>
<h3 style="font-family:var(--font-h);font-weight:800;margin-bottom:24px">Order form</h3>
<form id="orderForm" style="display:flex;flex-direction:column;gap:20px">
<div class="fg"><label>YOUR NAME</label><input type="text" name="name" placeholder="Full name" required></div>
<div class="fg"><label>EMAIL</label><input type="email" name="email" placeholder="your@email.com" required></div>
<div class="fg"><label>COMPANY / BRAND</label><input type="text" name="company" placeholder="Optional"></div>
<div class="fg"><label>VIDEO LENGTH</label><select name="length" style="width:100%;padding:14px 18px;border:2px solid var(--gray-200);border-radius:12px;font-size:15px;background:white"><option>30 seconds &mdash; $797</option><option selected>60 seconds &mdash; $1,397 (most popular)</option><option>90 seconds &mdash; $1,997</option><option>2 minutes &mdash; $2,597</option><option>3 minutes &mdash; $3,797</option></select></div>
<div class="fg"><label>VIDEO LANGUAGE</label><input type="text" name="language" placeholder="English" value="English"></div>
<div class="fg"><label>YOUR WEBSITE (OPTIONAL)</label><input type="text" name="website" placeholder="https://yoursite.com"></div>
<div class="fg"><label>TELL US ABOUT YOUR PRODUCT/SERVICE</label><textarea name="message" placeholder="What does your company do? Who is your target audience? What is the goal of the video?" required></textarea></div>
<button type="submit" class="btn btn-fill btn-lg">Submit Order →</button>
</form>
<script>
document.getElementById('orderForm').addEventListener('submit',function(e){
e.preventDefault();
var btn=this.querySelector('button[type=submit]');
btn.disabled=true;btn.textContent='Sending...';
var d=new FormData(this);
fetch('https://leads.mikaelhamrin.com/leads',{method:'POST',headers:{'Content-Type':'application/json','Authorization':'Bearer mikael-leads-2026'},body:JSON.stringify({name:d.get('name'),email:d.get('email'),message:'2D Animation Order - Length: '+d.get('length')+'\\nCompany: '+d.get('company')+'\\nLanguage: '+d.get('language')+'\\nWebsite: '+d.get('website')+'\\nMessage: '+d.get('message'),source:'expansionvideos-order',service:'2D Animation'})}).then(function(){try{sessionStorage.setItem('ev_order',JSON.stringify({name:d.get('name'),email:d.get('email'),company:d.get('company'),website:d.get('website')}));}catch(_){}window.location='/order/2d-animation/brief/';}).catch(function(){window.location='/order/2d-animation/brief/';});
});
</script>
</div>
</div>
<style>@media(max-width:768px){.order-layout{grid-template-columns:1fr !important;gap:32px !important;}}</style>
</div>
</section>"""}

# === Project brief pages (order -> brief -> thank-you) ===
_EV_BRIEF_TMPL = """
<section class="hero" style="padding-top:120px;padding-bottom:32px">
<div class="wrap-sm">
<p style="margin-bottom:8px"><a href="/order/@@PATH@@/" style="color:var(--blue);font-weight:600">&larr; Back to order</a></p>
<p class="label">PROJECT BRIEF &mdash; @@SVC@@</p>
<h1 class="h2">Tell us about <span class="blue">your project</span></h1>
<p class="sub" style="max-width:560px">The more you share, the better we can craft your video. Only name and email are required &mdash; fill in whatever you can and we'll cover the rest on our call.</p>
</div>
</section>
<section class="sec" style="padding-top:0">
<div class="wrap-sm">
<form id="briefForm" style="display:flex;flex-direction:column;gap:28px;max-width:680px">
<div>
<h3 style="font-family:var(--font-h);font-weight:800;margin-bottom:18px">1 &middot; Contact &amp; billing</h3>
<div style="display:flex;flex-direction:column;gap:18px">
<div class="fg"><label>YOUR NAME</label><input type="text" name="name" placeholder="Full name" required></div>
<div class="fg"><label>EMAIL</label><input type="email" name="email" placeholder="your@email.com" required></div>
<div class="fg"><label>COMPANY / BRAND</label><input type="text" name="company" placeholder="Company name"></div>
<div class="fg"><label>COMPANY REG. / VAT NUMBER</label><input type="text" name="org_number" placeholder="Optional"></div>
<div class="fg"><label>BILLING ADDRESS</label><input type="text" name="billing_address" placeholder="Street address"></div>
<div class="fg"><label>POSTAL / ZIP CODE</label><input type="text" name="postal_code" placeholder="Optional"></div>
<div class="fg"><label>CITY</label><input type="text" name="city" placeholder="Optional"></div>
<div class="fg"><label>BILLING EMAIL (IF DIFFERENT)</label><input type="email" name="billing_email" placeholder="Optional"></div>
<div class="fg"><label>YOUR WEBSITE</label><input type="text" name="website" placeholder="https://yoursite.com"></div>
</div>
</div>
<div>
<h3 style="font-family:var(--font-h);font-weight:800;margin-bottom:18px">2 &middot; Video specification</h3>
<div style="display:flex;flex-direction:column;gap:18px">
<div class="fg"><label>VIDEO TITLE / WORKING NAME</label><input type="text" name="video_title" placeholder="Optional"></div>
<div class="fg"><label>VIDEO LENGTH</label><select name="video_length" style="width:100%;padding:14px 18px;border:2px solid var(--gray-200);border-radius:12px;font-size:15px;background:white">@@LENGTHS@@</select></div>
<div class="fg"><label>VOICEOVER</label><select name="voiceover" style="width:100%;padding:14px 18px;border:2px solid var(--gray-200);border-radius:12px;font-size:15px;background:white"><option>Professional voiceover (recommended)</option><option>Male voice</option><option>Female voice</option><option>No voiceover</option><option>We'll provide our own</option></select></div>
<div class="fg"><label>EXTRA LANGUAGE VERSIONS</label><select name="extra_languages" style="width:100%;padding:14px 18px;border:2px solid var(--gray-200);border-radius:12px;font-size:15px;background:white"><option>No</option><option>Yes &mdash; 1 extra language</option><option>Yes &mdash; 2+ languages</option><option>Not sure yet</option></select></div>
<div class="fg"><label>SUBTITLES</label><select name="subtitles" style="width:100%;padding:14px 18px;border:2px solid var(--gray-200);border-radius:12px;font-size:15px;background:white"><option>No</option><option>Yes &mdash; English</option><option>Yes &mdash; other language</option><option>Not sure yet</option></select></div>
</div>
</div>
<div>
<h3 style="font-family:var(--font-h);font-weight:800;margin-bottom:18px">3 &middot; About the film</h3>
<div style="display:flex;flex-direction:column;gap:18px">
<div class="fg"><label>PURPOSE / GOAL OF THE VIDEO</label><textarea name="purpose" placeholder="What do you want this video to achieve?"></textarea></div>
<div class="fg"><label>TARGET AUDIENCE</label><textarea name="target_audience" placeholder="Who is this video for?"></textarea></div>
<div class="fg"><label>ABOUT YOUR COMPANY / ORGANIZATION</label><textarea name="about_company" placeholder="What does your company do?"></textarea></div>
<div class="fg"><label>COMPETITORS</label><textarea name="competitors" placeholder="Who are your main competitors?"></textarea></div>
<div class="fg"><label>WHAT SHOULD THE VIDEO COVER?</label><textarea name="topic" placeholder="Key points, product, message..."></textarea></div>
<div class="fg"><label>TONE &amp; STYLE</label><textarea name="tone" placeholder="Playful, corporate, bold, minimal?"></textarea></div>
<div class="fg"><label>SPECIFIC WISHES / MUST-HAVES</label><textarea name="wishes" placeholder="Anything that must be included?"></textarea></div>
<div class="fg"><label>WHERE WILL THE VIDEO BE USED?</label><textarea name="usage" placeholder="Website, social media, ads, trade shows?"></textarea></div>
<div class="fg"><label>KEY TAKEAWAY &mdash; ONE THING VIEWERS SHOULD REMEMBER</label><textarea name="takeaway" placeholder="The single most important message"></textarea></div>
<div class="fg"><label>CALL TO ACTION</label><textarea name="cta" placeholder="What should viewers do after watching?"></textarea></div>
<div class="fg"><label>REFERENCE VIDEOS YOU LIKE (LINKS)</label><input type="url" name="reference" placeholder="https://..."></div>
<div class="fg"><label>BRAND GUIDELINES &mdash; COLORS, FONTS, LOGO</label><textarea name="brand" placeholder="Describe or link your brand guidelines"></textarea></div>
<div class="fg"><label>LINK TO LOGOS / ASSETS / MATERIAL</label><input type="url" name="files" placeholder="Google Drive, Dropbox, WeTransfer..."></div>
</div>
</div>
<button type="submit" class="btn btn-fill btn-lg">Submit project brief &rarr;</button>
<p style="font-size:13px;color:#6b7280;margin-top:-12px">We'll review your brief and get back to you within 24 hours.</p>
</form>
<script>
(function(){var s={};try{s=JSON.parse(sessionStorage.getItem('ev_order')||'{}');}catch(_){}['name','email','company','website'].forEach(function(k){var el=document.querySelector('#briefForm [name='+k+']');if(el&&s[k])el.value=s[k];});
var f=document.getElementById('briefForm');
f.addEventListener('submit',function(e){e.preventDefault();var btn=f.querySelector('button[type=submit]');btn.disabled=true;btn.textContent='Sending...';var d=new FormData(f);
var msg='@@SVC@@ - PROJECT BRIEF'+'\\n\\nCONTACT & BILLING'+'\\nCompany: '+d.get('company')+'\\nReg/VAT: '+d.get('org_number')+'\\nBilling: '+d.get('billing_address')+', '+d.get('postal_code')+' '+d.get('city')+'\\nBilling email: '+d.get('billing_email')+'\\nWebsite: '+d.get('website')+'\\n\\nVIDEO SPEC'+'\\nTitle: '+d.get('video_title')+'\\nLength: '+d.get('video_length')+'\\nVoiceover: '+d.get('voiceover')+'\\nExtra languages: '+d.get('extra_languages')+'\\nSubtitles: '+d.get('subtitles')+'\\n\\nABOUT THE FILM'+'\\nPurpose: '+d.get('purpose')+'\\nAudience: '+d.get('target_audience')+'\\nAbout company: '+d.get('about_company')+'\\nCompetitors: '+d.get('competitors')+'\\nCovers: '+d.get('topic')+'\\nTone/style: '+d.get('tone')+'\\nWishes: '+d.get('wishes')+'\\nUsage: '+d.get('usage')+'\\nTakeaway: '+d.get('takeaway')+'\\nCTA: '+d.get('cta')+'\\nReferences: '+d.get('reference')+'\\nBrand: '+d.get('brand')+'\\nAssets: '+d.get('files');
fetch('https://leads.mikaelhamrin.com/leads',{method:'POST',headers:{'Content-Type':'application/json','Authorization':'Bearer mikael-leads-2026'},body:JSON.stringify({name:d.get('name'),email:d.get('email'),message:msg,source:'expansionvideos-brief',service:'@@SVC@@'})}).then(function(){try{sessionStorage.removeItem('ev_order');}catch(_){}window.location='/thank-you/';}).catch(function(){window.location='/thank-you/';});
});})();
</script>
</div>
</section>"""
def _ev_brief(svc, path, lengths):
    b=_EV_BRIEF_TMPL.replace('@@SVC@@',svc).replace('@@PATH@@',path).replace('@@LENGTHS@@',lengths)
    return {'title':'Project Brief - '+svc+' | ExpansionVideos','desc':'Tell us about your '+svc+' project so we can craft the perfect video.','body':b}
_EVL='<option>30 seconds</option><option selected>60 seconds</option><option>90 seconds</option><option>2 minutes</option><option>3 minutes</option>'
P['order/ai-video/brief/index.html']=_ev_brief('AI Video','ai-video',_EVL)
P['order/2d-animation/brief/index.html']=_ev_brief('2D Animation','2d-animation',_EVL)


P['case-studies/index.html'] = {
'title': 'Case Studies | Explainer Video Results | ExpansionVideos',
'desc': 'Real explainer video case studies from ExpansionVideos: the challenge, our solution, and the results, including a launch that drew 1,200 first-week viewers and a video with 3M+ views.',
'body': '''
<section class="hero" style="min-height:auto;padding-bottom:0">
<div class="wrap">
<div class="hero-text" style="max-width:760px;margin:0 auto;text-align:center">
    <p class="label">Case Studies</p>
    <h1 class="h1">Explainer videos that did the job</h1>
    <p class="sub">Real projects, real goals, real outcomes. Here is the challenge each client faced, what we made, and what happened next.</p>
</div>
</div>
</section>

<section class="sec">
<div class="wrap">
<div class="sec-hdr"><p class="label">Fintech</p><h2 class="h2">366 Security and Compliance</h2></div>
<p class="sub"><strong>Challenge.</strong> 366 wanted to clearly show the benefits of their Payment Hub and move prospects further along the buying journey. The hard part was visualizing complex payment flows in simple words.</p>
<p class="sub"><strong>Solution.</strong> We produced a subtitled explainer that shows how the Payment Hub routes payments across acquirers by cost and availability, built for fintech, e-commerce, and hospitality buyers.</p>
<p class="sub"><strong>Channels.</strong> YouTube, website, and Instagram.</p>
<p class="sub"><strong>Result.</strong> "We are extremely satisfied with how the entire project was handled, everything from information gathering to production." The team is planning more videos for other parts of the business.</p>
<div style="max-width:720px;margin:24px auto 0"><div class="port-video"><div class="yt-facade" onclick="this.outerHTML='<iframe src=\'https://www.youtube.com/embed/o_eILbXW3N8?rel=0&autoplay=1\' title=\'366 Security and Compliance explainer\' allow=\'accelerometer;autoplay;clipboard-write;encrypted-media;gyroscope;picture-in-picture\' allowfullscreen style=\'position:absolute;inset:0;width:100%;height:100%;border:none\'></iframe>'" style="position:absolute;inset:0;width:100%;height:100%;background:url(https://i.ytimg.com/vi/o_eILbXW3N8/hqdefault.jpg) center/cover no-repeat;cursor:pointer"><div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center"><div style="width:68px;height:48px;background:#ff0000;border-radius:12px;display:flex;align-items:center;justify-content:center"><svg viewBox='0 0 24 24' width='32' height='32' fill='white'><path d='M8 5v14l11-7z'/></svg></div></div></div></div></div>
</div></section>

<section class="sec sec-gray">
<div class="wrap">
<div class="sec-hdr"><p class="label">SaaS / Data</p><h2 class="h2">LEANalyser</h2></div>
<p class="sub"><strong>Challenge.</strong> LEANalyser needed people to actually try their tool. That meant explaining, fast, that one product finally lets a part-time analyst run data analysis without help and without juggling several tools.</p>
<p class="sub"><strong>Solution.</strong> We built a video that works like a virtual salesperson. It shows the full functionality a pro needs, aimed at business-savvy people who are not IT professionals.</p>
<p class="sub"><strong>Channels.</strong> LinkedIn, Mailchimp, and email.</p>
<p class="sub"><strong>Result.</strong> A LinkedIn launch brought about 1,200 viewers in the first week, strong for a brand-new product from a new company.</p>
<div style="max-width:720px;margin:24px auto 0"><div class="port-video"><div class="yt-facade" onclick="this.outerHTML='<iframe src=\'https://www.youtube.com/embed/8ELXaZIt3-Y?rel=0&autoplay=1\' title=\'LEANalyser explainer\' allow=\'accelerometer;autoplay;clipboard-write;encrypted-media;gyroscope;picture-in-picture\' allowfullscreen style=\'position:absolute;inset:0;width:100%;height:100%;border:none\'></iframe>'" style="position:absolute;inset:0;width:100%;height:100%;background:url(https://i.ytimg.com/vi/8ELXaZIt3-Y/hqdefault.jpg) center/cover no-repeat;cursor:pointer"><div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center"><div style="width:68px;height:48px;background:#ff0000;border-radius:12px;display:flex;align-items:center;justify-content:center"><svg viewBox='0 0 24 24' width='32' height='32' fill='white'><path d='M8 5v14l11-7z'/></svg></div></div></div></div></div>
</div></section>

<section class="sec">
<div class="wrap">
<div class="sec-hdr"><p class="label">E-commerce</p><h2 class="h2">Tailor Store</h2></div>
<p class="sub"><strong>Challenge.</strong> Tailor Store needed to explain why custom-fit shirts beat ill-fitting standard sizes, and re-engage people who visited the site but did not buy.</p>
<p class="sub"><strong>Solution.</strong> We created an explainer that positions Tailor Store as the new way to buy shirts, then used it for YouTube remarketing to bring visitors back.</p>
<p class="sub"><strong>Channels.</strong> YouTube.</p>
<div class="stats" style="margin-top:24px;border-radius:16px"><div class="wrap"><div class="stats-item"><h3>3M+</h3><p>Views on YouTube</p></div><div class="stats-item"><h3>"You did very well"</h3><p>Tailor Store</p></div></div></div>
</div></section>

<section class="cta">
<div class="wrap">
    <p class="label">Your project next</p>
    <h2 class="h2">Ready to create your video?</h2>
    <p class="sub">Book a free call and we'll map out the video that fits your goal.</p>
    <div class="cta-btns">
        <a href="https://calendly.com/mikael-hamrin/30min" class="btn btn-fill btn-lg">Book Free Call →</a>
        <a href="/pricing/" class="btn btn-outline btn-lg">See Pricing</a>
    </div>
</div></section>
'''}

# --- Per-page structured data (JSON-LD): reviews, offers, FAQ, service ---
P['index.html']['schema'] = '''<script type="application/ld+json">{"@context":"https://schema.org","@type":"Organization","@id":"https://expansionvideos.com/#org","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.9","reviewCount":"44","bestRating":"5"},"review":[{"@type":"Review","reviewRating":{"@type":"Rating","ratingValue":"5","bestRating":"5"},"author":{"@type":"Person","name":"Maren Buchmüller"},"reviewBody":"Together with Expansionvideos, we managed to package a complex topic into a great video."},{"@type":"Review","reviewRating":{"@type":"Rating","ratingValue":"5","bestRating":"5"},"author":{"@type":"Person","name":"Amit Joshi"},"reviewBody":"The team at Expansionvideos were fast, efficient and gave me advice throughout."},{"@type":"Review","reviewRating":{"@type":"Rating","ratingValue":"5","bestRating":"5"},"author":{"@type":"Person","name":"Vidyas"},"reviewBody":"Communication was smooth, with a proper understanding of our needs and good execution."},{"@type":"Review","reviewRating":{"@type":"Rating","ratingValue":"5","bestRating":"5"},"author":{"@type":"Person","name":"Stefan Konyi"},"reviewBody":"Simple and smooth process. Responsive to changes. Highly recommend."},{"@type":"Review","reviewRating":{"@type":"Rating","ratingValue":"5","bestRating":"5"},"author":{"@type":"Person","name":"Caroline Lindblad"},"reviewBody":"Incredibly easy to work with, even with considerable input. Easy all the way!"},{"@type":"Review","reviewRating":{"@type":"Rating","ratingValue":"5","bestRating":"5"},"author":{"@type":"Person","name":"Peter Ahlgren"},"reviewBody":"Impressed by the result. Good service, fast delivery, excellent outcome."}]}</script>'''

P['services/index.html']['schema'] = '''<script type="application/ld+json">{"@context":"https://schema.org","@type":"Organization","@id":"https://expansionvideos.com/#org","makesOffer":[{"@type":"Offer","priceCurrency":"USD","price":"497","itemOffered":{"@type":"Service","name":"AI Video","description":"AI-powered explainer videos from $497 per 30 seconds."}},{"@type":"Offer","priceCurrency":"USD","price":"797","itemOffered":{"@type":"Service","name":"2D Animation","description":"Hand-crafted custom 2D animation from $797 per 30 seconds."}},{"@type":"Offer","itemOffered":{"@type":"Service","name":"Premium / Custom Video Production","description":"Cinematic, fully customized production. Quote on request."}}]}</script>'''

P['ai-video/index.html']['schema'] = '''<script type="application/ld+json">{"@context":"https://schema.org","@type":"Service","name":"AI Video Production","serviceType":"AI-generated explainer video production","provider":{"@id":"https://expansionvideos.com/#org"},"areaServed":"Worldwide","description":"AI-powered explainer video production from $497 per 30 seconds, delivered in 5-7 days. Includes professional voiceover, music, and HD delivery.","offers":{"@type":"Offer","price":"497","priceCurrency":"USD","url":"https://expansionvideos.com/order/ai-video/","availability":"https://schema.org/InStock"}}</script>'''

P['pricing/index.html']['schema'] = '''<script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":"What's included?","acceptedAnswer":{"@type":"Answer","text":"Everything: script, voiceover, music, animation, HD delivery, and revisions."}},{"@type":"Question","name":"How long does it take?","acceptedAnswer":{"@type":"Answer","text":"AI Video: 5-7 days. Animated: 3-4 weeks. Premium: priority delivery."}},{"@type":"Question","name":"Do you offer a money-back guarantee?","acceptedAnswer":{"@type":"Answer","text":"Yes. If you're not satisfied after revisions, we offer a full refund."}},{"@type":"Question","name":"What languages do you support?","acceptedAnswer":{"@type":"Answer","text":"English, Spanish, French, German, Swedish, and 20+ more languages."}}]}</script>'''


P['explainer-video/index.html'] = {
'title': 'Explainer Video Production | Animated Explainer Videos | ExpansionVideos',
'desc': 'Animated explainer video production that makes your product easy to understand in 60 seconds. 500+ videos since 2015. From $797.',
'body': '''
<section class="hero" style="min-height:auto;padding:140px 32px 80px">
<div class="wrap"><div class="hero-text" style="max-width:100%">
    <p class="label"><a href="/services/" style="color:var(--blue,#2563eb)">← All services</a></p>
    <h1 class="h1">Explainer video <span class="blue">production that converts</span></h1>
    <p class="sub">An explainer video turns a complex product or service into a clear, 60-second story that your audience actually understands. It is often the single most effective element on a landing page.</p>
    <div class="hero-btns"><a href="https://calendly.com/mikael-hamrin/30min" class="btn btn-fill btn-lg">Book Free Call →</a><a href="/pricing/" class="btn btn-outline btn-lg">See Pricing</a></div>
</div></div></section>
<section class="sec" style="padding-top:80px">
<div class="wrap"><div class="sec-hdr tc"><p class="label">Explainer videos</p><h2 class="h2">Explainer video production that converts</h2></div>
<div class="guar-grid" style="margin-top:48px"><div class="guar-card"><div class="g-icon">🎯</div><h4>Clarity that converts</h4><p>We boil your message down to what matters, so viewers get it and act on it.</p></div><div class="guar-card"><div class="g-icon">🧩</div><h4>Built for complex products</h4><p>SaaS, fintech and deep tech are where a good explainer earns its keep.</p></div><div class="guar-card"><div class="g-icon">🌍</div><h4>Any language</h4><p>Reuse the same animation with new voiceover in 20+ languages.</p></div></div></div></section>
<section class="sec sec-gray">
<div class="wrap"><div class="sec-hdr tc"><p class="label">Use cases</p><h2 class="h2">When it works best</h2></div>
<div class="svc-grid" style="margin-top:48px"><div class="svc-card"><div class="svc-icon">🖥️</div><h3>Landing pages</h3><p>The classic homepage explainer that lifts conversion and time on page.</p></div><div class="svc-card"><div class="svc-icon">📣</div><h3>Paid ads</h3><p>Short cutdowns built for Meta, YouTube and LinkedIn.</p></div><div class="svc-card"><div class="svc-icon">🚀</div><h3>Product launches</h3><p>Set the narrative for a new feature or product in one clear video.</p></div><div class="svc-card"><div class="svc-icon">🤝</div><h3>Sales enablement</h3><p>Give your sales team one crisp video that pitches it perfectly every time.</p></div><div class="svc-card"><div class="svc-icon">📧</div><h3>Onboarding</h3><p>Help new users understand the value fast and reduce churn.</p></div><div class="svc-card"><div class="svc-icon">📊</div><h3>Investor decks</h3><p>Explain the opportunity to investors without a 30-slide deck.</p></div></div></div></section>
<section class="sec">
<div class="wrap"><div class="sec-hdr tc"><p class="label">FAQ</p><h2 class="h2">Frequently asked questions</h2></div>
<div class="faq-grid" style="margin-top:48px"><div class="faq-card"><h4>What is an explainer video?</h4><p>A short animated video, usually 60 to 90 seconds, that explains what a product or service does and why it matters. It is the most common format for homepages, ads and onboarding.</p></div><div class="faq-card"><h4>How much does an explainer video cost?</h4><p>Animated explainer videos start at $797 per 30 seconds. AI video starts at $497. Final price depends on length, complexity and number of languages.</p></div><div class="faq-card"><h4>How long does production take?</h4><p>Animated explainer videos take about 3 to 4 weeks. AI video is delivered in 5 to 7 days.</p></div><div class="faq-card"><h4>What is included?</h4><p>Script, professional voiceover, music, custom animation, HD delivery and revisions until you are happy.</p></div></div></div></section>
<section class="sec sec-gray">
<div class="wrap"><div class="sec-hdr tc"><p class="label">Related services</p><h2 class="h2">Explore more</h2></div>
<div class="svc-grid" style="margin-top:48px"><div class="svc-card"><div class="svc-icon">🤖</div><h3><a href="/ai-video/" style="color:inherit;text-decoration:none">AI Video</a></h3><p>Faster, lower-cost video powered by AI.</p><a href="/ai-video/" class="btn btn-outline" style="margin-top:16px">Learn more →</a></div><div class="svc-card"><div class="svc-icon">🎬</div><h3><a href="/2d-animation/" style="color:inherit;text-decoration:none">2D Animation</a></h3><p>Custom hand-crafted 2D animation.</p><a href="/2d-animation/" class="btn btn-outline" style="margin-top:16px">Learn more →</a></div><div class="svc-card"><div class="svc-icon">📦</div><h3><a href="/product-video/" style="color:inherit;text-decoration:none">Product Video</a></h3><p>Show what your product does and why it matters.</p><a href="/product-video/" class="btn btn-outline" style="margin-top:16px">Learn more →</a></div></div></div></section>
<section class="cta">
<div class="wrap"><h2 class="h2">Ready to get started?</h2><p class="sub">Book a free call and get a quote within 24 hours.</p>
<div class="cta-btns"><a href="https://calendly.com/mikael-hamrin/30min" class="btn btn-fill btn-lg">Book Free Call →</a><a href="/pricing/" class="btn btn-outline btn-lg">See Pricing</a></div>
</div></section>
'''}
P['explainer-video/index.html']['schema'] = '''<script type="application/ld+json">{"@context":"https://schema.org","@type":"Service","name":"Explainer Video Production","serviceType":"Animated explainer video production","provider":{"@id":"https://expansionvideos.com/#org"},"areaServed":"Worldwide","description":"Animated explainer video production that makes your product easy to understand in 60 seconds. 500+ videos since 2015. From $797.","url":"https://expansionvideos.com/explainer-video/"}</script><script type="application/ld+json">{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://expansionvideos.com/"},{"@type":"ListItem","position":2,"name":"Services","item":"https://expansionvideos.com/services/"},{"@type":"ListItem","position":3,"name":"Explainer Video Production","item":"https://expansionvideos.com/explainer-video/"}]}</script><script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":"What is an explainer video?","acceptedAnswer":{"@type":"Answer","text":"A short animated video, usually 60 to 90 seconds, that explains what a product or service does and why it matters. It is the most common format for homepages, ads and onboarding."}},{"@type":"Question","name":"How much does an explainer video cost?","acceptedAnswer":{"@type":"Answer","text":"Animated explainer videos start at $797 per 30 seconds. AI video starts at $497. Final price depends on length, complexity and number of languages."}},{"@type":"Question","name":"How long does production take?","acceptedAnswer":{"@type":"Answer","text":"Animated explainer videos take about 3 to 4 weeks. AI video is delivered in 5 to 7 days."}},{"@type":"Question","name":"What is included?","acceptedAnswer":{"@type":"Answer","text":"Script, professional voiceover, music, custom animation, HD delivery and revisions until you are happy."}}]}</script>'''

P['2d-animation/index.html'] = {
'title': '2D Animation Video Production | Custom Animated Video | ExpansionVideos',
'desc': 'Custom 2D animation video production. Hand-crafted characters, motion and design with professional voiceover. Our flagship since 2015. From $797.',
'body': '''
<section class="hero" style="min-height:auto;padding:140px 32px 80px">
<div class="wrap"><div class="hero-text" style="max-width:100%">
    <p class="label"><a href="/services/" style="color:var(--blue,#2563eb)">← All services</a></p>
    <h1 class="h1">2D animation <span class="blue">that tells your story</span></h1>
    <p class="sub">2D animation is our flagship. Hand-crafted characters, custom illustration and smooth motion that give your brand a look no template can match.</p>
    <div class="hero-btns"><a href="https://calendly.com/mikael-hamrin/30min" class="btn btn-fill btn-lg">Book Free Call →</a><a href="/pricing/" class="btn btn-outline btn-lg">See Pricing</a></div>
</div></div></section>
<section class="sec" style="padding-top:80px">
<div class="wrap"><div class="sec-hdr tc"><p class="label">2D animation</p><h2 class="h2">2D animation that tells your story</h2></div>
<div class="guar-grid" style="margin-top:48px"><div class="guar-card"><div class="g-icon">🎨</div><h4>Fully custom</h4><p>Characters, style and scenes designed around your brand, not a template.</p></div><div class="guar-card"><div class="g-icon">♾️</div><h4>Unlimited revisions</h4><p>We keep refining until it is right. No surprise fees.</p></div><div class="guar-card"><div class="g-icon">🗣️</div><h4>Pro voiceover</h4><p>Professional voice talent in the tone and language you need.</p></div></div></div></section>
<section class="sec sec-gray">
<div class="wrap"><div class="sec-hdr tc"><p class="label">Use cases</p><h2 class="h2">When it works best</h2></div>
<div class="svc-grid" style="margin-top:48px"><div class="svc-card"><div class="svc-icon">🖥️</div><h3>Explainer videos</h3><p>The flagship use: explain a product clearly and memorably.</p></div><div class="svc-card"><div class="svc-icon">🏢</div><h3>Brand stories</h3><p>Show who you are and what you stand for.</p></div><div class="svc-card"><div class="svc-icon">📚</div><h3>Educational content</h3><p>Make training and e-learning easier to follow and finish.</p></div><div class="svc-card"><div class="svc-icon">📱</div><h3>Social campaigns</h3><p>Scroll-stopping animation for Instagram, TikTok and LinkedIn.</p></div><div class="svc-card"><div class="svc-icon">💻</div><h3>SaaS demos</h3><p>Turn an abstract interface into a story anyone can follow.</p></div><div class="svc-card"><div class="svc-icon">📣</div><h3>Commercials</h3><p>Animated ads for broadcast and digital with a fixed price.</p></div></div></div></section>
<section class="sec">
<div class="wrap"><div class="sec-hdr tc"><p class="label">FAQ</p><h2 class="h2">Frequently asked questions</h2></div>
<div class="faq-grid" style="margin-top:48px"><div class="faq-card"><h4>What is 2D animation?</h4><p>2D animation is hand-crafted animated video using characters, illustration and motion in two dimensions. It is the most versatile and popular style for explainer and brand video.</p></div><div class="faq-card"><h4>How much does a 2D animated video cost?</h4><p>Custom 2D animation starts at $797 per 30 seconds. Price depends on length, scene count and style complexity.</p></div><div class="faq-card"><h4>How long does it take?</h4><p>Most 2D animation projects take 3 to 4 weeks from brief to final delivery.</p></div><div class="faq-card"><h4>Can you match our brand style?</h4><p>Yes. Every project is custom designed around your brand colors, tone and visual identity.</p></div></div></div></section>
<section class="sec sec-gray">
<div class="wrap"><div class="sec-hdr tc"><p class="label">Related services</p><h2 class="h2">Explore more</h2></div>
<div class="svc-grid" style="margin-top:48px"><div class="svc-card"><div class="svc-icon">💡</div><h3><a href="/explainer-video/" style="color:inherit;text-decoration:none">Explainer Video</a></h3><p>Explain your product in 60 seconds.</p><a href="/explainer-video/" class="btn btn-outline" style="margin-top:16px">Learn more →</a></div><div class="svc-card"><div class="svc-icon">📐</div><h3><a href="/motion-graphics/" style="color:inherit;text-decoration:none">Motion Graphics</a></h3><p>Animated graphics, data and text.</p><a href="/motion-graphics/" class="btn btn-outline" style="margin-top:16px">Learn more →</a></div><div class="svc-card"><div class="svc-icon">✍️</div><h3><a href="/whiteboard-animation/" style="color:inherit;text-decoration:none">Whiteboard Animation</a></h3><p>Classic hand-drawn explainer style.</p><a href="/whiteboard-animation/" class="btn btn-outline" style="margin-top:16px">Learn more →</a></div></div></div></section>
<section class="cta">
<div class="wrap"><h2 class="h2">Ready to get started?</h2><p class="sub">Book a free call and get a quote within 24 hours.</p>
<div class="cta-btns"><a href="https://calendly.com/mikael-hamrin/30min" class="btn btn-fill btn-lg">Book Free Call →</a><a href="/pricing/" class="btn btn-outline btn-lg">See Pricing</a></div>
</div></section>
'''}
P['2d-animation/index.html']['schema'] = '''<script type="application/ld+json">{"@context":"https://schema.org","@type":"Service","name":"2D Animation Video Production","serviceType":"Custom 2D animation video production","provider":{"@id":"https://expansionvideos.com/#org"},"areaServed":"Worldwide","description":"Custom 2D animation video production. Hand-crafted characters, motion and design with professional voiceover. Our flagship since 2015. From $797.","url":"https://expansionvideos.com/2d-animation/"}</script><script type="application/ld+json">{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://expansionvideos.com/"},{"@type":"ListItem","position":2,"name":"Services","item":"https://expansionvideos.com/services/"},{"@type":"ListItem","position":3,"name":"2D Animation Video Production","item":"https://expansionvideos.com/2d-animation/"}]}</script><script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":"What is 2D animation?","acceptedAnswer":{"@type":"Answer","text":"2D animation is hand-crafted animated video using characters, illustration and motion in two dimensions. It is the most versatile and popular style for explainer and brand video."}},{"@type":"Question","name":"How much does a 2D animated video cost?","acceptedAnswer":{"@type":"Answer","text":"Custom 2D animation starts at $797 per 30 seconds. Price depends on length, scene count and style complexity."}},{"@type":"Question","name":"How long does it take?","acceptedAnswer":{"@type":"Answer","text":"Most 2D animation projects take 3 to 4 weeks from brief to final delivery."}},{"@type":"Question","name":"Can you match our brand style?","acceptedAnswer":{"@type":"Answer","text":"Yes. Every project is custom designed around your brand colors, tone and visual identity."}}]}</script>'''

P['motion-graphics/index.html'] = {
'title': 'Motion Graphics Video Production | Animated Graphics | ExpansionVideos',
'desc': 'Motion graphics production that brings data, text and brand elements to life. Perfect for product, social and presentations. From $797.',
'body': '''
<section class="hero" style="min-height:auto;padding:140px 32px 80px">
<div class="wrap"><div class="hero-text" style="max-width:100%">
    <p class="label"><a href="/services/" style="color:var(--blue,#2563eb)">← All services</a></p>
    <h1 class="h1">Motion graphics <span class="blue">that make data move</span></h1>
    <p class="sub">Motion graphics is animated text, icons, charts and logos. It is the right format when the information is the point and you want it understood fast.</p>
    <div class="hero-btns"><a href="https://calendly.com/mikael-hamrin/30min" class="btn btn-fill btn-lg">Book Free Call →</a><a href="/pricing/" class="btn btn-outline btn-lg">See Pricing</a></div>
</div></div></section>
<section class="sec" style="padding-top:80px">
<div class="wrap"><div class="sec-hdr tc"><p class="label">Motion graphics</p><h2 class="h2">Motion graphics that make data move</h2></div>
<div class="guar-grid" style="margin-top:48px"><div class="guar-card"><div class="g-icon">📊</div><h4>Data made clear</h4><p>Numbers and processes become easy to grasp when they move.</p></div><div class="guar-card"><div class="g-icon">✨</div><h4>Logo animation</h4><p>Short animated logos for intros, outros and social.</p></div><div class="guar-card"><div class="g-icon">🔤</div><h4>Kinetic typography</h4><p>Text in motion that drives the message home.</p></div></div></div></section>
<section class="sec sec-gray">
<div class="wrap"><div class="sec-hdr tc"><p class="label">Use cases</p><h2 class="h2">When it works best</h2></div>
<div class="svc-grid" style="margin-top:48px"><div class="svc-card"><div class="svc-icon">🖥️</div><h3>Websites</h3><p>Short animated sequences that explain the offer and hold attention.</p></div><div class="svc-card"><div class="svc-icon">📱</div><h3>Social and ads</h3><p>Graphics built for scroll-stopping on social feeds.</p></div><div class="svc-card"><div class="svc-icon">🎤</div><h3>Presentations</h3><p>Lift a pitch or keynote above static slides.</p></div><div class="svc-card"><div class="svc-icon">🧩</div><h3>Explain complex</h3><p>Flows and relationships that are hard to describe in text.</p></div><div class="svc-card"><div class="svc-icon">📰</div><h3>Internal comms</h3><p>Results and news packaged so the whole team takes them in.</p></div><div class="svc-card"><div class="svc-icon">🎬</div><h3>Within a film</h3><p>Often combined with animation or live action for extra clarity.</p></div></div></div></section>
<section class="sec">
<div class="wrap"><div class="sec-hdr tc"><p class="label">FAQ</p><h2 class="h2">Frequently asked questions</h2></div>
<div class="faq-grid" style="margin-top:48px"><div class="faq-card"><h4>What are motion graphics?</h4><p>Motion graphics are animated graphic elements: text, icons, shapes, charts and logos in motion. They make information clear and lively without needing characters or a story.</p></div><div class="faq-card"><h4>How are motion graphics different from animation?</h4><p>Motion graphics focus on graphic elements and data in motion. Character animation focuses on story. Many videos combine both.</p></div><div class="faq-card"><h4>How much do motion graphics cost?</h4><p>Motion graphics production starts at $797 per 30 seconds, depending on length and complexity.</p></div><div class="faq-card"><h4>Can you animate our existing brand assets?</h4><p>Yes. We can animate your logo, icons and brand system, or design new graphics from scratch.</p></div></div></div></section>
<section class="sec sec-gray">
<div class="wrap"><div class="sec-hdr tc"><p class="label">Related services</p><h2 class="h2">Explore more</h2></div>
<div class="svc-grid" style="margin-top:48px"><div class="svc-card"><div class="svc-icon">🎬</div><h3><a href="/2d-animation/" style="color:inherit;text-decoration:none">2D Animation</a></h3><p>Custom hand-crafted 2D animation.</p><a href="/2d-animation/" class="btn btn-outline" style="margin-top:16px">Learn more →</a></div><div class="svc-card"><div class="svc-icon">💡</div><h3><a href="/explainer-video/" style="color:inherit;text-decoration:none">Explainer Video</a></h3><p>Explain your product in 60 seconds.</p><a href="/explainer-video/" class="btn btn-outline" style="margin-top:16px">Learn more →</a></div><div class="svc-card"><div class="svc-icon">📦</div><h3><a href="/product-video/" style="color:inherit;text-decoration:none">Product Video</a></h3><p>Show what your product does.</p><a href="/product-video/" class="btn btn-outline" style="margin-top:16px">Learn more →</a></div></div></div></section>
<section class="cta">
<div class="wrap"><h2 class="h2">Ready to get started?</h2><p class="sub">Book a free call and get a quote within 24 hours.</p>
<div class="cta-btns"><a href="https://calendly.com/mikael-hamrin/30min" class="btn btn-fill btn-lg">Book Free Call →</a><a href="/pricing/" class="btn btn-outline btn-lg">See Pricing</a></div>
</div></section>
'''}
P['motion-graphics/index.html']['schema'] = '''<script type="application/ld+json">{"@context":"https://schema.org","@type":"Service","name":"Motion Graphics Production","serviceType":"Motion graphics and animated graphics production","provider":{"@id":"https://expansionvideos.com/#org"},"areaServed":"Worldwide","description":"Motion graphics production that brings data, text and brand elements to life. Perfect for product, social and presentations. From $797.","url":"https://expansionvideos.com/motion-graphics/"}</script><script type="application/ld+json">{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://expansionvideos.com/"},{"@type":"ListItem","position":2,"name":"Services","item":"https://expansionvideos.com/services/"},{"@type":"ListItem","position":3,"name":"Motion Graphics Production","item":"https://expansionvideos.com/motion-graphics/"}]}</script><script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":"What are motion graphics?","acceptedAnswer":{"@type":"Answer","text":"Motion graphics are animated graphic elements: text, icons, shapes, charts and logos in motion. They make information clear and lively without needing characters or a story."}},{"@type":"Question","name":"How are motion graphics different from animation?","acceptedAnswer":{"@type":"Answer","text":"Motion graphics focus on graphic elements and data in motion. Character animation focuses on story. Many videos combine both."}},{"@type":"Question","name":"How much do motion graphics cost?","acceptedAnswer":{"@type":"Answer","text":"Motion graphics production starts at $797 per 30 seconds, depending on length and complexity."}},{"@type":"Question","name":"Can you animate our existing brand assets?","acceptedAnswer":{"@type":"Answer","text":"Yes. We can animate your logo, icons and brand system, or design new graphics from scratch."}}]}</script>'''

P['product-video/index.html'] = {
'title': 'Product Video & SaaS Demo Video Production | ExpansionVideos',
'desc': 'Animated product video and SaaS demo video production that shows what your product does and why it is worth buying. For web, product pages and ads. From $797.',
'body': '''
<section class="hero" style="min-height:auto;padding:140px 32px 80px">
<div class="wrap"><div class="hero-text" style="max-width:100%">
    <p class="label"><a href="/services/" style="color:var(--blue,#2563eb)">← All services</a></p>
    <h1 class="h1">Product and SaaS video <span class="blue">that sells while you sleep</span></h1>
    <p class="sub">A product video shows what your product does and why it is worth buying. For SaaS and digital products, animation is often the clearest way to show the interface and the value.</p>
    <div class="hero-btns"><a href="https://calendly.com/mikael-hamrin/30min" class="btn btn-fill btn-lg">Book Free Call →</a><a href="/pricing/" class="btn btn-outline btn-lg">See Pricing</a></div>
</div></div></section>
<section class="sec" style="padding-top:80px">
<div class="wrap"><div class="sec-hdr tc"><p class="label">Product video</p><h2 class="h2">Product and SaaS video that sells while you sleep</h2></div>
<div class="guar-grid" style="margin-top:48px"><div class="guar-card"><div class="g-icon">🛒</div><h4>Higher conversion</h4><p>Product pages with video convert better. Buyers understand faster.</p></div><div class="guar-card"><div class="g-icon">💻</div><h4>Great for SaaS</h4><p>Show the interface and the value without asking users to guess.</p></div><div class="guar-card"><div class="g-icon">🔁</div><h4>Reusable</h4><p>One product video works on the site, in ads, in email and at events.</p></div></div></div></section>
<section class="sec sec-gray">
<div class="wrap"><div class="sec-hdr tc"><p class="label">Use cases</p><h2 class="h2">When it works best</h2></div>
<div class="svc-grid" style="margin-top:48px"><div class="svc-card"><div class="svc-icon">💻</div><h3>SaaS and apps</h3><p>Show the UI and the value for a digital product.</p></div><div class="svc-card"><div class="svc-icon">📦</div><h3>Ecommerce</h3><p>Lift product pages and social ads and reduce returns.</p></div><div class="svc-card"><div class="svc-icon">⚙️</div><h3>Tech and hardware</h3><p>Explain how a product works, including what is hidden inside.</p></div><div class="svc-card"><div class="svc-icon">🚀</div><h3>Launches</h3><p>Build anticipation and explain the new product clearly.</p></div><div class="svc-card"><div class="svc-icon">📣</div><h3>Paid ads</h3><p>Short product cutdowns built for Meta, TikTok and YouTube.</p></div><div class="svc-card"><div class="svc-icon">🤝</div><h3>Sales</h3><p>Give the team a clear demo that lands the same way every time.</p></div></div></div></section>
<section class="sec">
<div class="wrap"><div class="sec-hdr tc"><p class="label">FAQ</p><h2 class="h2">Frequently asked questions</h2></div>
<div class="faq-grid" style="margin-top:48px"><div class="faq-card"><h4>What is a product video?</h4><p>A product video is a short video that shows what a product is, what it does and why it is worth buying. Animated product video is strong when the product is digital, technical or hard to film.</p></div><div class="faq-card"><h4>Do you make SaaS demo videos?</h4><p>Yes. Animation is often the best way to show software, because we can show the interface, flows and value clearly without expensive filming.</p></div><div class="faq-card"><h4>How much does a product video cost?</h4><p>Animated product video starts at $797 per 30 seconds. AI video starts at $497. Price depends on length and complexity.</p></div><div class="faq-card"><h4>What is the difference between a product video and a demo?</h4><p>A product video sells and sparks interest. A walkthrough demo shows step by step how it is used. Many clients want both.</p></div></div></div></section>
<section class="sec sec-gray">
<div class="wrap"><div class="sec-hdr tc"><p class="label">Related services</p><h2 class="h2">Explore more</h2></div>
<div class="svc-grid" style="margin-top:48px"><div class="svc-card"><div class="svc-icon">💡</div><h3><a href="/explainer-video/" style="color:inherit;text-decoration:none">Explainer Video</a></h3><p>Explain your product in 60 seconds.</p><a href="/explainer-video/" class="btn btn-outline" style="margin-top:16px">Learn more →</a></div><div class="svc-card"><div class="svc-icon">🤖</div><h3><a href="/ai-video/" style="color:inherit;text-decoration:none">AI Video</a></h3><p>Faster, lower-cost video powered by AI.</p><a href="/ai-video/" class="btn btn-outline" style="margin-top:16px">Learn more →</a></div><div class="svc-card"><div class="svc-icon">📐</div><h3><a href="/motion-graphics/" style="color:inherit;text-decoration:none">Motion Graphics</a></h3><p>Animated graphics, data and text.</p><a href="/motion-graphics/" class="btn btn-outline" style="margin-top:16px">Learn more →</a></div></div></div></section>
<section class="cta">
<div class="wrap"><h2 class="h2">Ready to get started?</h2><p class="sub">Book a free call and get a quote within 24 hours.</p>
<div class="cta-btns"><a href="https://calendly.com/mikael-hamrin/30min" class="btn btn-fill btn-lg">Book Free Call →</a><a href="/pricing/" class="btn btn-outline btn-lg">See Pricing</a></div>
</div></section>
'''}
P['product-video/index.html']['schema'] = '''<script type="application/ld+json">{"@context":"https://schema.org","@type":"Service","name":"Product Video Production","serviceType":"Product video and SaaS demo video production","provider":{"@id":"https://expansionvideos.com/#org"},"areaServed":"Worldwide","description":"Animated product video and SaaS demo video production that shows what your product does and why it is worth buying. For web, product pages and ads. From $797.","url":"https://expansionvideos.com/product-video/"}</script><script type="application/ld+json">{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://expansionvideos.com/"},{"@type":"ListItem","position":2,"name":"Services","item":"https://expansionvideos.com/services/"},{"@type":"ListItem","position":3,"name":"Product Video Production","item":"https://expansionvideos.com/product-video/"}]}</script><script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":"What is a product video?","acceptedAnswer":{"@type":"Answer","text":"A product video is a short video that shows what a product is, what it does and why it is worth buying. Animated product video is strong when the product is digital, technical or hard to film."}},{"@type":"Question","name":"Do you make SaaS demo videos?","acceptedAnswer":{"@type":"Answer","text":"Yes. Animation is often the best way to show software, because we can show the interface, flows and value clearly without expensive filming."}},{"@type":"Question","name":"How much does a product video cost?","acceptedAnswer":{"@type":"Answer","text":"Animated product video starts at $797 per 30 seconds. AI video starts at $497. Price depends on length and complexity."}},{"@type":"Question","name":"What is the difference between a product video and a demo?","acceptedAnswer":{"@type":"Answer","text":"A product video sells and sparks interest. A walkthrough demo shows step by step how it is used. Many clients want both."}}]}</script>'''

P['whiteboard-animation/index.html'] = {
'title': 'Whiteboard Animation Video Production | ExpansionVideos',
'desc': 'Whiteboard animation video production that explains ideas with a clean hand-drawn style. Great for education, training and complex topics. From $797.',
'body': '''
<section class="hero" style="min-height:auto;padding:140px 32px 80px">
<div class="wrap"><div class="hero-text" style="max-width:100%">
    <p class="label"><a href="/services/" style="color:var(--blue,#2563eb)">← All services</a></p>
    <h1 class="h1">Whiteboard animation <span class="blue">that explains simply</span></h1>
    <p class="sub">Whiteboard animation uses a clean hand-drawn style to walk the viewer through an idea step by step. It is a calm, trustworthy format that works well for education and complex topics.</p>
    <div class="hero-btns"><a href="https://calendly.com/mikael-hamrin/30min" class="btn btn-fill btn-lg">Book Free Call →</a><a href="/pricing/" class="btn btn-outline btn-lg">See Pricing</a></div>
</div></div></section>
<section class="sec" style="padding-top:80px">
<div class="wrap"><div class="sec-hdr tc"><p class="label">Whiteboard animation</p><h2 class="h2">Whiteboard animation that explains simply</h2></div>
<div class="guar-grid" style="margin-top:48px"><div class="guar-card"><div class="g-icon">✍️</div><h4>Step by step</h4><p>The drawing-as-you-watch effect keeps attention and aids recall.</p></div><div class="guar-card"><div class="g-icon">🎓</div><h4>Great for learning</h4><p>A proven format for training, education and how-to content.</p></div><div class="guar-card"><div class="g-icon">💸</div><h4>Cost-effective</h4><p>A clean style that delivers clarity without a big budget.</p></div></div></div></section>
<section class="sec sec-gray">
<div class="wrap"><div class="sec-hdr tc"><p class="label">Use cases</p><h2 class="h2">When it works best</h2></div>
<div class="svc-grid" style="margin-top:48px"><div class="svc-card"><div class="svc-icon">🎓</div><h3>Education and e-learning</h3><p>Walk learners through a concept at a pace that sticks.</p></div><div class="svc-card"><div class="svc-icon">🏥</div><h3>Healthcare and science</h3><p>Explain processes and research with a calm, credible style.</p></div><div class="svc-card"><div class="svc-icon">🏦</div><h3>Finance and insurance</h3><p>Make complex products and rules easy to follow.</p></div><div class="svc-card"><div class="svc-icon">🏢</div><h3>Internal training</h3><p>Onboarding and process training the whole team understands.</p></div><div class="svc-card"><div class="svc-icon">🧩</div><h3>Complex ideas</h3><p>Break down an abstract concept one drawn step at a time.</p></div><div class="svc-card"><div class="svc-icon">📣</div><h3>Thought leadership</h3><p>Turn a long article or talk into a short, watchable explainer.</p></div></div></div></section>
<section class="sec">
<div class="wrap"><div class="sec-hdr tc"><p class="label">FAQ</p><h2 class="h2">Frequently asked questions</h2></div>
<div class="faq-grid" style="margin-top:48px"><div class="faq-card"><h4>What is whiteboard animation?</h4><p>Whiteboard animation is a video style where illustrations appear to be drawn by hand on a white background while a voiceover explains the idea. It is popular for education and complex topics.</p></div><div class="faq-card"><h4>How much does whiteboard animation cost?</h4><p>Whiteboard animation starts at $797 per 30 seconds, depending on length and complexity.</p></div><div class="faq-card"><h4>How long does it take?</h4><p>Most whiteboard animation projects take 3 to 4 weeks from brief to delivery.</p></div><div class="faq-card"><h4>Is whiteboard animation still effective?</h4><p>Yes, when it fits the message. For clear step-by-step explanation and education it remains one of the most watchable formats.</p></div></div></div></section>
<section class="sec sec-gray">
<div class="wrap"><div class="sec-hdr tc"><p class="label">Related services</p><h2 class="h2">Explore more</h2></div>
<div class="svc-grid" style="margin-top:48px"><div class="svc-card"><div class="svc-icon">🎬</div><h3><a href="/2d-animation/" style="color:inherit;text-decoration:none">2D Animation</a></h3><p>Custom hand-crafted 2D animation.</p><a href="/2d-animation/" class="btn btn-outline" style="margin-top:16px">Learn more →</a></div><div class="svc-card"><div class="svc-icon">💡</div><h3><a href="/explainer-video/" style="color:inherit;text-decoration:none">Explainer Video</a></h3><p>Explain your product in 60 seconds.</p><a href="/explainer-video/" class="btn btn-outline" style="margin-top:16px">Learn more →</a></div><div class="svc-card"><div class="svc-icon">🎓</div><h3><a href="/2d-animation/" style="color:inherit;text-decoration:none">Educational video</a></h3><p>Make training easier to follow.</p><a href="/2d-animation/" class="btn btn-outline" style="margin-top:16px">Learn more →</a></div></div></div></section>
<section class="cta">
<div class="wrap"><h2 class="h2">Ready to get started?</h2><p class="sub">Book a free call and get a quote within 24 hours.</p>
<div class="cta-btns"><a href="https://calendly.com/mikael-hamrin/30min" class="btn btn-fill btn-lg">Book Free Call →</a><a href="/pricing/" class="btn btn-outline btn-lg">See Pricing</a></div>
</div></section>
'''}
P['whiteboard-animation/index.html']['schema'] = '''<script type="application/ld+json">{"@context":"https://schema.org","@type":"Service","name":"Whiteboard Animation Production","serviceType":"Whiteboard animation video production","provider":{"@id":"https://expansionvideos.com/#org"},"areaServed":"Worldwide","description":"Whiteboard animation video production that explains ideas with a clean hand-drawn style. Great for education, training and complex topics. From $797.","url":"https://expansionvideos.com/whiteboard-animation/"}</script><script type="application/ld+json">{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://expansionvideos.com/"},{"@type":"ListItem","position":2,"name":"Services","item":"https://expansionvideos.com/services/"},{"@type":"ListItem","position":3,"name":"Whiteboard Animation Production","item":"https://expansionvideos.com/whiteboard-animation/"}]}</script><script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":"What is whiteboard animation?","acceptedAnswer":{"@type":"Answer","text":"Whiteboard animation is a video style where illustrations appear to be drawn by hand on a white background while a voiceover explains the idea. It is popular for education and complex topics."}},{"@type":"Question","name":"How much does whiteboard animation cost?","acceptedAnswer":{"@type":"Answer","text":"Whiteboard animation starts at $797 per 30 seconds, depending on length and complexity."}},{"@type":"Question","name":"How long does it take?","acceptedAnswer":{"@type":"Answer","text":"Most whiteboard animation projects take 3 to 4 weeks from brief to delivery."}},{"@type":"Question","name":"Is whiteboard animation still effective?","acceptedAnswer":{"@type":"Answer","text":"Yes, when it fits the message. For clear step-by-step explanation and education it remains one of the most watchable formats."}}]}</script>'''

P['blog/index.html'] = {
'title': 'Blog | Video Marketing Guides | ExpansionVideos',
'desc': 'Guides on explainer videos, animation and video marketing from ExpansionVideos.',
'body': '''
<section class="hero" style="min-height:auto;padding:140px 32px 60px">
<div class="wrap"><div class="hero-text" style="max-width:100%">
    <p class="label">Blog</p>
    <h1 class="h1">Video marketing <span class="blue">guides</span></h1>
    <p class="sub">Clear, practical guides on explainer videos, animation and video marketing.</p>
</div></div></section>
<section class="sec" style="padding-top:40px"><div class="wrap">
<div class="blog-grid"><div class="blog-card"><div class="blog-card-body"><div class="blog-date">October 3, 2026</div><h3><a href="/blog/what-is-an-explainer-video/" style="color:inherit;text-decoration:none">What is an explainer video?</a></h3><p>What is an explainer video? A complete guide: what it is, when it works, how long it should be and what it costs, with examples.</p><a href="/blog/what-is-an-explainer-video/" class="blog-link">Read more →</a></div></div><div class="blog-card"><div class="blog-card-body"><div class="blog-date">October 3, 2026</div><h3><a href="/blog/what-are-motion-graphics/" style="color:inherit;text-decoration:none">What are motion graphics?</a></h3><p>What are motion graphics? A clear explanation of animated graphics, when they fit, how they differ from animation, and what they cost.</p><a href="/blog/what-are-motion-graphics/" class="blog-link">Read more →</a></div></div><div class="blog-card"><div class="blog-card-body"><div class="blog-date">October 3, 2026</div><h3><a href="/blog/2d-vs-3d-animation/" style="color:inherit;text-decoration:none">2D vs 3D animation: which should you choose?</a></h3><p>2D vs 3D animation: how they differ in look, time and cost, and how to choose the right format for your project.</p><a href="/blog/2d-vs-3d-animation/" class="blog-link">Read more →</a></div></div></div>
</div></section>
'''}
P['blog/index.html']['schema'] = '''<script type="application/ld+json">{"@context":"https://schema.org","@type":"Blog","name":"ExpansionVideos Blog","description":"Guides on explainer videos, animation and video marketing.","url":"https://expansionvideos.com/blog/","publisher":{"@id":"https://expansionvideos.com/#org"}}</script>'''

P['blog/what-is-an-explainer-video/index.html'] = {
'title': 'What Is an Explainer Video? Guide, Examples and Pricing | ExpansionVideos',
'desc': 'What is an explainer video? A complete guide: what it is, when it works, how long it should be and what it costs, with examples.',
'body': '''
<section class="hero" style="min-height:auto;padding:140px 32px 60px">
<div class="wrap"><div class="hero-text" style="max-width:100%">
    <p class="label"><a href="/blog/" style="color:var(--blue,#2563eb)">← Blog</a></p>
    <h1 class="h1">What is an explainer video?</h1>
    <p class="sub">October 3, 2026</p>
</div></div></section>
<section class="sec" style="padding-top:40px"><div class="wrap">
<div class="article-content" style="max-width:720px;margin:0 auto">
<p>Explainer video, animated explainer, product explainer. Different names for the same thing: a short animated video, usually 60 to 90 seconds, that explains what a company does, why it matters and how a customer gets started. It often sits at the top of the homepage and is frequently the single most effective element on a website.</p><h2>When an explainer video is the right call</h2><p>An explainer video earns its keep when the message is abstract or hard to grasp in text. Think SaaS, fintech, technical services and anything where the customer needs to understand a concept before they will buy. If the product is simple and obvious, an image may be enough. If it is even slightly complex, showing it in motion pays off.</p><h2>How long should it be?</h2><p>Keep it short. 60 to 90 seconds is enough to explain the essentials without losing the viewer. For ads and social we cut down to 15 to 30 seconds. Length should follow the message and where the video will run, not the other way around.</p><h2>What is included</h2><ul><li>Script and storyboard</li><li>Professional voiceover</li><li>Custom animation and design</li><li>Music and sound effects</li><li>HD delivery for web, social and ads</li></ul><h2>What does an explainer video cost?</h2><p>Animated explainer video starts at $797 per 30 seconds, and AI video from $497. Price depends on length, scene count and number of languages. See the full breakdown on our <a href="/pricing/">pricing page</a>.</p><h2>Next steps</h2><p>Want to see what an explainer video could look like for you? Read more about our <a href="/explainer-video/">explainer video production</a>, or compare it with <a href="/motion-graphics/">motion graphics</a> and <a href="/product-video/">product video</a> if you are unsure about the format.</p>
</div></div></section>
<section class="cta"><div class="wrap"><h2 class="h2">Want to make a video?</h2><p class="sub">Book a free call and get a quote within 24 hours.</p>
<div class="cta-btns"><a href="https://calendly.com/mikael-hamrin/30min" class="btn btn-fill btn-lg">Book Free Call →</a><a href="/pricing/" class="btn btn-outline btn-lg">See Pricing</a></div></div></section>
'''}
P['blog/what-is-an-explainer-video/index.html']['schema'] = '''<script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","headline":"What is an explainer video?","datePublished":"2026-10-03","author":{"@type":"Person","name":"Mikael Hamrin"},"publisher":{"@type":"Organization","name":"ExpansionVideos","logo":{"@type":"ImageObject","url":"https://expansionvideos.com/img/logo.png"}},"mainEntityOfPage":{"@type":"WebPage","@id":"https://expansionvideos.com/blog/what-is-an-explainer-video/"},"description":"What is an explainer video? A complete guide: what it is, when it works, how long it should be and what it costs, with examples.","image":"https://expansionvideos.com/img/logo.png","url":"https://expansionvideos.com/blog/what-is-an-explainer-video/"}</script><script type="application/ld+json">{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://expansionvideos.com/"},{"@type":"ListItem","position":2,"name":"Blog","item":"https://expansionvideos.com/blog/"},{"@type":"ListItem","position":3,"name":"What is an explainer video?","item":"https://expansionvideos.com/blog/what-is-an-explainer-video/"}]}</script>'''

P['blog/what-are-motion-graphics/index.html'] = {
'title': 'What Are Motion Graphics? How Animated Graphics Work | ExpansionVideos',
'desc': 'What are motion graphics? A clear explanation of animated graphics, when they fit, how they differ from animation, and what they cost.',
'body': '''
<section class="hero" style="min-height:auto;padding:140px 32px 60px">
<div class="wrap"><div class="hero-text" style="max-width:100%">
    <p class="label"><a href="/blog/" style="color:var(--blue,#2563eb)">← Blog</a></p>
    <h1 class="h1">What are motion graphics?</h1>
    <p class="sub">October 3, 2026</p>
</div></div></section>
<section class="sec" style="padding-top:40px"><div class="wrap">
<div class="article-content" style="max-width:720px;margin:0 auto">
<p>Motion graphics are animated text, icons, shapes, charts and logos. It is the right format when the information is the point and you want it understood fast. Movement guides the eye, and an abstract number suddenly becomes easy to take in.</p><h2>Motion graphics or animation?</h2><p>The difference is simple. Motion graphics focus on graphic elements, data and text in motion. Character animation is more about story. Many productions blend both: character animation for the narrative and motion graphics for charts and numbers.</p><h2>Where motion graphics work best</h2><ul><li>Data visualization: results, statistics and reports made clear</li><li>Logo animation for intros, outros and social</li><li>Kinetic typography that drives a message home</li><li>Explaining processes and flows that are hard to describe in text</li><li>Internal comms where the whole team needs the same numbers</li></ul><h2>What does it cost?</h2><p>Motion graphics production starts at $797 per 30 seconds. Price depends on length and how advanced the graphics are. Script, design, animation, music and revisions are included.</p><h2>Read more</h2><p>Want to go deeper? See our <a href="/motion-graphics/">motion graphics</a> service, or read about <a href="/explainer-video/">explainer video</a> if you need a video that also tells a story.</p>
</div></div></section>
<section class="cta"><div class="wrap"><h2 class="h2">Want to make a video?</h2><p class="sub">Book a free call and get a quote within 24 hours.</p>
<div class="cta-btns"><a href="https://calendly.com/mikael-hamrin/30min" class="btn btn-fill btn-lg">Book Free Call →</a><a href="/pricing/" class="btn btn-outline btn-lg">See Pricing</a></div></div></section>
'''}
P['blog/what-are-motion-graphics/index.html']['schema'] = '''<script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","headline":"What are motion graphics?","datePublished":"2026-10-03","author":{"@type":"Person","name":"Mikael Hamrin"},"publisher":{"@type":"Organization","name":"ExpansionVideos","logo":{"@type":"ImageObject","url":"https://expansionvideos.com/img/logo.png"}},"mainEntityOfPage":{"@type":"WebPage","@id":"https://expansionvideos.com/blog/what-are-motion-graphics/"},"description":"What are motion graphics? A clear explanation of animated graphics, when they fit, how they differ from animation, and what they cost.","image":"https://expansionvideos.com/img/logo.png","url":"https://expansionvideos.com/blog/what-are-motion-graphics/"}</script><script type="application/ld+json">{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://expansionvideos.com/"},{"@type":"ListItem","position":2,"name":"Blog","item":"https://expansionvideos.com/blog/"},{"@type":"ListItem","position":3,"name":"What are motion graphics?","item":"https://expansionvideos.com/blog/what-are-motion-graphics/"}]}</script>'''

P['blog/2d-vs-3d-animation/index.html'] = {
'title': '2D vs 3D Animation: Which Should You Choose? | ExpansionVideos',
'desc': '2D vs 3D animation: how they differ in look, time and cost, and how to choose the right format for your project.',
'body': '''
<section class="hero" style="min-height:auto;padding:140px 32px 60px">
<div class="wrap"><div class="hero-text" style="max-width:100%">
    <p class="label"><a href="/blog/" style="color:var(--blue,#2563eb)">← Blog</a></p>
    <h1 class="h1">2D vs 3D animation: which should you choose?</h1>
    <p class="sub">October 3, 2026</p>
</div></div></section>
<section class="sec" style="padding-top:40px"><div class="wrap">
<div class="article-content" style="max-width:720px;margin:0 auto">
<p>One of the most common questions we get: should the video be 2D or 3D? Both are strong, but they solve different problems. Here is a simple guide to choosing.</p><h2>2D animation</h2><p>2D animation is hand-crafted animation using characters, illustration and motion in two dimensions. It is the most versatile and popular format for explainer and brand video. It is faster and more cost-effective than 3D, and gives a clear, warm look that is easy to tailor to your brand.</p><h2>3D animation</h2><p>3D animation builds scenes and objects in three dimensions. It fits when you need to show a physical product from every angle, a technical process in depth, or a sense of premium and realism. 3D takes longer and costs more, but opens up possibilities 2D cannot.</p><h2>How to choose</h2><ul><li>Choose 2D for explainer video, messaging and story on a tighter budget and timeline</li><li>Choose 3D for product visualization, hardware and when realism or a premium feel is decisive</li><li>Not sure? We start with the goal and recommend the format that does the most for your budget</li></ul><h2>What does it cost?</h2><p>2D animation starts at $797 per 30 seconds. 3D is quoted per project since complexity varies. See the full picture on our <a href="/pricing/">pricing page</a>.</p><h2>Read more</h2><p>Dig into <a href="/2d-animation/">2D animation</a> or compare with our <a href="/product-video/">product video</a> service, or get in touch and we will help you choose.</p>
</div></div></section>
<section class="cta"><div class="wrap"><h2 class="h2">Want to make a video?</h2><p class="sub">Book a free call and get a quote within 24 hours.</p>
<div class="cta-btns"><a href="https://calendly.com/mikael-hamrin/30min" class="btn btn-fill btn-lg">Book Free Call →</a><a href="/pricing/" class="btn btn-outline btn-lg">See Pricing</a></div></div></section>
'''}
P['blog/2d-vs-3d-animation/index.html']['schema'] = '''<script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","headline":"2D vs 3D animation: which should you choose?","datePublished":"2026-10-03","author":{"@type":"Person","name":"Mikael Hamrin"},"publisher":{"@type":"Organization","name":"ExpansionVideos","logo":{"@type":"ImageObject","url":"https://expansionvideos.com/img/logo.png"}},"mainEntityOfPage":{"@type":"WebPage","@id":"https://expansionvideos.com/blog/2d-vs-3d-animation/"},"description":"2D vs 3D animation: how they differ in look, time and cost, and how to choose the right format for your project.","image":"https://expansionvideos.com/img/logo.png","url":"https://expansionvideos.com/blog/2d-vs-3d-animation/"}</script><script type="application/ld+json">{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://expansionvideos.com/"},{"@type":"ListItem","position":2,"name":"Blog","item":"https://expansionvideos.com/blog/"},{"@type":"ListItem","position":3,"name":"2D vs 3D animation: which should you choose?","item":"https://expansionvideos.com/blog/2d-vs-3d-animation/"}]}</script>'''

P['privacy-policy/index.html'] = {
'title': 'Privacy Policy | ExpansionVideos',
'desc': 'How ExpansionVideos handles your personal data: what we collect, why, how long we keep it and your rights.',
'body': '''
<section class="hero" style="min-height:auto;padding:140px 32px 60px">
<div class="wrap"><div class="hero-text" style="max-width:100%">
    <p class="label"><a href="/" style="color:var(--blue,#2563eb)">← Home</a></p>
    <h1 class="h1">Privacy Policy</h1>
    <p class="sub">Last updated: October 3, 2026</p>
</div></div></section>
<section class="sec" style="padding-top:40px"><div class="wrap">
<div class="article-content" style="max-width:720px;margin:0 auto">
<p>ExpansionVideos, part of Villadose LLC, respects your privacy and handles your personal data responsibly. This policy explains what we collect, why, and the rights you have.</p><h2>Who we are</h2><p>Villadose LLC, operating as ExpansionVideos, Sheridan, Wyoming, USA. Contact: <a href="mailto:studio@expansionvideos.com">studio@expansionvideos.com</a>.</p><h2>What we collect</h2><p>We collect the information you provide through our contact and order forms, our booking link, or by email: name, email address, company name and the project details you share. We also collect limited technical information through cookies, see our <a href="/cookie-policy/">cookie policy</a>.</p><h2>Why we process it</h2><ul><li>To answer enquiries and provide quotes</li><li>To deliver and administer the services you order</li><li>To understand and improve the website through aggregated statistics, only with your consent</li></ul><h2>Services we use</h2><p>We share data with providers that help us run the business, only as needed: Cloudflare (hosting), Calendly (booking), our form handling for enquiries, and, where enabled, Google Analytics for statistics. We never sell your data.</p><h2>How long we keep it</h2><p>We keep enquiry data as long as needed to handle the matter and any business relationship, and thereafter as required by law. Statistics are stored in aggregated form.</p><h2>Your rights</h2><p>You may request access to, correction or deletion of your data, object to or restrict processing, and request data portability. You can withdraw consent at any time. Contact us at <a href="mailto:studio@expansionvideos.com">studio@expansionvideos.com</a>.</p><h2>Changes</h2><p>We may update this policy. The latest version is always on this page.</p>
</div></div></section>
'''}
P['privacy-policy/index.html']['schema'] = '''<script type="application/ld+json">{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://expansionvideos.com/"},{"@type":"ListItem","position":2,"name":"Privacy Policy","item":"https://expansionvideos.com/privacy-policy/"}]}</script>'''

P['terms-of-service/index.html'] = {
'title': 'Terms of Service | ExpansionVideos',
'desc': 'Terms of service for ExpansionVideos: quotes and orders, pricing, delivery, revisions, the satisfaction guarantee, rights and liability.',
'body': '''
<section class="hero" style="min-height:auto;padding:140px 32px 60px">
<div class="wrap"><div class="hero-text" style="max-width:100%">
    <p class="label"><a href="/" style="color:var(--blue,#2563eb)">← Home</a></p>
    <h1 class="h1">Terms of Service</h1>
    <p class="sub">Last updated: October 3, 2026</p>
</div></div></section>
<section class="sec" style="padding-top:40px"><div class="wrap">
<div class="article-content" style="max-width:720px;margin:0 auto">
<p>These terms apply to services delivered by ExpansionVideos, part of Villadose LLC. We keep them short and plain so it is easy to work with us.</p><h2>Quotes and orders</h2><p>We provide a free quote based on your brief. An order becomes binding once you approve the quote and scope in writing, for example by email or through our order form.</p><h2>Pricing and payment</h2><p>Prices are in US dollars unless stated otherwise. Current pricing is on our <a href="/pricing/">pricing page</a>. Payment terms appear on the invoice. For larger projects we may invoice in stages.</p><h2>Delivery and revisions</h2><p>We agree delivery time at order. The number of revision rounds is stated in the quote. We work until you are happy within the agreed scope. Significant additions beyond the agreed scope may affect price and timeline.</p><h2>Satisfaction guarantee</h2><p>We offer a satisfaction guarantee. If you are not satisfied after the agreed revision rounds, we will find a solution, which may include a refund as agreed.</p><h2>Intellectual property</h2><p>On full payment, the right to use the finished video transfers to you as agreed. We reserve the right to show finished work in our own portfolio and marketing unless agreed otherwise.</p><h2>Liability</h2><p>Our liability is limited to the amount you paid for the service in question. We are not liable for indirect damages. Nothing in these terms limits liability that cannot be limited under applicable law.</p><h2>Contact</h2><p>Questions about these terms: <a href="mailto:studio@expansionvideos.com">studio@expansionvideos.com</a>.</p>
</div></div></section>
'''}
P['terms-of-service/index.html']['schema'] = '''<script type="application/ld+json">{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://expansionvideos.com/"},{"@type":"ListItem","position":2,"name":"Terms of Service","item":"https://expansionvideos.com/terms-of-service/"}]}</script>'''

P['cookie-policy/index.html'] = {
'title': 'Cookie Policy | ExpansionVideos',
'desc': 'How ExpansionVideos uses cookies: essential cookies, click-to-load video, and consent-gated analytics.',
'body': '''
<section class="hero" style="min-height:auto;padding:140px 32px 60px">
<div class="wrap"><div class="hero-text" style="max-width:100%">
    <p class="label"><a href="/" style="color:var(--blue,#2563eb)">← Home</a></p>
    <h1 class="h1">Cookie Policy</h1>
    <p class="sub">Last updated: October 3, 2026</p>
</div></div></section>
<section class="sec" style="padding-top:40px"><div class="wrap">
<div class="article-content" style="max-width:720px;margin:0 auto">
<p>This page explains how ExpansionVideos uses cookies and similar technologies.</p><h2>What are cookies?</h2><p>Cookies are small text files stored in your browser. They are used to make a website work and to understand how it is used.</p><h2>Cookies we use</h2><ul><li><strong>Essential.</strong> Needed for the website to work. Always on.</li><li><strong>Video.</strong> We load YouTube videos only when you click play, so no video cookies are set until then.</li><li><strong>Analytics.</strong> If analytics is enabled, it loads only with your consent and helps us understand how the site is used.</li></ul><h2>Managing cookies</h2><p>You can control or delete cookies in your browser settings at any time. Blocking essential cookies may affect how the site works.</p><h2>More information</h2><p>How we handle personal data is described in our <a href="/privacy-policy/">privacy policy</a>. Questions: <a href="mailto:studio@expansionvideos.com">studio@expansionvideos.com</a>.</p>
</div></div></section>
'''}
P['cookie-policy/index.html']['schema'] = '''<script type="application/ld+json">{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://expansionvideos.com/"},{"@type":"ListItem","position":2,"name":"Cookie Policy","item":"https://expansionvideos.com/cookie-policy/"}]}</script>'''

P['recruitment-video/index.html'] = {
'title': 'Recruitment Video & Employer Branding Video | ExpansionVideos',
'desc': 'Animated recruitment video that shows your culture and attracts the right candidates. For careers pages, LinkedIn and ads. From $797.',
'body': '''
<section class="hero" style="min-height:auto;padding:140px 32px 80px">
<div class="wrap"><div class="hero-text" style="max-width:100%">
    <p class="label"><a href="/services/" style="color:var(--blue,#2563eb)">← All services</a></p>
    <h1 class="h1">Recruitment video and <span class="blue">employer branding</span></h1>
    <p class="sub">A recruitment video shows what it is really like to work with you, in a way a job ad never can. The right candidates recognise themselves, the wrong ones opt out.</p>
    <div class="hero-btns"><a href="https://calendly.com/mikael-hamrin/30min" class="btn btn-fill btn-lg">Book Free Call →</a><a href="/pricing/" class="btn btn-outline btn-lg">See Pricing</a></div>
</div></div></section>
<section class="sec" style="padding-top:80px"><div class="wrap"><div class="sec-hdr tc"><p class="label">Why recruitment video</p><h2 class="h2">Show the culture, not just the role</h2></div>
<div class="guar-grid" style="margin-top:48px">
<div class="guar-card"><div class="g-icon">🎯</div><h4>Right candidates</h4><p>Show the day-to-day honestly so the people who fit recognise themselves and apply.</p></div>
<div class="guar-card"><div class="g-icon">💬</div><h4>Consistent message</h4><p>The same employer story in every channel, from the careers page to LinkedIn.</p></div>
<div class="guar-card"><div class="g-icon">🔁</div><h4>Easy to update</h4><p>When the offer or team changes, we update the video without a new shoot.</p></div>
</div></div></section>
<section class="sec sec-gray"><div class="wrap"><div class="sec-hdr tc"><p class="label">Use cases</p><h2 class="h2">Where it works best</h2></div>
<div class="svc-grid" style="margin-top:48px">
<div class="svc-card"><div class="svc-icon">💼</div><h3>Careers page</h3><p>Give visitors a quick, honest feel for working with you.</p></div>
<div class="svc-card"><div class="svc-icon">🔗</div><h3>LinkedIn</h3><p>Employer branding that reaches passive candidates where they already are.</p></div>
<div class="svc-card"><div class="svc-icon">📣</div><h3>Recruitment ads</h3><p>Short cutdowns built for Meta, LinkedIn and YouTube.</p></div>
<div class="svc-card"><div class="svc-icon">🎓</div><h3>Onboarding</h3><p>Welcome new hires and explain culture and process from day one.</p></div>
<div class="svc-card"><div class="svc-icon">🌍</div><h3>Multiple languages</h3><p>Hiring internationally? Reuse the video with new voiceover and text.</p></div>
<div class="svc-card"><div class="svc-icon">🏢</div><h3>Career fairs</h3><p>A video that draws attention and tells your story on the stand.</p></div>
</div></div></section>
<section class="sec"><div class="wrap"><div class="sec-hdr tc"><p class="label">FAQ</p><h2 class="h2">Frequently asked questions</h2></div>
<div class="faq-grid" style="margin-top:48px">
<div class="faq-card"><h4>What is a recruitment video?</h4><p>A recruitment video is a short video that shows what it is like to work at your company: the culture, the way you work and the people. It is used on careers pages, in ads and on LinkedIn to attract the right candidates.</p></div><div class="faq-card"><h4>Why animated recruitment video?</h4><p>Animation lets you show culture, values and benefits clearly and consistently, without a big shoot. It is easy to update and works just as well in several languages.</p></div><div class="faq-card"><h4>What does a recruitment video cost?</h4><p>An animated recruitment video starts at $797 per 30 seconds. Price depends on length, scene count and number of languages. We provide a free quote.</p></div>
</div></div></section>
<section class="cta"><div class="wrap"><h2 class="h2">Ready to attract the right candidates?</h2><p class="sub">Book a free call and get a quote within 24 hours.</p>
<div class="cta-btns"><a href="https://calendly.com/mikael-hamrin/30min" class="btn btn-fill btn-lg">Book Free Call →</a><a href="/pricing/" class="btn btn-outline btn-lg">See Pricing</a></div></div></section>
'''}
P['recruitment-video/index.html']['schema'] = '''<script type="application/ld+json">{"@context":"https://schema.org","@type":"Service","name":"Recruitment Video Production","serviceType":"Recruitment and employer branding video","provider":{"@id":"https://expansionvideos.com/#org"},"areaServed":"Worldwide","description":"Animated recruitment video and employer branding video that shows your culture and attracts the right candidates. From $797.","url":"https://expansionvideos.com/recruitment-video/"}</script><script type="application/ld+json">{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://expansionvideos.com/"},{"@type":"ListItem","position":2,"name":"Services","item":"https://expansionvideos.com/services/"},{"@type":"ListItem","position":3,"name":"Recruitment Video","item":"https://expansionvideos.com/recruitment-video/"}]}</script><script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":"What is a recruitment video?","acceptedAnswer":{"@type":"Answer","text":"A recruitment video is a short video that shows what it is like to work at your company: the culture, the way you work and the people. It is used on careers pages, in ads and on LinkedIn to attract the right candidates."}},{"@type":"Question","name":"Why animated recruitment video?","acceptedAnswer":{"@type":"Answer","text":"Animation lets you show culture, values and benefits clearly and consistently, without a big shoot. It is easy to update and works just as well in several languages."}},{"@type":"Question","name":"What does a recruitment video cost?","acceptedAnswer":{"@type":"Answer","text":"An animated recruitment video starts at $797 per 30 seconds. Price depends on length, scene count and number of languages. We provide a free quote."}}]}</script>'''

P['portfolio/index.html'] = {
'title': 'Portfolio | Animated Explainer Video Examples | ExpansionVideos',
'desc': 'See animated explainer videos we have produced for companies worldwide: Deloitte, Toyota, Veritas, Assignar, Metaforce and many more.',
'body': '''
<section class="hero" style="min-height:auto;padding:140px 32px 60px">
<div class="wrap"><div class="hero-text" style="max-width:100%">
<p class="label">Portfolio</p>
<h1 class="h1">See our videos in <span class="blue">action</span></h1>
<p class="sub">A selection of animated explainer videos we have produced for companies worldwide. Click any film to play it.</p>
</div></div></section>
<section class="sec" style="padding-top:40px"><div class="wrap">
<div class="port-grid">
<div class="port-card"><div class="port-video"><div class="yt-facade" onclick="this.outerHTML='<iframe loading=&quot;lazy&quot; src=&quot;https://www.youtube.com/embed/CD86XpxKh48?rel=0&autoplay=1&quot; title=&quot;Deloitte - ExpansionVideos&quot; allow=&quot;accelerometer;autoplay;clipboard-write;encrypted-media;gyroscope;picture-in-picture&quot; allowfullscreen style=&quot;position:absolute;inset:0;width:100%;height:100%;border:none&quot;></iframe>'" style="position:absolute;inset:0;background:#000 url('https://i.ytimg.com/vi/CD86XpxKh48/hqdefault.jpg') center/cover no-repeat;cursor:pointer" role="button" aria-label="Play video for Deloitte"><div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;background:rgba(0,0,0,0.28)"><div style="width:64px;height:64px;background:#ff0000;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;font-size:22px">▶</div></div></div></div><div class="port-info"><h4>Deloitte</h4><p>Audit, tax, consulting and risk advisory</p></div></div>
<div class="port-card"><div class="port-video"><div class="yt-facade" onclick="this.outerHTML='<iframe loading=&quot;lazy&quot; src=&quot;https://www.youtube.com/embed/MbDgRyaIUwc?rel=0&autoplay=1&quot; title=&quot;Toyota - ExpansionVideos&quot; allow=&quot;accelerometer;autoplay;clipboard-write;encrypted-media;gyroscope;picture-in-picture&quot; allowfullscreen style=&quot;position:absolute;inset:0;width:100%;height:100%;border:none&quot;></iframe>'" style="position:absolute;inset:0;background:#000 url('https://i.ytimg.com/vi/MbDgRyaIUwc/hqdefault.jpg') center/cover no-repeat;cursor:pointer" role="button" aria-label="Play video for Toyota"><div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;background:rgba(0,0,0,0.28)"><div style="width:64px;height:64px;background:#ff0000;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;font-size:22px">▶</div></div></div></div><div class="port-info"><h4>Toyota</h4><p>Electric and hybrid cars explainer</p></div></div>
<div class="port-card"><div class="port-video"><div class="yt-facade" onclick="this.outerHTML='<iframe loading=&quot;lazy&quot; src=&quot;https://www.youtube.com/embed/3jhOxZUxheY?rel=0&autoplay=1&quot; title=&quot;Veritas - ExpansionVideos&quot; allow=&quot;accelerometer;autoplay;clipboard-write;encrypted-media;gyroscope;picture-in-picture&quot; allowfullscreen style=&quot;position:absolute;inset:0;width:100%;height:100%;border:none&quot;></iframe>'" style="position:absolute;inset:0;background:#000 url('https://i.ytimg.com/vi/3jhOxZUxheY/hqdefault.jpg') center/cover no-repeat;cursor:pointer" role="button" aria-label="Play video for Veritas"><div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;background:rgba(0,0,0,0.28)"><div style="width:64px;height:64px;background:#ff0000;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;font-size:22px">▶</div></div></div></div><div class="port-info"><h4>Veritas</h4><p>Data management explainer</p></div></div>
<div class="port-card"><div class="port-video"><div class="yt-facade" onclick="this.outerHTML='<iframe loading=&quot;lazy&quot; src=&quot;https://www.youtube.com/embed/RxOZTHFAbZM?rel=0&autoplay=1&quot; title=&quot;Ridian - ExpansionVideos&quot; allow=&quot;accelerometer;autoplay;clipboard-write;encrypted-media;gyroscope;picture-in-picture&quot; allowfullscreen style=&quot;position:absolute;inset:0;width:100%;height:100%;border:none&quot;></iframe>'" style="position:absolute;inset:0;background:#000 url('https://i.ytimg.com/vi/RxOZTHFAbZM/hqdefault.jpg') center/cover no-repeat;cursor:pointer" role="button" aria-label="Play video for Ridian"><div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;background:rgba(0,0,0,0.28)"><div style="width:64px;height:64px;background:#ff0000;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;font-size:22px">▶</div></div></div></div><div class="port-info"><h4>Ridian</h4><p>Animated 2D explainer</p></div></div>
<div class="port-card"><div class="port-video"><div class="yt-facade" onclick="this.outerHTML='<iframe loading=&quot;lazy&quot; src=&quot;https://www.youtube.com/embed/fX9SFWBZztI?rel=0&autoplay=1&quot; title=&quot;Aigo - ExpansionVideos&quot; allow=&quot;accelerometer;autoplay;clipboard-write;encrypted-media;gyroscope;picture-in-picture&quot; allowfullscreen style=&quot;position:absolute;inset:0;width:100%;height:100%;border:none&quot;></iframe>'" style="position:absolute;inset:0;background:#000 url('https://i.ytimg.com/vi/fX9SFWBZztI/hqdefault.jpg') center/cover no-repeat;cursor:pointer" role="button" aria-label="Play video for Aigo"><div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;background:rgba(0,0,0,0.28)"><div style="width:64px;height:64px;background:#ff0000;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;font-size:22px">▶</div></div></div></div><div class="port-info"><h4>Aigo</h4><p>Animated 2D explainer</p></div></div>
<div class="port-card"><div class="port-video"><div class="yt-facade" onclick="this.outerHTML='<iframe loading=&quot;lazy&quot; src=&quot;https://www.youtube.com/embed/AyB-U1NJL9U?rel=0&autoplay=1&quot; title=&quot;MAPS - ExpansionVideos&quot; allow=&quot;accelerometer;autoplay;clipboard-write;encrypted-media;gyroscope;picture-in-picture&quot; allowfullscreen style=&quot;position:absolute;inset:0;width:100%;height:100%;border:none&quot;></iframe>'" style="position:absolute;inset:0;background:#000 url('https://i.ytimg.com/vi/AyB-U1NJL9U/hqdefault.jpg') center/cover no-repeat;cursor:pointer" role="button" aria-label="Play video for MAPS"><div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;background:rgba(0,0,0,0.28)"><div style="width:64px;height:64px;background:#ff0000;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;font-size:22px">▶</div></div></div></div><div class="port-info"><h4>MAPS</h4><p>Animated 2D explainer</p></div></div>
<div class="port-card"><div class="port-video"><div class="yt-facade" onclick="this.outerHTML='<iframe loading=&quot;lazy&quot; src=&quot;https://www.youtube.com/embed/6IrrbP4ZwR4?rel=0&autoplay=1&quot; title=&quot;Pacific West - ExpansionVideos&quot; allow=&quot;accelerometer;autoplay;clipboard-write;encrypted-media;gyroscope;picture-in-picture&quot; allowfullscreen style=&quot;position:absolute;inset:0;width:100%;height:100%;border:none&quot;></iframe>'" style="position:absolute;inset:0;background:#000 url('https://i.ytimg.com/vi/6IrrbP4ZwR4/hqdefault.jpg') center/cover no-repeat;cursor:pointer" role="button" aria-label="Play video for Pacific West"><div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;background:rgba(0,0,0,0.28)"><div style="width:64px;height:64px;background:#ff0000;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;font-size:22px">▶</div></div></div></div><div class="port-info"><h4>Pacific West</h4><p>Animated 2D and 3D film</p></div></div>
<div class="port-card"><div class="port-video"><div class="yt-facade" onclick="this.outerHTML='<iframe loading=&quot;lazy&quot; src=&quot;https://www.youtube.com/embed/Cct44jluKnQ?rel=0&autoplay=1&quot; title=&quot;Metaforce - ExpansionVideos&quot; allow=&quot;accelerometer;autoplay;clipboard-write;encrypted-media;gyroscope;picture-in-picture&quot; allowfullscreen style=&quot;position:absolute;inset:0;width:100%;height:100%;border:none&quot;></iframe>'" style="position:absolute;inset:0;background:#000 url('https://i.ytimg.com/vi/Cct44jluKnQ/hqdefault.jpg') center/cover no-repeat;cursor:pointer" role="button" aria-label="Play video for Metaforce"><div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;background:rgba(0,0,0,0.28)"><div style="width:64px;height:64px;background:#ff0000;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;font-size:22px">▶</div></div></div></div><div class="port-info"><h4>Metaforce</h4><p>Explainer for a data-driven company</p></div></div>
<div class="port-card"><div class="port-video"><div class="yt-facade" onclick="this.outerHTML='<iframe loading=&quot;lazy&quot; src=&quot;https://www.youtube.com/embed/ZUg7hfg2hAY?rel=0&autoplay=1&quot; title=&quot;Assignar - ExpansionVideos&quot; allow=&quot;accelerometer;autoplay;clipboard-write;encrypted-media;gyroscope;picture-in-picture&quot; allowfullscreen style=&quot;position:absolute;inset:0;width:100%;height:100%;border:none&quot;></iframe>'" style="position:absolute;inset:0;background:#000 url('https://i.ytimg.com/vi/ZUg7hfg2hAY/hqdefault.jpg') center/cover no-repeat;cursor:pointer" role="button" aria-label="Play video for Assignar"><div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;background:rgba(0,0,0,0.28)"><div style="width:64px;height:64px;background:#ff0000;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;font-size:22px">▶</div></div></div></div><div class="port-info"><h4>Assignar</h4><p>SaaS explainer video</p></div></div>
<div class="port-card"><div class="port-video"><div class="yt-facade" onclick="this.outerHTML='<iframe loading=&quot;lazy&quot; src=&quot;https://www.youtube.com/embed/KYmFe1HMOgw?rel=0&autoplay=1&quot; title=&quot;CaCharge - ExpansionVideos&quot; allow=&quot;accelerometer;autoplay;clipboard-write;encrypted-media;gyroscope;picture-in-picture&quot; allowfullscreen style=&quot;position:absolute;inset:0;width:100%;height:100%;border:none&quot;></iframe>'" style="position:absolute;inset:0;background:#000 url('https://i.ytimg.com/vi/KYmFe1HMOgw/hqdefault.jpg') center/cover no-repeat;cursor:pointer" role="button" aria-label="Play video for CaCharge"><div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;background:rgba(0,0,0,0.28)"><div style="width:64px;height:64px;background:#ff0000;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;font-size:22px">▶</div></div></div></div><div class="port-info"><h4>CaCharge</h4><p>Car service station explainer</p></div></div>
<div class="port-card"><div class="port-video"><div class="yt-facade" onclick="this.outerHTML='<iframe loading=&quot;lazy&quot; src=&quot;https://www.youtube.com/embed/DmiSolaqGJM?rel=0&autoplay=1&quot; title=&quot;Priceindx - ExpansionVideos&quot; allow=&quot;accelerometer;autoplay;clipboard-write;encrypted-media;gyroscope;picture-in-picture&quot; allowfullscreen style=&quot;position:absolute;inset:0;width:100%;height:100%;border:none&quot;></iframe>'" style="position:absolute;inset:0;background:#000 url('https://i.ytimg.com/vi/DmiSolaqGJM/hqdefault.jpg') center/cover no-repeat;cursor:pointer" role="button" aria-label="Play video for Priceindx"><div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;background:rgba(0,0,0,0.28)"><div style="width:64px;height:64px;background:#ff0000;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;font-size:22px">▶</div></div></div></div><div class="port-info"><h4>Priceindx</h4><p>Ecommerce app explainer</p></div></div>
<div class="port-card"><div class="port-video"><div class="yt-facade" onclick="this.outerHTML='<iframe loading=&quot;lazy&quot; src=&quot;https://www.youtube.com/embed/rUqOgZer5jQ?rel=0&autoplay=1&quot; title=&quot;Globanet - ExpansionVideos&quot; allow=&quot;accelerometer;autoplay;clipboard-write;encrypted-media;gyroscope;picture-in-picture&quot; allowfullscreen style=&quot;position:absolute;inset:0;width:100%;height:100%;border:none&quot;></iframe>'" style="position:absolute;inset:0;background:#000 url('https://i.ytimg.com/vi/rUqOgZer5jQ/hqdefault.jpg') center/cover no-repeat;cursor:pointer" role="button" aria-label="Play video for Globanet"><div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;background:rgba(0,0,0,0.28)"><div style="width:64px;height:64px;background:#ff0000;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;font-size:22px">▶</div></div></div></div><div class="port-info"><h4>Globanet</h4><p>Collaboration and compliance tools</p></div></div>
<div class="port-card"><div class="port-video"><div class="yt-facade" onclick="this.outerHTML='<iframe loading=&quot;lazy&quot; src=&quot;https://www.youtube.com/embed/RbbfxJw6cO8?rel=0&autoplay=1&quot; title=&quot;COS Systems - ExpansionVideos&quot; allow=&quot;accelerometer;autoplay;clipboard-write;encrypted-media;gyroscope;picture-in-picture&quot; allowfullscreen style=&quot;position:absolute;inset:0;width:100%;height:100%;border:none&quot;></iframe>'" style="position:absolute;inset:0;background:#000 url('https://i.ytimg.com/vi/RbbfxJw6cO8/hqdefault.jpg') center/cover no-repeat;cursor:pointer" role="button" aria-label="Play video for COS Systems"><div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;background:rgba(0,0,0,0.28)"><div style="width:64px;height:64px;background:#ff0000;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;font-size:22px">▶</div></div></div></div><div class="port-info"><h4>COS Systems</h4><p>Product explainer video</p></div></div>
<div class="port-card"><div class="port-video"><div class="yt-facade" onclick="this.outerHTML='<iframe loading=&quot;lazy&quot; src=&quot;https://www.youtube.com/embed/08gkvA02s9g?rel=0&autoplay=1&quot; title=&quot;Naneco - ExpansionVideos&quot; allow=&quot;accelerometer;autoplay;clipboard-write;encrypted-media;gyroscope;picture-in-picture&quot; allowfullscreen style=&quot;position:absolute;inset:0;width:100%;height:100%;border:none&quot;></iframe>'" style="position:absolute;inset:0;background:#000 url('https://i.ytimg.com/vi/08gkvA02s9g/hqdefault.jpg') center/cover no-repeat;cursor:pointer" role="button" aria-label="Play video for Naneco"><div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;background:rgba(0,0,0,0.28)"><div style="width:64px;height:64px;background:#ff0000;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;font-size:22px">▶</div></div></div></div><div class="port-info"><h4>Naneco</h4><p>Animated 2D explainer</p></div></div>
<div class="port-card"><div class="port-video"><div class="yt-facade" onclick="this.outerHTML='<iframe loading=&quot;lazy&quot; src=&quot;https://www.youtube.com/embed/yIdu7JiDUNo?rel=0&autoplay=1&quot; title=&quot;Sellmate - ExpansionVideos&quot; allow=&quot;accelerometer;autoplay;clipboard-write;encrypted-media;gyroscope;picture-in-picture&quot; allowfullscreen style=&quot;position:absolute;inset:0;width:100%;height:100%;border:none&quot;></iframe>'" style="position:absolute;inset:0;background:#000 url('https://i.ytimg.com/vi/yIdu7JiDUNo/hqdefault.jpg') center/cover no-repeat;cursor:pointer" role="button" aria-label="Play video for Sellmate"><div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;background:rgba(0,0,0,0.28)"><div style="width:64px;height:64px;background:#ff0000;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;font-size:22px">▶</div></div></div></div><div class="port-info"><h4>Sellmate</h4><p>Animation explainer video</p></div></div>
<div class="port-card"><div class="port-video"><div class="yt-facade" onclick="this.outerHTML='<iframe loading=&quot;lazy&quot; src=&quot;https://www.youtube.com/embed/bBmUMH04Ky4?rel=0&autoplay=1&quot; title=&quot;Stuvo - ExpansionVideos&quot; allow=&quot;accelerometer;autoplay;clipboard-write;encrypted-media;gyroscope;picture-in-picture&quot; allowfullscreen style=&quot;position:absolute;inset:0;width:100%;height:100%;border:none&quot;></iframe>'" style="position:absolute;inset:0;background:#000 url('https://i.ytimg.com/vi/bBmUMH04Ky4/hqdefault.jpg') center/cover no-repeat;cursor:pointer" role="button" aria-label="Play video for Stuvo"><div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;background:rgba(0,0,0,0.28)"><div style="width:64px;height:64px;background:#ff0000;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;font-size:22px">▶</div></div></div></div><div class="port-info"><h4>Stuvo</h4><p>Storage service explainer</p></div></div>
<div class="port-card"><div class="port-video"><div class="yt-facade" onclick="this.outerHTML='<iframe loading=&quot;lazy&quot; src=&quot;https://www.youtube.com/embed/nzBflthtJ3s?rel=0&autoplay=1&quot; title=&quot;Kattis - ExpansionVideos&quot; allow=&quot;accelerometer;autoplay;clipboard-write;encrypted-media;gyroscope;picture-in-picture&quot; allowfullscreen style=&quot;position:absolute;inset:0;width:100%;height:100%;border:none&quot;></iframe>'" style="position:absolute;inset:0;background:#000 url('https://i.ytimg.com/vi/nzBflthtJ3s/hqdefault.jpg') center/cover no-repeat;cursor:pointer" role="button" aria-label="Play video for Kattis"><div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;background:rgba(0,0,0,0.28)"><div style="width:64px;height:64px;background:#ff0000;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;font-size:22px">▶</div></div></div></div><div class="port-info"><h4>Kattis</h4><p>Code and programming explainer</p></div></div>
<div class="port-card"><div class="port-video"><div class="yt-facade" onclick="this.outerHTML='<iframe loading=&quot;lazy&quot; src=&quot;https://www.youtube.com/embed/qxFqxoHW2ok?rel=0&autoplay=1&quot; title=&quot;Zelly - ExpansionVideos&quot; allow=&quot;accelerometer;autoplay;clipboard-write;encrypted-media;gyroscope;picture-in-picture&quot; allowfullscreen style=&quot;position:absolute;inset:0;width:100%;height:100%;border:none&quot;></iframe>'" style="position:absolute;inset:0;background:#000 url('https://i.ytimg.com/vi/qxFqxoHW2ok/hqdefault.jpg') center/cover no-repeat;cursor:pointer" role="button" aria-label="Play video for Zelly"><div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;background:rgba(0,0,0,0.28)"><div style="width:64px;height:64px;background:#ff0000;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;font-size:22px">▶</div></div></div></div><div class="port-info"><h4>Zelly</h4><p>Software company explainer</p></div></div>
<div class="port-card"><div class="port-video"><div class="yt-facade" onclick="this.outerHTML='<iframe loading=&quot;lazy&quot; src=&quot;https://www.youtube.com/embed/oK-3gX7if3k?rel=0&autoplay=1&quot; title=&quot;Merge1 - ExpansionVideos&quot; allow=&quot;accelerometer;autoplay;clipboard-write;encrypted-media;gyroscope;picture-in-picture&quot; allowfullscreen style=&quot;position:absolute;inset:0;width:100%;height:100%;border:none&quot;></iframe>'" style="position:absolute;inset:0;background:#000 url('https://i.ytimg.com/vi/oK-3gX7if3k/hqdefault.jpg') center/cover no-repeat;cursor:pointer" role="button" aria-label="Play video for Merge1"><div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;background:rgba(0,0,0,0.28)"><div style="width:64px;height:64px;background:#ff0000;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;font-size:22px">▶</div></div></div></div><div class="port-info"><h4>Merge1</h4><p>Rebranding explainer video</p></div></div>
<div class="port-card"><div class="port-video"><div class="yt-facade" onclick="this.outerHTML='<iframe loading=&quot;lazy&quot; src=&quot;https://www.youtube.com/embed/hPiSgR8LxIQ?rel=0&autoplay=1&quot; title=&quot;Enyo Tech - ExpansionVideos&quot; allow=&quot;accelerometer;autoplay;clipboard-write;encrypted-media;gyroscope;picture-in-picture&quot; allowfullscreen style=&quot;position:absolute;inset:0;width:100%;height:100%;border:none&quot;></iframe>'" style="position:absolute;inset:0;background:#000 url('https://i.ytimg.com/vi/hPiSgR8LxIQ/hqdefault.jpg') center/cover no-repeat;cursor:pointer" role="button" aria-label="Play video for Enyo Tech"><div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;background:rgba(0,0,0,0.28)"><div style="width:64px;height:64px;background:#ff0000;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;font-size:22px">▶</div></div></div></div><div class="port-info"><h4>Enyo Tech</h4><p>Business explainer video</p></div></div>
<div class="port-card"><div class="port-video"><div class="yt-facade" onclick="this.outerHTML='<iframe loading=&quot;lazy&quot; src=&quot;https://www.youtube.com/embed/C4H3reyMGwA?rel=0&autoplay=1&quot; title=&quot;Yalla Build - ExpansionVideos&quot; allow=&quot;accelerometer;autoplay;clipboard-write;encrypted-media;gyroscope;picture-in-picture&quot; allowfullscreen style=&quot;position:absolute;inset:0;width:100%;height:100%;border:none&quot;></iframe>'" style="position:absolute;inset:0;background:#000 url('https://i.ytimg.com/vi/C4H3reyMGwA/hqdefault.jpg') center/cover no-repeat;cursor:pointer" role="button" aria-label="Play video for Yalla Build"><div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;background:rgba(0,0,0,0.28)"><div style="width:64px;height:64px;background:#ff0000;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;font-size:22px">▶</div></div></div></div><div class="port-info"><h4>Yalla Build</h4><p>Website explainer video</p></div></div>
<div class="port-card"><div class="port-video"><div class="yt-facade" onclick="this.outerHTML='<iframe loading=&quot;lazy&quot; src=&quot;https://www.youtube.com/embed/PQkPjduArjQ?rel=0&autoplay=1&quot; title=&quot;Linqspot - ExpansionVideos&quot; allow=&quot;accelerometer;autoplay;clipboard-write;encrypted-media;gyroscope;picture-in-picture&quot; allowfullscreen style=&quot;position:absolute;inset:0;width:100%;height:100%;border:none&quot;></iframe>'" style="position:absolute;inset:0;background:#000 url('https://i.ytimg.com/vi/PQkPjduArjQ/hqdefault.jpg') center/cover no-repeat;cursor:pointer" role="button" aria-label="Play video for Linqspot"><div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;background:rgba(0,0,0,0.28)"><div style="width:64px;height:64px;background:#ff0000;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;font-size:22px">▶</div></div></div></div><div class="port-info"><h4>Linqspot</h4><p>Animated 2D explainer</p></div></div>
</div></div></section>
<section class="cta"><div class="wrap"><h2 class="h2">Want a video like these?</h2><p class="sub">Book a free call and get a quote within 24 hours.</p>
<div class="cta-btns"><a href="https://calendly.com/mikael-hamrin/30min" class="btn btn-fill btn-lg">Book Free Call →</a><a href="/pricing/" class="btn btn-outline btn-lg">See Pricing</a></div></div></section>
'''}
P['portfolio/index.html']['schema'] = '''<script type="application/ld+json">{"@context":"https://schema.org","@type":"CollectionPage","name":"Portfolio - ExpansionVideos","url":"https://expansionvideos.com/portfolio/","description":"A selection of animated explainer videos produced for companies worldwide.","hasPart":[{"@type":"VideoObject","name":"Deloitte - animated explainer video","description":"Audit, tax, consulting and risk advisory","thumbnailUrl":"https://i.ytimg.com/vi/CD86XpxKh48/hqdefault.jpg","embedUrl":"https://www.youtube.com/embed/CD86XpxKh48","contentUrl":"https://www.youtube.com/watch?v=CD86XpxKh48"},{"@type":"VideoObject","name":"Toyota - animated explainer video","description":"Electric and hybrid cars explainer","thumbnailUrl":"https://i.ytimg.com/vi/MbDgRyaIUwc/hqdefault.jpg","embedUrl":"https://www.youtube.com/embed/MbDgRyaIUwc","contentUrl":"https://www.youtube.com/watch?v=MbDgRyaIUwc"},{"@type":"VideoObject","name":"Veritas - animated explainer video","description":"Data management explainer","thumbnailUrl":"https://i.ytimg.com/vi/3jhOxZUxheY/hqdefault.jpg","embedUrl":"https://www.youtube.com/embed/3jhOxZUxheY","contentUrl":"https://www.youtube.com/watch?v=3jhOxZUxheY"},{"@type":"VideoObject","name":"Ridian - animated explainer video","description":"Animated 2D explainer","thumbnailUrl":"https://i.ytimg.com/vi/RxOZTHFAbZM/hqdefault.jpg","embedUrl":"https://www.youtube.com/embed/RxOZTHFAbZM","contentUrl":"https://www.youtube.com/watch?v=RxOZTHFAbZM"},{"@type":"VideoObject","name":"Aigo - animated explainer video","description":"Animated 2D explainer","thumbnailUrl":"https://i.ytimg.com/vi/fX9SFWBZztI/hqdefault.jpg","embedUrl":"https://www.youtube.com/embed/fX9SFWBZztI","contentUrl":"https://www.youtube.com/watch?v=fX9SFWBZztI"},{"@type":"VideoObject","name":"MAPS - animated explainer video","description":"Animated 2D explainer","thumbnailUrl":"https://i.ytimg.com/vi/AyB-U1NJL9U/hqdefault.jpg","embedUrl":"https://www.youtube.com/embed/AyB-U1NJL9U","contentUrl":"https://www.youtube.com/watch?v=AyB-U1NJL9U"},{"@type":"VideoObject","name":"Pacific West - animated explainer video","description":"Animated 2D and 3D film","thumbnailUrl":"https://i.ytimg.com/vi/6IrrbP4ZwR4/hqdefault.jpg","embedUrl":"https://www.youtube.com/embed/6IrrbP4ZwR4","contentUrl":"https://www.youtube.com/watch?v=6IrrbP4ZwR4"},{"@type":"VideoObject","name":"Metaforce - animated explainer video","description":"Explainer for a data-driven company","thumbnailUrl":"https://i.ytimg.com/vi/Cct44jluKnQ/hqdefault.jpg","embedUrl":"https://www.youtube.com/embed/Cct44jluKnQ","contentUrl":"https://www.youtube.com/watch?v=Cct44jluKnQ"},{"@type":"VideoObject","name":"Assignar - animated explainer video","description":"SaaS explainer video","thumbnailUrl":"https://i.ytimg.com/vi/ZUg7hfg2hAY/hqdefault.jpg","embedUrl":"https://www.youtube.com/embed/ZUg7hfg2hAY","contentUrl":"https://www.youtube.com/watch?v=ZUg7hfg2hAY"},{"@type":"VideoObject","name":"CaCharge - animated explainer video","description":"Car service station explainer","thumbnailUrl":"https://i.ytimg.com/vi/KYmFe1HMOgw/hqdefault.jpg","embedUrl":"https://www.youtube.com/embed/KYmFe1HMOgw","contentUrl":"https://www.youtube.com/watch?v=KYmFe1HMOgw"},{"@type":"VideoObject","name":"Priceindx - animated explainer video","description":"Ecommerce app explainer","thumbnailUrl":"https://i.ytimg.com/vi/DmiSolaqGJM/hqdefault.jpg","embedUrl":"https://www.youtube.com/embed/DmiSolaqGJM","contentUrl":"https://www.youtube.com/watch?v=DmiSolaqGJM"},{"@type":"VideoObject","name":"Globanet - animated explainer video","description":"Collaboration and compliance tools","thumbnailUrl":"https://i.ytimg.com/vi/rUqOgZer5jQ/hqdefault.jpg","embedUrl":"https://www.youtube.com/embed/rUqOgZer5jQ","contentUrl":"https://www.youtube.com/watch?v=rUqOgZer5jQ"},{"@type":"VideoObject","name":"COS Systems - animated explainer video","description":"Product explainer video","thumbnailUrl":"https://i.ytimg.com/vi/RbbfxJw6cO8/hqdefault.jpg","embedUrl":"https://www.youtube.com/embed/RbbfxJw6cO8","contentUrl":"https://www.youtube.com/watch?v=RbbfxJw6cO8"},{"@type":"VideoObject","name":"Naneco - animated explainer video","description":"Animated 2D explainer","thumbnailUrl":"https://i.ytimg.com/vi/08gkvA02s9g/hqdefault.jpg","embedUrl":"https://www.youtube.com/embed/08gkvA02s9g","contentUrl":"https://www.youtube.com/watch?v=08gkvA02s9g"},{"@type":"VideoObject","name":"Sellmate - animated explainer video","description":"Animation explainer video","thumbnailUrl":"https://i.ytimg.com/vi/yIdu7JiDUNo/hqdefault.jpg","embedUrl":"https://www.youtube.com/embed/yIdu7JiDUNo","contentUrl":"https://www.youtube.com/watch?v=yIdu7JiDUNo"},{"@type":"VideoObject","name":"Stuvo - animated explainer video","description":"Storage service explainer","thumbnailUrl":"https://i.ytimg.com/vi/bBmUMH04Ky4/hqdefault.jpg","embedUrl":"https://www.youtube.com/embed/bBmUMH04Ky4","contentUrl":"https://www.youtube.com/watch?v=bBmUMH04Ky4"},{"@type":"VideoObject","name":"Kattis - animated explainer video","description":"Code and programming explainer","thumbnailUrl":"https://i.ytimg.com/vi/nzBflthtJ3s/hqdefault.jpg","embedUrl":"https://www.youtube.com/embed/nzBflthtJ3s","contentUrl":"https://www.youtube.com/watch?v=nzBflthtJ3s"},{"@type":"VideoObject","name":"Zelly - animated explainer video","description":"Software company explainer","thumbnailUrl":"https://i.ytimg.com/vi/qxFqxoHW2ok/hqdefault.jpg","embedUrl":"https://www.youtube.com/embed/qxFqxoHW2ok","contentUrl":"https://www.youtube.com/watch?v=qxFqxoHW2ok"},{"@type":"VideoObject","name":"Merge1 - animated explainer video","description":"Rebranding explainer video","thumbnailUrl":"https://i.ytimg.com/vi/oK-3gX7if3k/hqdefault.jpg","embedUrl":"https://www.youtube.com/embed/oK-3gX7if3k","contentUrl":"https://www.youtube.com/watch?v=oK-3gX7if3k"},{"@type":"VideoObject","name":"Enyo Tech - animated explainer video","description":"Business explainer video","thumbnailUrl":"https://i.ytimg.com/vi/hPiSgR8LxIQ/hqdefault.jpg","embedUrl":"https://www.youtube.com/embed/hPiSgR8LxIQ","contentUrl":"https://www.youtube.com/watch?v=hPiSgR8LxIQ"},{"@type":"VideoObject","name":"Yalla Build - animated explainer video","description":"Website explainer video","thumbnailUrl":"https://i.ytimg.com/vi/C4H3reyMGwA/hqdefault.jpg","embedUrl":"https://www.youtube.com/embed/C4H3reyMGwA","contentUrl":"https://www.youtube.com/watch?v=C4H3reyMGwA"},{"@type":"VideoObject","name":"Linqspot - animated explainer video","description":"Animated 2D explainer","thumbnailUrl":"https://i.ytimg.com/vi/PQkPjduArjQ/hqdefault.jpg","embedUrl":"https://www.youtube.com/embed/PQkPjduArjQ","contentUrl":"https://www.youtube.com/watch?v=PQkPjduArjQ"}]}</script><script type="application/ld+json">{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://expansionvideos.com/"},{"@type":"ListItem","position":2,"name":"Portfolio","item":"https://expansionvideos.com/portfolio/"}]}</script>'''

FAB = '<a href="/order/" class="order-fab" aria-label="Order now">Order now →</a><style>.order-fab{position:fixed;right:20px;bottom:20px;z-index:99990;background:var(--blue,#2563eb);color:#fff;font-family:-apple-system,BlinkMacSystemFont,sans-serif;font-weight:800;font-size:15px;letter-spacing:.3px;padding:14px 26px;border-radius:100px;box-shadow:0 6px 24px rgba(0,0,0,.28);text-decoration:none;transition:transform .2s,box-shadow .2s}.order-fab:hover{transform:translateY(-2px);box-shadow:0 10px 30px rgba(0,0,0,.38);color:#fff}@media(max-width:768px){.order-fab{right:14px;bottom:14px;padding:12px 20px;font-size:14px}}</style>'

P['order/index.html'] = {
'title': 'Order Animated Video | Get Started in Minutes | ExpansionVideos',
'desc': 'Order your animated video directly. AI video from $497, 2D animation from $797, or premium. Fixed price, everything included, money-back guarantee.',
'body': '''
<section class="hero" style="min-height:auto;padding:140px 32px 60px">
<div class="wrap"><div class="hero-text" style="max-width:100%">
    <p class="label">Order</p>
    <h1 class="h1">Order your video, <span class="blue">start today</span></h1>
    <p class="sub">Pick the format that fits your project. Fixed price, everything included, and we work until you are happy. Not sure which to choose? <a href="https://calendly.com/mikael-hamrin/30min" class="blue">Book a free call</a> and we will help.</p>
</div></div></section>
<section class="sec" style="padding-top:40px"><div class="wrap">
<div class="price-grid">
    <div class="price-card"><div class="price-dur">AI Video</div><div class="price-amt">$497 <small>/30s</small></div><div class="price-desc">Fast, cost-effective AI production. Ideal for ads, social and volume. Delivered in 5 to 7 days.</div><ul class="price-list"><li>AI-generated animation</li><li>Professional voiceover</li><li>Music and HD delivery</li><li>5 to 7 day delivery</li></ul><a href="/order/ai-video/" class="btn btn-fill btn-w100">Order AI Video →</a></div>
    <div class="price-card pop"><div class="price-dur">2D Animation</div><div class="price-amt">$797 <small>/30s</small></div><div class="price-desc">Our flagship. Custom hand-crafted 2D animation with unlimited revisions. The standard choice for most.</div><ul class="price-list"><li>Custom design</li><li>Script and pro voiceover</li><li>Unlimited revisions</li><li>Satisfaction guarantee</li></ul><a href="/order/2d-animation/" class="btn btn-fill btn-w100">Order 2D Animation →</a></div>
    <div class="price-card"><div class="price-dur">Premium / Custom</div><div class="price-amt">Quote</div><div class="price-desc">Exclusive cinematic production for demanding projects. Senior team and priority delivery.</div><ul class="price-list"><li>Fully customized</li><li>Senior production</li><li>Priority delivery</li><li>Quote within 24 hours</li></ul><a href="/contact/" class="btn btn-ghost btn-w100">Request a Quote →</a></div>
</div>
<p class="sub mx-a tc" style="margin-top:32px;max-width:640px">Want to see pricing for longer videos and add-ons first? <a href="/pricing/" class="blue">See full pricing</a>.</p>
</div></section>
<section class="sec sec-gray"><div class="wrap"><div class="sec-hdr tc"><p class="label">You take no risk</p><h2 class="h2">Order with confidence</h2></div>
<div class="guar-grid" style="margin-top:48px">
<div class="guar-card"><div class="g-icon">💰</div><h4>Money-back guarantee</h4><p>Not satisfied after revisions? We will find a solution, including a refund.</p></div>
<div class="guar-card"><div class="g-icon">🔄</div><h4>Unlimited revisions</h4><p>We work until you are 100% happy, at no extra cost.</p></div>
<div class="guar-card"><div class="g-icon">📅</div><h4>Clear deadline</h4><p>You know exactly when your video is ready. No vague promises.</p></div>
</div></div></section>
<section class="cta"><div class="wrap"><h2 class="h2">Not sure? We will help you choose</h2><p class="sub">Book a free 20-minute call. We review your project and recommend the right format and price.</p>
<div class="cta-btns"><a href="https://calendly.com/mikael-hamrin/30min" class="btn btn-fill btn-lg">Book Free Call →</a><a href="/contact/" class="btn btn-outline btn-lg">Contact Us</a></div></div></section>
'''}
P['order/index.html']['schema'] = '''<script type="application/ld+json">{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://expansionvideos.com/"},{"@type":"ListItem","position":2,"name":"Order","item":"https://expansionvideos.com/order/"}]}</script>'''

BUILD_TS = str(int(time.time()))
for fn, pg in P.items():
    fp = os.path.join(SITE, fn)
    os.makedirs(os.path.dirname(fp), exist_ok=True)
    _url = 'https://expansionvideos.com/' + ('' if fn == 'index.html' else fn.replace('index.html', ''))
    html = HEAD.format(title=pg['title'], desc=pg['desc'], schema=pg.get('schema', ''), url=_url) + pg['body'] + FOOT
    html = html.replace('</head>', f'<!-- build:{BUILD_TS} --></head>', 1)
    if not (fn.startswith('order/') or 'thank-you' in fn):
        html = html.replace('</body>', FAB + '</body>', 1)
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

# --- Post-loop emit: pages added after the main write loop (e.g. thank-you) ---
import shutil
for _fn in ['thank-you/index.html']:
    if _fn in P:
        _pg = P[_fn]
        _fp = os.path.join(SITE, _fn)
        os.makedirs(os.path.dirname(_fp), exist_ok=True)
        _url = 'https://expansionvideos.com/' + ('' if _fn == 'index.html' else _fn.replace('index.html', ''))
        _html = HEAD.format(title=_pg['title'], desc=_pg['desc'], schema=_pg.get('schema', ''), url=_url) + _pg['body'] + FOOT
        _html = _html.replace('</head>', f'<!-- build:{BUILD_TS} --></head>', 1)
        with open(_fp, 'w', encoding='utf-8') as _f:
            _f.write(_html)
        print(f'thank-you emitted: {_fn} ({len(_html):,} bytes)')

# --- Emit stylesheet: every page links /css/style.css, so copy it into the build ---
_css_src = os.path.join(os.path.dirname(__file__), 'style.css')
_css_dst = os.path.join(SITE, 'css', 'style.css')
os.makedirs(os.path.dirname(_css_dst), exist_ok=True)
shutil.copyfile(_css_src, _css_dst)
print(f'css emitted: css/style.css ({os.path.getsize(_css_dst):,} bytes)')

# --- Emit JS: cookie consent manager ---
_js_src = os.path.join(os.path.dirname(__file__), 'js', 'cookie-consent.js')
_js_dst = os.path.join(SITE, 'js', 'cookie-consent.js')
os.makedirs(os.path.dirname(_js_dst), exist_ok=True)
shutil.copyfile(_js_src, _js_dst)
print('js emitted: js/cookie-consent.js')

# --- robots.txt: welcome all crawlers (including AI search engines) + sitemap ---
_robots = """# ExpansionVideos - all crawlers welcome, including AI search engines.
User-agent: *
Allow: /

Sitemap: https://expansionvideos.com/sitemap.xml
"""
with open(os.path.join(SITE, 'robots.txt'), 'w', encoding='utf-8') as _f:
    _f.write(_robots)
print('robots.txt written')

# --- sitemap.xml: primary indexable pages (exclude thank-you + brief funnels) ---
_today = time.strftime('%Y-%m-%d')
_exclude = ('thank-you', 'brief')
_urls = []
for _k in P.keys():
    if any(_x in _k for _x in _exclude):
        continue
    _path = '/' if _k == 'index.html' else '/' + _k.replace('index.html', '')
    _urls.append(_path)
_urls = sorted(set(_urls), key=lambda p: (p != '/', p))
_rows = ''.join(
    f'  <url><loc>https://expansionvideos.com{u}</loc><lastmod>{_today}</lastmod>'
    f'<changefreq>{"weekly" if u == "/" else "monthly"}</changefreq>'
    f'<priority>{"1.0" if u == "/" else "0.8"}</priority></url>\n' for u in _urls
)
_sitemap = ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
            f'{_rows}</urlset>\n')
with open(os.path.join(SITE, 'sitemap.xml'), 'w', encoding='utf-8') as _f:
    _f.write(_sitemap)
print(f'sitemap.xml written ({len(_urls)} urls)')

# --- llms.txt: concise, structured summary for AI readers (llmstxt.org convention) ---
_llms = """# ExpansionVideos

> Animated explainer video production studio. 2D animation, AI video, and premium custom production. 500+ videos for 56+ industries since 2015. Serves clients worldwide. English-language.

## Services
- AI Video: AI-powered explainer videos from $497 per 30 seconds, delivered in 5-7 days. Best for social media, ads, and volume.
- 2D Animation: hand-crafted custom 2D animation from $797 per 30 seconds. Most popular service since 2015. Includes scriptwriting, voiceover, and unlimited revisions.
- Premium / Custom: cinematic, fully customized production for demanding clients. Quote on request.

## What's included
Script, professional voiceover, music, animation, HD delivery, and revisions. Money-back guarantee. Available in English, Spanish, French, German, Swedish, and 20+ more languages.

## Pages
- Home: https://expansionvideos.com/
- Services: https://expansionvideos.com/services/
- AI Video: https://expansionvideos.com/ai-video/
- Case Studies: https://expansionvideos.com/case-studies/
- Pricing: https://expansionvideos.com/pricing/
- Contact: https://expansionvideos.com/contact/

## Contact
- Email: studio@expansionvideos.com
- Book a call: https://calendly.com/mikael-hamrin/30min
- Company: Villadose LLC, Sheridan, Wyoming, USA
"""
with open(os.path.join(SITE, 'llms.txt'), 'w', encoding='utf-8') as _f:
    _f.write(_llms)
print('llms.txt written')


# --- _headers: security headers + long cache for static assets ---
_headers = """/*
  X-Content-Type-Options: nosniff
  X-Frame-Options: SAMEORIGIN
  Referrer-Policy: strict-origin-when-cross-origin
  Permissions-Policy: camera=(), microphone=(), geolocation=()

/css/*
  Cache-Control: public, max-age=31536000, immutable

/img/*
  Cache-Control: public, max-age=31536000, immutable
"""
with open(os.path.join(SITE, '_headers'), 'w', encoding='utf-8') as _f:
    _f.write(_headers)
print('_headers written')

# --- _redirects: 301 old WordPress URLs to closest current page (specific first) ---
_redirects = """# 301 redirects from old WordPress URLs to the current structure.
# Specific rules first; first match wins.

# Old service / landing pages
/our-services/  /services/  301
/explainer_video/  /services/  301
/explainervideo/*  /services/  301
/animated-video/  /services/  301
/company-animation/  /services/  301
/commercial-video/  /services/  301
/short-video/  /services/  301
/it-tech/  /services/  301
/process/  /services/  301
/prices/  /pricing/  301
/offer/  /pricing/  301
/video-offer  /pricing/  301
/faq/  /pricing/  301
/faqs/  /pricing/  301
/book-call/  /contact/  301
/project-form-video-brief/  /pricing/  301
/form_thanks/  /thank-you/  301
/testimonials/  /case-studies/  301
/about-us/  /  301
/who-we-are  /  301
/team-details-2/  /  301
/become-reseller/  /  301
/become-reseller-svenska/  /  301
/en/home/  /  301
/sv/hem/  /  301
/sv/kontakta-oss/  /contact/  301

# Old blog articles (no blog on current site)
/10-new-things-in-video-marketing-2022-and-how-your-company-can-benefit-from-them/  /  301
/10-reasons-why-video-is-key-to-marketing-success/  /  301
/2021-year-of-animation-explainer-videos/  /  301
/6-successful-marketing-strategies/  /  301
/6-successful-social-media-strategies-and-why-they-worked/  /  301
/7-best-animated-explainer-videos-of-2020/  /  301
/advantages-of-explainer-videos/  /  301
/best-animated-videos-for-2020/  /  301
/branding-how-to-create-a-strong-brand/  /  301
/how-to-create-exceptional-testimonial-animated-explainer-videos/  /  301
/how-to-do-great-branding/  /  301
/how-your-company-can-use-our-services/  /  301
/the-advantages-of-using-animated-explainer-videos-for-your-company/  /  301
/the-numbers-behind-investing-in-your-advertising/  /  301
/top-10-explainer-video-marketing-disruptor-in-the-united-states/  /  301
/top-6-explainer-video-trends-for-2020/  /  301
/toyota-electric-and-hybrid-cars-animated-2d-video/  /case-studies/  301
/video-format-essential-for-digital-marketing-strategy/  /  301
/why-2021-will-be-the-year-of-animation-explainer-videos/  /  301
/why-video-format-is-essential-for-your-companys-digital-marketing-strategy/  /  301

# WordPress taxonomy, archives and project pages
/category/*  /  301
/author/*  /  301
/tag/*  /  301
/blog-old/*  /  301
/2020/*  /  301
/2021/*  /  301
/2022/*  /  301
/2023/*  /  301
/project/*  /case-studies/  301
/project-category/*  /case-studies/  301
/service/*  /services/  301
"""
with open(os.path.join(SITE, '_redirects'), 'w', encoding='utf-8') as _f:
    _f.write(_redirects)
print(f'_redirects written ({_redirects.count(chr(10)+chr(47))} rules)')


# --- 404.html: proper branded 404 so unmatched URLs return 404, not homepage-200 ---
_404_body = """
<section class="hero" style="min-height:70vh;display:flex;align-items:center;justify-content:center;text-align:center">
<div class="wrap">
    <p class="label">Error 404</p>
    <h1 class="h1">Page not found</h1>
    <p class="sub" style="max-width:520px;margin:1rem auto 2rem">The page you were looking for does not exist or has moved. Here are some good ways forward.</p>
    <div class="hero-btns" style="justify-content:center">
        <a href="/" class="btn btn-fill btn-lg">Back to home</a>
        <a href="/services/" class="btn btn-outline btn-lg">Our services</a>
    </div>
    <p class="sub" style="margin-top:28px;font-size:15px">Or go to <a href="/pricing/">Pricing</a>, <a href="/case-studies/">Case Studies</a> or <a href="/contact/">Contact</a>.</p>
</div>
</section>
"""
_404 = HEAD.format(title='Page not found (404) | ExpansionVideos', desc='The page could not be found.', schema='', url='https://expansionvideos.com/404.html') + _404_body + FOOT
_404 = _404.replace('<head>', '<head>\n<meta name="robots" content="noindex,follow">', 1)
with open(os.path.join(SITE, '404.html'), 'w', encoding='utf-8') as _f:
    _f.write(_404)
print('404.html written')
