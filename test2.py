#global var


#functions
def sum(num1, num2):

    result = num1 + num2
    print(result)


def divition(num1, num2):
    result = num1 / num2
    print(result)
    if num2 == 0:
        print("cant divide by zero")


def print_numbers():
    nums = [12,2,25,23,67,36,3,46,785,46,]
    for n in nums:
     print(nums)
    if n < 50:
     print(n)

def print_greater(num1, num2):
    if num1 > num2:
     print(num1)
    else:
     print(num2)


def print_list():
    names =['jason', 'jessie']

    #add an element
    names.append('jesenia')
    names.append('jes')
    

   # read
    print(names[1])
    print(names[0])

    if 'sergio' not in names:
      names.append('sergio')

    print(names)

#call function
sum(21, 21)
sum(-2, 345)
sum(123155, 46566)



divition(100, 10)
divition(0, 10)
divition(10, 2)


print("-------------------")
print_numbers()

print_greater(3, 7)
print_greater(12, 10)
print_greater(9, 9)