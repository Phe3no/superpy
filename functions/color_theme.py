

theme1 = [
    "red",
    "blue",
    "orange3",
    "yellow3",
    "grey82"
]

theme2 = [
    "dark_red",
    "dark_magenta",
    "orange4",
    "plum4",
    "grey82"
]

theme3 = [
    "bright_red",
    "bright_green",
    "bright_yellow",
    "bright_blue",
    "bright_magenta"
]


def get_theme(num_theme):
    result = {"alert": "", "title": "",
              "text": "", "price": "", "frame": ""}

    try:
        # eval returns the value of a variable that was expressed as a string
        result["alert"] = eval("theme" + str(num_theme) + "[0]")
        result["title"] = eval("theme" + str(num_theme) + "[1]")
        result["text"] = eval("theme" + str(num_theme) + "[2]")
        result["price"] = eval("theme" + str(num_theme) + "[3]")
        result["frame"] = eval("theme" + str(num_theme) + "[4]")
    except (NameError):
        print("Color_theme not loaded!")

    return result
