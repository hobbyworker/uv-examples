#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.13"
# dependencies = ["segno"]
# ///
"""Save a QR code for a URL as qr.png."""

import sys

import segno

url = sys.argv[1] if len(sys.argv) > 1 else "https://hobbyworker.me/"
segno.make(url).save("qr.png", scale=8)
print(f"Saved qr.png for {url}")
