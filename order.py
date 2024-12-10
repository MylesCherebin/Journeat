class Order:
    def __init__(self, num):
        self.num = num
        self.time = 5
        
    def order_complete(self):
        print("Order number " + str(self.num) + " completed")