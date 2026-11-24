#!/usr/bin/env python3
"""Charm the Commuter: Forecast a City That Isn't — make.fun entry.

A one-line weather forecast for Mislaid, a city that does not exist,
written to make a bored commuter smile. The program writes exactly
that line to /output/entry.txt: 135 characters, no trailing newline,
the same bytes on every run.
"""

import os

ENTRY = "Good morning, Mislaid: sunshine all day, 18 degrees \u2014 the only cloud hangs over your stop, where your umbrella has lived since Tuesday."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
