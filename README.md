# uv-examples

[![CI](https://github.com/hobbyworker/uv-examples/actions/workflows/ci.yml/badge.svg)](https://github.com/hobbyworker/uv-examples/actions/workflows/ci.yml)

Sample code for the [uv Guide](https://hobbyworker.me/en/series/uv-guide/) series on hobbyworker.me. [uv](https://docs.astral.sh/uv/) is a fast Python package and project manager by Astral.

| Part | Post | Folder |
|---|---|---|
| 1 | [Installing uv and managing Python versions](https://hobbyworker.me/en/dev/2026-10-11-uv-guide-1-install-and-python-versions/) | (commands only) |
| 2 | [Creating projects and managing dependencies](https://hobbyworker.me/en/dev/2026-10-12-uv-guide-2-projects-and-dependencies/) | [`02-project/pkgver`](02-project/pkgver) |
| 3 | [Running single-file scripts](https://hobbyworker.me/en/dev/2026-10-13-uv-guide-3-single-file-scripts/) | [`03-scripts`](03-scripts) |
| 4 | [Command-line tools with uvx and uv tool](https://hobbyworker.me/en/dev/2026-10-14-uv-guide-4-uvx-and-uv-tool/) | (commands only) |
| 5 | [Formatting and checking code with format, check, and audit](https://hobbyworker.me/en/dev/2026-10-15-uv-guide-5-format-check-audit/) | [`05-checks/wordcount`](05-checks/wordcount) |
| 6 | [Migrating pip and requirements.txt projects](https://hobbyworker.me/en/dev/2026-10-16-uv-guide-6-migrating-from-pip/) | [`06-migrate`](06-migrate) (`before`, `after`) |
| 7 | [Using uv in GitHub Actions and Docker](https://hobbyworker.me/en/dev/2026-10-17-uv-guide-7-github-actions-and-docker/) | [`.github/workflows/ci.yml`](.github/workflows/ci.yml), [`02-project/pkgver/Dockerfile`](02-project/pkgver/Dockerfile) |

The posts are published one per day from 2026-10-11 to 2026-10-17.

## Requirements

- uv 0.13.0 or later
- Python is installed by uv when needed. The projects require Python 3.13 or later.

## Run

```bash
cd 02-project/pkgver
uv run pkgver requests pandas
```

```bash
cd 03-scripts
uv run blog_feed.py
```

Last checked on 2026-10-10 with uv 0.13.0 on macOS (Apple Silicon). The CI workflow runs the tests on Python 3.13, 3.14 and 3.15, runs `uv format --check`, `uv check` and `uv audit`, and builds the Docker image.

## License

[MIT](LICENSE)
