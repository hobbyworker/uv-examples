from rich.console import Console
from rich.table import Table

table = Table("tool", "what it does")
table.add_row("uv run", "run a script")
table.add_row("uv add --script", "add a dependency to a script")
Console().print(table)
