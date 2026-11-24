import datetime
import time

x = max(3,2,1)
print(x)

my_list = []

def timer(my_list):
    for i in range(10):
        current_time = datetime.datetime.now()
        my_list.append(i)
        time.sleep(3)
        print(my_list)

if __name__ == "__main__":
    timer(my_list)


# use time delta