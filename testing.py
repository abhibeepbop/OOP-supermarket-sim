import datetime
import random
import time

customer_num = random.randint(1,10)
items_num = random.randint(1,30)

#variables for checkout time
self_time = 4
cashier_time = 6
total_time = 0

initial = {}
details = {}
#print(customer_num)
class Customers:
    def __init__(self):
        self.initialnumber = customer_num
        self.items = random.randint(1,30)

# creating a function so that the inital number of custmoers are added to a dictionary, where the key is the customer id
# and the value is the number of items in their basket.
    def detailsfunc(self):
        for i in range(1,self.initialnumber):
            id = i
            b_items = random.randint(1,30)
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

#if customerid in details:
   # print(f"customer {customerid} has {details[customerid]} items")

#checkout time for each lane


# calculating the total time taken to checkout all the customers in a line, only did for self checkout.
for _ in details.values():
    time_taken = _ * self_time
    total_time = total_time + time_taken

print("time taken for checkout = ",total_time, "seconds")


#cashiertime = 4
#total_cashiertime = 4 * details.values()
#time.sleep(total_cashiertime)

#processing time (in self checkout lane for now)




# awarding the lottery ticket, using random number generator to give the lottery ticket


id_list = list(details.keys())
item_list = list(details.values())



for i in item_list:
    if i < 10:
        print(f"customer {item_list.index(i) + 1} ---> items in basket: {i}")
    if i >= 10:
        winner = random.randint(1, 2)
        ind = item_list.index(i)
        #print("customer ",id_list[ind], "has >= than 10 items")
        if winner == 1:
            print(f"customer {id_list[ind]} --> items in basket : {item_list[ind]}, has won a lottery ticket, time to process at self checout lane = {customers1.timefunc()}")

        else:
            print(f"customer {id_list[ind]} --> items in basket : {item_list[ind]}, has  NOT won a lottery ticket, time to process at self checout lane = {customers1.timefunc()}")








    #ticketholder = details.get(10)
    #print(ticketholder)