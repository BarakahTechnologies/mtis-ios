#!/usr/bin/env python3
"""Generate the MTIS website: index / privacy / support in en, es, ar."""
import os

BUILD_DIR = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(BUILD_DIR)
BASE = "https://mtis.barakahtechnologies.net"
LANGS = ["en", "es", "ar"]
RTL = {"ar"}

# ---- per-language UI strings --------------------------------------------------
UI = {
    "en": dict(
        native="English", dir="ltr",
        nav_features="Features", nav_privacy="Privacy", nav_support="Support", nav_policy="Policy",
        f_privacy_policy="Privacy Policy", f_support="Support",
        copyright="© 2026 BARAKAH TECHNOLOGIES, INC. All rights reserved.",
    ),
    "es": dict(
        native="Español", dir="ltr",
        nav_features="Funciones", nav_privacy="Privacidad", nav_support="Soporte", nav_policy="Política",
        f_privacy_policy="Política de Privacidad", f_support="Soporte",
        copyright="© 2026 BARAKAH TECHNOLOGIES, INC. Todos los derechos reservados.",
    ),
    "ar": dict(
        native="العربية", dir="rtl",
        nav_features="الميزات", nav_privacy="الخصوصية", nav_support="الدعم", nav_policy="السياسة",
        f_privacy_policy="سياسة الخصوصية", f_support="الدعم",
        copyright="© 2026 BARAKAH TECHNOLOGIES, INC. جميع الحقوق محفوظة.",
    ),
}

PAGES = ["index", "privacy", "support"]

HOME_LABELS = {'en': 'Home', 'ar': 'الرئيسية', 'es': 'Inicio', 'fr': 'Accueil', 'tr': 'Ana sayfa'}

def fname(page, lang):
    return f"{page}.html" if lang == "en" else f"{page}.{lang}.html"

with open(os.path.join(OUT, "assets", "site.css"), encoding="utf-8") as _f:
    SITE_CSS = _f.read()

def head(page, lang, title, desc):
    alts = "\n".join(
        f'  <link rel="alternate" hreflang="{l}" href="{BASE}/{fname(page, l)}" />'
        for l in LANGS
    ) + f'\n  <link rel="alternate" hreflang="x-default" href="{BASE}/{fname(page, "en")}" />'
    return f"""<!DOCTYPE html>
<html lang="{lang}" dir="{UI[lang]['dir']}">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="color-scheme" content="light" />
  <meta name="description" content="{desc}" />
  <meta name="theme-color" content="#1f6fd8" />
  <link rel="icon" type="image/png" sizes="32x32" href="assets/icon-32.png" />
  <link rel="icon" type="image/png" sizes="180x180" href="assets/icon-180.png" />
  <link rel="apple-touch-icon" href="assets/icon-180.png" />
  <link rel="canonical" href="{BASE}/{fname(page, lang)}" />
  <title>{title}</title>
{alts}
  <style>
{SITE_CSS}
  </style>
  <link rel="stylesheet" href="assets/family.css?v=20260927-home" />
  <link rel="stylesheet" href="assets/design-system.css?v=20260927-shared">
</head>
<body>"""

def nav(page, lang, home_anchor=True):
    u = UI[lang]
    feat = "#features" if page == "index" else fname("index", lang) + "#features"
    priv = "#privacy" if page == "index" else fname("index", lang) + "#privacy"
    menu_lines = []
    for l in LANGS:
        current = ' aria-current="page"' if l == lang else ""
        menu_lines.append(
            f'            <a href="{fname(page, l)}" lang="{l}"{current}>{UI[l]["native"]}</a>'
        )
    menu = "\n".join(menu_lines)
    return f"""  <header class="nav">
    <div class="wrap nav-inner">
      <a class="brand" href="{fname("index", lang)}" aria-label="MTIS home">
        <img class="brand-mark" src="assets/icon-64.png" alt="MTIS app icon" width="34" height="34" />
        <span>MTIS</span>
      </a>
      <nav class="nav-links" aria-label="Primary navigation">
        <a class="home-button" href="https://barakahtechnologies.net/{fname("index", lang)}" aria-label="Barakah Technologies — {HOME_LABELS[lang]}">{HOME_LABELS[lang]}</a>
        <a href="{feat}">{u['nav_features']}</a>
        <a href="{priv}">{u['nav_privacy']}</a>
        <a href="{fname('support', lang)}">{u['nav_support']}</a>
        <a href="{fname('privacy', lang)}">{u['nav_policy']}</a>
        <details class="lang-switch">
          <summary aria-label="Change language">🌐 {u['native']}</summary>
          <div class="lang-menu">
{menu}
          </div>
        </details>
      </nav>
    </div>
  </header>"""

def footer(lang):
    u = UI[lang]
    return f"""  <footer class="site">
    <div class="wrap footer-inner">
      <p>{u['copyright']}</p>
      <div class="footer-links">
        <a href="https://barakahtechnologies.net/{fname("index", lang)}">Barakah Technologies</a>
        <a href="{fname('privacy', lang)}">{u['f_privacy_policy']}</a>
        <a href="{fname('support', lang)}">{u['f_support']}</a>
      </div>
    </div>
  </footer>
</body>
</html>
"""

