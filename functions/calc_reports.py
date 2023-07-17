from functions.read_write_csv import get_file_contents
from functions.read_write_txt import get_time
from functions.color_theme import get_theme
from datetime import datetime, timedelta
from classes.report import Report
from rich.console import Console
from rich.theme import Theme

current_theme = Theme(get_theme(3))
console = Console(theme=current_theme)
today = get_time()


def prepare_reports(list, spaces):
    obj = Report(**list[0])
    obj.create_report_full_header(spaces)

    for elem in list:
        elem = Report(**elem)
        elem.create_value_bar(spaces)

    obj.create_header(spaces, "-")


def inventory_report(given_date):
    data = (get_file_contents("data/inventory.csv"))
    res = []
    count = 0
    calc_date = None

    # find out what the user has entered as date format
    if len(given_date) == 4:
        the_date = datetime.strptime(given_date, "%Y").date()
        tdelta = timedelta(days=370)
        calc_date = the_date + tdelta
        calc_date = calc_date.strftime('%Y')
        print(calc_date)

    elif len(given_date) == 7:
        the_date = datetime.strptime(given_date, "%Y-%m").date()
        tdelta = timedelta(days=35)
        calc_date = the_date + tdelta
        calc_date = calc_date.strftime('%Y-%m')
        print(calc_date)

    elif len(given_date) == 10:
        calc_date = given_date

    else:
        console.print(
            "\n[alert]You did not give a good date format. Can't do anything with:[/] ", given_date)
        exit()

    for item in data:
        if item["buy_date"] <= calc_date and int(item["quantity"]) > 0:
            # if given_date in item["buy_date"] and int(item["quantity"]) > 0:
            if item["expiration_date"] > get_time().strftime('%Y-%m-%d'):
                res.append(item)
            else:
                count += 1
    if count > 0:
        console.print(
            "\n[text]===== We don't show them here but there are still products in the inventory that are out of date! =====[/]")
        console.print(
            "[text]===== Get rid of them! Hire a professional developer who can write the necessary module for this! =====[/]")

    console.print("\n[title]==== Inventory Report ====[/]")
    if len(res) > 0:
        spaces = [4, 30, 10, 20, 10, 20]
        prepare_reports(res, spaces)
        print("\n")
    else:
        console.print(
            "[bold][alert]On the day you specified there was nothing in inventory!\n[/][/]")


def revenue_report(given_date):
    data = (get_file_contents("data/sold.csv"))
    res = []
    for item in data:
        if given_date in item["sell_date"]:
            res.append(item)

    console.print("\n[title]==== Revenue Report ====[/]")
    revenue = 0
    revenue_list = []
    if len(res) > 0:
        for elem in res:
            elem_revenue = round(
                int(elem["quantity"]) * float(elem["sell_price"]), 2)
            copy_elem = elem.copy()
            copy_elem.update({"revenue": elem_revenue})
            revenue_list.append(copy_elem)
            revenue += elem_revenue

        spaces = [4, 12, 18, 10, 10, 10, 10]
        prepare_reports(revenue_list, spaces)

        console.print(
            f"[bold][text]Total revenue {given_date}:[/][price] {round(revenue, 2)}[/][/] :thumbs_up:\n")
    else:
        console.print(
            "[bold][alert]In the period of time you specified, no products were sold![/][/]\n")


def profit_report(given_date):
    data = (get_file_contents("data/sold.csv"))
    res = []
    for item in data:
        if given_date in item["sell_date"] and item["sell_date"] <= today.strftime("%Y-%m-%d"):
            res.append(item)

    console.print("\n[title]==== Profit Report ====[/]")
    profit = 0
    profit_list = []
    if len(res) > 0:
        for elem in res:
            elem_profit = round(int(
                elem["quantity"]) * (float(elem["sell_price"]) - float(elem["buy_price"])), 2)
            copy_elem = elem.copy()
            copy_elem.update({"profit": elem_profit})
            profit_list.append(copy_elem)
            profit += elem_profit

        spaces = [4, 12, 18, 10, 10, 10, 10]
        prepare_reports(profit_list, spaces)

        console.print(
            f"[bold][title]Total profit {given_date}:[/][price] {round(profit, 2)}[/][/] :thumbs_up:\n")
    else:
        console.print(
            "[action]In the period of time you specified, no products were sold![/]")
