# sorting
import random

# swap values

a = 1
b = 2
print(a, b)

temp = a # store before we destroy
a = b
b = temp

print(a, b)

# the pythonic way
a, b = b, a
print(a, b)

# make a random list of 100 numbers with value 1 to 99
number_list = [random.randrange(1, 100) for x in range(100)]
print(number_list)

def selection_sort(my_list):
    for cur_pos in range(len(my_list)):
        min_pos = cur_pos
        for scan_pos in range(cur_pos + 1, len(my_list)):
            if my_list[scan_pos] < my_list[min_pos]:
                min_pos = scan_pos
        my_list[cur_pos], my_list[min_pos] = my_list[min_pos], my_list[cur_pos]
    print(my_list)

selection_sort(number_list)

# insertion sort

number_list = [random.randrange(1, 100) for x in range(100)]
print(number_list)

for key_pos in range(1, len(number_list)):
    key_val = number_list[key_pos]
    scan_pos = key_pos - 1 # look to dancer on the left
    while (scan_pos >= 0) and (number_list[scan_pos] > key_val):
        number_list[scan_pos + 1] = number_list[scan_pos]
        scan_pos -= 1
    number_list[scan_pos + 1] = key_val

print(number_list)

# Sorting in real life with Python
rand_list = [random.randrange(1, 100) for x in range(100)]
print(rand_list)

# sort method (sorts in place; changes list directly)
start_time = time.perf_counter()
rand_list.sort()
print(rand_list)
print("Total time", time.perf_counter() - start_time)


# sorted function (returns a sorted list)
rand_list = [random.randrange(1, 100) for x in range(100)]
print(rand_list)

rand_list2 = sorted(rand_list)  # capture the returned list
print(rand_list2)


#  optional parameters
print("Hello", end="")  # end="" is an optional parameter that has a default value of "\n"
print("World")

def hello(name, time="1:00PM"):
    print("Hello", name, "it is now", time)

hello("Karen", time="2:00PM")


# Lambda Function (anonymous function on a single line)
double_me = lambda x: 2 * x  # lambda parameter: return
print(double_me(10))


# Sorted function using a lambda function
# optional key parameter is what you are using to sort the list.
my_list = ["Abel", "evan", "Zed", "Piper", "len", "Jenny", "Kip"]
my_sort = sorted(my_list, key=lambda x: x.upper())
print(my_sort)

my_list.append("Alex")
my_sort = sorted(my_list, key=lambda x: len(x))
print(my_sort)

my_list = [["Abel", 8], ["evan", 10], ["Zed", 11], ["Piper", 17], ["len", 16], ["Jenny", 28], ["Kip", 80]]
my_sort = sorted(my_list, key=lambda x: x[1])
print(my_sort)
