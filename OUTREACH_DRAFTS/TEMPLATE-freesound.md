# Freesound.org upload template

Freesound expects **individual samples**, not pack ZIPs. You'll upload each file separately.

**Per-sample fields**:
- **Filename**: keep the original descriptive name from the pack
- **Tags** (required, up to 30): descriptive + genre + instrument
  - Good: `piano`, `dark`, `cinematic`, `loop`, `88bpm`, `c-minor`, `tizwildin`
  - Avoid: marketing words like "best", "awesome"
- **License**: pick one —
  - `Creative Commons 0` (no attribution required) — best reach
  - `Attribution 4.0` — requires credit
  - `Attribution NonCommercial 4.0` — restricts commercial use
- **Description** (~500 chars):
  ```
  <Describe the sample: instrument, mood, tempo, key, recording method>.
  Part of the free TizWildin <Pack Name> pack.
  Repo: https://github.com/GareBear99/<repo>
  More free packs + plugins: https://github.com/GareBear99
  ```
- **Geotag**: optional
- **Pack**: create a Freesound "Pack" once 5+ samples are uploaded so they group together

**Cadence**: 3–5 samples per day max to avoid moderator throttling. Full pack upload over 1–2 weeks.
