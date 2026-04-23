# awesome-audio-lists [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of curated audio lists — where to submit your audio plugins, sample packs, synthesis tools, and DSP projects. Tracks each list's scope, submission format, contribution rules, and the real-world acceptance status of my own submissions.

Maintained by [GareBear99](https://github.com/GareBear99) · Used to track where [FreeEQ8](https://github.com/GareBear99/FreeEQ8), the [TizWildin plugin ecosystem](https://github.com/GareBear99/TizWildinEntertainmentHUB), and the TizWildin sample packs are listed.

## Contents
- [How to use this list](#how-to-use-this-list)
- [Audio plugin lists (GitHub, general)](#audio-plugin-lists-github-general)
- [JUCE / framework-specific lists](#juce--framework-specific-lists)
- [Music production lists](#music-production-lists)
- [Web Audio lists](#web-audio-lists)
- [Audio DSP / engineering lists](#audio-dsp--engineering-lists)
- [Sample-pack directories](#sample-pack-directories)
- [Non-GitHub plugin directories](#non-github-plugin-directories)
- [Submission playbook](#submission-playbook)
- [Legend](#legend)
- [Contributing](#contributing)

## How to use this list
1. Find a list that matches your plugin's scope and format (plugin / framework / DSP / sample pack).
2. Read the **Rules** column — many lists forbid paid or self-promoted products.
3. Follow the **Submission format** column exactly (PR / Issue / web form / email).
4. Track your submission status locally; this list records the maintainer's decision on a public product (FreeEQ8 / TizWildin) as a real-world signal.

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

## Web Audio lists

### [notthetup/awesome-webaudio](https://github.com/notthetup/awesome-webaudio) ★ 1.3k
Curated Web Audio packages and resources.
- **Scope**: Web Audio API, browser-based audio tools.
- **Submission format**: Issue → maintainer adds.
- **Rules**: browser/JS-focused; desktop plugins accepted only if they have a web-audio angle.
- **FreeEQ8 status**: ⏳ [Issue #83](https://github.com/notthetup/awesome-webaudio/issues/83) pending since 2026-03-27 — tenuous fit (FreeEQ8 is not a Web Audio plugin).

---

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
The largest plugin database. Submission at [`kvraudio.com/addplugin.php`](https://www.kvraudio.com/addplugin.php). Requires account. Commercial + free plugins accepted. Editorial review.

### [Plugins4Free](https://www.plugins4free.com/)
Free-plugins-only directory. Submission via [contact form](https://www.plugins4free.com/contact/).

### [Bedroom Producers Blog](https://bedroomproducersblog.com/)
Editorial; pitch by email. Covers free plugins heavily. Higher bar for coverage (editor's pick, not directory).

### [LinuxAudio.org wiki](https://wiki.linuxaudio.org/)
GPL / open-source Linux-compatible audio software. Self-edit wiki (requires account).

### [audio-plugin-dev-skills (iPlug3 marketplace)](https://github.com/iPlug3/audio-plugin-dev-skills)
Claude Code skill marketplace — publish a skill that describes how to use your plugin or framework.

### Community / forums
- **[JUCE Forum](https://forum.juce.com/) — "Showcase" category** — announcement thread for JUCE plugins.
- **[KVR DIY](https://www.kvraudio.com/forum/viewforum.php?f=33) — "Instruments and Effects" threads** — announcement posts accepted.
- **[r/audioengineering](https://www.reddit.com/r/audioengineering/)** + **[r/WeAreTheMusicMakers](https://www.reddit.com/r/WeAreTheMusicMakers/)** — weekly "free plugin" and "what you built" threads.

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
