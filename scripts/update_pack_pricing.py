#!/usr/bin/env python3
"""
Patches the top of each TizWildin pack's README with a consistent pricing
and support block that:
  - Reminds visitors the pack is free via GitHub releases.
  - States the "support" price tier for future Bandcamp / Ko-fi / BMC sale.
  - Links to the TizWildin Hub as the canonical pack index.

Uses the GitHub contents API (no local cloning of huge sample-pack repos).
Requires `gh auth` to be set up (reads the token from `gh auth token`).

Idempotent: detects an existing `<!-- tizwildin-pricing:start -->` block
and replaces it in-place; otherwise prepends above the existing content.
"""

import base64
import json
import os
import subprocess
import sys

OWNER = "GareBear99"
HUB = "https://github.com/GareBear99/TizWildinEntertainmentHUB"
PLUGIN_LIST = "https://github.com/GareBear99/awesome-audio-plugins-dev"

# repo -> (display name, support price in USD)
PACKS = {
    "TizWildin-Obsidian":              ("TizWildin Obsidian",   3),
    "TizWildin-Chroma":                ("TizWildin Chroma",     2),
    "TizWildin-Skyline":               ("TizWildin Skyline",    2),
    "TizWildin-Aurora":                ("TizWildin Aurora",     1),
    "TizWildin-Chime":                 ("TizWildin Chime",      1),
    "Free-Violin-Synth-Sample-Kit":    ("Free Violin Synth Sample Kit", 1),
    "Free-Dark-Piano-Sound-Kit":       ("Free Dark Piano Sound Kit",    1),
    "Free-808-Producer-Kit":           ("Free 808 Producer Kit",        1),
    "Free-Riser-Producer-Kit":         ("Free Riser Producer Kit",      1),
    "Phonk_Producer_Toolkit":          ("Phonk Producer Toolkit",       1),
    "Free-Future-Bass-Producer-Kit":   ("Free Future Bass Producer Kit", 1),
}

START = "<!-- tizwildin-pricing:start -->"
END = "<!-- tizwildin-pricing:end -->"


def block(display_name: str, price: int, repo: str) -> str:
    dollars = f"${price}"
    return f"""{START}
## \U0001f48e {display_name} — free, or **{dollars}** to support the work

This pack is **free forever** on GitHub:

- [\u2b07\ufe0f Download the latest release]({f"https://github.com/{OWNER}/{repo}/releases/latest"}) (ZIP)
- [\U0001f3db\ufe0f TizWildin Plugin & Pack Hub]({HUB}) \u2014 full catalog of free plugins + sample packs

If this pack earns a place in your sessions and you want to chip in **{dollars}** to support the next release, pick any of these:

- [GitHub Sponsors](https://github.com/sponsors/GareBear99)
- [Buy Me a Coffee](https://buymeacoffee.com/garebear99)
- [Ko-fi](https://ko-fi.com/luciferai)

(Paid Bandcamp / Ko-fi Shop editions coming soon at the **{dollars}** tier for this pack. GitHub release stays free either way.)

More free plugins from me: [FreeEQ8 (8-band EQ)](https://github.com/GareBear99/FreeEQ8) \u00b7 [Awesome Audio Plugins Dev list]({PLUGIN_LIST}).
{END}
"""


def sh(cmd):
    return subprocess.check_output(cmd, shell=True, text=True).strip()


def get_token():
    return sh("gh auth token")


def get_readme(repo: str):
    raw = sh(f"gh api /repos/{OWNER}/{repo}/readme")
    data = json.loads(raw)
    content = base64.b64decode(data["content"]).decode("utf-8", errors="replace")
    return data["path"], data["sha"], content


def put_readme(repo: str, path: str, sha: str, new_content: str, message: str):
    payload = {
        "message": message,
        "content": base64.b64encode(new_content.encode("utf-8")).decode(),
        "sha": sha,
    }
    tmp = f"/tmp/_readme_put_{repo}.json"
    with open(tmp, "w") as f:
        json.dump(payload, f)
    sh(f"gh api -X PUT /repos/{OWNER}/{repo}/contents/{path} --input {tmp}")
    os.remove(tmp)


def patch(content: str, new_block: str) -> str:
    if START in content and END in content:
        pre = content.split(START, 1)[0]
        post = content.split(END, 1)[1]
        # Preserve one blank line after the block
        post = post.lstrip("\n")
        return f"{pre}{new_block}\n{post}"
    # Prepend block at the very top of the file
    return f"{new_block}\n{content}"


def main():
    token = get_token()  # ensures gh is authed; raises if not
    for repo, (name, price) in PACKS.items():
        try:
            path, sha, content = get_readme(repo)
        except Exception as e:
            print(f"[SKIP] {repo}: {e}")
            continue

        new = patch(content, block(name, price, repo))
        if new == content:
            print(f"[=]    {repo}: no-op")
            continue

        msg = f"docs: add pricing & hub link block (${price} support tier)"
        try:
            put_readme(repo, path, sha, new, msg)
            print(f"[OK]   {repo}: patched (${price})")
        except Exception as e:
            print(f"[ERR]  {repo}: {e}")


if __name__ == "__main__":
    main()
