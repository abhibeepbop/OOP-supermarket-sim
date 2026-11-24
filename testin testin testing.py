import datetime
import random


class Customer:
    def __init__(self):
        self.items = random.randint(1, 5)
        self.processed = False
        self.will_process = None

# generating the a list of 10 customers
customers = [Customer() for _ in range(10)]


for customer in customers:
    # calculating the amount of time the item gets processes
    will_process_time = datetime.datetime.now() + datetime.timedelta(seconds=customer.items * 1)

    #assigning the time the cheout will get finished to self.willprocess
    customer.will_process = will_process_time

    print(customer.will_process)

# creating a loop, using while
while True:
    print(customers)

    for customer in customers:
        print(customer.will_process)
        if datetime.datetime.now() > customer.will_process:
            customers.remove(customer)


x = max(3,2,1)
print(x)