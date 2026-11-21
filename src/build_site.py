import base64, json

import os
D = os.path.dirname(os.path.abspath(__file__)) + '/'
ROOT = os.path.dirname(D.rstrip('/')) + '/'
s = open(D + 'template.html').read()

def uri(p):
    return 'data:image/jpeg;base64,' + base64.b64encode(open(p, 'rb').read()).decode()

def rep(a, b):
    global s
    assert a in s, a[:60]
    s = s.replace(a, b)

# Earlier fixes
rep('#contact .eyebrow { color: var(--lemon); }\n:root[data-theme="dark"] #contact .eyebrow { color: #6B3D00; }',
    '#contact .eyebrow { color: var(--brand-ink); opacity: 0.85; }')
rep('<small>PER CASE OF 24</small>', '<small>PER CASE<br>OF 24</small>')
rep('<a class="v" id="email" href=', '<a class="v" id="email" style="font-size: clamp(18px, 2.4vw, 24px)" href=')

# Flavor list CSS + detail view CSS
old_css = s[s.index('.flavors { display: grid;'):s.index('/* Energy */')]
new_css = '''.flavors { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 14px; }
.flavor { background: var(--surface); border: 1.5px solid var(--line); border-radius: 18px; overflow: hidden; display: flex; align-items: stretch; min-height: 150px; color: inherit; text-decoration: none; transition: transform 0.15s, border-color 0.15s, box-shadow 0.15s; }
.flavor:hover { border-color: var(--brand); transform: translateY(-2px); box-shadow: 0 10px 24px -14px rgba(75, 30, 120, 0.45); }
@media (prefers-reduced-motion: reduce) { .flavor, .flavor:hover { transition: none; transform: none; } }
.flavor .shot { flex: none; width: 112px; display: flex; align-items: center; justify-content: center; padding: 8px 0; background: #FFFFFF; border-right: 1.5px solid var(--line); }
.flavor .shot img { height: 140px; width: auto; max-width: 100px; object-fit: contain; }
.flavor img { display: block; max-width: 100%; }
.flavor .lbl { padding: 14px 16px; display: flex; flex-direction: column; justify-content: center; gap: 6px; min-width: 0; flex: 1; }
.flavor .lbl b { font-family: var(--display); font-weight: 800; font-size: 22px; line-height: 1.05; }
.flavor .lbl span { font-size: 13px; font-weight: 700; color: var(--muted); }
.flavor .lbl i { display: block; width: 36px; height: 6px; border-radius: 3px; }
.flavor .lbl em { font-style: normal; font-size: 13px; font-weight: 800; color: var(--brand); }

/* Flavor detail view */
.detail { position: fixed; inset: 0; z-index: 20; background: var(--bg); overflow-y: auto; padding-top: env(safe-area-inset-top, 0px); padding-bottom: env(safe-area-inset-bottom, 0px); }
.detail-bar { position: sticky; top: 0; z-index: 2; background: var(--surface); border-bottom: 1px solid var(--line); }
.detail-bar .wrap { display: flex; align-items: center; justify-content: space-between; gap: 12px; padding-block: 10px; }
.detail-bar .logo { font-size: 30px; }
.iconbtn { min-height: 44px; padding: 0 16px; border-radius: 999px; border: 2px solid var(--line); background: var(--surface); color: var(--fg); font-family: var(--body); font-weight: 800; font-size: 15px; cursor: pointer; display: inline-flex; align-items: center; gap: 8px; }
.iconbtn:hover { border-color: var(--brand); }
.detail-body { display: grid; grid-template-columns: minmax(0, 0.9fr) minmax(0, 1.1fr); gap: 40px; padding-block: 40px 56px; align-items: start; }
.visual { border-radius: 28px; min-height: 440px; padding: 36px; position: relative; overflow: hidden; display: flex; flex-direction: column; justify-content: space-between; gap: 28px; }
.visual .ring { position: absolute; width: 400px; height: 400px; border-radius: 50%; right: -130px; bottom: -150px; background: rgba(255, 255, 255, 0.2); }
.visual .vtag { position: relative; font-weight: 800; font-size: 14px; letter-spacing: 0.18em; text-transform: uppercase; }
.visual .vname { position: relative; display: block; max-width: 100%; font-family: var(--display); font-weight: 800; font-size: 88px; line-height: 0.92; text-wrap: balance; }
.visual .chip { position: relative; align-self: flex-end; background: #FFFFFF; border-radius: 22px; padding: 16px 20px; box-shadow: 0 18px 30px -16px rgba(0, 0, 0, 0.5); }
.visual img { display: block; max-width: 100%; }
.visual img { height: 280px; width: auto; max-width: 220px; object-fit: contain; }
.visual img.photo { height: auto; width: 300px; max-width: 100%; border-radius: 14px; }

.dcopy { display: flex; flex-direction: column; gap: 18px; min-width: 0; }
.dcopy .eyebrow { color: var(--juice-ink); }
.dcopy h2 { font-size: clamp(44px, 6vw, 72px); }
.dcopy .swatch { width: 64px; height: 8px; border-radius: 4px; }
.dcopy .taste { font-size: 20px; line-height: 1.55; max-width: 32em; }
.claims { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 10px; }
.claim { display: flex; align-items: center; gap: 10px; background: var(--surface); border: 1.5px solid var(--line); border-radius: 14px; padding: 12px 14px; font-weight: 800; font-size: 15px; }
.claim svg { flex: none; width: 22px; height: 22px; color: var(--leaf); }
.dspecs { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 10px; }
.dspec { background: var(--brand-soft); border-radius: 14px; padding: 14px; }
.dspec b { display: block; font-family: var(--display); font-weight: 800; font-size: 28px; line-height: 1; color: var(--brand); font-variant-numeric: tabular-nums; }
.dspec span { font-size: 13px; font-weight: 700; color: var(--muted); }
.dnote { font-size: 14px; color: var(--muted); font-weight: 600; }
.dactions { display: flex; gap: 12px; flex-wrap: wrap; }
.dnav { display: flex; justify-content: space-between; gap: 12px; flex-wrap: wrap; border-top: 1px solid var(--line); padding-top: 18px; }
body.lock { overflow: hidden; }
@media (max-width: 900px) {
  .detail-body { grid-template-columns: minmax(0, 1fr); padding-block: 24px 40px; gap: 24px; }
  .visual { min-height: 320px; padding: 26px; }
}
@media (max-width: 520px) {
  .claims, .dspecs { grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); }
  .dspecs .dspec:last-child { grid-column: span 2; }
}

'''
s = s.replace(old_css, new_css)
rep('.flavors { grid-template-columns: repeat(3, minmax(0, 1fr)); }', '.flavors { grid-template-columns: repeat(2, minmax(0, 1fr)); }')
rep('.flavors { grid-template-columns: repeat(2, minmax(0, 1fr)); }\n  .tag', '.flavors { grid-template-columns: minmax(0, 1fr); }\n  .tag')

