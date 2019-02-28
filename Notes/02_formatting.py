import random

for i in range(10):
    x = random.randrange(1, 101)
    y = random.randrange(1, 101)
    z = round(x / y, 2)
    print(z)

# format method
a = 3.1415926
print("My number is: {:.2f}".format(a)) # . means decimal, 2 means number of places, f means float

b = 32873
print("b is: {:15}".format(b))

for i in range(20):
    c = random.randrange(10000)
    print("{:5}".format(c))

# other stuff it can do
# :spaceholder+justification+sign+width+commas?+precision+datatype+notation

for i in range(20):
    c = random.randrange(100000)
    print("{:>10}".format(c))   # left is <, center is ^, right is >

for i in range(20):
    c = random.randrange(-100000, 100000)
    print("{:+}".format(c))  # sign (+, -)

for i in range(20):
    c = random.randrange(10000)
    print("{:11,}".format(c)) # commas or not

for i in range(20):
    c = random.random() # random float from 0 to 1
    print("{:11.2f}".format(c)) # precision to 2 decimals

for i in range(20):
    c = random.random() # random float from 0 to 1
    print("{:11f}".format(c)) # datatype -- can't force, but can convert between two if applicable (f [float], d [int],
                              # b [binary])

for i in range(20):
    c = random.random()  # random float from 0 to 1
    print("{:5%}".format(c))  # % or e (scientific notation)

for i in range(20):
    c = random.randrange(-1000, 1000) * random.random()
    print("${:>12.2f}".format(c))

for i in range(20):
    x = random.random()
    y = random.randrange(1000)
    print("x is: {:.2f}\ny is {}".format(x, y))

for i in range(20):
    x = random.random()
    y = random.randrange(1000)
    print()
    print("y is: {1:3}\nx is {0:}\ny is: {1:2}".format(x, y))    # index to left of colon