# ---- INDEX content ----------------------------------------------------------
IX = {
 "en": dict(
  title="MTIS — Mechanic Tool Inventory",
  desc="MTIS is a private, on-device tool inventory for iPhone — track photos, serial numbers, warranty and calibration dates, and value. No account, no server.",
  badge="Private, on-device tool inventory",
  h1_a="Every tool you own,", h1_b="accounted for.",
  lead="MTIS tracks tools, photos, serial and stock numbers, warranty and calibration due dates, maintenance history, and inventory value — all on your iPhone. No account. No server.",
  btn_store="Coming to the App&nbsp;Store", btn_support="Get Support",
  hl0="💵 $7.99 once, no subscription", hl1="🔒 No account", hl2="📴 Works offline", hl3="🚫 No tracking",
  dash="🔧 Dashboard", tools_n="21 tools",
  s_tools="Tools", s_value="Value", s_cal="Cal overdue", s_war="Warranty 30d",
  attn="Needs attention",
  r1a='1/2" torque wrench', r1b="Calibration overdue",
  r2a='3/8" impact wrench', r2b="Warranty expiring",
  r3a="27-pc bit set", r3b="24 of 27 pieces",
  strip_a="Coming soon", strip_b="to the App&nbsp;Store.",
  feat_h="Built for the people who own the tools.",
  feat_p="Fast to log, clear to search, and honest about what everything's worth.",
  features=[
    ("🔧","Tool records","Photo, brand, model, serial and stock number, cost, condition, and location for every tool you own."),
    ("📅","Calibration &amp; warranty","Set due dates and MTIS flags what's overdue or expiring within 30 days, right on the dashboard."),
    ("🧰","Toolboxes &amp; kits","Organize by chest, cabinet, drawer, or truck bin — with nesting — and track multi-piece kit completeness."),
    ("🔎","Scan to find","Photograph a label to read the part number, or scan a QR/barcode to jump straight to a tool or start a new one."),
    ("📄","Reports &amp; export","CSV export, a PDF inventory list, an insurance-claim document with photos and values, and a depreciation estimate."),
    ("💾","Backup &amp; audit","Back up your whole inventory to one file, and run a guided walk-through to confirm nothing's missing."),
  ],
  pp_h="Your inventory stays yours.",
  pp_p="MTIS has no account and no server. Everything you enter lives on your device — nothing is uploaded, ever.",
  pp=["No account, no sign-up","No server — nothing leaves your device","No ads, no analytics, no tracking","CSV, PDF &amp; backups only when you export them","Optional Face ID / Touch ID app lock"],
  cta_h="Set up your inventory once.",
  cta_p="Add your tools, snap a photo of each, and let MTIS keep track of what's due, what's under warranty, and what everything's worth.",
  cta_btn2="Contact Support",
  fine="Free to use · optional one-time $7.99 unlock · no subscription",
 ),
 "es": dict(
  title="MTIS — Inventario de Herramientas",
  desc="MTIS es un inventario de herramientas privado y sin conexión para iPhone: fotos, números de serie, garantía y calibración. Sin cuenta, sin servidor.",
  badge="Inventario de herramientas privado y sin conexión",
  h1_a="Cada herramienta que tienes,", h1_b="bajo control.",
  lead="MTIS registra herramientas, fotos, números de serie y de inventario, fechas de garantía y calibración, historial de mantenimiento y el valor del inventario, todo en tu iPhone. Sin cuenta. Sin servidor.",
  btn_store="Muy pronto en el App&nbsp;Store", btn_support="Obtener soporte",
  hl0="💵 $7.99 pago único, sin suscripción", hl1="🔒 Sin cuenta", hl2="📴 Funciona sin conexión", hl3="🚫 Sin rastreo",
  dash="🔧 Panel", tools_n="21 herramientas",
  s_tools="Herramientas", s_value="Valor", s_cal="Cal. vencida", s_war="Garantía 30 d",
  attn="Requiere atención",
  r1a='Llave dinamométrica 1/2"', r1b="Calibración vencida",
  r2a='Llave de impacto 3/8"', r2b="Garantía por vencer",
  r3a="Juego de 27 puntas", r3b="24 de 27 piezas",
  strip_a="Muy pronto", strip_b="en el App&nbsp;Store.",
  feat_h="Hecho para quien es dueño de las herramientas.",
  feat_p="Rápido de registrar, claro de buscar y honesto sobre cuánto vale todo.",
  features=[
    ("🔧","Fichas de herramienta","Foto, marca, modelo, número de serie y de inventario, costo, estado y ubicación de cada herramienta que tienes."),
    ("📅","Calibración y garantía","Define fechas de vencimiento y MTIS avisa lo que está vencido o vence en 30 días, en el panel."),
    ("🧰","Cajas y juegos","Organiza por cofre, gabinete, cajón o bin de camión —con anidamiento— y controla las piezas de cada juego."),
    ("🔎","Escanear para encontrar","Fotografía una etiqueta para leer el número de pieza, o escanea un QR/código de barras para ir directo a una herramienta."),
    ("📄","Informes y exportación","Exportación CSV, lista de inventario en PDF, un documento para reclamo de seguro con fotos y valores, y una estimación de depreciación."),
    ("💾","Copia de seguridad y auditoría","Respalda todo tu inventario en un archivo y realiza un recorrido guiado para confirmar que no falta nada."),
  ],
  pp_h="Tu inventario es tuyo.",
  pp_p="MTIS no tiene cuenta ni servidor. Todo lo que ingresas vive en tu dispositivo; nada se sube, nunca.",
  pp=["Sin cuenta, sin registro","Sin servidor: nada sale de tu dispositivo","Sin anuncios, sin analíticas, sin rastreo","CSV, PDF y copias solo cuando tú las exportas","Bloqueo opcional con Face ID / Touch ID"],
  cta_h="Configura tu inventario una vez.",
  cta_p="Agrega tus herramientas, toma una foto de cada una y deja que MTIS controle qué vence, qué tiene garantía y cuánto vale todo.",
  cta_btn2="Contactar soporte",
  fine="Gratis · desbloqueo opcional único de $7.99 · sin suscripción",
 ),
 "ar": dict(
  title="MTIS — جرد أدوات الميكانيكي",
  desc="‏MTIS تطبيق جرد أدوات خاص يعمل دون اتصال على iPhone — الصور والأرقام التسلسلية وأرقام المخزون وتواريخ الضمان والمعايرة وسجل الصيانة والقيمة. بلا حساب، بلا خادم.",
  badge="جرد أدوات خاص يعمل دون اتصال",
  h1_a="كل أداة تملكها،", h1_b="تحت السيطرة.",
  lead="‏MTIS يتتبّع الأدوات والصور والأرقام التسلسلية وأرقام المخزون وتواريخ الضمان والمعايرة وسجل الصيانة وقيمة الجرد — كل ذلك على iPhone. بلا حساب. بلا خادم.",
  btn_store="قريباً على App&nbsp;Store", btn_support="الحصول على الدعم",
  hl0="💵 7.99$ دفعة واحدة بلا اشتراك", hl1="🔒 بلا حساب", hl2="📴 يعمل دون اتصال", hl3="🚫 بلا تتبّع",
  dash="🔧 لوحة القيادة", tools_n="٢١ أداة",
  s_tools="الأدوات", s_value="القيمة", s_cal="معايرة متأخرة", s_war="الضمان ٣٠ يوم",
  attn="يحتاج انتباهاً",
  r1a='مفتاح عزم 1/2"', r1b="معايرة متأخرة",
  r2a='مفتاح صدم 3/8"', r2b="الضمان ينتهي قريباً",
  r3a="طقم ٢٧ قطعة", r3b="٢٤ من ٢٧ قطعة",
  strip_a="قريباً", strip_b="على App&nbsp;Store.",
  feat_h="مصنوع لمن يملك الأدوات.",
  feat_p="سريع في التسجيل، واضح في البحث، وصادق بشأن قيمة كل شيء.",
  features=[
    ("🔧","سجلات الأدوات","صورة وعلامة تجارية وطراز ورقم تسلسلي ورقم مخزون وتكلفة وحالة وموقع لكل أداة تملكها."),
    ("📅","المعايرة والضمان","حدّد تواريخ الاستحقاق ويُبرز MTIS ما فات موعده أو ينتهي خلال ٣٠ يوماً، على لوحة القيادة مباشرة."),
    ("🧰","الصناديق والأطقم","نظّم حسب الصندوق أو الخزانة أو الدرج أو صندوق الشاحنة — مع التداخل — وتتبّع اكتمال الأطقم متعددة القطع."),
    ("🔎","امسح لتجد","صوّر ملصقاً لقراءة رقم القطعة، أو امسح رمز QR/باركود للانتقال مباشرة إلى أداة أو لبدء أداة جديدة."),
    ("📄","التقارير والتصدير","تصدير CSV، وقائمة جرد PDF، ومستند مطالبة تأمين بالصور والقيم، وتقدير للإهلاك."),
    ("💾","النسخ الاحتياطي والجرد","انسخ جردك بالكامل إلى ملف واحد، ونفّذ جولة إرشادية للتأكد من عدم وجود نواقص."),
  ],
  pp_h="جردك يبقى ملكك.",
  pp_p="‏MTIS بلا حساب وبلا خادم. كل ما تُدخله يبقى على جهازك — لا شيء يُرفَع، أبداً.",
  pp=["بلا حساب، بلا تسجيل","بلا خادم — لا شيء يغادر جهازك","بلا إعلانات، بلا تحليلات، بلا تتبّع","‏CSV و PDF والنسخ الاحتياطية فقط عندما تصدّرها بنفسك","قفل اختياري بـ Face ID / Touch ID"],
  cta_h="أعدّ جردك مرة واحدة.",
  cta_p="أضف أدواتك، والتقط صورة لكل منها، ودع MTIS يتابع ما يستحق الصيانة وما هو تحت الضمان وقيمة كل شيء.",
  cta_btn2="تواصل مع الدعم",
  fine="مجاني · فتح اختياري لمرة واحدة بـ$7.99 · بلا اشتراك",
 ),
}

