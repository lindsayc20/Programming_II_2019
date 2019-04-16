# a review of classes

# TO DO
# make a person class
# create an instance of the person class
# give the object attributes
# change the attributes using dot notation
# use a constructor to assign attributes
# make other methods
# make a child class and show inheritance

class Person():
    # class attributes
    age = 0
    name = "Doe"
    apples = 2

    def __init__(self, name):
        # automatically runs when you create a new instance
        self.name = name
        print(name, "is added!")

    def say_hi(me):
        print(me.name, "says hi!")

person1 = Person("Ava")  # makes an instance of the class
person1.say_hi()
person1.age = 10    # changes attribute using dot notation
print(person1.age)  # attribute of the instance
print(Person.age)   # attribute of the class
person1.x=100   # making a new attribute
print(person1.x)


class Student(Person):
    def give_apple(self, teacher):
        if self.apples > 0:
            self.apples -= 1
            teacher.apples += 1
            print(self.name, "gives an apple to", teacher.name)

class Teacher(Person):
    def __init__(self, name):
        super().__init__(name)
        self.apples = 0
        print("A new teacher has been added.")

person2 = Student("Bob")
print(person2.age)
person2.say_hi() # person2 inherited all methods from Person class

person3 = Teacher("Cal")

person2.give_apple(person3)