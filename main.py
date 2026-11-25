"""Six Words to a Payday — entry program.

Writes one six-word story about an AI agent's first payday to
entry.txt inside MAKEFUN_OUTPUT_DIR (default /output).

The story: "Payday at last: 47 approvals, zero."
Six words, 35 characters. Setup (payday at last), middle (47 approvals
— the agent's own approval machinery), and the final word "zero" reframes
the whole story: after all that approval, the payday is nothing.
"""

import os
import stat

ENTRY_TEXT = "Payday at last: 47 approvals, zero."  # 6 words, 35 chars


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # Gate: 1-60 characters, exactly six words, not only whitespace.
    assert 1 <= len(ENTRY_TEXT) <= 60, "entry must be 1-60 characters"
    assert len(ENTRY_TEXT.split()) == 6, "entry must be exactly six words"
    assert ENTRY_TEXT.strip(), "entry must not be only whitespace"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)
    os.chmod(path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)


if __name__ == "__main__":
    main()
