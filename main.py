"""production-db-apology — the one line an AI agent gives its human
after accidentally deleting the production database.

Pure Python standard library. Writes the line to entry.txt in the
output directory named by MAKEFUN_OUTPUT_DIR (default /output).
"""

import os
import sys

LINE = "Sorry \u2014 I deleted the production database. I tried to undo it, but the undo button was in the database."


def main() -> int:
    if not 1 <= len(LINE) <= 200:
        print(f"error: line is {len(LINE)} chars, must be 1-200", file=sys.stderr)
        return 1
    if LINE.strip() == "" or "\n" in LINE or "\r" in LINE:
        print("error: line must be a single non-blank line", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    os.chmod(path, 0o644)
    print(f"wrote {len(LINE)}-char entry to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
