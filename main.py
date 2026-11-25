"""The Funniest Toaster Error Message.

Writes one deadpan error line to /output/entry.txt (1-120 chars).
Standard library only, deterministic.
"""

import os

TEXT = "The bread is fine. It is you I am worried about."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
