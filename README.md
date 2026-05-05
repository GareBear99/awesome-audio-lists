# Awesome Audio Lists [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

![GitHub stars](https://img.shields.io/github/stars/GareBear99/awesome-audio-lists?style=social) ![GitHub forks](https://img.shields.io/github/forks/GareBear99/awesome-audio-lists?style=social) ![Last commit](https://img.shields.io/github/last-commit/GareBear99/awesome-audio-lists) ![License](https://img.shields.io/github/license/GareBear99/awesome-audio-lists)

> A curated discovery and submission hub for audio plugin directories, free VST/AU plugin promotion, JUCE and DSP resources, music-production awesome lists, sample-pack directories, music-platform submissions, editorial review targets, press outlets, and independent-artist release surfaces.

Maintained by [GareBear99](https://github.com/GareBear99) · Canonical hub for the TizWildin / GareBearProductionz audio-network graph: [FreeEQ8](https://github.com/GareBear99/FreeEQ8), [FreeVox8](https://github.com/GareBear99/FreeVox8), [awesome-python-audio-science](https://github.com/GareBear99/awesome-python-audio-science), the [TizWildin plugin ecosystem](https://github.com/GareBear99/TizWildinEntertainmentHUB), TizWildin sample packs, independent music releases, and satellite awesome lists.

## Contents
- [Hub network](#hub-network)
- [How to use this list](#how-to-use-this-list)
- [Audio plugin lists (GitHub, general)](#audio-plugin-lists-github-general)
- [JUCE / framework-specific lists](#juce--framework-specific-lists)
- [Music production lists](#music-production-lists)
- [Music platforms / artist distribution / creator storefronts](#music-platforms--artist-distribution--creator-storefronts)
- [Web Audio lists](#web-audio-lists)
- [Audio DSP / engineering lists](#audio-dsp--engineering-lists)
- [Python scientific audio / MIR lists](#python-scientific-audio--mir-lists)
- [Sample-pack directories](#sample-pack-directories)
- [Non-GitHub plugin directories](#non-github-plugin-directories)
- [Editorial reviews & promotional outlets](#editorial-reviews--promotional-outlets)
- [Submission playbook](#submission-playbook)
- [Legend](#legend)
- [Contributing](#contributing)

## Hub network

This repo is the **root discovery hub** for the GareBear99 / TizWildin audio ecosystem. Keep repo names lowercase for URL consistency, and use readable capitalized titles inside READMEs.

### Canonical satellite lists

- [GareBear99/awesome-audio-plugins-dev](https://github.com/GareBear99/awesome-audio-plugins-dev) — Free audio plugins, open-source DSP tools, JUCE/plugin-development resources, and plugin ecosystem discovery.
- [GareBear99/awesome-music-platforms](https://github.com/GareBear99/awesome-music-platforms) — Music platforms for streaming, distribution, beat selling, sample packs, sync licensing, promotion, analytics, creator storefronts, visualization, and independent musician tools.
- [GareBear99/awesome-python-audio-science](https://github.com/GareBear99/awesome-python-audio-science) — Python scientific audio, DSP, MIR, machine-learning audio, datasets, notebooks, plugin analysis, and creator-audio automation resources.

### Canonical product/project anchors

- [FreeEQ8](https://github.com/GareBear99/FreeEQ8) — free JUCE equalizer and primary plugin-discovery proof point.
- [FreeVox8](https://github.com/GareBear99/FreeVox8) — spectral vocoder / ghost-resynthesis plugin line.
- [TizWildinEntertainmentHUB](https://github.com/GareBear99/TizWildinEntertainmentHUB) — plugin ecosystem launcher and public project hub.
- [TizWildinEntertainmentHUB public .io router](https://garebear99.github.io/TizWildinEntertainmentHUB/) — public route for plugins, packs, lists, deconstructed loops, visualizers, and release-surface routing.
- [Voxel Audio](https://github.com/GareBear99/Voxel_Audio) — RGB waveform visualizer and audio export tool.
- [TizWildin Release Vault](https://github.com/GareBear99/TizWildin-Release-Vault/) — official release catalog and proof surface.

Recommended link graph:

```text
awesome-audio-lists
├─ awesome-audio-plugins-dev
├─ awesome-music-platforms
├─ awesome-python-audio-science
├─ FreeEQ8 / FreeVox8 / plugin repos
├─ Voxel Audio / visualizer tools
└─ TizWildin music, deconstructed loops, sample packs, .io router, release vault, and SoundCloud/YouTube surfaces
```

## How to use this list
1. Find a list or platform directory that matches your project scope and format: plugin, framework, DSP, sample pack, music release, beat pack, visualizer, or creator platform.
2. Read the **Rules** column — many lists forbid paid or self-promoted products.
3. Follow the **Submission format** column exactly (PR / Issue / web form / email).
4. Track your submission status locally; this list records real-world acceptance signals for FreeEQ8, FreeVox8, TizWildin packs, and the wider TizWildin / GareBearProductionz ecosystem.
5. Use the Python audio science / MIR satellite list when the target is research, dataset, notebook, ML-audio, analysis, or scientific-DSP tooling rather than a finished plugin or artist platform.

---

## Audio plugin lists (GitHub, general)

### [GareBear99/awesome-audio-plugins-dev](https://github.com/GareBear99/awesome-audio-plugins-dev) ★ own list
Curated list of free audio plugins, open-source DSP tools, and plugin development frameworks. **Maintained here** — this is the canonical home for FreeEQ8 and the TizWildin ecosystem.
- **Scope**: free plugins, open-source plugins, frameworks, DSP resources.
- **Submission format**: PR against `README.md`.
- **Rules**: concise entry, alphabetical within category, no paid-only products.
- **FreeEQ8 status**: ✅ listed under *Equalizers*.

### [webprofusion/OpenAudio](https://github.com/webprofusion/OpenAudio) ★ 2.5k
Open audio plugin database (`data/plugins.json` + generated `README.md`).
- **Scope**: audio plugins across all formats.
- **Submission format**: Issue — use the issue template `[Plugin] <name>`. Maintainer adds to `data/plugins.json`.
- **Rules**: open-source preferred; plugin must be downloadable and cross-platform-friendly.
- **FreeEQ8 status**: ✅ listed (issues [#207](https://github.com/webprofusion/OpenAudio/issues/207), [#209](https://github.com/webprofusion/OpenAudio/issues/209), [#210](https://github.com/webprofusion/OpenAudio/issues/210) all closed on acceptance).

### [dreikanter/awesome-vst](https://github.com/dreikanter/awesome-vst) ★ 15
Curated VST plugins reference.
- **Scope**: time-tested VST plugins you actually use.
- **Submission format**: PR.
- **Rules** (`contributing.md`): concise non-marketing description, alphabetical within category, `(Free)` or 🆓 label for free plugins, no copying random products from oversaturated VST marketplaces.
- **FreeEQ8 status**: ⏳ [PR #18](https://github.com/dreikanter/awesome-vst/pull/18) pending.

### [matthewamend/awesome-audio-plugins](https://github.com/matthewamend/awesome-audio-plugins) ★ 1
Audio-plugin-related tools and resources.
- **Scope**: plugin APIs (CLAP / VST / AU / AAX / LV2), libraries, dev tools, online communities, more lists.
- **Submission format**: PR.
- **Rules**: awesome-lint.
- **FreeEQ8 status**: ❌ not a fit — list is for APIs/libraries, not end-user plugins. No Open-Source-Plugins section yet.

---

## JUCE / framework-specific lists

### [olilarkin/awesome-musicdsp](https://github.com/olilarkin/awesome-musicdsp) ★ 2.9k
Oli Larkin's curated list of music DSP and audio programming resources.
- **Scope**: frameworks, libraries, textbooks, open-source plugin projects (*exemplary* and *miscellaneous*), hardware, tools, talks.
- **Submission format**: PR.
- **Rules**: first-person informal style, personally-recommended only.
- **FreeEQ8 status**: ⏳ [PR #11](https://github.com/olilarkin/awesome-musicdsp/pull/11) pending — under *Exemplary open source audio plug-in projects* with an emphasis on the Milestone-A RT-safety pass.

### [sudara/awesome-juce](https://github.com/sudara/awesome-juce) ★ 1.2k
Sudara's JUCE modules / templates / plugins.
- **Scope**: JUCE modules, templates, plugins.
- **Submission format**: PR (issue templates also exist).
- **Rules**: awesome-lint; JUCE-related only.
- **FreeEQ8 status**: ⏳ [PR #61](https://github.com/sudara/awesome-juce/pull/61) pending since 2026-02-26.

### [BillyDM/awesome-audio-dsp](https://github.com/BillyDM/awesome-audio-dsp) ★ 1.3k
Audio DSP + plugin development resources.
- **Scope**: libraries, cookbooks, playgrounds, frameworks, APIs, books, open-source plugins.
- **Submission format**: PR on [Codeberg mirror](https://codeberg.org/BillyDM/awesome-audio-dsp) (GitHub is read-only).
- **Rules**: no generative-AI-adjacent resources, no self-promotion with financial incentive, alphabetical order.
- **FreeEQ8 status**: ❌ intentionally not submitted — ProEQ8 is $20, which violates the financial-incentive rule.

### [Tremus/awesome-audio-plugin-framework](https://github.com/Tremus/awesome-audio-plugin-framework) ★ 49
Small C/C++ libraries for building your own plug-in framework.
- **Scope**: frameworks only (JUCE / iPlug / DPF / CLAP / CPLUG). No end-user plugins.
- **Submission format**: PR.
- **FreeEQ8 status**: ❌ not a fit — FreeEQ8 is a plugin, not a framework.

### [iPlug3 marketplace](https://github.com/iPlug3/audio-plugin-dev-skills) — Claude Code skill marketplace for audio plugin dev.
- Not a traditional awesome list; skills marketplace. Worth monitoring.

---

## Music production lists

### [noteflakes/awesome-music](https://github.com/noteflakes/awesome-music) ★ 2.3k
Awesome Music Projects.
- **Scope**: broad — music software, libraries, tools, resources.
- **Submission format**: Issue with a specific format (see [contributing](https://github.com/noteflakes/awesome-music#contributing)) — body must be the exact line to insert.
- **Rules**: awesome-lint, alphabetical.
- **FreeEQ8 status**: ⏳ [Issue #101](https://github.com/noteflakes/awesome-music/issues/101) pending since 2026-04-15.

### [ad-si/awesome-music-production](https://github.com/ad-si/awesome-music-production) ★ 1.4k
Software, services, and resources to create and distribute music.
- **Scope**: DAWs, plugins, services, resources.
- **Submission format**: PR against `readme.md` (lowercase), `Plugins` section.
- **Rules**: ISC license, alphabetical, link-reference style (`[Name]: url` at bottom).
- **FreeEQ8 status**: ✅ listed (merged via [PR #197](https://github.com/ad-si/awesome-music-production/pull/197) on 2026-03-16).

### [ad-si/awesome-soundfonts](https://github.com/ad-si/awesome-soundfonts) ★ 163
Soundfont software, libraries, and resources.
- **Scope**: soundfonts (SF2/SFZ), related software.
- **Submission format**: PR.
- **Applicable to**: TizWildin sample-pack repos that ship SF2/SFZ instruments (e.g., Instrudio).

### [albertmeronyo/awesome-midi-sources](https://github.com/albertmeronyo/awesome-midi-sources) ★ 324
Sites with MIDI files on the Web.
- **Scope**: MIDI file archives, generators, and related tools.
- **Submission format**: PR.
- **Applicable to**: TizWildin packs that ship MIDI content (Free Dark Piano Sound Kit, Phonk Producer Toolkit).

---

## Music platforms / artist distribution / creator storefronts

### [GareBear99/awesome-music-platforms](https://github.com/GareBear99/awesome-music-platforms) ★ own list
Curated list of music platforms for streaming, distribution, beat selling, sample packs, sync licensing, artist promotion, analytics, creator storefronts, music visualization, and independent musician tools.
- **Scope**: artist platforms, streaming services, distributors, beat stores, sample-pack marketplaces, sync/licensing platforms, music-promotion tools, analytics, creator storefronts, communities, and open-source music resources.
- **Submission format**: PR against `README.md` or issue using the platform template.
- **Rules**: useful public platforms only; short neutral descriptions; no spam, scams, dead links, adult-only sites, or fake growth services.
- **TizWildin status**: ✅ canonical satellite list for music-platform discovery and release-surface mapping.

Use this satellite list when the target is not only an audio-plugin list, but a broader music release, music marketing, sample-pack sales, beat-store, creator-storefront, sync/licensing, or analytics platform.

---

## Web Audio lists

### [notthetup/awesome-webaudio](https://github.com/notthetup/awesome-webaudio) ★ 1.3k
Curated Web Audio packages and resources.
- **Scope**: Web Audio API, browser-based audio tools.
- **Submission format**: Issue → maintainer adds.
- **Rules**: browser/JS-focused; desktop plugins accepted only if they have a web-audio angle.
- **FreeEQ8 status**: ⏳ [Issue #83](https://github.com/notthetup/awesome-webaudio/issues/83) pending since 2026-03-27 — tenuous fit (FreeEQ8 is not a Web Audio plugin).

---


## Python scientific audio / MIR lists

### [GareBear99/awesome-python-audio-science](https://github.com/GareBear99/awesome-python-audio-science) ★ own list
Curated public list of Python scientific audio, audio DSP, music information retrieval, machine-learning audio, datasets, notebooks, plugin analysis, and creator-audio automation. This is the canonical Python/scientific-audio satellite for the GareBear99 / TizWildin ecosystem.
- **Scope**: Python audio analysis, DSP/transforms, MIR, speech/voice/alignment, source separation, loudness/perceptual audio, realtime audio/MIDI, datasets, notebooks, visualization, plugin testing, and creator-routing automation.
- **Submission format**: PR against `README.md` or issue using the platform/resource template.
- **Rules**: useful public resources only; neutral descriptions; no fake growth services, spam, malware, or unsupported claims.
- **TizWildin status**: ✅ canonical satellite for Python audio science, deconstructed-loop analysis, IO/router automation, Voxel Audio support tooling, and future FreeEQ8/FreeVox8 testing notebooks.

### [faroit/awesome-python-scientific-audio](https://github.com/faroit/awesome-python-scientific-audio) ★ 1.7k+
Established curated list of Python packages and resources for scientific audio research, audio analysis, MIR, source separation, deep learning, realtime apps, datasets, and audio plugin wrappers.
- **Scope**: scientific Python audio packages and research tooling.
- **Submission format**: PR.
- **Rules**: curated scientific-audio relevance; keep descriptions concise and useful.
- **TizWildin status**: Reference/inspiration lane only. Use `awesome-python-audio-science` as the ecosystem-controlled satellite and submit only broadly useful Python tooling upstream where appropriate.

## Audio DSP / engineering lists

### [DolbyIO/awesome-audio](https://github.com/DolbyIO/awesome-audio) ★ 323
Audio technology resources for developers.
- **Scope**: developer APIs (Dolby.io, AWS Transcribe, Google STT), DAWs, SDKs.
- **Submission format**: PR.
- **FreeEQ8 status**: ❌ not a fit — no dedicated section for open-source plugins; list is infrastructure/API-focused.

### [sgtm-club/awesome-audio-engineering](https://github.com/sgtm-club/awesome-audio-engineering) ★ 12
Audio/music/sound reverse-engineering / analysis / creation.
- **Scope**: reverse-engineering tools, analysis libraries, creation tools — narrow technical focus.
- **Submission format**: PR.

### [KennethanCeyer/awesome-audio-speech](https://github.com/KennethanCeyer/awesome-audio-speech) ★ 15
Audio, Speech, and DSP.
- **Scope**: heavy on speech processing and ML.
- **Submission format**: PR.

### [hwclass/awesome-sound](https://github.com/hwclass/awesome-sound) ★ 122
Delightful sound packages and resources.
- **Scope**: broad — sound libraries, packages, generative sound.
- **Submission format**: PR.

### [yamathcy/awesome-music-informatics](https://github.com/yamathcy/awesome-music-informatics) ★ 191
Music-informatics articles, tutorials, libraries.
- **Scope**: music-IR / MIR, academic.

### [Mo-way/awesome-aoip](https://github.com/Mo-way/awesome-aoip) ★ 123
Audio over IP + AES67.
- **Scope**: AoIP only — niche, likely not a fit for desktop plugins.

---

## Sample-pack directories

> GitHub has minimal curation for sample packs. The real distribution surface is **non-GitHub platforms** below. TizWildin packs and similar free sample-pack releases should target those first.

### GitHub curated lists that accept sample packs
- [**ad-si/awesome-soundfonts**](https://github.com/ad-si/awesome-soundfonts) ★ 163 — SF2/SFZ soundfonts only. PR submission.
- [**albertmeronyo/awesome-midi-sources**](https://github.com/albertmeronyo/awesome-midi-sources) ★ 324 — MIDI files. PR submission.

### Non-GitHub sample-pack directories (ordered by producer-facing reach)

#### [freesound.org](https://freesound.org) — very high traffic
- **Submission**: free account → [upload page](https://freesound.org/home/upload/). Each sample uploaded individually. Supports license tagging (CC0 / CC-BY / CC-BY-NC).
- **Rules**: descriptive filename, accurate tags, real preview audio. Moderator review.
- **Fit**: individual one-shots, loops, field recordings. Not ideal for packs as bundles (upload per-sample).
- **Used by**: Logic Pro, Ableton Live (in-app browsing).

#### [Looperman](https://www.looperman.com) — producer-first community
- **Submission**: free account → [upload page](https://www.looperman.com/members/account/upload). Pack uploads accepted.
- **Rules**: royalty-free license, original content only, BPM + key metadata required.
- **Fit**: TizWildin loop packs (Aurora, Skyline, Chroma, Chime).

#### [Sample Focus](https://samplefocus.com) — curated free samples
- **Submission**: account → upload.
- **Rules**: pre-screened for quality. Higher bar than Freesound/Looperman.

#### [Splice](https://splice.com) — commercial platform
- **Submission**: [creator application](https://splice.com/sounds/creator-program). Revenue share.
- **Rules**: high production quality + original content. Curated roster.
- **Fit**: only the most polished TizWildin packs; not a free distribution channel.

#### [Bandcamp](https://bandcamp.com) — direct listener purchase / free download
- **Submission**: artist account. Upload packs as ZIP + audio previews. Can price at $0 or "pay what you want".
- **Rules**: no submission gatekeeping.
- **Fit**: release each TizWildin pack as a Bandcamp release alongside GitHub.

#### [r/WeAreTheMusicMakers](https://www.reddit.com/r/WeAreTheMusicMakers/) — "Feedback Friday" + "Free Sample Pack" threads
- **Submission**: weekly self-post thread; include pack name, BPM, genre, license, download link. Comment-only for some threads.
- **Rules**: no drive-by self-promotion, comment on others' posts too.

#### [r/WeAreTheMusicMakers — "I Made A Thing" Monday](https://www.reddit.com/r/WeAreTheMusicMakers/)
- Weekly self-promotion thread; post pack link + description.

#### [r/edmproduction](https://www.reddit.com/r/edmproduction/) — weekly feedback threads
- **Fit**: EDM-leaning TizWildin content (Skyline, Chroma, Future Bass Kit).

#### [r/trapproduction](https://www.reddit.com/r/trapproduction/) / [r/phonk](https://www.reddit.com/r/phonk/)
- Genre-specific communities. Phonk Producer Toolkit belongs here.

#### [Hive Sound](https://www.hivesound.com) — editorial / curated free pack roundup
- **Submission**: contact form / email editor.
- **Rules**: editorial. Pitch required.

#### [Audio Assault Free Packs](https://www.audioassault.com/pages/free-downloads) — some accept submissions via contact
- **Submission**: email editor.

#### [Bedroom Producers Blog — "Best Free Sample Packs of …"](https://bedroomproducersblog.com/category/free-samples/)
- **Submission**: email editor; editorial. Highest bar, highest reach in producer press.

#### [Production Music Live — free sample pack roundup](https://productionmusiclive.com/)
- **Submission**: contact form / email.

#### TizWildin-owned distribution
- **GitHub Releases** (current): each pack repo ships ZIP assets on `releases/latest`.
- **GitHub Pages** (optional): single landing page aggregating all packs.
- **YouTube pack walkthroughs**: upload a preview video with download link in description; high SEO.

---

## Non-GitHub plugin directories

> These are where actual producers browse for plugins. Higher reach than most GitHub awesome lists.

### [KVR Audio](https://www.kvraudio.com/)
The largest plugin database. Submission at [`kvraudio.com/addplugin.php`](https://www.kvraudio.com/addplugin.php) or through the KVR submissions workflow. Requires account for product listings. Commercial + free plugins accepted. Editorial review.

### [Plugins4Free](https://www.plugins4free.com/)
Free-plugins-only directory. Submission via [contact form](https://www.plugins4free.com/contact/).

### [Bedroom Producers Blog](https://bedroomproducersblog.com/)
Editorial; use the contact form for news/review pitches. Covers free plugins heavily. Higher bar for coverage (editor's pick, not directory).

### [LinuxAudio.org wiki](https://wiki.linuxaudio.org/)
GPL / open-source Linux-compatible audio software. Self-edit wiki (requires account).

### [audio-plugin-dev-skills (iPlug3 marketplace)](https://github.com/iPlug3/audio-plugin-dev-skills)
Claude Code skill marketplace — publish a skill that describes how to use your plugin or framework.

### Community / forums
- **[JUCE Forum](https://forum.juce.com/) — "Showcase" category** — announcement thread for JUCE plugins.
- **[KVR DIY](https://www.kvraudio.com/forum/viewforum.php?f=33) — "Instruments and Effects" threads** — announcement posts accepted.
- **[r/audioengineering](https://www.reddit.com/r/audioengineering/)** + **[r/WeAreTheMusicMakers](https://www.reddit.com/r/WeAreTheMusicMakers/)** — weekly "free plugin" and "what you built" threads.

---

## Editorial reviews & promotional outlets

> Use this section for **audio plugin review requests, free VST/AU plugin promotion, music-tech news tips, press releases, creator-story pitches, and professional studio review outreach**. These are not normal directory submissions: keep each pitch short, truthful, and tailored to the outlet. Do not claim certification, awards, chart placement, or studio adoption unless the proof is public.

This section helps independent audio developers, JUCE plugin builders, DSP researchers, sample-pack creators, and producer-developers find legitimate places to submit open-source audio plugins, free music-production tools, soundware, and creator-tech stories.

### Priority audio-plugin review, press, and promotion targets

| Outlet | Contact / submission path | SEO/search intent | Best angle | Fit | Notes |
|---|---|---|---|---|---|
| [Sound On Sound](https://www.soundonsound.com/information/write-sound-on-sound) | Use the listed editorial/contact routes on their Write for SOS page | pro audio review, studio review, audio engineering magazine | Professional studio review / technical assessment | High | Best for serious credibility. Pitch FreeEQ8 as an honest open-source EQ evaluation, not hype. |
| [KVR Audio submissions](https://www.kvraudio.com/submissions) | `contactus@kvraudio.com` or developer/product submission flow | audio plugin database, VST plugin listing, plugin news | Plugin database listing + release news | Very high | Durable discovery signal for free VST/AU plugins. Use account-based product submission when possible. |
| [MusicTech](https://musictech.com/contact/) | `editors@musictech.com` | music technology news, producer tools, plugin release | News tip / independent developer story | High | Use the solo producer-developer angle: open-source plugins, JUCE development, and creator ecosystem. |
| [MusicTech / NME Networks press office](https://nmenetworks.com/brands/musictech) | `press@nmenetworks.com` | music-tech press release, product launch | Formal press release | Medium | Use only for polished release announcements with clean download links and screenshots. |
| [Bedroom Producers Blog](https://bedroomproducersblog.com/contact/) | Contact form | free VST plugin, freeware plugin, free music software | Free plugin / freeware news | Very high | Strong fit for FreeEQ8, FreeVox8, sample packs, and producer utilities. Keep the pitch concise. |
| [Sonicstate](https://sonicstate.com/about/contact.cfm) | Contact form | music gear news, music technology, software instruments | Music-tech news / creator story | Medium | Better for the indie developer ecosystem story than a simple EQ listing. |
| [DJ Mag pitch guide](https://djmag.com/information/how-pitch-dj-mag) | Follow the pitch-guide instructions | electronic music producer story, artist technology | Artist + technology story | Low–medium | Use only if connecting FreeEQ8/FreeVox8 to TizWildin releases and independent production workflow. |
| [Production Expert](https://www.production-expert.com/) | Contact / editorial route | pro tools workflow, audio production tips, plugin review | Pro-audio workflow article / plugin mention | Medium | Pitch practical mix scenarios and workflow value. Avoid broad claims. |
| [Ask.Audio / macProVideo](https://ask.audio/) | Contact / editorial route | audio tutorial, music production tutorial, plugin tutorial | Tutorial / review / music tech article | Medium | Best with a quick-start tutorial or mix example. |
| [Rekkerd](https://rekkerd.org/) | Contact / news submission route | plugin news, free plugin news, soundware news | Plugin news / freeware roundup | High | Good fit for free plugin updates, sample packs, soundware, and release announcements. |
| [Gearspace](https://gearspace.com/) | Forum post in appropriate software/plugin area | pro audio forum, plugin feedback, studio community | Community visibility / user feedback | Medium | Do not spam. Post once with download, license, screenshots, supported formats, and limitations. |
| [JUCE Forum Showcase](https://forum.juce.com/) | Showcase/category post | JUCE plugin, open-source audio plugin, C++ audio development | Developer-facing proof + feedback | High | Strong credibility signal for JUCE-built tools. Include architecture notes and repo link. |
| [Reddit: r/audioengineering](https://www.reddit.com/r/audioengineering/) | Appropriate weekly/showcase thread if allowed | audio engineering feedback, free plugin feedback | Engineering feedback | Medium | Read rules first. Avoid drive-by self-promo. |
| [Reddit: r/musicproduction](https://www.reddit.com/r/musicproduction/) | Appropriate weekly/showcase thread if allowed | music production tools, free plugins | Producer adoption / free tool discovery | Medium | Lead with usefulness, open-source status, and screenshots. |
| [Reddit: r/edmproduction](https://www.reddit.com/r/edmproduction/) | Weekly feedback/resource thread if allowed | EDM production plugin, free EQ plugin, producer resources | EDM producer utility | Medium | Best for FreeEQ8, FreeVox8, sample packs, visualizer tools, and production workflows. |
| [Hacker News — Show HN](https://news.ycombinator.com/show) | Show HN post | Show HN open-source audio, developer tool, local software | Open-source engineering story | Medium | Use only when README, releases, screenshots, install path, and limitations are extremely clean. |

### Outreach keyword map

Use these phrases naturally in descriptions, titles, and submission notes. Do **not** keyword-stuff.

- free open-source audio plugin
- free 8-band parametric EQ plugin
- open-source JUCE plugin
- free VST3 EQ / AU EQ plugin
- audio plugin review submission
- music production plugin news
- independent audio developer
- producer-built music software
- low-overhead EQ plugin
- DSP audio plugin project
- FreeEQ8 by Gary Doman / GareBear99 / neo-VECTR

### Promotional pitch rules

- **One outlet, one tailored pitch.** Do not send the same long email everywhere.
- **Lead with the outlet’s audience:** studio credibility for Sound On Sound, freeware utility for Bedroom Producers Blog, developer story for MusicTech, product listing for KVR.
- **Use a clear subject line.** Include the product name, format/category, and why it is relevant.
- **Attach nothing on first contact unless requested.** Link the GitHub repo, public hub, screenshots, and release/download page.
- **State honest status.** Say open-source, in development, release candidate, stable build, tested build, or public source only when true.
- **Include proof links.** Repo, release page, screenshots, documentation hub, SoundCloud/artist context, and GitHub profile are enough for first contact.
- **Track every send in `SUBMISSION_TRACKER.md`.** Record date, target, contact route, status, follow-up date, and outcome.

### Reusable subject lines

```text
FreeEQ8 — Free open-source 8-band EQ plugin for review/news consideration
FreeEQ8 — Free 8-band parametric EQ plugin built with JUCE
FreeEQ8 — Open-source JUCE EQ plugin from solo producer/developer
FreeVox8 — Open-source spectral vocoder / ghost-resynthesis plugin for review consideration
Independent producer/developer building open-source audio plugins
```

### FreeEQ8 short pitch block

```text
FreeEQ8 is a free, open-source 8-band parametric EQ plugin built by Gary Doman / GareBear99 under neo-VECTR. It is designed for precise corrective and creative EQ work, transparent public development, low-overhead performance goals, and a producer-built workflow connected to the TizWildin audio ecosystem.

GitHub: https://github.com/GareBear99/FreeEQ8
Hub: https://garebear99.github.io/TizWildinEntertainmentHUB/
GitHub profile: https://github.com/GareBear99
SoundCloud: https://soundcloud.com/tizwildin
```

### FreeEQ8 one-line directory listing

```text
[FreeEQ8](https://github.com/GareBear99/FreeEQ8) — Free open-source 8-band parametric EQ plugin built with JUCE for corrective, surgical, and creative music-production workflows.
```

---

## Submission playbook

A compact checklist used for every list on this page:

1. **Read `CONTRIBUTING.md`** (or `contributing.md` / `.github/CONTRIBUTING.md`) before drafting. 90% of rejections are format violations.
2. **Check license rules** — some lists forbid paid products, generative-AI-adjacent tools, or proprietary software.
3. **Match the exact entry format** — punctuation, link style, description length, category placement.
4. **Alphabetize** within the target section (or follow whatever the list's rule is).
5. **Submit via the listed channel** — PR > Issue > email. Prefer PRs when the list uses them; maintainers merge faster.
6. **No bulk outreach** — submit to one list per day max per plugin; looks less automated and reduces cross-list rejection risk.
7. **Track status** here under the list's "Status" field. If merged, update to ✅. If closed without merge, note the reason.

Example PR body template is in [`TEMPLATES/pr_body.md`](TEMPLATES/pr_body.md).

---

## Legend

| Symbol | Meaning |
|:---:|---|
| ✅ | Accepted / listed |
| ⏳ | Submitted, awaiting review |
| ❌ | Intentionally not submitted (rule mismatch, scope mismatch, license conflict) |
| 🛑 | Submitted and rejected |
| ★ | Stargazer count at last audit |

---

## Contributing

Contributions welcome — if you know of a curated audio list that accepts plugins, sample packs, or DSP projects and isn't on this page, open a PR or issue. See [`CONTRIBUTING.md`](CONTRIBUTING.md).

## License

[CC0 1.0](LICENSE) — content is in the public domain. Use it, fork it, mirror it.

> 🎛️ Part of the [TizWildin Plugin Ecosystem](https://garebear99.github.io/TizWildinEntertainmentHUB/) — 19 free audio plugins with a live update dashboard.
>
> [FreeEQ8](https://github.com/GareBear99/FreeEQ8) · [XyloCore](https://github.com/GareBear99/XyloCore) · [Instrudio](https://github.com/GareBear99/Instrudio) · [Therum](https://github.com/GareBear99/Therum_JUCE-Plugin) · [BassMaid](https://github.com/GareBear99/BassMaid) · [SpaceMaid](https://github.com/GareBear99/SpaceMaid) · [GlueMaid](https://github.com/GareBear99/GlueMaid) · [MixMaid](https://github.com/GareBear99/MixMaid) · [MultiMaid](https://github.com/GareBear99/MultiMaid) · [MeterMaid](https://github.com/GareBear99/MeterMaid) · [ChainMaid](https://github.com/GareBear99/ChainMaid) · [PaintMask](https://github.com/GareBear99/PaintMask_Free-JUCE-Plugin) · [WURP](https://github.com/GareBear99/WURP_Toxic-Motion-Engine_JUCE) · [AETHER](https://github.com/GareBear99/AETHER_Choir-Atmosphere-Designer) · [WhisperGate](https://github.com/GareBear99/WhisperGate_Free-JUCE-Plugin) · [RiftWave](https://github.com/GareBear99/RiftWaveSuite_RiftSynth_WaveForm_Lite) · [FreeSampler](https://github.com/GareBear99/FreeSampler_v0.3) · [VF-PlexLab](https://github.com/GareBear99/VF-PlexLab) · [PAP-Forge-Audio](https://github.com/GareBear99/PAP-Forge-Audio)
>
> 🎧 **SoundCloud:** [TizWildin on SoundCloud](https://soundcloud.com/tizwildin) — original music, remixes, VIP mixes, experimental drops, and underground releases.
>
> 🎵 [Awesome Audio Plugins Dev](https://github.com/GareBear99/awesome-audio-plugins-dev) — free audio plugins, DSP, and plugin-development discovery  
> 🌐 [Awesome Music Platforms](https://github.com/GareBear99/awesome-music-platforms) — streaming, distribution, storefronts, sync, promotion, analytics, and music-platform discovery
> 🧪 [Awesome Python Audio Science](https://github.com/GareBear99/awesome-python-audio-science) — Python scientific audio, MIR, DSP, datasets, notebooks, and creator-audio automation
>
> ▶️ **[YouTube](https://www.youtube.com/@gfgfvmhj)** — music, visuals, demos, and releases  
> 🌊 **[Voxel Audio](https://github.com/GareBear99/Voxel_Audio)** — free RGB waveform visualizer and audio export tool  
> 📘 **[Facebook Page](https://www.facebook.com/profile.php?id=61564485196765)** — TizWildin / GareBearProductionz updates and Media  
> 🗂️ **[Release Vault](https://garebear99.github.io/TizWildin-Release-Vault/)** — official monetized releases, distributed tracks, and catalog proof
> 🔀 **[TizWildin .io Router](https://garebear99.github.io/TizWildinEntertainmentHUB/)** — public router for plugins, lists, deconstructed loops, sample packs, visualizers, and release surfaces

> 🗂️ **Release Vault Repo:** [https://github.com/GareBear99/TizWildin-Release-Vault](https://github.com/GareBear99/TizWildin-Release-Vault)