def build_index(lang):
    d = IX[lang]
    feats = "\n".join(f"""          <article class="feature">
            <div class="feature-icon">{ic}</div>
            <h3>{t}</h3>
            <p>{p}</p>
          </article>""" for ic, t, p in d["features"])
    pilist = "\n".join(f'            <div class="privacy-item">{x}</div>' for x in d["pp"])
    return head("index", lang, d["title"], d["desc"]) + "\n" + nav("index", lang) + f"""
  <main>
    <section class="hero">
      <div class="wrap hero-grid">
        <div>
          <a class="parent-link" href="https://barakahtechnologies.net/{fname("index", lang)}#products">{ {"en": "All apps", "es": "Todas las apps", "ar": "جميع التطبيقات"}[lang] }</a>
          <div class="badge">{d['badge']}</div>
          <h1>{d['h1_a']} <span>{d['h1_b']}</span></h1>
          <p class="lead">{d['lead']}</p>
          <div class="actions">
            <!-- Swap for a real <a href="https://apps.apple.com/..."> once MTIS is live on the App Store -->
            <span class="button button-primary" aria-disabled="true">{d['btn_store']}</span>
            <a class="button button-secondary" href="{fname('support', lang)}">{d['btn_support']}</a>
          </div>
          <div class="privacy-line" aria-label="Highlights">
            <span class="hl-price">{d['hl0']}</span>
            <span>{d['hl1']}</span>
            <span>{d['hl2']}</span>
            <span>{d['hl3']}</span>
          </div>
        </div>
        <aside class="phone-card" aria-label="MTIS app preview">
          <div class="phone-screen">
            <div class="screen-header">
              <span class="dash-pill">{d['dash']}</span>
              <span class="mini-meta">{d['tools_n']}</span>
            </div>
            <div class="stat-grid">
              <div class="stat"><div class="stat-label">{d['s_tools']}</div><div class="stat-value">21</div></div>
              <div class="stat"><div class="stat-label">{d['s_value']}</div><div class="stat-value">$4,180</div></div>
              <div class="stat"><div class="stat-label">{d['s_cal']}</div><div class="stat-value alert">2</div></div>
              <div class="stat"><div class="stat-label">{d['s_war']}</div><div class="stat-value alert">1</div></div>
            </div>
            <div class="attention">
              <h3>{d['attn']}</h3>
              <div class="attention-row"><span>{d['r1a']}</span><strong>{d['r1b']}</strong></div>
              <div class="attention-row"><span>{d['r2a']}</span><strong>{d['r2b']}</strong></div>
              <div class="attention-row"><span>{d['r3a']}</span><strong>{d['r3b']}</strong></div>
            </div>
            <div class="store-strip">
              <span class="dot" aria-hidden="true"></span>
              <span><strong>{d['strip_a']}</strong> {d['strip_b']}</span>
            </div>
          </div>
        </aside>
      </div>
    </section>

    <section id="features" class="section">
      <div class="wrap">
        <div class="section-head">
          <h2>{d['feat_h']}</h2>
          <p>{d['feat_p']}</p>
        </div>
        <div class="feature-grid">
{feats}
        </div>
      </div>
    </section>

    <section id="privacy" class="section">
      <div class="wrap">
        <div class="privacy-panel">
          <div>
            <h2>{d['pp_h']}</h2>
            <p>{d['pp_p']}</p>
          </div>
          <div class="privacy-list">
{pilist}
          </div>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="wrap">
        <div class="cta">
          <h2>{d['cta_h']}</h2>
          <p>{d['cta_p']}</p>
          <div class="actions" style="justify-content:center;">
            <span class="button button-primary" aria-disabled="true">{d['btn_store']}</span>
            <a class="button button-secondary" href="mailto:mtis-app@proton.me">{d['cta_btn2']}</a>
          </div>
          <p class="fine">{d['fine']}</p>
        </div>
      </div>
    </section>
  </main>
""" + footer(lang)


