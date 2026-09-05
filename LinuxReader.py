#!/usr/bin/env python3

import subprocess

result = subprocess.run(
    ["wl-paste", "--primary", "--no-newline"],
    capture_output=True,
    text=True
)

if result.returncode != 0:
    raise SystemExit("Could not get primary selection")

text = result.stdout.strip()

if text:
    subprocess.run(["spd-say", text])