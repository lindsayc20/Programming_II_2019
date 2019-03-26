# plotting (with matplotlib)

import matplotlib.pyplot as plt
import random

plt.figure(1)   # create a new window

plt.plot([1, 2, 4, 4])    # plots y against the index
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])    #plot(x_data, y_data)

plt.figure(2)

x1 = [x for x in range(1, 101)]
y1 = [y ** 2 for y in x1]

plt.plot(x1, y1)

x2 = [x for x in range(1, 101)]
y2 = [random.randrange(1000) for y in range(100)]

plt.plot(x2, y2, color='green', marker='o', markersize=10, linestyle='-')

# title axes label unit numbers key
plt.xlabel('time (seconds)')
plt.ylabel('intensity(dB)')
plt.title('Example Plot')
plt.axis([0, 50, 0, 1000])    # xmin, xmax, ymin, ymax

# plt.show()

import csv
import matplotlib.pyplot as plt

with open("data/Libraries_-_2018_Visitors_by_Location.csv") as f:
    reader = csv.reader(f)   # make a reader object to pull in the data
    data = list(reader)     # cast the reader as a list

print(data)
header = data.pop(0)
print(header)
print(data)

library_names = [x[0] for x in data]
print(library_names)

monthly_data = [x[1:-1] for x in data]
print(monthly_data)

print(library_names)

lp_data = monthly_data[library_names.index('Lincoln Park')]
print(lp_data)

try:
    lp_data = [int(x) for x in lp_data]
except:
    print("could not convert the data val to int")

print(lp_data)

months = [x for x in header[1:-1]]

plt.figure(3, tight_layout=True)
plt.axis([0, 12, 0, 18000])
plt.plot(lp_data)
month_numbers = [x for x in range(12)]
plt.xticks(month_numbers, months, rotation=45)    # puts text on axis
plt.show()

# Let's plots every library YTD attendance as a bar graph

plt.figure(4, tight_layout = True) # makes sure the text doesn't run off the screen

# x-axis list is library names
library_numbers = [x for x in range(len(library_names))]
print(library_numbers)

# y-axis list is the "Year to Date" attendances
try:
    library_ytd = [int(x[-1]) for x in data]
except:
    print("Could not convert to integer")

plt.bar(library_numbers, library_ytd, 1, alpha=1, color='white', edgecolor='hotpink', linewidth = 1)
plt.xticks(library_numbers, library_names, rotation=90, fontsize=6)

plt.xlabel("Chicago Library Branch")
plt.ylabel("Total Visitors")
plt.title("Chicago Public Library Visitors 2018")
plt.legend()

plt.show()