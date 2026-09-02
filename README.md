# MTIS — Public Website

This repository hosts the public website for **MTIS (Mechanic Tool Inventory
System)**, a private, on-device tool inventory app for iOS.

Published via GitHub Pages at:
**https://m-t-i-s.github.io/iOS**

## Pages

| File | URL | Purpose |
|------|-----|---------|
| `index.html` | `/` | Landing page |
| `privacy.html` | `/privacy.html` | Privacy Policy |
| `support.html` | `/support.html` | Support & FAQ |

Each page has Spanish and Arabic versions selected from the language switcher
in the top-right of the nav:

| Language | Suffix | Direction |
|----------|--------|-----------|
| English  | `.html`     | LTR |
| Español  | `.es.html`  | LTR |
| العربية  | `.ar.html`  | RTL (`dir="rtl"`) |

Each page is self-contained: the styles live inline in a `<style>` block
(same as the reference template). `assets/site.css` is the editable source,
and `build/generate.py` regenerates all nine pages from it — run
`python3 build/generate.py` after changing the CSS or copy. `<link
rel="alternate" hreflang>` tags in each `<head>` tell search engines about
the translations.

## About MTIS

MTIS tracks tools, photos, serial and stock numbers, warranty and calibration
due dates, maintenance history, toolboxes, and inventory value — all stored
locally on device. CSV/PDF export, insurance and depreciation reports, OCR
label scanning, QR/barcode lookup, printable QR labels, and single-file local
backup. No account, no server, no tracking.

Free 3-day trial, then a one-time $4.99 purchase. No subscription.

**Contact:** mtis-app@proton.me
**© 2026 AbdurRahman Rozell**

## Before publishing

MTIS is a closed-source app — this repo holds the website only.

- Replace the `#appstore` placeholder links with the real App Store URL once
  the app is live — two per `index*.html` (hero and CTA), plus the
  "Coming soon" strip in the hero mockup.
- Set the App Store Connect **Privacy Policy URL** to
  `https://m-t-i-s.github.io/iOS/privacy.html` and the **Support URL** to
  `https://m-t-i-s.github.io/iOS/support.html`.
- The `es` / `ar` translations are a first pass and should get a
  native-speaker review before launch (same as the app's own translations).

## Design

Static pages, no build step. Type: Archivo (display) + IBM Plex Sans (body),
from Google Fonts. Palette sampled from the app icon: near-black `#0c1218` with an azure-blue
accent `#1f6fd8`. Light theme only, all colors explicit. Directional CSS
uses logical properties so the Arabic pages mirror correctly.

`assets/AppIcon-1024.png` is the source icon; `assets/icon-{32,64,180}.png`
are the resized favicon / touch-icon / nav mark (regenerate with
`sips -Z <size> --out assets/icon-<size>.png assets/AppIcon-1024.png`).
