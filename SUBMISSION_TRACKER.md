# Submission Tracker — TizWildin packs × directories

Matrix of every TizWildin sample pack × every realistic directory. Status per cell: `—` (not applicable), `pending`, `submitted YYYY-MM-DD`, `✅ listed`, `🛑 rejected`.

## Automation state (as of 2026-04-23)

- ✅ **All 11 pack READMEs patched** with pricing + hub-link block. Script: [`scripts/update_pack_pricing.py`](scripts/update_pack_pricing.py). Idempotent.
- ✅ **All 11 packs have `v1.0.0` GitHub releases** with auto-generated source ZIPs. Every pack's `/releases/latest` now resolves, and `/archive/refs/heads/main.zip` is the always-current free-download URL used in the pricing block.
- ❌ **`awesome-midi-sources` skipped** — list is scoped to *sites that host MIDI archives* (VGMusic, FreeMidi, Lakh dataset). Plugin-supplement packs bundling MIDI don't fit the pattern. Forcing a submission would be a rejection risk.
- ⏳ **Non-GitHub outreach requires account creation** — signup pages opened in browser: Bandcamp, Looperman, freesound.org, Sample Focus, Splice (creator program), KVR Audio, Plugins4Free, Bedroom Producers Blog.

## Legend
- `—` = out of scope for this directory
- `pending` = draft ready in `OUTREACH_DRAFTS/`, not submitted
- `submitted YYYY-MM-DD` = submitted, awaiting review
- `✅` = accepted / live
- `🛑` = submitted and rejected


## Satellite list status

