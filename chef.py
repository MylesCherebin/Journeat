import time

class Chef:
    def __init__(self, name):
        self.name = "Chef " + str(name)
        self.order = None
        print(self.name + " has been hired!")
        print("")
        print("")

    def work(self, orders):
        print(self.name + " is looking for orders" )
        if len(orders) > 0:
            self.order = orders.pop()
            print(self.name + " is working on order " + str(self.order.num))
            time.sleep(self.order.time)
            self.order.order_complete()
        #return orders


