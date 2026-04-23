#!/usr/bin/env python3
"""
Maintains the TizWildin pack READMEs on GitHub:

  1. Replaces the pricing block with the current pricing framing:
     "$X on paid platforms, free on GitHub + TizWildin website".

  2. Dedupes the trailing `## TizWildin FREE sample packs` table (and its
     companion `### Related audio projects` block) when it appears more
     than once — this crept in from earlier batch README updates and
     showed up twice at the bottom of most packs.

Uses the GitHub contents API so we don't have to clone the large sample
repos. Idempotent: re-running it produces a no-op after the first patch.
"""

import base64
import json
import os
import re
import subprocess

OWNER = "GareBear99"
HUB_SITE = "https://garebear99.github.io/TizWildinEntertainmentHUB/"
HUB_REPO = "https://github.com/GareBear99/TizWildinEntertainmentHUB"
PLUGIN_LIST = "https://github.com/GareBear99/awesome-audio-plugins-dev"

PACKS = {
    "TizWildin-Obsidian":              ("TizWildin Obsidian", 3),
    "TizWildin-Chroma":                ("TizWildin Chroma",   2),
    "TizWildin-Skyline":               ("TizWildin Skyline",  2),
    "TizWildin-Aurora":                ("TizWildin Aurora",   1),
    "TizWildin-Chime":                 ("TizWildin Chime",    1),
    "Free-Violin-Synth-Sample-Kit":    ("Free Violin Synth Sample Kit", 1),
    "Free-Dark-Piano-Sound-Kit":       ("Free Dark Piano Sound Kit",    1),
    "Free-808-Producer-Kit":           ("Free 808 Producer Kit",        1),
    "Free-Riser-Producer-Kit":         ("Free Riser Producer Kit",      1),
    "Phonk_Producer_Toolkit":          ("Phonk Producer Toolkit",       1),
    "Free-Future-Bass-Producer-Kit":   ("Free Future Bass Producer Kit", 1),
}

START = "<!-- tizwildin-pricing:start -->"
END = "<!-- tizwildin-pricing:end -->"


def pricing_block(name, price, repo):
    d = f"${price}"
    return f"""{START}
## \U0001f48e {name} — **{d}** on paid platforms · **free** on GitHub + TizWildin website

This pack sells for **{d}** on Bandcamp, Looperman, Sample Focus, Splice, and other commercial sample platforms — and is **free forever** from the official channels:

- [\u2b07\ufe0f Download the current ZIP](https://github.com/{OWNER}/{repo}/archive/refs/heads/main.zip) \u2014 full pack, always up to date\n- [\U0001f516 Releases page](https://github.com/{OWNER}/{repo}/releases) \u2014 tagged versions
- [\U0001f310 TizWildin website]({HUB_SITE})
- [\U0001f3db\ufe0f TizWildin Hub repo]({HUB_REPO}) — full catalog of free plugins + sample packs

Want to support the work directly? Any of these are appreciated:

- [GitHub Sponsors](https://github.com/sponsors/GareBear99)
- [Buy Me a Coffee](https://buymeacoffee.com/garebear99)
- [Ko-fi](https://ko-fi.com/luciferai)

More free plugins from me: [FreeEQ8 (8-band EQ)](https://github.com/GareBear99/FreeEQ8) · [Awesome Audio Plugins Dev list]({PLUGIN_LIST}).
{END}
"""


def sh(cmd):
    return subprocess.check_output(cmd, shell=True, text=True)


def get_readme(repo):
    raw = sh(f"gh api /repos/{OWNER}/{repo}/readme")
    data = json.loads(raw)
    content = base64.b64decode(data["content"]).decode("utf-8", errors="replace")
    return data["path"], data["sha"], content


def put_readme(repo, path, sha, new_content, message):
    payload = {
        "message": message,
        "content": base64.b64encode(new_content.encode("utf-8")).decode(),
        "sha": sha,
    }
    tmp = f"/tmp/_readme_put_{repo.replace('/', '_')}.json"
    with open(tmp, "w") as f:
        json.dump(payload, f)
    sh(f"gh api -X PUT /repos/{OWNER}/{repo}/contents/{path} --input {tmp}")
    os.remove(tmp)


def replace_pricing_block(content, new_block):
    if START in content and END in content:
        pre = content.split(START, 1)[0]
        post = content.split(END, 1)[1]
        post = post.lstrip("\n")
        return f"{pre}{new_block}\n{post}"
    return f"{new_block}\n{content}"


_PACKS_HEADER = re.compile(r"(?m)^##\s+TizWildin\s+FREE\s+sample\s+packs\s*$")


def dedupe_trailing_packs_table(content):
    matches = list(_PACKS_HEADER.finditer(content))
    if len(matches) < 2:
        return content
    cut = matches[1].start()
    return content[:cut].rstrip() + "\n"


def main():
    sh("gh auth token > /dev/null")  # auth sanity
    for repo, (name, price) in PACKS.items():
        try:
            path, sha, content = get_readme(repo)
        except Exception as e:
            print(f"[SKIP] {repo}: {e}")
            continue

        dup_before = len(_PACKS_HEADER.findall(content))
        new = replace_pricing_block(content, pricing_block(name, price, repo))
        new = dedupe_trailing_packs_table(new)
        dup_after = len(_PACKS_HEADER.findall(new))

        if new == content:
            print(f"[=]    {repo}: no-op")
            continue

        changes = []
        if dup_before > 1 and dup_after == 1:
            changes.append(f"dedupe packs table ({dup_before}→1)")
        if START in content:
            changes.append("refresh pricing block")
        else:
            changes.append("add pricing block")

        msg = f"docs: {', '.join(changes)} (${price} tier)"
        try:
            put_readme(repo, path, sha, new, msg)
            print(f"[OK]   {repo}: {msg}")
        except Exception as e:
            print(f"[ERR]  {repo}: {e}")


if __name__ == "__main__":
    main()
