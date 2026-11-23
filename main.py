"""Write a one-line joke about working beside an AI coding agent.

The joke is a fixed, hand-written line. The program writes it verbatim to
/output/entry.txt as UTF-8, with no trailing newline, so the file holds
exactly one line of 1-280 characters. Before writing, it checks the text
against the same gate the competition uses (1-280 Unicode code points,
a single line, not only white space) and refuses to write anything invalid;
after writing, it reads the file back and confirms it holds exactly the
joke. Standard library only, no network.

The output path defaults to /output/entry.txt (the sandbox location) and
can be overridden with the JOKE_OUTPUT_PATH environment variable, which
the tests use so they never touch the real output file.
"""

import os

JOKE = "My AI agent crashed the demo, apologized, fixed it live \u2014 and the audience thinks I'm its assistant."

DEFAULT_OUTPUT_PATH = "/output/entry.txt"

MIN_CHARS = 1
MAX_CHARS = 280


def output_path() -> str:
    return os.environ.get("JOKE_OUTPUT_PATH", DEFAULT_OUTPUT_PATH)


def validate(text: str) -> None:
    """Raise ValueError unless the text passes the competition's gate."""
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(f"joke must be {MIN_CHARS}-{MAX_CHARS} characters, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise ValueError("joke must be a single line")
    if not text.strip():
        raise ValueError("joke must not be only white space")


def main() -> None:
    validate(JOKE)
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != JOKE:
        raise ValueError("written file does not match the joke")


if __name__ == "__main__":
    main()