# ---- PRIVACY content ------------------------------------------------------
PV = {
 "en": dict(
  title="Privacy Policy — MTIS",
  desc="MTIS privacy policy. Every tool, photo, and note stays on your device. No account, no server, no tracking.",
  h="Privacy Policy", sub="Short version: nothing you enter ever leaves your device.",
  updated="Last updated: September 20, 2026",
  tldr_h="The short version",
  tldr=["MTIS has no account, no login, and no sign-up.",
        "Every tool, photo, and note is stored only on your iPhone or iPad.",
        "There is no MTIS server. Nothing you enter is uploaded — there is no cloud sync.",
        "No ads, no analytics, no third-party tracking of any kind.",
        "Files leave the device only when you explicitly export or share them.",
        "Delete the app to erase all of its data."],
  sections=[
   ("1. Who we are", "<p>MTIS (Mechanic Tool Inventory System, “the app”) is developed and published by BARAKAH TECHNOLOGIES, INC. For questions about this policy, email <a href=\"mailto:mtis-app@proton.me\">mtis-app@proton.me</a>.</p>"),
   ("2. What data the app stores", "<p>MTIS stores only the information you enter about your tools and equipment. This may include:</p><ul><li><strong>Tool details:</strong> name, brand, model, serial number, stock/asset number, category and subcategory, size, material, torque range, quantity, condition, location, vendor, purchase date, cost, replacement value, warranty and calibration dates, an inspection interval, and notes</li><li><strong>Photos</strong> you attach to a tool, from your camera or photo library, and an optional label for each (serial plate, receipt, condition shot, and so on)</li><li><strong>Loan records:</strong> if you lend a tool, the name you type for the borrower and the loan and due-back dates</li><li><strong>Tool history:</strong> an on-device log of drawer checks, condition changes, and loans — each with a date and an optional note or photo</li><li><strong>Maintenance log entries:</strong> service date, description, and cost</li><li><strong>Toolboxes:</strong> name, type, brand, SKU, cost, purchase date, and how they nest</li><li><strong>App preferences:</strong> language choice, appearance, the app-lock setting, sort order, and similar options</li></ul><p>All of this is entered by you and stays entirely under your control. The borrower name is free text you choose to type; if you would rather not record a person’s name, use initials or a label instead.</p>"),
   ("3. Where data is stored", "<p>All data is stored locally on your device: structured records in Apple’s SwiftData framework, and photo files in the app’s private container. MTIS does <strong>not</strong> use iCloud, CloudKit, or any sync service, and it does <strong>not</strong> operate an application server, cloud database, or backend API. Your data exists only on the devices you put it on.</p>"),
   ("4. Backups and exports", "<p>MTIS can produce CSV files, PDF reports (inventory, insurance documentation, depreciation estimate), printable QR-label sheets, and a single-file backup archive of your whole inventory. These are created only when you tap Export, Print, or Backup, and they leave your device only through the iOS share sheet action <em>you</em> choose — Files, Mail, Messages, AirDrop, and so on. MTIS never transmits them anywhere on its own.</p>"),
   ("5. Camera and photo library", "<p>Camera and photo-library access are used only to attach a photo to a tool, or to read text or a barcode on a label using Apple’s on-device Vision framework (for example, to capture a serial number or look up a part). Images, recognized text, and scanned codes are processed on your device and are never uploaded.</p>"),
   ("6. Siri and Shortcuts", "<p>If you use Siri or the Shortcuts app, MTIS can answer questions like “where’s my torque wrench” by reading a tool’s location, its status, and — if you have lent it out — the borrower name you entered, and returning that in the spoken or on-screen result. It can also open the app to a new tool entry or a drawer check. These actions run on your device against your local data. How Siri itself processes your spoken request is governed by your device’s Siri &amp; Search settings and Apple’s privacy policy, not by MTIS.</p>"),
   ("7. Face ID, Touch ID, and passcode", "<p>MTIS offers an optional app lock, turned off by default. When enabled, it requires Face ID, Touch ID, or your device passcode to open the app after it has been in the background. Authentication is handled entirely by Apple’s LocalAuthentication framework; MTIS never receives or stores biometric data.</p>"),
   ("8. In-app purchase", "<p>MTIS is free to use for a full tool inventory. An optional one-time purchase (“MTIS Pro”) unlocks tool photos, the maintenance log and history, backup and restore, CSV import and export, and the PDF and value reports. The purchase is processed entirely by Apple’s App Store. MTIS does not collect, see, or store any payment information. Apple may process purchase-related data under its own privacy policy.</p>"),
   ("9. No tracking or advertising", "<p>MTIS contains no advertising SDK, no analytics SDK, and no third-party tracking library. It does not use the Advertising Identifier (IDFA), and it does not build a profile of you or your usage.</p>"),
   ("10. Network use", "<p>MTIS makes no network connections except to Apple’s App Store for the optional purchase and to restore a previous purchase. There is no crash-reporting service, no remote configuration, and no “phone home” of any kind.</p>"),
   ("11. Required-reason API disclosure", "<p>Per Apple’s privacy-manifest requirements, MTIS declares that it accesses file timestamps (to read and write its own data and export files), disk space (to check capacity before creating a backup), and <code>UserDefaults</code> (to store your local preferences). None of this information is collected or transmitted.</p>"),
   ("12. Data deletion", "<p>To delete all your data, delete MTIS from your iPhone or iPad. Because nothing is stored on a server or in iCloud, removing the app removes everything. You can also delete individual tools, toolboxes, and log entries at any time inside the app.</p>"),
   ("13. Children’s privacy", "<p>MTIS is a tool for tradespeople, technicians, and hobbyists. It is not directed at children, does not knowingly collect data from anyone directly, and connects to no online service that would.</p>"),
   ("14. Changes to this policy", "<p>If we make material changes, we will update the date at the top of this page. The current policy is always available at this URL.</p>"),
   ("15. Contact", "<p>Questions or concerns about privacy? Email <a href=\"mailto:mtis-app@proton.me\">mtis-app@proton.me</a>.</p>"),
  ],
 ),
 "es": dict(
  title="Política de Privacidad — MTIS",
  desc="Política de privacidad de MTIS. Cada herramienta, foto y nota permanece en tu dispositivo. Sin cuenta, sin servidor, sin rastreo.",
  h="Política de Privacidad", sub="Versión corta: nada de lo que ingresas sale de tu dispositivo.",
  updated="Última actualización: 20 de septiembre de 2026",
  tldr_h="La versión corta",
  tldr=["MTIS no tiene cuenta, ni inicio de sesión, ni registro.",
        "Cada herramienta, foto y nota se guarda únicamente en tu iPhone o iPad.",
        "No hay servidor de MTIS. Nada de lo que ingresas se sube — no hay sincronización en la nube.",
        "Sin anuncios, sin analíticas, sin rastreo de terceros de ningún tipo.",
        "Los archivos salen del dispositivo solo cuando tú los exportas o compartes explícitamente.",
        "Elimina la app para borrar todos sus datos."],
  sections=[
   ("1. Quiénes somos", "<p>MTIS (Mechanic Tool Inventory System, “la app”) es desarrollada y publicada por BARAKAH TECHNOLOGIES, INC. Para consultas sobre esta política, escribe a <a href=\"mailto:mtis-app@proton.me\">mtis-app@proton.me</a>.</p>"),
   ("2. Qué datos guarda la app", "<p>MTIS guarda únicamente la información que tú ingresas sobre tus herramientas y equipos. Esto puede incluir:</p><ul><li><strong>Datos de la herramienta:</strong> nombre, marca, modelo, número de serie, número de inventario, categoría y subcategoría, tamaño, material, rango de torque, cantidad, estado, ubicación, proveedor, fecha de compra, costo, valor de reemplazo, fechas de garantía y calibración, un intervalo de inspección y notas</li><li><strong>Fotos</strong> que adjuntas a una herramienta, desde la cámara o la fototeca, y una etiqueta opcional para cada una (placa de serie, recibo, foto del estado, etc.)</li><li><strong>Registros de préstamo:</strong> si prestas una herramienta, el nombre que escribes para quien la recibe y las fechas de préstamo y de devolución</li><li><strong>Historial de la herramienta:</strong> un registro en el dispositivo de revisiones de cajón, cambios de estado y préstamos, cada uno con fecha y una nota o foto opcional</li><li><strong>Registros de mantenimiento:</strong> fecha del servicio, descripción y costo</li><li><strong>Cajas de herramientas:</strong> nombre, tipo, marca, SKU, costo, fecha de compra y cómo se anidan</li><li><strong>Preferencias de la app:</strong> idioma, apariencia, ajuste de bloqueo, orden y opciones similares</li></ul><p>Todo esto lo ingresas tú y permanece por completo bajo tu control. El nombre de quien recibe el préstamo es texto libre que tú eliges escribir; si prefieres no registrar el nombre de una persona, usa iniciales o una etiqueta.</p>"),
   ("3. Dónde se guardan los datos", "<p>Todos los datos se guardan localmente en tu dispositivo: los registros en el framework SwiftData de Apple y los archivos de fotos en el contenedor privado de la app. MTIS <strong>no</strong> usa iCloud, CloudKit ni ningún servicio de sincronización, y <strong>no</strong> opera ningún servidor de aplicación, base de datos en la nube ni API. Tus datos existen solo en los dispositivos donde tú los pones.</p>"),
   ("4. Copias de seguridad y exportaciones", "<p>MTIS puede generar archivos CSV, informes PDF (inventario, documentación de seguro, estimación de depreciación), hojas de etiquetas QR imprimibles y un archivo único de copia de seguridad de todo tu inventario. Estos se crean solo cuando pulsas Exportar, Imprimir o Copia de seguridad, y salen de tu dispositivo únicamente mediante la acción de compartir de iOS que <em>tú</em> elijas: Archivos, Mail, Mensajes, AirDrop, etc. MTIS nunca los transmite a ningún sitio por su cuenta.</p>"),
   ("5. Cámara y fototeca", "<p>El acceso a la cámara y a la fototeca se usa solo para adjuntar una foto a una herramienta o para leer texto o un código de barras de una etiqueta con el framework Vision de Apple, en el dispositivo (por ejemplo, para capturar un número de serie o buscar una pieza). Las imágenes, el texto reconocido y los códigos escaneados se procesan en tu dispositivo y nunca se suben.</p>"),
   ("6. Siri y Atajos", "<p>Si usas Siri o la app Atajos, MTIS puede responder preguntas como «dónde está mi llave dinamométrica» leyendo la ubicación de una herramienta, su estado y —si la has prestado— el nombre que ingresaste de quien la tiene, y devolviendo eso en el resultado hablado o en pantalla. También puede abrir la app en una nueva ficha de herramienta o en una revisión de cajón. Estas acciones se ejecutan en tu dispositivo con tus datos locales. Cómo procesa Siri tu solicitud hablada lo controlan los ajustes de Siri y Buscar de tu dispositivo y la política de privacidad de Apple, no MTIS.</p>"),
   ("7. Face ID, Touch ID y código", "<p>MTIS ofrece un bloqueo opcional, desactivado por defecto. Cuando se activa, requiere Face ID, Touch ID o el código del dispositivo para abrir la app después de que haya estado en segundo plano. La autenticación la gestiona por completo el framework LocalAuthentication de Apple; MTIS nunca recibe ni guarda datos biométricos.</p>"),
   ("8. Compra dentro de la app", "<p>MTIS es gratis para un inventario de herramientas completo. Una compra única opcional (“MTIS Pro”) desbloquea las fotos de herramientas, el registro de mantenimiento e historial, la copia de seguridad y restauración, la importación y exportación CSV, y los informes PDF y de valor. La compra la procesa por completo el App Store de Apple. MTIS no recopila, ve ni guarda información de pago. Apple puede procesar datos relacionados con la compra según su propia política de privacidad.</p>"),
   ("9. Sin rastreo ni publicidad", "<p>MTIS no incluye ningún SDK de publicidad, ningún SDK de analítica ni ninguna librería de rastreo de terceros. No usa el identificador de publicidad (IDFA) y no crea un perfil de ti ni de tu uso.</p>"),
   ("10. Uso de red", "<p>MTIS no realiza ninguna conexión de red salvo con el App Store de Apple para la compra opcional y para restaurar una compra anterior. No hay servicio de informes de fallos, ni configuración remota, ni ningún tipo de “llamada a casa”.</p>"),
   ("11. Divulgación de APIs de motivo requerido", "<p>Conforme a los requisitos del manifiesto de privacidad de Apple, MTIS declara que accede a marcas de tiempo de archivos (para leer y escribir sus propios datos y archivos de exportación), al espacio en disco (para comprobar la capacidad antes de una copia de seguridad) y a <code>UserDefaults</code> (para guardar tus preferencias locales). Nada de esta información se recopila ni se transmite.</p>"),
   ("12. Eliminación de datos", "<p>Para eliminar todos tus datos, borra MTIS de tu iPhone o iPad. Como no hay nada guardado en un servidor ni en iCloud, quitar la app lo elimina todo. También puedes borrar herramientas, cajas y registros individuales en cualquier momento dentro de la app.</p>"),
   ("13. Privacidad de menores", "<p>MTIS es una herramienta para profesionales de oficios, técnicos y aficionados. No está dirigida a menores, no recopila conscientemente datos de nadie de forma directa y no se conecta a ningún servicio en línea que lo haría.</p>"),
   ("14. Cambios en esta política", "<p>Si hacemos cambios importantes, actualizaremos la fecha en la parte superior de esta página. La política vigente siempre está disponible en esta URL.</p>"),
   ("15. Contacto", "<p>¿Preguntas o inquietudes sobre privacidad? Escribe a <a href=\"mailto:mtis-app@proton.me\">mtis-app@proton.me</a>.</p>"),
  ],
 ),
 "ar": dict(
  title="سياسة الخصوصية — MTIS",
  desc="سياسة خصوصية MTIS. كل أداة وصورة وملاحظة تبقى على جهازك. بلا حساب، بلا خادم، بلا تتبّع.",
  h="سياسة الخصوصية", sub="باختصار: لا شيء مما تُدخله يغادر جهازك.",
  updated="آخر تحديث: ٢٠ سبتمبر ٢٠٢٦",
  tldr_h="النسخة المختصرة",
  tldr=["‏MTIS بلا حساب وبلا تسجيل دخول وبلا اشتراك.",
        "كل أداة وصورة وملاحظة تُحفظ فقط على iPhone أو iPad الخاص بك.",
        "لا يوجد خادم لـ MTIS. لا شيء مما تُدخله يُرفَع — ولا توجد مزامنة سحابية.",
        "بلا إعلانات، بلا تحليلات، بلا تتبّع من أطراف خارجية من أي نوع.",
        "لا تغادر الملفات جهازك إلا عندما تصدّرها أو تشاركها أنت صراحةً.",
        "احذف التطبيق لمسح كل بياناته."],
  sections=[
   ("١. من نحن", "<p>‏MTIS (نظام جرد أدوات الميكانيكي، “التطبيق”) تطوّره وتنشره BARAKAH TECHNOLOGIES, INC. للأسئلة حول هذه السياسة، راسل <a href=\"mailto:mtis-app@proton.me\">mtis-app@proton.me</a>.</p>"),
   ("٢. ما البيانات التي يحفظها التطبيق", "<p>يحفظ MTIS فقط المعلومات التي تُدخلها عن أدواتك ومعداتك. قد تشمل:</p><ul><li><strong>تفاصيل الأداة:</strong> الاسم والعلامة التجارية والطراز والرقم التسلسلي ورقم المخزون والفئة والفئة الفرعية والمقاس والخامة ونطاق العزم والكمية والحالة والموقع والمورّد وتاريخ الشراء والتكلفة وقيمة الاستبدال وتواريخ الضمان والمعايرة وفترة الفحص والملاحظات</li><li><strong>الصور</strong> التي ترفقها بأداة، من الكاميرا أو مكتبة الصور، وتصنيف اختياري لكل صورة (لوحة الرقم التسلسلي، إيصال، صورة الحالة، وغيرها)</li><li><strong>سجلات الإعارة:</strong> إذا أعرتَ أداة، الاسم الذي تكتبه للمستعير وتاريخا الإعارة والإرجاع</li><li><strong>سجل الأداة:</strong> سجل على الجهاز لعمليات فحص الأدراج وتغييرات الحالة والإعارات، لكل منها تاريخ وملاحظة أو صورة اختيارية</li><li><strong>سجلات الصيانة:</strong> تاريخ الخدمة والوصف والتكلفة</li><li><strong>صناديق الأدوات:</strong> الاسم والنوع والعلامة التجارية ورمز المنتج والتكلفة وتاريخ الشراء وطريقة تداخلها</li><li><strong>تفضيلات التطبيق:</strong> اختيار اللغة والمظهر وإعداد القفل وترتيب الفرز وخيارات مشابهة</li></ul><p>كل هذا تُدخله أنت ويبقى بالكامل تحت سيطرتك. اسم المستعير نص حر تختار كتابته؛ وإذا كنت تفضّل عدم تسجيل اسم شخص، فاستخدم الأحرف الأولى أو تصنيفاً بدلاً من ذلك.</p>"),
   ("٣. أين تُحفظ البيانات", "<p>تُحفظ كل البيانات محلياً على جهازك: السجلات المنظّمة في إطار عمل SwiftData من Apple، وملفات الصور في حاوية التطبيق الخاصة. لا يستخدم MTIS <strong>إطلاقاً</strong> iCloud أو CloudKit أو أي خدمة مزامنة، ولا يُشغّل <strong>أي</strong> خادم تطبيقات أو قاعدة بيانات سحابية أو واجهة برمجية. بياناتك موجودة فقط على الأجهزة التي تضعها عليها.</p>"),
   ("٤. النسخ الاحتياطية والتصدير", "<p>يمكن لـ MTIS إنشاء ملفات CSV وتقارير PDF (جرد، وثائق تأمين، تقدير إهلاك) وأوراق ملصقات QR قابلة للطباعة وأرشيف نسخة احتياطية بملف واحد لجردك بالكامل. تُنشأ هذه فقط عند الضغط على تصدير أو طباعة أو نسخ احتياطي، ولا تغادر جهازك إلا عبر إجراء المشاركة في iOS الذي <em>تختاره أنت</em> — الملفات أو Mail أو الرسائل أو AirDrop وغيرها. لا يرسلها MTIS إلى أي مكان من تلقاء نفسه.</p>"),
   ("٥. الكاميرا ومكتبة الصور", "<p>يُستخدم الوصول إلى الكاميرا ومكتبة الصور فقط لإرفاق صورة بأداة، أو لقراءة نص أو رمز شريطي على ملصق باستخدام إطار Vision من Apple على الجهاز (مثلاً لالتقاط رقم تسلسلي أو البحث عن قطعة). تُعالَج الصور والنص المُتعرَّف عليه والرموز الممسوحة على جهازك ولا تُرفَع أبداً.</p>"),
   ("٦. Siri والاختصارات", "<p>إذا كنت تستخدم Siri أو تطبيق الاختصارات، يمكن لـ MTIS الإجابة عن أسئلة مثل «أين مفتاح العزم» بقراءة موقع الأداة وحالتها — وإن كنت قد أعرتَها — اسم المستعير الذي أدخلتَه، وإرجاع ذلك في النتيجة المنطوقة أو المعروضة. كما يمكنه فتح التطبيق على إدخال أداة جديد أو فحص درج. تُنفَّذ هذه الإجراءات على جهازك باستخدام بياناتك المحلية. أما كيفية معالجة Siri لطلبك المنطوق فتتحكم بها إعدادات «Siri والبحث» في جهازك وسياسة خصوصية Apple، لا MTIS.</p>"),
   ("٧. Face ID و Touch ID ورمز الدخول", "<p>يوفّر MTIS قفلاً اختيارياً للتطبيق، مُعطَّلاً افتراضياً. عند تفعيله، يتطلّب Face ID أو Touch ID أو رمز دخول جهازك لفتح التطبيق بعد أن يكون في الخلفية. تتولّى المصادقة بالكامل إطار LocalAuthentication من Apple؛ ولا يستقبل MTIS بيانات حيوية أو يحفظها إطلاقاً.</p>"),
   ("٨. الشراء داخل التطبيق", "<p>‏MTIS مجاني لجرد أدوات كامل. عملية شراء واحدة اختيارية (“MTIS Pro”) تفتح صور الأدوات وسجل الصيانة والمحفوظات والنسخ الاحتياطي والاستعادة واستيراد وتصدير CSV وتقارير PDF والقيمة. تتم معالجة الشراء بالكامل عبر App Store من Apple. لا يجمع MTIS أي معلومات دفع ولا يراها ولا يحفظها. قد تعالج Apple بيانات متعلقة بالشراء وفق سياسة الخصوصية الخاصة بها.</p>"),
   ("٩. بلا تتبّع أو إعلانات", "<p>لا يحتوي MTIS على أي حزمة تطوير إعلانات أو تحليلات أو أي مكتبة تتبّع من أطراف خارجية. لا يستخدم مُعرِّف المُعلِنين (IDFA)، ولا يبني ملفاً عنك أو عن استخدامك.</p>"),
   ("١٠. استخدام الشبكة", "<p>لا يُجري MTIS أي اتصالات شبكية باستثناء الاتصال بـ App Store من Apple للشراء الاختياري ولاستعادة عملية شراء سابقة. لا توجد خدمة إبلاغ عن الأعطال ولا تهيئة عن بُعد ولا أي “اتصال بالمنزل” من أي نوع.</p>"),
   ("١١. الإفصاح عن واجهات برمجية ذات سبب مطلوب", "<p>وفق متطلبات بيان الخصوصية من Apple، يُصرّح MTIS بأنه يصل إلى طوابع زمنية للملفات (لقراءة وكتابة بياناته وملفات التصدير)، ومساحة القرص (للتحقق من السعة قبل إنشاء نسخة احتياطية)، و<code>UserDefaults</code> (لحفظ تفضيلاتك المحلية). لا يُجمع أي من هذه المعلومات ولا يُنقل.</p>"),
   ("١٢. حذف البيانات", "<p>لحذف كل بياناتك، احذف MTIS من iPhone أو iPad الخاص بك. ولأن لا شيء محفوظ على خادم أو في iCloud، فإن إزالة التطبيق تزيل كل شيء. يمكنك أيضاً حذف أدوات وصناديق وسجلات مفردة في أي وقت داخل التطبيق.</p>"),
   ("١٣. خصوصية الأطفال", "<p>‏MTIS أداة للحرفيين والفنيين والهواة. وهو غير موجَّه للأطفال، ولا يجمع بيانات من أي شخص مباشرةً عن علم، ولا يتصل بأي خدمة عبر الإنترنت تفعل ذلك.</p>"),
   ("١٤. التغييرات على هذه السياسة", "<p>إذا أجرينا تغييرات جوهرية، فسنحدّث التاريخ أعلى هذه الصفحة. السياسة الحالية متاحة دائماً على هذا الرابط.</p>"),
   ("١٥. التواصل", "<p>أسئلة أو مخاوف بشأن الخصوصية؟ راسل <a href=\"mailto:mtis-app@proton.me\">mtis-app@proton.me</a>.</p>"),
  ],
 ),
}

