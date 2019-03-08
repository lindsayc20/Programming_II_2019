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