STD = ['No sugar added', 'Never from concentrate', '100% fruit juice']
PULP = ['100% real juice', 'With real fruit pulp']
FL = [
 ('mango', 'Mango', '#F5A623', 'Sweet, golden and rich, with the full body of ripe tropical mango. Smooth and satisfying in every sip.', '16.9 oz', '500 ml', STD),
 ('apple', 'Apple', '#E0453A', 'Crisp and clean, with the familiar sweetness of fresh-pressed apples. Light and refreshing for all ages.', '16.57 oz', '500 ml', STD),
 ('orange', 'Orange', '#F7931E', 'Bright and zesty, with the sweet citrus taste of fresh oranges. A breakfast classic, ready to grab and go.', '16.57 oz', '500 ml', STD),
 ('sugarcane', 'Sugarcane with Calamansi', '#8DBF3F', 'Fresh-pressed sugarcane with a squeeze of calamansi lime. Naturally sweet, with a light citrus lift.', '16.9 oz', '500 ml', STD),
 ('passion-fruit', 'Passion Fruit', '#7B2D8E', 'Bold, tangy and exotic, with the bright tartness of fresh passion fruit. A lively balance of sweet and sour.', '16.9 oz', '500 ml', STD),
 ('pink-guava', 'Pink Guava', '#E8758A', 'Fragrant and smooth, with the gentle sweetness and floral aroma of ripe pink guava. A tropical favorite with a soft, velvety finish.', '16.9 oz', '500 ml', STD),
 ('pineapple', 'Pineapple', '#F2C230', 'Juicy and tangy, with the bright sweetness of ripe pineapple and real pineapple pulp. Refreshing, with a tropical zing.', '16.57 oz', '490 ml', PULP),
 ('strawberry', 'Strawberry', '#D9283E', 'Sweet and fruity, with the bright berry taste of ripe strawberries. A crowd favorite for every cooler.', '16.57 oz', '500 ml', STD),
 ('watermelon', 'Watermelon', '#E84A5F', 'Light, juicy and thirst quenching, with the cool sweetness of fresh watermelon. Perfect on a hot day.', '16.9 oz', '500 ml', STD),
 ('red-grape', 'Red Grape', '#7A1F3D', 'Deep, rich and fruity, with the bold sweetness of ripe red grapes. Full flavored, with a smooth finish.', '16.57 oz', '500 ml', STD),
 ('lychee', 'Lychee', '#D7263D', 'Delicate and floral, with the light, juicy sweetness of fresh lychee. Clean and refreshing, best served ice cold.', '16.9 oz', '500 ml', STD),
 ('cranberry', 'Cranberry', '#B3123A', 'Tart and crisp, with the bright, tangy bite of cranberry. Refreshing, with a clean finish.', '16.57 oz', '500 ml', STD),
 ('strawberry-lemon', 'Strawberry & Lemon', '#E83F5B', 'Sweet strawberry with a zesty squeeze of lemon. A bright, refreshing mix of sweet and tart.', '16.57 oz', '500 ml', STD),
 ('peach', 'Peach', '#F7A07A', 'Soft and sweet, with the mellow, fragrant flavor of ripe peaches. Smooth and summery.', '8.45 oz', '250 ml', ['With fruit pulp']),
 ('papaya', 'Papaya', '#F28C38', 'Mellow and sweet, with the soft, buttery taste of ripe papaya. Smooth and naturally tropical.', '16.9 oz', '500 ml', STD),
 ('soursop', 'Soursop', '#5FA53A', 'Creamy and tropical, with hints of pineapple and strawberry in one unique fruit. A smooth, rich texture with real soursop pulp.', '16.57 oz', '490 ml', PULP),
]

