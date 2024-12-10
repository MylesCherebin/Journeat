from chef import Chef
from customer import Customer
from  order import Order
import threading
import time

orders = []
chefs = []
customers = []
customer_num = 1
chef_num = 1
thread_num = 1
order_num = 1

#locks
chef_lock = threading.Lock()
cust_lock = threading.Lock()

def get_chef(name):
    chef = Chef(chef_num)
    while(1):
        chef_lock.acquire()
        chef.work(orders)
        chef_lock.release()

if __name__ == "__main__":
    print("the game has started.")
    print("")
    x = threading.Thread(target=get_chef, args=(1,))
    thread_num += 1
    y = threading.Thread(target=get_chef, args=(2,))
    

    # jim = Customer("jim",customer_num)
    # customer_num += 1
    # ron = Customer("ron", customer_num)
    for i in range(1,6):
        orders.append(Order(order_num))
        order_num += 1
    print("orders added")

    #x.start()
    y.start()



    
