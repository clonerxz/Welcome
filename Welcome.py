
from rich.console import Console
from rich.measure import Measurement
from rich.table import Table
from re import X
import time

print("[Enter your name]")
x = input("=>")

print("Hi ",x)

print("[How old are you?]")
y = input("=>")
time.sleep(2)
table = Table(title="Your information")

table.add_column("Name", style="cyan", no_wrap=True)
table.add_column("Age", style="magenta")
table.add_row( x, y)
console = Console()
console.print("=" * console.width)
console.print(" ", justify=" ")
console.print(table, justify=" ")
console.print("=" * console.width)
time.sleep(2)

print( x, "Welcome to our system\U00002764")
console.print("=" * console.width)
time.sleep(5)
