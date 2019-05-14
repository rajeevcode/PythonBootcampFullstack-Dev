    #Inhertiance
class Animal():

    def __init__(self):
        print("ANIMAL CREATED")

    def whoAmI(self):
        print("EATING")

    def eat(self):
        print("EATING")

mya = Animal()
mya.whoAmI()
mya.eat()


class Dog(Animal):

    def __init__(self):
        # Animal.__init__(self)
        print("DOG CREATED")

    def bark(self):
        print("WOOF")

    def eat(self):
        print("DOG EATING")

mydog = Dog()
mydog.whoAmI()
mydog.eat()
mydog.bark()

#Special Methods

class Book():
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        # return "hello"
        return "Title: {}, Author:{}, Pages:{}".format(self.title,self.author,self.pages)

    def _len_(self):
        return self.pages

    def _del_(self):
        print("a book is destroyed")

b =  Book("Python","Jose",200)
print(b)

del b

# print(len(b))
# mylist = [1,2,3]
# print(mylist)