| Satellite | Role | Status | Next action |
|---|---|---|---|
| [awesome-audio-plugins-dev](https://github.com/GareBear99/awesome-audio-plugins-dev) | Plugin/dev discovery | ✅ live | Keep synced with FreeEQ8/FreeVox8 releases |
| [awesome-music-platforms](https://github.com/GareBear99/awesome-music-platforms) | Artist platforms/distribution/selling | ✅ live | Continue backlink submissions and weekly updates |
| [awesome-python-audio-science](https://github.com/GareBear99/awesome-python-audio-science) | Python scientific audio, MIR, DSP, ML-audio, datasets, notebooks, creator automation | ✅ live | Add to hub README, link from `.io` router, and submit useful neutral additions upstream where appropriate |

## Packs

| Pack | BPM | Genre | Format | Content |
|------|----:|-------|--------|---------|
| [TizWildin-Aurora](https://github.com/GareBear99/TizWildin-Aurora) | varies | Neon / cinematic synth | WAV loops + stems | 3-segment synth melody pack |
| [TizWildin-Obsidian](https://github.com/GareBear99/TizWildin-Obsidian) | varies | Dark cinematic | WAV loops | Choir, menu loops, transitions, bass, atmosphere, drums, e-banjo |
| [TizWildin-Skyline](https://github.com/GareBear99/TizWildin-Skyline) | 30 | Synthwave / darkwave | WAV loops | 30-BPM tagged |
| [TizWildin-Chroma](https://github.com/GareBear99/TizWildin-Chroma) | varies | Game synthwave | WAV loops | Multi-segment |
| [TizWildin-Chime](https://github.com/GareBear99/TizWildin-Chime) | 88 | Multi (glass/void/halo/reed/neon) | WAV | 88-BPM chime collection |
| [Free-Violin-Synth-Sample-Kit](https://github.com/GareBear99/Free-Violin-Synth-Sample-Kit) | — | Physical model violin | WAV one-shots | Rendered from Instrudio |
| [Free-Dark-Piano-Sound-Kit](https://github.com/GareBear99/Free-Dark-Piano-Sound-Kit) | varies | Dark cinematic piano | WAV + MIDI | 88 notes + loops + MIDI |
| [Free-808-Producer-Kit](https://github.com/GareBear99/Free-808-Producer-Kit) | — | 808 bass | WAV one-shots | 94 samples, every chromatic key |
| [Free-Riser-Producer-Kit](https://github.com/GareBear99/Free-Riser-Producer-Kit) | — | FX | WAV | 115 risers + 63 downlifters |
| [Phonk-Producer-Toolkit](https://github.com/GareBear99/Phonk_Producer_Toolkit) | varies | Drift phonk | WAV + MIDI | 808s, cowbells, drums, MIDI |
| [Free-Future-Bass-Producer-Kit](https://github.com/GareBear99/Free-Future-Bass-Producer-Kit) | varies | Future bass | WAV | Loops, fills, drums, bass, synths |

## Directory fit matrix

> Rows: packs. Columns: directories. Cells: fit + status.

### GitHub lists

| Pack ↓ / List → | awesome-soundfonts (SF2/SFZ only) | awesome-midi-sources (MIDI only) |
|---|:---:|:---:|
| Aurora | — | — |
| Obsidian | — | — |
| Skyline | — | — |
| Chroma | — | — |
| Chime | — | — |
| Free-Violin-Synth | — | — |
| Free-Dark-Piano | — | pending |
| Free-808 | — | — |
| Free-Riser | — | — |
| Phonk-Toolkit | — | pending |
| Free-Future-Bass | — | — |

### Non-GitHub platforms

| Pack ↓ / Platform → | freesound | Looperman | Sample Focus | Bandcamp | r/WATMM FF | r/genre subs |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| Aurora | pending | pending | pending | pending | pending | r/synthwave |
| Obsidian | pending | pending | pending | pending | pending | r/darkambient |
| Skyline | pending | pending | pending | pending | pending | r/synthwave |
| Chroma | pending | pending | pending | pending | pending | r/gamedev, r/synthwave |
| Chime | pending | pending | pending | pending | pending | — |
| Free-Violin-Synth | pending | — | pending | pending | pending | — |
| Free-Dark-Piano | pending | pending | pending | pending | pending | — |
| Free-808 | pending | pending | pending | pending | pending | r/trapproduction |
| Free-Riser | pending | pending | pending | pending | pending | r/edmproduction |
| Phonk-Toolkit | pending | pending | pending | pending | pending | r/phonk |
| Free-Future-Bass | pending | pending | pending | pending | pending | r/edmproduction |

### Editorial press (one-shot pitches)

| Outlet | Status |
|---|---|
| Bedroom Producers Blog (Best Free Sample Packs roundup) | pending — 1 pitch per calendar quarter, batch 3–4 packs |
| Production Music Live | pending |
| Hive Sound | pending |

## Editorial reviews & promotional outreach

Use this table for **audio plugin review, free VST/AU plugin promotion, music-tech press, freeware roundup, and creator-story outreach**. Keep statuses truthful and include the date submitted. This tracker is intentionally SEO-aware, but every pitch should still read human and non-spammy.

| Outlet | Contact / route | Search/SEO intent | Best use | FreeEQ8 status | FreeVox8 status | Next action |
|---|---|---|---|---|---|---|
| Sound On Sound | Official Write for SOS/contact routes | professional studio review, pro audio magazine | Professional studio review / technical assessment | submitted 2026-05-05 | pending | Wait 7–10 business days before one concise follow-up |
| KVR Audio | `contactus@kvraudio.com` or developer submission flow | audio plugin database, VST plugin listing | Plugin database listing + release news | pending | pending | Submit through product/developer flow first; email only if needed |
| MusicTech editorial | `editors@musictech.com` | music technology news, plugin release | News tip / indie developer story | pending | pending | Send short solo-dev pitch |
| MusicTech / NME press office | `press@nmenetworks.com` | music-tech press release | Formal press-release route | pending | pending | Use only for polished release announcement |
| Bedroom Producers Blog | Contact form | free VST plugin, freeware music software | Free plugin / freeware coverage | pending | pending | Submit concise free-plugin pitch |
| Sonicstate | Contact form | music gear news, software instruments | Music-tech news / independent developer story | pending | pending | Submit short ecosystem story |
| DJ Mag | Pitch-guide route | electronic music producer story | Artist/developer profile angle | pending | pending | Use only if tying plugin work to TizWildin creator story |
| Rekkerd | Contact/news route | plugin news, freeware roundup | Plugin release news / freeware roundup | pending | pending | Send after download/release page is clean |
| Production Expert | Contact/editorial route | pro-audio workflow, mix tutorial | Workflow article / plugin mention | pending | pending | Pitch practical EQ/vocoder workflow, not broad claims |
| Ask.Audio | Contact/editorial route | music production tutorial, plugin tutorial | Tutorial / review / music tech article | pending | pending | Pair with quick-start workflow or mix example |
| JUCE Forum Showcase | Forum post | JUCE plugin, C++ audio development | Developer feedback + JUCE credibility | pending | pending | Post build notes, screenshots, repo link |
| Gearspace | Appropriate software/plugin forum | pro audio forum, plugin feedback | User feedback / credibility | pending | pending | Post only once after stable binaries are obvious |
| Reddit: r/audioengineering | Allowed weekly/showcase thread | audio engineering feedback | Engineering feedback | pending | pending | Check rules first |
| Reddit: r/musicproduction | Allowed weekly/showcase thread | music production tools, free plugins | Producer discovery | pending | pending | Check rules first |
| Reddit: r/edmproduction | Weekly resource/feedback thread | EDM production plugin, producer resources | EDM producer discovery | pending | pending | Check rules first |
| Hacker News / Show HN | Show HN post | open-source audio, developer tool | Open-source engineering visibility | pending | pending | Use only after repo/release/install path is polished |

### Outreach pacing

1. Submit/update **KVR** first because it creates a durable plugin database signal.
2. Send **BPB / Rekkerd** next for freeware visibility.
3. Send **MusicTech / Sonicstate** with the indie developer ecosystem angle.
4. Use **forums/Reddit** only after the public download path, screenshots, and known limitations are easy to find.
5. Follow up once after 7–10 business days, then stop.


## Submission order (recommended pacing)

To avoid the cross-platform-spam signal that gets accounts flagged:

1. **Week 1** — Bandcamp (own-channel, no gatekeeper): upload all 11 packs as free/pay-what-you-want releases.
2. **Week 2** — Looperman + Sample Focus: 1–2 packs per day.
3. **Week 3** — freesound.org: split packs into individual samples, tag + upload.
4. **Week 4** — Reddit genre subs: 1 pack per week per subreddit in the appropriate weekly thread.
5. **Month 2** — Editorial pitches (BPB, PML, Hive Sound): consolidated 3–4 pack pitch.
6. **GitHub awesome lists**: Free-Dark-Piano (MIDI content) → `awesome-midi-sources` PR.

Update this file after each submission. Keep the status truthful.
