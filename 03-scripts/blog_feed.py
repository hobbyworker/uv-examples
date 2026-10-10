# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "httpx>=0.28.1",
#     "rich>=15.0.0",
# ]
# ///
"""Print the five latest posts on hobbyworker.me."""

import sys
import xml.etree.ElementTree as ET
from email.utils import parsedate_to_datetime

import httpx
from rich.console import Console
from rich.table import Table


def main() -> None:
    lang = sys.argv[1] if len(sys.argv) > 1 else "en"
    response = httpx.get(f"https://hobbyworker.me/{lang}/index.xml", timeout=10)
    response.raise_for_status()
    items = list(ET.fromstring(response.content).iter("item"))[:5]
    table = Table("date", "title")
    for item in items:
        date = parsedate_to_datetime(item.findtext("pubDate"))
        table.add_row(f"{date:%Y-%m-%d}", item.findtext("title"))
    Console().print(table)


if __name__ == "__main__":
    main()
