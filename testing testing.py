import datetime
import random
import time
import multiprocessing

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

        print(f"Customer {ind} --> Items in basket: {items}, {lottery_status}")





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

# this function (is_full) was made with the help of AI
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
        if not self.is_full() and customer.items < 10:
            self.queue.append(customer)
            return True
        else:
            return False


# checks out the self-service customers in groups of 8
    def process_customers(self):
        def process_customers(self):
            while self.queue:
                for customer in self.queue:
                    checkout_time = datetime.datetime.now() + datetime.timedelta(seconds=customer.items * 6)
                    print(
                        f"Processing Customer {customer.id} at {self.lane_type} Lane. Checkout time: {checkout_time} seconds")

                    customer.will_process = checkout_time
                    print(customer.will_process)

                for customer in self.queue[:]:
                    if datetime.datetime.now() > customer.will_process:
                        self.queue.remove(customer)
                        print(f"Customer {customer.id} processed and removed from {self.lane_type} Lane")


    def display(self):
        customers_str = " ".join(str(customer.id) for customer in self.queue)
        return f"{self.lane_type} Lane ({len(self.queue)}/{self.capacity}): {customers_str}"

class Regular_lane(Lane):
    def __init__(self, lane_type, capacity):
        super().__init__(lane_type, capacity)

    def add_customer(self):
        if not self.is_full():
            self.queue.append(customer)
            return True
        else:
            return False



    def process_customer(self):
        for customer in self.queue:
            checkout_time = datetime.datetime.now() + datetime.timedelta(seconds=customer.items * 6)
            print(
                f"Processing Customer {customer.id} at {self.lane_type} Lane. Checkout time: {checkout_time} seconds")

            customer.will_process = checkout_time
            print(customer.will_process)

        while True:
            for customer in self.queue:
                if datetime.datetime.now() > customer.will_process:
                    self.queue.remove(customer)
                    print(f"customer {customer.id} was removed from queue")
    def display(self):
        customers_str = " ".join(str(customer.id) for customer in self.queue)
        return f"{self.lane_type} Lane ({len(self.queue)}/{self.capacity}): {customers_str}"

# creating one service lane and 5 regular lanes

service_lane = Service_lane("Self-Checkout", 15)
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

for regular_lane in regular_lanes:
    print(regular_lane.display())

print(service_lane.display())

# Process customers in lanes

for regular_lane in regular_lanes:
    regular_lane.process_customer()

service_lane.process_customer()


