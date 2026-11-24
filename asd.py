import datetime
import random
import time
import tkinter as tk


customer_num = random.randint(1, 10)
items_num = random.randint(1, 30)

# variables for checkout time
self_time = 4
cashier_time = 6
total_time = 0

initial = {}
details = {}


# print(customer_num)
class Customers:
    def __init__(self):
        self.initialnumber = customer_num
        self.items = random.randint(1, 30)

    # creating a function so that the inital number of custmoers are added to a dictionary, where the key is the customer id
    # and the value is the number of items in their basket.
    def detailsfunc(self):
        for i in range(1, self.initialnumber):
            id = i
            b_items = random.randint(1, 30)
            details[id] = b_items

    def oncoming_customers(self):
        length = customer_num
        for i in range(1000):
            time.sleep(5)
            additional_time = datetime.datetime.now() + datetime.timedelta(seconds=30)
            new_id = length
            details[new_id] = random.randint(1, 30)
            length += 1
            print(f"Customer {new_id} arrived at {additional_time}")
            time.sleep(25)
            id_list.append(new_id)
            item_list.append(details[new_id])
    def timefunc(self):
        for h in details.values():
            we = h * self_time
            return we


class Basket(Customers):
    pass


# creating the instances
customers1 = Customers()
customers1.detailsfunc()

print(details)




# printing the number of items in the basket for a customer

customerid = int(input("enter the customer id: "))

if customerid in details:
    print(f"customer {customerid} has {details[customerid]} items")

# checkout time for each lane


# calculating the total time taken to checkout all the customers in a line, only did for self checkout.
for _ in details.values():
    time_taken = _ * self_time
    total_time = total_time + time_taken

print("time taken for checkout = ", total_time, "seconds")



# awarding the lottery ticket, using random number generator to give the lottery ticket


id_list = list(details.keys())
item_list = list(details.values())
# enumerating the item_list as to reduce errors when displaying,
# when there are multiple customers with the same amount of items in their basket

# indexing = list(enumerate(item_list))
# print(indexing)
# was tested using the file nkk.py

for ind, items in enumerate(item_list, start=1):
    if items < 10:
        print(f"Customer {ind} ---> Items in basket: {items}")
    else:
        winner = random.randint(1, 2)
        lottery_status = "has NOT won a lottery ticket"

        if winner == 1:
            lottery_status = "has won a lottery ticket"

        print(f"Customer {ind} --> Items in basket: {items}, {lottery_status}, time to process at self checkout lane")

customers1.timefunc()
for _ in range(5):  # Adjust the number of iterations as needed
    customers1.oncoming_customers()
    time.sleep(30)


print(details)

