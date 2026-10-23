from rich.console import Console
from rich.text import Text

# Beispiel Daten
'''averages = [
    ("A", 2.16),
    ("B", 4.33),
    ("C", 6.57),
    ("D", 8.71),
]'''

def render_bar_chart(values):
    console = Console()

    def scale_bar(value, width=40):
            if value <= 0:
                return 0
            return round(value / 10 * width)

    how_to_style = {
        "A": "bold yellow",
        "B": "bold green",
        "C": "bold magenta",
        "D": "bold cyan",
    }
       
    for value in values:
        letter, mean = value
        scaled_mean = scale_bar(mean, 20)
        line = Text(f"{letter} |")
        line.append("█" * scaled_mean, style=how_to_style[letter])
        line.append(Text(str(mean)))
        console.print(line)

    return console