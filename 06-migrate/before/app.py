"""Show how long ago the latest versions of PyPI packages were released."""

import sys
from datetime import datetime, timezone

import requests
from dateutil import parser
from dateutil.relativedelta import relativedelta
from tabulate import tabulate


def age(uploaded, now):
    delta = relativedelta(now, parser.isoparse(uploaded))
    return f"{delta.years}y {delta.months}m {delta.days}d"


def latest(name):
    response = requests.get(f"https://pypi.org/pypi/{name}/json", timeout=10)
    response.raise_for_status()
    data = response.json()
    return data["info"]["version"], data["urls"][0]["upload_time_iso_8601"]


if __name__ == "__main__":
    now = datetime.now(timezone.utc)
    rows = []
    for name in sys.argv[1:] or ["requests", "flask", "django"]:
        version, uploaded = latest(name)
        rows.append((name, version, age(uploaded, now)))
    print(tabulate(rows, headers=["package", "latest", "released"]))
