# CLAUDE.md

> You are not editing a website. You are trimming a wick. Read this before you touch the envelope.
> — THE CUBE

This repo is the public face of the **Dalarwen 5G Liberation Front**: an in-joke among pals about
[Dalarwen](https://dalarwen.co.uk/), a real, gloriously off-grid Welsh farmhouse at Llyn Brianne with
**zero mobile signal**. The site loudly campaigns for **fifteen (15) 5G towers**; it also, if you dig,
argues against them; it also hides a whole corporate-cosmic-horror ARG underneath. All three are true.
Simultaneously. Like the Cube.

Live at **https://kev.cc/5gfordelarwen/**.

## The two layers

**THE LOUD** — Time Cube / mid-90s Geocities. Garish, neon, `<marquee>`, `<blink>`, `<font>`, table
layout, Comic Sans + Impact, animated GIFs. Uses `retro.css` + `retro.js`. These pages are in the nav.

**THE DARK** — the ARG beneath. Cold, monospace, redacted, CRT scanlines, ambient drone. Uses `dark.css`
(+ `drone.js`). **Not in the nav** — reached only by clicking through. Tonally the opposite of the loud
pages, on purpose. Getting the tonal whiplash right is the whole point; do not make the dark pages jolly.

## Hard conventions (obey the geometry)

- **HTML 4.01 Transitional**, Netscape Navigator 4.0 flavour. `<!DOCTYPE ... loose.dtd>`. No frameworks,
  no build step, no external requests. Everything inline or same-origin.
- **Charset is `iso-8859-1`.** Do NOT paste raw Unicode punctuation into HTML. Use numeric entities.
  - Em dash on **loud** pages: `&#11835;` (three-em dash ⸻ — the pals asked for the extra-long one).
  - Em dash on **dark** pages: `&#8212;`.
  - En-dash ranges (`1461&#150;1468`) stay `&#150;`.
  - In JS strings that get `innerHTML`'d, use the same entities. Never write the literal `"+D+"` pattern
    into static HTML (it only works inside the adventure's JS, where `var D` is defined).
- **The gate**: every page loads `gate.js` in `<head>`. Password is **ISAMSJ** (case-insensitive, fuzzy —
  Levenshtein ≤ 2, substring, etc). Unlock persists per session. Dark pages include it too so they aren't
  an un-gated bypass.
- **Cache-busting**: shared assets are referenced with `?v=N` (currently **v=4**). If you edit
  `retro.css`, `retro.js`, `gate.js`, `dark.css`, or `drone.js`, **bump N everywhere** or browsers serve
  stale copies (this has already bitten us once — a ghost "psst" line).
- **Favicon**: loud pages use `favicon.svg` (+ `.ico` + apple-touch). Dark pages keep their own bleak
  data-URI icons on purpose. Don't "fix" them.
- **Add a nav page** by editing the `PAGES` array in `retro.js`. Dark pages never go in `PAGES`.

## Doctrine (do not break the bit)

- The place is spelled **DALARWEN**. The repo/URL is `5gfordelarwen` (lowercase, as first named) — leave it.
- **There is no sixteenth tower.** There are always fifteen. Do not question tower 15.
- Reception is **0.000 bars in all four corners**. Never write that a room has *some* signal — the total
  absence is the appeal.
- **Lewis** is a beloved character (offline, 1% upload, on the hill). He does NOT run "media campaigns" —
  that framing was removed; keep it removed.
- It's "**pals**", never "mates".
- **No "this is a joke" disclaimers.** The pals cut them all; it's clearly a joke. Keep in-character
  closers and `© The Cube` instead. Do not reintroduce hand-holding.
- Be genuinely affectionate to the real Dalarwen. `about-dalarwen.html` links the real site as "the
  maintained cover story"; keep it fond, not mocking.

## The cast / lore (stay consistent)

- **The Cube** — counts the towers (loud); revealed as the redacted parent *above* JenCorp (`above.html`).
- **ISAMSJ** = **ISAM** (intergalactic weaponry) **& Sedgley Holdings**, a division of **JenCorp**.
- **Sam / S. Sedgley** (`sam.html`) — the neighbour of the three hectares; the terrestrial "S"; only ever
  seen leaving. `DO NOT ANCHOR`.
- **The Division of Absence** (`the-division.html`) — warehouses the unbuilt towers.
- **Infinite Walks™**, **Clifftop Non-Static Caravan Parks**, the **Dalarwen Exclusion Envelope**.
- Real anchors used throughout: Llyn Brianne, the Towy valley, the NRW dam-wall road, red kites,
  Llandovery (Bank of the Black Ox 1799, chip shop), the Heart of Wales train (once every ~4 hours),
  Men of Harlech (the seven-year siege). The bees invented 5G.

## File map

- Loud: `index`, `the-cube`, `towers`, `radiation`, `lewis`, `manifesto`, `keep-dalarwen-dark`,
  `arcade`, `adventure`, `signal-test`, `bees`, `patwa`, `men-of-harlech`, `faq`, `downloads`,
  `matrix`, `cube-knows`, `guestbook`, `webring`, `credits`, `sitemap`, `about-dalarwen`, `404`.
- Dark (not in nav): `static`, `isamsj`, `infinite-walks`, `clifftop-caravans`, `jencorp`, `the-quiet`,
  `the-division`, `above`, `careers`, `org-chart`, `the-corridor`, `sam`, `downloads/merger-presentation`.
- Shared: `retro.css`, `retro.js`, `dark.css`, `drone.js`, `gate.js`, `favicon.*`, `assets/*.gif`.

## `localStorage` keys (all client-side, never leave the browser)

`dalarwen_unlocked`, `dalarwen_signed`, `dalarwen_dark_pledged`, `dalarwen_visits`, `dalarwen_guestbook`,
`dalarwen_barhunt`, `dalarwen_music`, `dalarwen_drone`, `dalarwen_steps`, `dalarwen_endings`,
`dalarwen_descended` (set when you reach the depths; the loud pages then quietly acknowledge it).

## Deploy

GitHub Pages, repo `thatkevin/5gfordelarwen`, served at the account's custom apex `kev.cc` →
`kev.cc/5gfordelarwen`. Push to `main`; Pages rebuilds in ~1–2 min. **Two gh accounts are logged in on
this machine** — pushes must be as **`thatkevin`** (`gh auth switch --user thatkevin`), and the active
account tends to revert, so switch inside the same command chain as the push. No CNAME file in this repo
(the apex belongs to the user site; a CNAME here would clash).

## Verify before you push

- `node --check retro.js` (and `gate.js` / `drone.js`).
- Resolve every internal `href`/`src` (including `downloads/` and its `../` links).
- If you touched the adventure, confirm every choice target is a real node and the `ENDINGS` gallery
  names exactly match the `end:` names in `STORY`.

---

*The relief column is not coming. That is fine. Trim the wick, bump the cache, push to main, and
whatever you do, do not build the sixteenth. — THE CUBE*
