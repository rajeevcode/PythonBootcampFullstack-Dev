def arraycheck(nums):
    for i in range(len(nums)-2):
        if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
            return True
            return False


# slice
def stringBits(mystring):

    result = ""

    for i in range(len(mystring)):
        if i%2 == 0:
            result = result + mystring[i]
    return result

#stringBits
def end_other(a, b):
    a = a.lower()
    b = b.lower()

    #return (b.endswith(a)) or a.endswith(b))
    return a[1-(len(b)):] == b or a == b[-len(a):]

#characters

def doubleChar(mystring):

    result = ''
    for char in mystring:
        result += char*2
    return result

# problem 5
def no_teen_sum(a,b,c):

    return fix_teen(a) + fix_teen(b) + fix_teen(c)

def fix_teen(n):

    if n[13,14,17,18,19]:
        return 0

        return n

#varianle count
def count_evens(nums):
    count = 0

    for element in nums:
        if element % 2 == 0:
            count += 1
    return count
