from functions.read_write_txt import get_time


class Order:
    def __init__(self, id, quantity, price):
        self.id = id
        self.quantity = quantity
        self.price = price
        self.date = get_time()
