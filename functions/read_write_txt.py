from datetime import datetime, date, timedelta
from rich.console import Console
from rich.theme import Theme
from functions.color_theme import get_theme


def set_time(time):
    print(time)
    with open("data/advanced_time.txt", "w") as file:
        file.write(time)


def get_time():
    try:
        with open("data/advanced_time.txt") as file:
            saved_time = file.readline()
            return datetime.strptime(saved_time, "%B %d %Y").date()
    except OSError:
        set_time(date.today())


def show_time():
    # if (get_time() - date.today() != timedelta(days=0)):
    return f"{get_time().strftime('%A, %d %B %Y')}"
