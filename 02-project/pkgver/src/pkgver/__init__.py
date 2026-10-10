"""Show the latest versions of PyPI packages."""

import sys

import httpx
from rich.console import Console
from rich.table import Table

PYPI_URL = "https://pypi.org/pypi/{name}/json"


def latest_version(client: httpx.Client, name: str) -> tuple[str, str]:
    """Return the latest version of a package and the date it was uploaded."""
    response = client.get(PYPI_URL.format(name=name))
    response.raise_for_status()
    data = response.json()
    files = data["urls"]
    uploaded = files[0]["upload_time"][:10] if files else ""
    return data["info"]["version"], uploaded


def main() -> None:
    names = sys.argv[1:] or ["uv", "httpx", "rich"]
    table = Table("package", "latest", "uploaded")
    with httpx.Client(timeout=10) as client:
        for name in names:
            version, uploaded = latest_version(client, name)
            table.add_row(name, version, uploaded)
    Console().print(table)
