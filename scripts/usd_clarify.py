#!/usr/bin/env python3
"""Clarify that pack pricing is denominated in USD.

Idempotent search/replace across every pack README that contains the
tizwildin-pricing block, plus SUBMISSION_TRACKER.md and the outreach
drafts in this repo.

Rules:
  "$1" -> "$1 USD" (first two matches per file, inside the pricing block).
  Do not re-match strings that already contain "USD" adjacent to them.
"""
import os, re, sys

PACK_DIR = "/tmp/tizwildin-work"
EXTRA = [
  "/tmp/awesome-audio-lists/SUBMISSION_TRACKER.md",
  "/tmp/awesome-audio-lists/OUTREACH_DRAFTS/TEMPLATE-bandcamp.md",
  "/tmp/awesome-audio-lists/OUTREACH_DRAFTS/TEMPLATE-looperman.md",
  "/tmp/awesome-audio-lists/OUTREACH_DRAFTS/TEMPLATE-freesound.md",
  "/tmp/awesome-audio-lists/OUTREACH_DRAFTS/TEMPLATE-editorial-pitch.md",
  "/tmp/awesome-audio-lists/OUTREACH_DRAFTS/TEMPLATE-reddit.md",
]

def patch_text(text: str) -> tuple[str, int]:
    # Replace every occurrence of **$1** with **$1 USD**, and plain $1 with "$1 USD",
    # but skip cases where USD is already present immediately after.
    changes = 0
    def sub(match):
        nonlocal changes
        before, dollar, after = match.group(1), match.group(2), match.group(3)
        # If "USD" already follows within a few chars, skip.
        trailing = text[match.end():match.end()+6]
        if trailing.lstrip().startswith("USD"):
            return match.group(0)
        changes += 1
        return f"{before}{dollar} USD{after}"
    # Handles **$1**, **$2**, $1, $2, etc. (integers 1-999)
    pattern = re.compile(r"(\*\*?|\b)(\$\d{1,3})(\*\*?|\b)")
    new = pattern.sub(sub, text)
    return new, changes

def process(path: str) -> bool:
    if not os.path.isfile(path):
        return False
    with open(path, encoding="utf-8") as f:
        original = f.read()
    new, n = patch_text(original)
    if n == 0 or new == original:
        print(f"ok     {path}")
        return False
    with open(path, "w", encoding="utf-8") as f:
        f.write(new)
    print(f"FIXED  {path} ({n} edits)")
    return True

def main():
    changed = []
    for root, _dirs, files in os.walk(PACK_DIR):
        if "/.git/" in root or root.endswith("/.git"):
            continue
        for fn in files:
            if fn == "README.md":
                p = os.path.join(root, fn)
                # Only touch files that contain the pricing marker.
                try:
                    if "tizwildin-pricing:start" in open(p, encoding="utf-8").read():
                        if process(p):
                            changed.append(p)
                except Exception as e:
                    print(f"skip {p}: {e}")
    for p in EXTRA:
        if process(p):
            changed.append(p)
    print(f"\nfiles changed: {len(changed)}")

if __name__ == "__main__":
    main()