def build_privacy(lang):
    d = PV[lang]
    tldr = "\n".join(f"      <li>{x}</li>" for x in d["tldr"])
    secs = "\n".join(f"  <h2>{t}</h2>\n  {body}" for t, body in d["sections"])
    note = ""
    if lang != "en":
        note = '<p style="font-size:13px;color:var(--muted);margin-bottom:24px;">' + (
          "Traducción de cortesía. En caso de discrepancia, prevalece la versión en inglés." if lang == "es"
          else "ترجمة مقدَّمة للتيسير. عند وجود اختلاف، تُعتمد النسخة الإنجليزية.") + '</p>'
    platform = {"en": "Apple platforms · iPhone and iPad", "es": "Plataformas Apple · iPhone y iPad", "ar": "منصات Apple · iPhone وiPad"}[lang]
    return head("privacy", lang, d["title"], d["desc"]) + "\n" + nav("privacy", lang) + f"""
<div class="page-header">
  <p><strong>{platform}</strong></p>
  <h1>{d['h']}</h1>
  <p>{d['sub']}</p>
</div>
<div class="content">
  <p class="updated">{d['updated']}</p>
  {note}
  <div class="tl-dr">
    <h2>{d['tldr_h']}</h2>
    <ul>
{tldr}
    </ul>
  </div>
{secs}
</div>
""" + footer(lang)