def img_uri(slug):
    return '/images/cans/' + slug + '.webp'

tiles = ''
data = []
for slug, name, color, desc, oz, ml, claims in FL:
    nm = name.replace('&', '&amp;')
    tiles += (f'<a class="flavor" href="#flavor-{slug}" data-slug="{slug}" aria-label="{nm}: see details">'
              f'<div class="shot"><img src="{img_uri(slug)}" alt="VINUT {nm} juice can" loading="lazy"></div>'
              f'<div class="lbl"><i style="background:{color}"></i><b>{nm}</b><span>{ml} can · $35 per case</span><em>View flavor &rsaquo;</em></div></a>\n')
    h = color.lstrip('#'); r, g, b = (int(h[i:i+2], 16) for i in (0, 2, 4))
    lum = (0.2126*r + 0.7152*g + 0.0722*b) / 255
    data.append({'slug': slug, 'name': name, 'color': color, 'ink': '#2A1B3D' if lum > 0.6 else '#FFFFFF',
                 'desc': desc, 'oz': oz, 'ml': ml, 'claims': claims, 'group': 'vinut', 'price': '$35', 'eyebrow': 'VINUT Fruit Juice', 'vtag': 'VINUT', 'back': 'Back to all flavors', 'home': 'vinut', 'photo': False})
data.append({'slug': 'monster', 'name': 'Monster Energy Original', 'color': '#0B0B0B', 'ink': '#7AC943', 'desc': 'The original green Monster in the big 16 oz can. A bold, sweet energy drink and one of the fastest movers in any store cooler.', 'oz': '16 oz', 'ml': '473 ml', 'claims': ['Original flavor', 'Big 16 fl oz can', 'Sold by the case'], 'group': 'energy', 'price': '$40', 'eyebrow': 'Energy Drink', 'vtag': 'MONSTER ENERGY', 'back': 'Back to energy drinks', 'home': 'energy', 'photo': True})
data.append({'slug': 'redbull', 'name': 'Red Bull Energy Drink', 'color': '#1C2B6B', 'ink': '#F5C400', 'desc': "The world's best-known energy drink in its classic 8.4 oz slim can. A must-have for every cooler and checkout counter.", 'oz': '8.4 oz', 'ml': '250 ml', 'claims': ['Original flavor', 'Classic 8.4 fl oz can', 'Sold by the case'], 'group': 'energy', 'price': '$40', 'eyebrow': 'Energy Drink', 'vtag': 'RED BULL', 'back': 'Back to energy drinks', 'home': 'energy', 'photo': True})

