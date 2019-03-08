# searching (program arcade games chapter 15)

# open a file to read
file = open('data/villains.txt', 'r')    # default is 'r' or read

for line in file:
    print(line.strip())     # strip removes leading and trailing spaces, /n, /t.

# make sure to close the file
file.close()


# to go through the file again, just reopen it
file = open('data/villains.txt', 'r')    # default is 'r' or read
for line in file:
    print("Hello,", line.strip())

file.close()

# open a file to append to it.
file = open('data/villains.txt', 'a')   # a for append

file.write("\nHitler")

file.close()

file = open('data/villains.txt', 'r')    # default is 'r' or read
for line in file:
    print("Hello,", line.strip())

file.close()

# open and write to a file (THIS OVERWRITES YOUR FILE)

file = open('data/oscars.txt', 'w')  # if it doesn't exist, it creates one

file.write("Best Picture: Green Book\n")
file.write("Makeup: Vice")

file.close()

# easier way to open a file and read it
with open('data/villains.txt') as f:
    # we opened villains to read and assigned it a name f
    for line in f:
        print(line.strip(), end ='!\n')

# to use the data, read it into a list
with open('data/villains.txt') as f:
    villain_list = [x.strip() for x in f]

print(villain_list)

# Linear Search
key = "Hitler" # what we are looking for
i = 0 # the index of the loop

while i < len(villain_list) and key != villain_list[i]:
    i += 1 # loop will stop when it finds "THE DEADLY RAVEN"

if i < len(villain_list):
    print("Found", key, "at position", i)
else:
    print("Could not find", key)

# Binary Search  --- he basically just played a game with us to demonstrate this point: https://www.geeksforgeeks.org/binary-search/
villain_list.sort()
print(villain_list)
key = "RENARD THE TORTURER" # "Save big money at Renard's" -Nicky Lerner

lower_bound = 0
upper_bound = len(villain_list) - 1
found = False
loops = 0 # counts the number of tries it took to find things
# with 2^7 loops, you can search 2^7 items in just 7 tries


# loop until we find it
while lower_bound <= upper_bound and not found:
    loops += 1
    middle_pos = (upper_bound + lower_bound) // 2
    if villain_list[middle_pos] < key:
        lower_bound = middle_pos + 1
    elif villain_list[middle_pos] > key:
        upper_bound = middle_pos - 1
    else:
        found = True
if found:
    print("\nFound", key, "at position", middle_pos, "with", loops, "loops")
else:
    print("Could not find", key, "after", loops, "loops")

# go here now: http://programarcadegames.com/index.php?chapter=lab_spell_check
# this project is due at some random nebulous point in the future like all of our assignments

import re
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)


villains = open("data/villains.txt")

for villain in villains:
    # print(villain.strip())
    words = split_line(villain.strip())
    for word in words:
        print(word)

def linear_search(key, dictionary):
    i = 0
    while i == (len(villains) - 1) and key!= villains[i]:
        i += 1

    if i < len(villains):
        print("Found", key, "at position", i)
    else:
        print("Could not find", key)