# ---- SUPPORT content -----------------------------------------------------
SP = {
 "en": dict(
  title="Support — MTIS",
  desc="Get help with MTIS. FAQs on adding tools, scanning labels, reports, toolboxes, pricing, and privacy.",
  h="Support", sub="Answers to common questions, and how to get help.",
  cc_h="Can't find your answer?",
  cc_p="Email us — we usually reply within 1–2 business days.",
  faq_h="Frequently asked questions",
  groups=[
   ("Getting started", [
     ("Do I need to create an account?", "<p>No. MTIS has no account, no login, and no email sign-up. Open the app and start adding tools. Everything is stored on your device.</p>"),
     ("How do I add a tool?", "<p>Go to the <strong>Tools</strong> tab and tap <strong>+</strong> (top right). Fill in at least a name and either a serial number or a stock number, then tap <strong>Save</strong>. Everything else — photo, brand, cost, dates — is optional and can be added later.</p>"),
     ("What's the difference between a serial number and a stock number?", "<p>The <strong>serial number</strong> is the manufacturer's. The <strong>stock number</strong> is your own shop or asset number — use it for tools that have no serial, or that use an unusual numbering scheme. Every tool needs at least one of the two.</p>"),
     ("How do I remove the pre-loaded sample tools?", "<p>Go to <strong>Settings → Clear Sample Data</strong>. Only the pre-loaded examples are removed; your own tools are untouched, and the samples won't come back.</p>"),
   ]),
   ("Pricing & purchase", [
     ("Is MTIS free?", "<p>Yes. Building and browsing your full tool list is free, with no limits. A one-time $7.99 purchase (“MTIS Pro”) adds tool photos, the maintenance log and history, backup and restore, CSV import and export, and every PDF and value report.</p>"),
     ("Is it a subscription?", "<p>No. One payment, yours to keep. Nothing renews and nothing is charged automatically.</p>"),
     ("How do I restore my purchase on a new device?", "<p>On the purchase screen, or in <strong>Settings → Restore Purchase</strong>, tap Restore. Make sure you're signed in with the same Apple ID you used to buy MTIS.</p>"),
   ]),
   ("Scanning", [
     ("How does label scanning work?", "<p>Open the <strong>Scan</strong> tab, tap <strong>Scan Label</strong>, and photograph the tool's label. MTIS reads the text on your device and lets you drop a recognized value into the Serial, Stock, or Model field.</p>"),
     ("What about QR codes and barcodes?", "<p>Tap <strong>Scan QR/Barcode</strong> on the Scan tab. If the code matches a tool's serial or stock number, MTIS opens that tool. If it doesn't match anything, MTIS starts a new tool with the code pre-filled.</p>"),
     ("Can I print my own QR labels?", "<p>Yes — <strong>Settings → Print QR Labels</strong> generates a PDF sheet with one code per tool. Print it, cut it up, and stick one on every tool, drawer, or box.</p>"),
   ]),
   ("Reports & data", [
     ("What can I export?", "<p>From <strong>Settings → Data</strong>: a CSV of your whole inventory, a PDF inventory report, an insurance-claim PDF with a photo and value for every tool, and a straight-line depreciation estimate.</p>"),
     ("Does the CSV work with Excel or Numbers?", "<p>Yes. The column order matches common tool-inventory exports, and importing tolerates extra, missing, or reordered columns.</p>"),
     ("How do backups work?", "<p><strong>Settings → Backup</strong> writes your entire inventory — database and photos — to a single file, which you save through the share sheet. <strong>Restore</strong> reads that file back; relaunch MTIS afterward for it to take effect. Your current data is left untouched unless the restore fully succeeds.</p>"),
   ]),
   ("Organizing", [
     ("What are toolboxes for?", "<p>They represent physical containers — a tool chest, a roller-cabinet drawer, a truck bin. Assign tools to them, nest drawers inside a cabinet, and track a toolbox's own brand, SKU, cost, and purchase date.</p>"),
     ("Adding a roll cab with a lot of drawers?", "<p>When you create the toolbox, enter a drawer count and MTIS creates “Drawer 1”, “Drawer 2”, … inside it automatically (up to 60).</p>"),
     ("What's an inventory audit?", "<p><strong>Settings → Start Inventory Audit</strong> walks you through your tools one at a time to confirm each is physically present, then shows you a list of what wasn't confirmed. Scope it to all tools or a single toolbox.</p>"),
   ]),
   ("Privacy & security", [
     ("Does MTIS send my data anywhere?", "<p>No. There is no server, no cloud sync, and no analytics. Everything lives on your device. See the full <a href=\"privacy.html\">Privacy Policy</a>.</p>"),
     ("How do I lock the app?", "<p><strong>Settings → Security → Require Face ID to Unlock</strong>. It's off by default. When on, MTIS shows a lock screen after it has been in the background, and falls back to your passcode.</p>"),
     ("How do I delete all my data?", "<p>Delete MTIS from your iPhone or iPad. Nothing is stored anywhere else, so removing the app removes everything.</p>"),
   ]),
   ("Languages", [
     ("Which languages does MTIS support?", "<p>English, with Spanish and Arabic in progress. Choose a language on the welcome screen or from the lock screen, then reopen MTIS for it to take effect.</p>"),
   ]),
  ],
 ),
 "es": dict(
  title="Soporte — MTIS",
  desc="Obtén ayuda con MTIS. Preguntas frecuentes sobre agregar herramientas, escanear etiquetas, informes, cajas, precios y privacidad.",
  h="Soporte", sub="Respuestas a preguntas comunes y cómo obtener ayuda.",
  cc_h="¿No encuentras tu respuesta?",
  cc_p="Escríbenos — normalmente respondemos en 1–2 días hábiles.",
  faq_h="Preguntas frecuentes",
  groups=[
   ("Primeros pasos", [
     ("¿Necesito crear una cuenta?", "<p>No. MTIS no tiene cuenta, ni inicio de sesión, ni registro por correo. Abre la app y empieza a agregar herramientas. Todo se guarda en tu dispositivo.</p>"),
     ("¿Cómo agrego una herramienta?", "<p>Ve a la pestaña <strong>Herramientas</strong> y pulsa <strong>+</strong> (arriba a la derecha). Completa al menos un nombre y un número de serie o de inventario, y pulsa <strong>Guardar</strong>. Lo demás —foto, marca, costo, fechas— es opcional.</p>"),
     ("¿Cuál es la diferencia entre número de serie y número de inventario?", "<p>El <strong>número de serie</strong> es el del fabricante. El <strong>número de inventario</strong> es el de tu taller — úsalo para herramientas sin serie o con una numeración poco común. Cada herramienta necesita al menos uno de los dos.</p>"),
     ("¿Cómo elimino las herramientas de muestra?", "<p>Ve a <strong>Ajustes → Borrar datos de muestra</strong>. Solo se quitan los ejemplos precargados; tus herramientas no se tocan y las muestras no volverán.</p>"),
   ]),
   ("Precios y compra", [
     ("¿MTIS es gratis?", "<p>Sí. Crear y consultar tu lista completa de herramientas es gratis, sin límites. Una compra única de $7.99 (“MTIS Pro”) añade las fotos de herramientas, el registro de mantenimiento e historial, la copia de seguridad y restauración, la importación y exportación CSV, y todos los informes PDF y de valor.</p>"),
     ("¿Es una suscripción?", "<p>No. Un solo pago, tuyo para siempre. Nada se renueva ni se cobra automáticamente.</p>"),
     ("¿Cómo restauro mi compra en un dispositivo nuevo?", "<p>En la pantalla de compra, o en <strong>Ajustes → Restaurar compra</strong>, pulsa Restaurar. Usa el mismo Apple ID con el que compraste MTIS.</p>"),
   ]),
   ("Escaneo", [
     ("¿Cómo funciona el escaneo de etiquetas?", "<p>Abre la pestaña <strong>Escanear</strong>, pulsa <strong>Escanear etiqueta</strong> y fotografía la etiqueta de la herramienta. MTIS lee el texto en tu dispositivo y te deja pasar un valor reconocido a los campos Serie, Inventario o Modelo.</p>"),
     ("¿Y los códigos QR y de barras?", "<p>Pulsa <strong>Escanear QR/código de barras</strong> en la pestaña Escanear. Si el código coincide con el número de serie o de inventario de una herramienta, MTIS la abre. Si no coincide con nada, MTIS crea una herramienta nueva con el código ya puesto.</p>"),
     ("¿Puedo imprimir mis propias etiquetas QR?", "<p>Sí — <strong>Ajustes → Imprimir etiquetas QR</strong> genera una hoja PDF con un código por herramienta. Imprímela, recórtala y pega una en cada herramienta, cajón o caja.</p>"),
   ]),
   ("Informes y datos", [
     ("¿Qué puedo exportar?", "<p>Desde <strong>Ajustes → Datos</strong>: un CSV de todo tu inventario, un informe de inventario en PDF, un PDF para reclamo de seguro con foto y valor de cada herramienta, y una estimación de depreciación lineal.</p>"),
     ("¿El CSV funciona con Excel o Numbers?", "<p>Sí. El orden de columnas coincide con las exportaciones habituales de inventario de herramientas, y la importación tolera columnas de más, de menos o reordenadas.</p>"),
     ("¿Cómo funcionan las copias de seguridad?", "<p><strong>Ajustes → Copia de seguridad</strong> escribe todo tu inventario —base de datos y fotos— en un solo archivo, que guardas mediante la hoja de compartir. <strong>Restaurar</strong> lo vuelve a leer; reinicia MTIS después para que surta efecto. Tus datos actuales no se tocan a menos que la restauración se complete por completo.</p>"),
   ]),
   ("Organización", [
     ("¿Para qué sirven las cajas de herramientas?", "<p>Representan contenedores físicos: un cofre, un cajón de gabinete, un bin de camión. Asigna herramientas, anida cajones dentro de un gabinete y controla la marca, el SKU, el costo y la fecha de compra de la propia caja.</p>"),
     ("¿Agregar un gabinete con muchos cajones?", "<p>Al crear la caja, indica un número de cajones y MTIS crea “Cajón 1”, “Cajón 2”, … dentro automáticamente (hasta 60).</p>"),
     ("¿Qué es una auditoría de inventario?", "<p><strong>Ajustes → Iniciar auditoría de inventario</strong> te guía por tus herramientas una por una para confirmar que cada una está presente, y luego te muestra la lista de lo que no se confirmó. Puedes limitarla a todas las herramientas o a una sola caja.</p>"),
   ]),
   ("Privacidad y seguridad", [
     ("¿MTIS envía mis datos a algún sitio?", "<p>No. No hay servidor, ni sincronización en la nube, ni analíticas. Todo vive en tu dispositivo. Consulta la <a href=\"privacy.es.html\">Política de Privacidad</a> completa.</p>"),
     ("¿Cómo bloqueo la app?", "<p><strong>Ajustes → Seguridad → Requerir Face ID para desbloquear</strong>. Está desactivado por defecto. Cuando se activa, MTIS muestra una pantalla de bloqueo tras estar en segundo plano y recurre a tu código.</p>"),
     ("¿Cómo elimino todos mis datos?", "<p>Borra MTIS de tu iPhone o iPad. No hay nada guardado en ningún otro sitio, así que quitar la app lo elimina todo.</p>"),
   ]),
   ("Idiomas", [
     ("¿Qué idiomas admite MTIS?", "<p>Inglés, con español y árabe en curso. Elige un idioma en la pantalla de bienvenida o desde la pantalla de bloqueo, y vuelve a abrir MTIS para que surta efecto.</p>"),
   ]),
  ],
 ),
 "ar": dict(
  title="الدعم — MTIS",
  desc="احصل على مساعدة بشأن MTIS. أسئلة شائعة حول إضافة الأدوات ومسح الملصقات والتقارير والصناديق والأسعار والخصوصية.",
  h="الدعم", sub="إجابات عن الأسئلة الشائعة وكيفية الحصول على المساعدة.",
  cc_h="لم تجد إجابتك؟",
  cc_p="راسلنا — نردّ عادةً خلال يوم إلى يومَي عمل.",
  faq_h="الأسئلة الشائعة",
  groups=[
   ("البداية", [
     ("هل يلزمني إنشاء حساب؟", "<p>لا. ‏MTIS بلا حساب وبلا تسجيل دخول وبلا اشتراك بالبريد. افتح التطبيق وابدأ بإضافة الأدوات. كل شيء يُحفظ على جهازك.</p>"),
     ("كيف أضيف أداة؟", "<p>انتقل إلى تبويب <strong>الأدوات</strong> واضغط <strong>+</strong> (أعلى اليسار). أدخل على الأقل اسماً ورقماً تسلسلياً أو رقم مخزون، ثم اضغط <strong>حفظ</strong>. الباقي — صورة، علامة تجارية، تكلفة، تواريخ — اختياري ويمكن إضافته لاحقاً.</p>"),
     ("ما الفرق بين الرقم التسلسلي ورقم المخزون؟", "<p>‏<strong>الرقم التسلسلي</strong> هو رقم الشركة المصنّعة. و<strong>رقم المخزون</strong> هو رقمك في الورشة — استخدمه للأدوات التي لا رقم تسلسلي لها أو التي تتبع ترقيماً غير معتاد. كل أداة تحتاج واحداً منهما على الأقل.</p>"),
     ("كيف أحذف الأدوات النموذجية المُحمَّلة مسبقاً؟", "<p>انتقل إلى <strong>الإعدادات → مسح البيانات النموذجية</strong>. تُزال الأمثلة المُحمَّلة مسبقاً فقط؛ أدواتك لا تُمَس، والعيّنات لن تعود.</p>"),
   ]),
   ("الأسعار والشراء", [
     ("هل MTIS مجاني؟", "<p>نعم. إنشاء قائمة أدواتك الكاملة وتصفّحها مجاني بلا حدود. عملية شراء واحدة بقيمة $7.99 (“MTIS Pro”) تضيف صور الأدوات وسجل الصيانة والمحفوظات والنسخ الاحتياطي والاستعادة واستيراد وتصدير CSV وكل تقارير PDF والقيمة.</p>"),
     ("هل هو اشتراك؟", "<p>لا. دفعة واحدة، وهو ملكك. لا شيء يتجدّد ولا شيء يُخصَم تلقائياً.</p>"),
     ("كيف أستعيد عملية الشراء على جهاز جديد؟", "<p>في شاشة الشراء، أو في <strong>الإعدادات → استعادة الشراء</strong>، اضغط استعادة. تأكد من تسجيل الدخول بنفس Apple ID الذي اشتريت به MTIS.</p>"),
   ]),
   ("المسح", [
     ("كيف يعمل مسح الملصقات؟", "<p>افتح تبويب <strong>مسح</strong>، اضغط <strong>مسح الملصق</strong>، وصوّر ملصق الأداة. يقرأ MTIS النص على جهازك ويتيح لك إدراج قيمة مُتعرَّف عليها في حقل الرقم التسلسلي أو المخزون أو الطراز.</p>"),
     ("وماذا عن رموز QR والباركود؟", "<p>اضغط <strong>مسح رمز QR/باركود</strong> في تبويب مسح. إذا طابق الرمز الرقم التسلسلي أو رقم المخزون لأداة، يفتحها MTIS. وإن لم يطابق شيئاً، يبدأ MTIS أداة جديدة والرمز مُدرَج مسبقاً.</p>"),
     ("هل يمكنني طباعة ملصقات QR خاصة بي؟", "<p>نعم — <strong>الإعدادات → طباعة ملصقات QR</strong> يُنشئ ورقة PDF برمز واحد لكل أداة. اطبعها وقُصّها والصق واحدة على كل أداة أو درج أو صندوق.</p>"),
   ]),
   ("التقارير والبيانات", [
     ("ما الذي يمكنني تصديره؟", "<p>من <strong>الإعدادات → البيانات</strong>: ملف CSV لجردك بالكامل، وتقرير جرد PDF، وملف PDF لمطالبة تأمين بصورة وقيمة لكل أداة، وتقدير إهلاك بالطريقة الثابتة.</p>"),
     ("هل يعمل CSV مع Excel أو Numbers؟", "<p>نعم. ترتيب الأعمدة يطابق عمليات تصدير جرد الأدوات الشائعة، والاستيراد يتحمّل أعمدة زائدة أو ناقصة أو مُعاد ترتيبها.</p>"),
     ("كيف تعمل النسخ الاحتياطية؟", "<p><strong>الإعدادات → نسخ احتياطي</strong> يكتب جردك بالكامل — قاعدة البيانات والصور — في ملف واحد تحفظه عبر ورقة المشاركة. <strong>استعادة</strong> تقرأ ذلك الملف؛ أعد تشغيل MTIS بعدها ليأخذ مفعوله. بياناتك الحالية لا تُمَس ما لم تكتمل الاستعادة بالكامل.</p>"),
   ]),
   ("التنظيم", [
     ("ما فائدة صناديق الأدوات؟", "<p>تمثّل حاويات فعلية — صندوق أدوات، درج خزانة متحرّكة، صندوق شاحنة. أسنِد الأدوات إليها، وضع الأدراج داخل خزانة، وتتبّع العلامة التجارية ورمز المنتج والتكلفة وتاريخ الشراء للصندوق نفسه.</p>"),
     ("تضيف خزانة متحرّكة بأدراج كثيرة؟", "<p>عند إنشاء الصندوق، أدخل عدد الأدراج وينشئ MTIS “درج ١” و“درج ٢”… بداخله تلقائياً (حتى ٦٠).</p>"),
     ("ما هو جرد المخزون؟", "<p><strong>الإعدادات → بدء جرد المخزون</strong> يمرّ بك على أدواتك واحدة تلو الأخرى لتأكيد وجود كل منها، ثم يعرض قائمة بما لم يُؤكَّد. يمكن قصره على كل الأدوات أو على صندوق واحد.</p>"),
   ]),
   ("الخصوصية والأمان", [
     ("هل يرسل MTIS بياناتي إلى أي مكان؟", "<p>لا. لا يوجد خادم ولا مزامنة سحابية ولا تحليلات. كل شيء يبقى على جهازك. راجع <a href=\"privacy.ar.html\">سياسة الخصوصية</a> كاملةً.</p>"),
     ("كيف أقفل التطبيق؟", "<p><strong>الإعدادات → الأمان → طلب Face ID لإلغاء القفل</strong>. مُعطَّل افتراضياً. عند تفعيله، يعرض MTIS شاشة قفل بعد وجوده في الخلفية، ويرجع إلى رمز الدخول عند الحاجة.</p>"),
     ("كيف أحذف كل بياناتي؟", "<p>احذف MTIS من iPhone أو iPad الخاص بك. لا شيء محفوظ في أي مكان آخر، لذا فإن إزالة التطبيق تزيل كل شيء.</p>"),
   ]),
   ("اللغات", [
     ("ما اللغات التي يدعمها MTIS؟", "<p>الإنجليزية، مع العربية والإسبانية قيد الإنجاز. اختر لغة من شاشة الترحيب أو من شاشة القفل، ثم أعد فتح MTIS ليأخذ التغيير مفعوله.</p>"),
   ]),
  ],
 ),
}

