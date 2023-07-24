import csv
from os import SEEK_END, SEEK_CUR
from functions.read_write_txt import get_time
from rich.console import Console

console = Console()


def get_last_order_id(file):
    # read the file as a 'byte' string (rb) so we can use: seek()
    with open(file, "rb") as csv_file:
        try:
            # seek the second last char in the file
            csv_file.seek(-2, SEEK_END)
            # read back until a new line literal is found
            while csv_file.read(1) != b"\n":
                csv_file.seek(-2, SEEK_CUR)
        except OSError:
            # on error go to begin of file
            csv_file.seek(0)
        try:
            # convert byte-string to a normal string (.decode())
            last_line = csv_file.readline().decode()
            # split the string on a ','
            res = last_line.split(",")
            # convert the first string element to int and return
            res = int(res[0])
            return res
        except ValueError:
            # if not an int, return 0 (in case no product is found)
            print(f"==== First product added to the {file} ====")
            return 0
    # with - open - as: should close the file automatically, therefor no: csv_file.close()


def append_order(file, new_order):
    with open(file, "a", newline="") as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=",")
        if file == "data/bought.csv":
            with open("data/inventory.csv", "a", newline="") as inventory_file:
                inventory_writer = csv.writer(inventory_file, delimiter=",")
                inventory_writer.writerow(new_order)
        if csv_writer.writerow(new_order):
            print(f"==== Another product added to the {file} ====")
            return True
        else:
            return False


# def update_inventory(file, bought_id, quantity):
def update_inventory(file, product_name, quantity):
    def check_for_product(file, product_name):
        with open(file, "r") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for line in csv_reader:
                if line["product_name"] in product_name:
                    return line["id"]
            console.print(
                f"\n----- [red]Unfortunatly we can't sell [blue]{product_name}[/]. If you want to now what you can buy, check the inventory![/] -----\n")
            exit()

    data = []
    buy_price = ""
    product_id = check_for_product(file, product_name)
    print(product_id)
    with open(file, "r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            if line["id"] == str(product_id):
                # check stock
                if (int(line["quantity"]) - quantity) < 0:
                    console.print(
                        "\n----- [red]Unfortunately there is not enough of this product in stock![/] -----\n")
                    exit()
                # check expiration date
                if (line["expiration_date"]) < get_time().strftime("%Y-%m-%d"):
                    console.print(
                        "\n-----  [red]Unfortunately you are not allowed to buy this product, it has past it's expiration date![/] -----\n")
                    exit()
                # enough stock, change quantity
                line["quantity"] = int(line["quantity"]) - quantity
                buy_price = line["buy_price"]
            data.append(line)

    with open(file, "w", newline="") as csv_file:
        fieldnames = ["id", "product_name", "quantity",
                      "buy_date", "buy_price", "expiration_date"]
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writeheader()
        for line in data:
            csv_writer.writerow(line)

    return {"price": buy_price, "id": product_id}


def get_file_contents(file):
    data = []
    with open(file, "r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            data.append(line)
    return data
