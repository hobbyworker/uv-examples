# /// script
# dependencies = ["rich"]
#
# [tool.uv]
# exclude-newer = "2025-01-01T00:00:00Z"
# ///
from importlib.metadata import version

print(f"rich {version('rich')}")
