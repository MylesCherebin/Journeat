from order import Order

class Customer:
    def __init__(self, name, order_num):
        self.name = "Customer " + str(name)
        self.order = Order(order_num)
        order_num += 1
        print(self.name + "'s order has been placed")