rep('__FLAVORS__', tiles)
def brow(d):
    nm = d['name'].replace('&', '&amp;')
    if d['group'] == 'vinut': nm = 'VINUT ' + nm
    return (f'<div class="brow" data-sku="{d["slug"]}"><span class="nm"><i style="background:{d["color"]}"></i>{nm}</span>'
            f'<span class="stepper"><button type="button" data-dec aria-label="Remove one case of {nm}">&minus;</button>'
            f'<output aria-label="Cases of {nm}">0</output>'
            f'<button type="button" data-inc aria-label="Add one case of {nm}">+</button></span></div>')
rows = '<div class="bgroup"><span>VINUT Juices</span><span>$35 / case of 24</span></div>' + ''.join(brow(d) for d in data if d['group'] == 'vinut')
rows += '<div class="bgroup"><span>Energy drinks</span><span>$40 / case of 24</span></div>' + ''.join(brow(d) for d in data if d['group'] == 'energy')

s = s.replace('__MONSTER__', '/images/drinks/monster-original.webp').replace('__REDBULL__', '/images/drinks/redbull-8oz.webp')

check = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"></circle><path d="m7.5 12.5 3 3 6-6.5"></path></svg>'
detail = f'''
<div class="detail" id="detail" role="dialog" aria-modal="true" aria-labelledby="d-name" hidden>
  <div class="detail-bar">
    <div class="wrap">
      <span class="logo" aria-hidden="true">KS<svg viewBox="0 0 80 115"><use href="#glass"/></svg>GA</span>
      <button class="iconbtn" type="button" id="d-close">&larr; <span id="d-back">Back to all flavors</span></button>
    </div>
  </div>
  <div class="wrap detail-body">
    <div class="visual" id="d-visual"><span class="ring" aria-hidden="true"></span><div><p class="vtag" id="d-vtag">VINUT</p><p class="vname" id="d-vname" aria-hidden="true"></p></div><div class="chip" id="d-chip"><img id="d-img" alt=""></div></div>
    <div class="dcopy">
      <p class="eyebrow" id="d-eyebrow">VINUT Fruit Juice</p>
      <span class="swatch" id="d-swatch"></span>
      <h2 id="d-name">Flavor</h2>
      <p class="taste" id="d-desc"></p>
      <div class="claims" id="d-claims"></div>
      <p class="dnote" id="d-note">The only sugar is the natural sugar from the fruit.</p>
      <div class="dspecs">
        <div class="dspec"><b id="d-price">$35</b><span>per case</span></div>
        <div class="dspec"><b>24</b><span>cans per case</span></div>
        <div class="dspec"><b id="d-oz">16.9 oz</b><span id="d-ml">per can</span></div>
      </div>
      <div class="dactions">
        <button class="btn primary" type="button" id="d-add">Add 1 case to order</button>
        <a class="btn ghost" href="mailto:singhkawaljeet1204@gmail.com" id="d-order">Email to order</a>
        <a class="btn ghost" href="tel:+16304735519">Call to order</a>
      </div>
      <div class="dnav">
        <button class="iconbtn" type="button" id="d-prev">&lsaquo; <span></span></button>
        <button class="iconbtn" type="button" id="d-next"><span></span> &rsaquo;</button>
      </div>
    </div>
  </div>
</div>
'''
rep('</main>', '</main>\n' + detail)

