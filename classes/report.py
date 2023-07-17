from datetime import date, datetime
from rich.console import Console
from rich.theme import Theme
from functions.color_theme import get_theme


class Report:
    # get the colors needed for rich
    current_theme = Theme(get_theme(3))
    console = Console(theme=current_theme)

    # constructor
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    # create a dictionarie with the values of a Report object
    def to_dict(self):
        return {
            key: value
            for key, value in self.__dict__.items()
            if not key.startswith("_")
        }

    # create the horizontal frames for the report
    def create_header(self, spaces, char):
        count = 0
        for key, value in self.to_dict().items():
            self.console.print(
                f"[frame]+ {char.ljust(spaces[count], char)}[/] ", end='')
            count += 1
        self.console.print("[frame]+[/]")

    # create the title bar of a report
    def create_title_bar(self, spaces):
        count = 0
        for key, value in self.to_dict().items():
            self.console.print(
                f"[frame]|[/] [title]{key.ljust(spaces[count], ' ').title()} [/]", end='')
            count += 1
        self.console.print("[frame]|[/]")

    # create the value rows
    def create_value_bar(self, spaces):
        count = 0
        # get the nessasary values of this object (buy-order, sell-order, inventory, revenue or profit object)
        for key, value in self.to_dict().items():
            if type(value) == int:
                value = str(value)
                self.console.print(
                    f"[frame]|[/] [red]{value.center(spaces[count], ' ')} [/]", end='')
            elif type(value) == float:
                value = str(value)
                self.console.print(
                    f"[frame]|[/] [text]{value.rjust(spaces[count], ' ')} [/]", end='')
            elif type(value) == date or type(value) == datetime:
                value = value.strftime("%d %B %Y")
                self.console.print(
                    f"[frame]|[/] [text]{value.ljust(spaces[count], ' ')} [/]", end='')
            elif "price" in key:
                self.console.print(
                    f"[frame]|[/] [price]{value.rjust(spaces[count], ' ')} [/]", end='')
            else:
                self.console.print(
                    f"[frame]|[/] [text]{value.ljust(spaces[count], ' ').title()} [/]", end='')
            count += 1
        self.console.print("[frame]|[/]")

    # create a complete report, only usable for a single value row

    def create_report(self, spaces):
        self.create_header(spaces, "-")
        self.create_title_bar(spaces)
        self.create_header(spaces, "=")
        self.create_value_bar(spaces)
        self.create_header(spaces, "-")

    # create only the header for a report (first frame row, title, en second frame row)
    def create_report_full_header(self, spaces):
        self.create_header(spaces, "-")
        self.create_title_bar(spaces)
        self.create_header(spaces, "=")
