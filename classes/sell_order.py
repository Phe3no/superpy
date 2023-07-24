from classes.order import Order
from classes.report import Report

from functions.read_write_csv import append_order, update_inventory


class SellOrder(Order):
    def __init__(self, id, product_name, quantity, price):
        super().__init__(id, quantity, price)
        self.product_name = product_name

    def __str__(self):
        return format(f"| {str(self.id).rjust(4)} | {self.product_name.ljust(30, ' ')} | {str(self.quantity).center(6, ' ')} | {self.buy_date.ljust(10, ' ')} | {str(self.buy_price).ljust(10, ' ')} | {self.expiration_date.ljust(15, ' ')} |")

    def append_sell_order(self):
        result = update_inventory(
            "data/inventory.csv", self.product_name, self.quantity)
        self.buy_price = result["price"]
        return append_order("data/sold.csv",
                            [self.id, result["id"], self.date, self.quantity, self.price, result["price"]])

    # insert the data of the buy-order in a dictionary, make a Report object
    # call create_report and pass in the nessasary spaces for the column with
    def report(self):
        data = {
            "id": self.id,
            "product_name": self.product_name,
            "sell date": self.date,
            "quantity": self.quantity,
            "sell price": self.price,
            "buy price": self.buy_price
        }
        report = Report(**data)
        report.create_report([4, 30, 18, 10, 10, 10])
