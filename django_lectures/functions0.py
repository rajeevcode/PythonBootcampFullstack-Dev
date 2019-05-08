def my_func(param1='default'):

    """
    THIS IS THE DOCSTRING
    """
    print("my first python function!".format(param1))

my_func()

# documentation screen
def hello():
    print("hello")

hello()
# result
def hi():
    return "Hi!"

result = hi()

print(result)

# add numbers
def addNum(num1,num2):
    if type(num1)==type(num2)==type(10):
        return num1+num2
    else:
        return "Sorry,I need integers!"

result = addNum("2","3")
print(result)
print(type(result))

#Lambda or anaymous Expression - break down of a function
mylist = [1,2,3,4,5,6,7,8]

evens = filter(lambda num:num%2 == 0,mylist)
print(list(evens))


# Filter
mylist = [1,2,3,4,5,6,7,8]

def even_bool(num):
    return num%2 == 0

evens = filter(even_bool,mylist)
print(evens)
print(list(evens))

#common used functions
tweet = "Go Sports! #Sports"
result = tweet.split('#')
print(tweet)

#in operator
print('x' in [1,2,3])