def build_support(lang):
    d = SP[lang]
    groups = []
    for gtitle, items in d["groups"]:
        qs = "\n".join(f"""    <details>
      <summary>{q}</summary>
      <div class="faq-body">{a}</div>
    </details>""" for q, a in items)
        groups.append(f'  <div class="faq-group">\n    <h3>{gtitle}</h3>\n{qs}\n  </div>')
    groups_html = "\n\n".join(groups)
    return head("support", lang, d["title"], d["desc"]) + "\n" + nav("support", lang) + f"""
<div class="page-header">
  <h1>{d['h']}</h1>
  <p>{d['sub']}</p>
</div>
<div class="content" style="max-width:none;padding-bottom:0;">
  <div class="contact-card">
    <h2>{d['cc_h']}</h2>
    <p>{d['cc_p']}</p>
    <div class="links">
      <a href="mailto:mtis-app@proton.me">mtis-app@proton.me</a>
    </div>
  </div>

  <div class="faq">
    <h2>{d['faq_h']}</h2>
{groups_html}
  </div>
</div>
<div style="height:60px;"></div>
""" + footer(lang)


os.makedirs(OUT, exist_ok=True)
builders = {"index": build_index, "privacy": build_privacy, "support": build_support}
for page in PAGES:
    for lang in LANGS:
        path = os.path.join(OUT, fname(page, lang))
        with open(path, "w", encoding="utf-8") as f:
            f.write(builders[page](lang))
        print("wrote", fname(page, lang))
