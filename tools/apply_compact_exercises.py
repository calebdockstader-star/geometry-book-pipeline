#!/usr/bin/env python3
"""Wrap every numbered exercise group in the shared compact column layout.

The chapter sources predate ``exercisecols`` and therefore mix full-width
lists with ordinary ``multicols`` wrappers.  This migration is deliberately
idempotent: it removes only those wrappers inside an ``exercisegroup`` block,
then wraps all active ``exlist`` material belonging to that group once.
"""

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
CHAPTERS = sorted((ROOT / "chapters").glob("ch[0-9][0-9].tex"))
EXPECTED_GROUPS = 137

GROUP_RE = re.compile(r"\\exercisegroup\{[^}]+\}")
BOUNDARY_RE = re.compile(r"\\(?:exercisegroup\{|section\*\{)")
BEGIN_LIST_RE = re.compile(r"\\begin\{exlist\}(?:\[[^]]*\])?")
END_LIST_RE = re.compile(r"\\end\{exlist\}")
WRAPPER_LINE_RE = re.compile(
    r"(?m)^[ \t]*\\(?:begin\{(?:multicols\}\{2|VIexcols|exercisecols)\}"
    r"|end\{(?:multicols|VIexcols|exercisecols)\})[ \t]*(?:%[^\n]*)?\n?"
)


def active_matches(pattern: re.Pattern[str], text: str) -> list[re.Match[str]]:
    """Return matches that are not in the comment portion of their line."""
    matches = []
    for match in pattern.finditer(text):
        line_start = text.rfind("\n", 0, match.start()) + 1
        prefix = text[line_start : match.start()]
        # A percent escaped by an odd number of backslashes is not a comment.
        comment = False
        for percent in (m.start() for m in re.finditer("%", prefix)):
            slashes = 0
            cursor = percent - 1
            while cursor >= 0 and prefix[cursor] == "\\":
                slashes += 1
                cursor -= 1
            if slashes % 2 == 0:
                comment = True
                break
        if not comment:
            matches.append(match)
    return matches


def migrate(text: str, chapter: str) -> tuple[str, int]:
    groups = active_matches(GROUP_RE, text)
    changed = 0
    for group in reversed(groups):
        following = text[group.end() :]
        boundary = next(iter(active_matches(BOUNDARY_RE, following)), None)
        end = group.end() + boundary.start() if boundary else len(text)
        region = text[group.end() : end]
        region = WRAPPER_LINE_RE.sub("", region)

        starts = active_matches(BEGIN_LIST_RE, region)
        finishes = active_matches(END_LIST_RE, region)
        if not starts or not finishes:
            raise RuntimeError(f"{chapter}: exercise group has no complete exlist")
        first = starts[0].start()
        last = finishes[-1].end()
        region = (
            region[:first]
            + "\\begin{exercisecols}\n"
            + region[first:last]
            + "\n\\end{exercisecols}"
            + region[last:]
        )
        text = text[: group.end()] + region + text[end:]
        changed += 1
    return text, changed


def main() -> None:
    total = 0
    for path in CHAPTERS:
        source = path.read_text()
        revised, count = migrate(source, path.name)
        if revised != source:
            path.write_text(revised)
        total += count
        if count:
            print(f"{path.name}: {count} exercise groups")
    if total != EXPECTED_GROUPS:
        raise SystemExit(
            f"expected {EXPECTED_GROUPS} exercise groups, migrated {total}"
        )
    print(f"migrated {total} exercise groups")


if __name__ == "__main__":
    main()