js = '''
var FLAVORS = __DATA__;
var CART = {};
try { CART = JSON.parse(localStorage.getItem('ksuga-cart') || '{}') || {}; } catch (e) { CART = {}; }
function saveCart() { try { localStorage.setItem('ksuga-cart', JSON.stringify(CART)); } catch (e) {} }
function toast(msg) {
  var el = document.getElementById('toast'); el.textContent = msg; el.hidden = false;
  clearTimeout(toast.t); toast.t = setTimeout(function () { el.hidden = true; }, 1800);
}
function priceOf(f) { return f.group === 'vinut' ? 35 : 40; }
function labelOf(f) { return f.group === 'vinut' ? 'VINUT ' + f.name + ' Juice' : f.name; }
function renderCart() {
  var lines = document.getElementById('b-lines'); lines.textContent = '';
  var total = 0, cases = 0, msg = [];
  FLAVORS.forEach(function (f) {
    var q = CART[f.slug] || 0;
    var row = document.querySelector('.brow[data-sku="' + f.slug + '"]');
    if (row) { row.querySelector('output').textContent = q; row.classList.toggle('on', q > 0); }
    if (!q) return;
    var amt = q * priceOf(f); total += amt; cases += q;
    var d = document.createElement('div');
    var a = document.createElement('span'); a.textContent = q + ' × ' + labelOf(f);
    var b = document.createElement('span'); b.textContent = '$' + amt;
    d.appendChild(a); d.appendChild(b); lines.appendChild(d);
    msg.push(q + ' x ' + labelOf(f) + ' ($' + amt + ')');
  });
  if (!cases) { var p = document.createElement('p'); p.className = 'empty'; p.textContent = 'No cases added yet.'; lines.appendChild(p); }
  document.getElementById('b-total').textContent = '$' + total;
  document.getElementById('b-cases').textContent = cases + (cases === 1 ? ' case' : ' cases');
  var badge = document.getElementById('m-badge'); badge.hidden = !cases; badge.textContent = cases;
  var store = document.getElementById('b-store').value.trim();
  var addr = document.getElementById('b-addr').value.trim();
  var body = 'Hi KSUGA INC,\\n\\nI would like to place this order:\\n\\n' + msg.join('\\n') +
    '\\n\\nTotal: ' + cases + ' cases, $' + total + '\\n\\nStore name: ' + store + '\\nStore address: ' + addr + '\\n\\nThank you,\\n';
  var em = document.getElementById('b-email'), tx = document.getElementById('b-text');
  em.href = 'mailto:singhkawaljeet1204@gmail.com?subject=' + encodeURIComponent('New order' + (store ? ': ' + store : '')) + '&body=' + encodeURIComponent(body);
  tx.href = 'sms:+16304735519?&body=' + encodeURIComponent(body);
  em.setAttribute('aria-disabled', cases ? 'false' : 'true');
  tx.setAttribute('aria-disabled', cases ? 'false' : 'true');
  saveCart();
}
function addCase(slug, n) {
  CART[slug] = Math.max(0, (CART[slug] || 0) + n);
  if (!CART[slug]) delete CART[slug];
  renderCart();
}
var CHECK = __CHECK__;
(function () {
  var detail = document.getElementById('detail');
  var img = document.getElementById('d-img');
  var lastSlug = null;
  function bySlug(slug) { for (var i = 0; i < FLAVORS.length; i++) { if (FLAVORS[i].slug === slug) return i; } return -1; }
  function show(slug) {
    var i = bySlug(slug); if (i < 0) return hide();
    var f = FLAVORS[i];
    var tile = f.group === 'vinut' ? document.querySelector('.flavor[data-slug="' + slug + '"] img') : document.querySelector('#' + slug + ' .photo img');
    img.src = tile ? tile.src : '';
    img.alt = tile ? tile.alt : f.name;
    img.className = f.photo ? 'photo' : '';
    document.getElementById('d-vtag').textContent = f.vtag;
    document.getElementById('d-eyebrow').textContent = f.eyebrow;
    document.getElementById('d-price').textContent = f.price;
    document.getElementById('d-back').textContent = f.back;
    var prod = f.group === 'vinut' ? 'VINUT ' + f.name + ' Juice' : f.name;
    var mbody = 'Hi KSUGA INC,\\n\\nI would like to order ' + prod + ' (' + f.price + ' per case of 24).\\n\\nStore name:\\nStore address:\\nNumber of cases:\\nPreferred delivery day:\\n\\nThank you,\\n';
    document.getElementById('d-order').href = 'mailto:singhkawaljeet1204@gmail.com?subject=' + encodeURIComponent('Order: ' + prod) + '&body=' + encodeURIComponent(mbody);
    var vn = document.getElementById('d-vname'); vn.textContent = f.name;
    function fit() {
      var size = 88; vn.style.fontSize = size + 'px';
      while (size > 36 && vn.scrollWidth > vn.clientWidth + 1) { size -= 4; vn.style.fontSize = size + 'px'; }
    }
    requestAnimationFrame(fit);
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(fit);
    var vis = document.getElementById('d-visual'); vis.style.background = f.color; vis.style.color = f.ink;
    document.getElementById('d-swatch').style.background = f.color;
    document.getElementById('d-name').textContent = f.name;
    document.getElementById('d-desc').textContent = f.desc;
    var cl = document.getElementById('d-claims'); cl.textContent = '';
    f.claims.forEach(function (c) {
      var d = document.createElement('div'); d.className = 'claim';
      d.innerHTML = CHECK; d.appendChild(document.createTextNode(c)); cl.appendChild(d);
    });
    document.getElementById('d-note').hidden = f.claims.indexOf('No sugar added') < 0;
    document.getElementById('d-oz').textContent = f.oz;
    document.getElementById('d-ml').textContent = f.ml + ' can';
    var grp = FLAVORS.filter(function (x) { return x.group === f.group; });
    var gi = grp.indexOf(f);
    var prev = grp[(gi - 1 + grp.length) % grp.length];
    var next = grp[(gi + 1) % grp.length];
    var pb = document.getElementById('d-prev'), nb = document.getElementById('d-next');
    pb.querySelector('span').textContent = prev.name; pb.dataset.slug = prev.slug;
    nb.querySelector('span').textContent = next.name; nb.dataset.slug = next.slug;
    pb.hidden = grp.length < 3;
    document.querySelector('.dnav').style.justifyContent = grp.length < 3 ? 'flex-end' : '';
    detail.hidden = false; detail.scrollTop = 0;
    document.body.classList.add('lock');
    lastSlug = slug;
    document.getElementById('d-close').focus({ preventScroll: true });
  }
  function hide() {
    if (detail.hidden) return;
    detail.hidden = true;
    document.body.classList.remove('lock');
    if (lastSlug) {
      var t = document.querySelector('.flavor[data-slug="' + lastSlug + '"]') || document.getElementById(lastSlug);
      if (t) { t.scrollIntoView({ block: 'center' }); t.focus({ preventScroll: true }); }
    }
  }
  function setHash(h) { try { history.replaceState(null, '', '#' + h); } catch (e) {} }
  function open(slug) { show(slug); setHash('flavor-' + slug); }
  function close() {
    var f = FLAVORS[bySlug(lastSlug)];
    hide(); setHash(f ? f.home : 'vinut');
  }
  function route() {
    var h = (location.hash || '').replace('#', '');
    if (h.indexOf('flavor-') === 0) show(h.slice(7)); else hide();
  }
  window.addEventListener('hashchange', route);
  document.querySelectorAll('.flavor[data-slug]').forEach(function (card) {
    card.addEventListener('click', function (e) { e.preventDefault(); open(card.getAttribute('data-slug')); });
  });
  document.getElementById('d-close').addEventListener('click', close);
  document.querySelectorAll('[data-open]').forEach(function (el) {
    el.addEventListener('click', function (e) {
      if (el.tagName === 'ARTICLE' && e.target.closest('a')) return;
      e.preventDefault(); e.stopPropagation(); open(el.getAttribute('data-open'));
    });
  });
  ['d-prev', 'd-next'].forEach(function (id) {
    document.getElementById(id).addEventListener('click', function (e) { open(e.currentTarget.dataset.slug); });
  });
  detail.addEventListener('keydown', function (e) { if (e.key === 'Escape') close(); });
  document.querySelectorAll('.brow').forEach(function (row) {
    var sku = row.getAttribute('data-sku');
    row.querySelector('[data-inc]').addEventListener('click', function () { addCase(sku, 1); });
    row.querySelector('[data-dec]').addEventListener('click', function () { addCase(sku, -1); });
  });
  ['b-store', 'b-addr'].forEach(function (id) { document.getElementById(id).addEventListener('input', renderCart); });
  document.getElementById('b-clear').addEventListener('click', function () { CART = {}; renderCart(); });
  document.getElementById('d-add').addEventListener('click', function () {
    if (!lastSlug) return; addCase(lastSlug, 1);
    var f = FLAVORS[bySlug(lastSlug)];
    toast('Added: ' + labelOf(f) + ' (' + CART[lastSlug] + ' in order)');
  });
  var yr = document.getElementById('yr'); if (yr) yr.textContent = new Date().getFullYear();
  renderCart();
  route();
})();
'''.replace('__DATA__', json.dumps(data)).replace('__CHECK__', json.dumps(check))
rep('</script>', js + '</script>')

# Price list links (from previous step, in case template lacks them)
s = s.replace('__BUILDER_ROWS__', rows)
if 'a class="pricerow"' not in s:
    raise SystemExit('template missing pricerow links')
head = open(D + 'head.html').read()
open(ROOT + 'index.html', 'w').write('<!doctype html>\n<html lang="en">\n<head>\n' + head + '</head>\n<body>\n' + s + '\n</body>\n</html>\n')
print(len(s) // 1024, 'KB')
