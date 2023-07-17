from classes.order import Order
from classes.report import Report
from datetime import datetime

from functions.read_write_csv import append_order


class BuyOrder(Order):
    def __init__(self, id, product_name, quantity, price, expiration_date):
        super().__init__(id, quantity, price)
        self.product_name = product_name
        self.expiration_date = datetime.strptime(
            expiration_date, '%Y-%m-%d').date()

    def __str__(self):
        return format(f"| {str(self.id).rjust(4)} | {self.product_name.ljust(30, ' ')} | {str(self.quantity).center(10, ' ')} | {self.date.strftime('%d %B %Y').ljust(18, ' ')} | {str(self.price).center(10, ' ')} | {self.expiration_date.strftime('%d %B %Y').ljust(18, ' ')} |")

    def append_buy_order(self):
        return append_order("data/bought.csv", [self.id, self.product_name, self.quantity,
                                                self.date, self.price, self.expiration_date])

    # insert the data of the buy-order in a dictionary, make a Report object
    # call create_report and pass in the nessasary spaces for the column with
    def report(self):
        data = {
            "id": self.id,
            "product name": self.product_name,
            "quantity": self.quantity,
            "buy date": self.date,
            "buy price": self.price,
            "expiration date": self.expiration_date
        }
        report = Report(**data)
        report.create_report([4, 30, 10, 20, 10, 20])
