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

    def timefunc(self):
        for h in details.values():
            we = h * self_time
            return we


class Basket(Customers):
    pass


# creating the instances
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



# awarding the lottery ticket, using random number generator to give the lottery ticket


id_list = list(details.keys())
item_list = list(details.values())
# enumerating the item_list as to reduce errors when displaying,
# when there are multiple customers with the same amount of items in their basket


for ind, items in enumerate(item_list, start=1):
    if items < 10:
        print(f"Customer {ind} ---> Items in basket: {items}, time to process = {items * 6} seconds")
    # using a randome number generator to produce the lottery ticket
    else:
        winner = random.randint(1, 2)
        lottery_status = "has NOT won a lottery ticket"

        if winner == 1:
            lottery_status = "has won a lottery ticket"

        print(f"Customer {ind} --> Items in basket: {items}, {lottery_status}, time to process at self checkout lane = {items * 4} seconds")


# creating a function that adds customers to the queue every 30 seconds



#####################################################################################################################################################

# lanes sections


from abc import ABC, abstractmethod


# making the parent class for lanes, wich has 2 abstract classes that decide how to add a customer and if the lane is full

# class used to reassign values, made with help of AI
class Customers:
    def __init__(self, customer_id, items):
        self.id = customer_id
        self.items = items
        self.will_process = None

class Lane:
    def __init__(self, lane_type, capacity):
        self.lane_type = lane_type
        self.capacity = capacity
        self.queue = []
        self.serv = []
        self.reg = []
# this function was made with the help of AI
    def is_full(self):
        return len(self.queue) >= self.capacity

    @abstractmethod
    def add_customer(self):
        pass

    @abstractmethod
    def process_customer(self):
        pass

    @abstractmethod
    def display(self):
        pass

class Service_lane(Lane):
    def __init__(self, lane_type, capacity):
        super().__init__(lane_type, capacity)

# stating the conditions for which the customer can join the selfservice lane
    def add_customer(self, customer):
        lane_serv = []
        if not self.is_full() and customer.items < 10:
            self.serv.append(customer)
            return True
        else:
            return False

    def process_customer(self):
        for customer in self.serv:
            checkout_time = datetime.datetime.now() + datetime.timedelta(seconds=customer.items * 6)
            print(
                f"Processing Customer {customer.id} at {self.lane_type} Lane. Checkout time: {checkout_time} seconds")

            customer.will_process = checkout_time
            print(customer.will_process)

        for customer in self.serv[:8]:
            if datetime.datetime.now() > customer.will_process:
                self.serv.remove(customer)
                print(f"Customer {customer.id} processed and removed from Lane")
    def display(self):
        customers_str = " ".join(str(customer.id) for customer in self.serv)
        return f"{self.lane_type} Lane ({len(self.serv)}/{self.capacity}): {customers_str}"

class Regular_lane(Lane):
    def __init__(self, lane_type, capacity):
        super().__init__(lane_type, capacity)

    def add_customer(self):
        if not self.is_full():
            self.reg.append(customer)
            return True
        else:
            return False

    def process_customer(self):
        for customer in self.reg:
            checkout_time = customer.items * 4
            print(f"Processing Customer {customer.id} at {self.lane_type} Lane. Checkout time: {checkout_time} seconds")
            # Simulating checkout time with time.sleep
            removing = datetime.datetime.now() + datetime.timedelta(seconds = checkout_time)
            customer.will_process = removing

            while customer in self.reg:
                for customer in self.reg:
                    if datetime.datetime.now() > removing:
                        self.reg.remove(customer)
                        print(f"{customer.id} has exited queue")


    def display(self):
        customers_str = " ".join(str(customer.id) for customer in self.reg)
        return f"{self.lane_type} Lane ({len(self.reg)}/{self.capacity}): {customers_str}"

# creating one service lane and 5 regular lanes

service_lane = Service_lane("Self-Checkout", 8)
regular_lanes = [Regular_lane("Regular", 5) for _ in range(5)]

for customer_id, items in details.items():
    customer = Customers(customer_id, items)

    # Try to add customer to the service lane
    if service_lane.add_customer(customer):
        print(f"Customer {customer_id} added to {service_lane.lane_type} Lane")
    else:
        # If service lane is full, add customer to one of the regular lanes
        for regular_lane in regular_lanes:
            if regular_lane.add_customer():
                print(f"Customer {customer_id} added to {regular_lane.lane_type} Lane")
                break

print(service_lane.display())
for regular_lane in regular_lanes:
    print(regular_lane.display())

# Process customers in lanes
service_lane.process_customer()

for regular_lane in regular_lanes:
    regular_lane.process_customer()

customers1.timefunc()
for _ in range(5):  # only 5 new customers can join the queue during this simulation
    customers1.oncoming_customers()
    time.sleep(30)

#######################################################################################################################

