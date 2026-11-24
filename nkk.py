import random

id_list = [1, 2, 3, 4, 5]
item_list = [12, 12, 3, 4, 3]

for ind, items in enumerate(item_list, start=1):
    if items < 10:
        print(f"Customer {ind} ---> Items in basket: {items}")
    else:
        winner = random.randint(1, 2)
        lottery_status = "has NOT won a lottery ticket"

        if winner == 1:
            lottery_status = "has won a lottery ticket"

        print(f"Customer {ind} --> Items in basket: {items}, {lottery_status}, time to process at self checkout lane")
import random

class CheckoutLane:
    def __init__(self, lane_type, capacity):
        self.lane_type = lane_type
        self.capacity = capacity
        self.queue = []

    def is_full(self):
        return len(self.queue) >= self.capacity

    def add_customer(self, customer):
        if not self.is_full():
            self.queue.append(customer)
            return True
        else:
            return False

    def process_customers(self):
        for customer in self.queue:
            # Assuming self-checkout time is 4 seconds per item
            checkout_time = customer.items * 4
            print(f"Processing Customer {customer.id} at {self.lane_type} Lane. Checkout time: {checkout_time} seconds")
            # Simulating checkout time with time.sleep
            time.sleep(checkout_time)

    def display(self):
        customers_str = " ".join(str(customer.id) for customer in self.queue)
        return f"{self.lane_type} Lane ({len(self.queue)}/{self.capacity}): {customers_str}"

class Customers:
    def __init__(self, customer_id, items):
        self.id = customer_id
        self.items = items

# Your existing code
import datetime
import random
import time

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

    def timefunc(self):
        for h in details.values():
            we = h * self_time
            return we


class Basket(Customers):
    pass


# this works yep, ask chatgpt how
customers1 = Customers()
customers1.detailsfunc()
customers1.timefunc()
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

# cashiertime = 4
# total_cashiertime = 4 * details.values()
# time.sleep(total_cashiertime)

# processing time (in self checkout lane for now)


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


# Creating instances of the CheckoutLane class
service_lane = CheckoutLane("Self-Checkout", 1)
regular_lanes = [CheckoutLane("Regular", 5) for _ in range(5)]

# Adding customers to lanes
for customer_id, items in details.items():
    customer = Customers(customer_id, items)

    # Try to add customer to the service lane
    if service_lane.add_customer(customer):
        print(f"Customer {customer_id} added to {service_lane.lane_type} Lane")
    else:
        # If service lane is full, add customer to one of the regular lanes
        for regular_lane in regular_lanes:
            if regular_lane.add_customer(customer):
                print(f"Customer {customer_id} added to {regular_lane.lane_type} Lane")
                break

# Display the lanes
print(service_lane.display())
for regular_lane in regular_lanes:
    print(regular_lane.display())

# Process customers in lanes
service_lane.process_customers()
for regular_lane in regular_lanes:
    regular_lane.process_customers()
