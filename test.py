last_name = "Guerrero"
first_name = "Jessie"
age = 30
price = 100.99
found = False


print(first_name)
print(last_name)
print(first_name + " " + last_name)

print(age / 2)

print(first_name + str(age))


#if and else

if age < 100:
    print("dont worry you are young")
    print("inside the f")

elif age == 100:
    print('great')
else:
    print('sorry your old')

print("outside the if")


#functions

def say_hello():
 print("hello from fn")
 say_hello()
 say_hello()
 say_hello()



def greet(name):
 print("Hello" + name)
   #call this function  
 greet(jessie)
 greet(jessie)