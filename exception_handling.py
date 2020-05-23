#KEYBOARD INTERRUPT ERROR
def function():
     try:
         x = int(input("Enter a number\n"))
         print(x ** 3)
     except KeyboardInterrupt:
         print("\nKeyboard Interrupt detected.")

try:
	x = input("Enter Ctrl + C to interrupt OR Enter anything :\n")

except KeyboardInterrupt:
	print("\nKeyboardInterrupt Detected.")

else:
	print("KeyboardInterrupt didn't occur.")

########################################################################################

#STANDARD ERROR

#1) ZERO DIVISION ERROR
# DIVISION BY ZERO
def divide():
    try:
        print("Division of 2 numbers:")
        x = int(input("Enter first number\n"))
        y = int(input("Enter second number\n"))
        z = x / y
    except ZeroDivisionError:
        print("Division by zero not possible !!!")
    else:
        print(z)


########################################################################################

#2) OVERFLOW ERROR
# RESULT TOO BIG TO STORE
def expo():
    import math
    try:
        x = int(input("Enter a number\n"))
        y = math.exp(x)
    except OverflowError:
        print("Number too large to store !!")
    else:
        print(y)

########################################################################################

#3) ASSERTION ERROR
# RAISED WHEN A != B
try:
    a = 100
    b = "DataCamp"
    assert a == b
except AssertionError:
    print ("Assertion Exception Raised.")
else:
    print ("Success, no error!")

########################################################################################

#4) ATTRIBUTE ERROR
# RAISED WHEN ATTRIBUTE DOESN'T EXIST IN CLASS
class animal():
    legs = 4
    tail = 1
    species = "Tiger"

try:
    x = animal()
    print(x.legs)
    print(x.color)
except AttributeError:
    print("This Attribute doesn't exist")

########################################################################################

#5) IMPORT ERROR
# WHEN IT IS UNABLE TO LOAD THE MODULE / PACKAGE
try:
    import tensorflow
except:
    print("Unable to import the module.")
########################################################################################

#6) INDEX ERROR
# INDEX OUT OF RANGE
try :
    l = ['a','t','h','a','r','v']
    print(l[6])
except IndexError:
    print("Array index out of range.")

########################################################################################

#7) NAME ERROR
# WHEN THE NAME OF A VARIABLE IS NOT FOUND
try :
    print(new_var)
except NameError:
    print("Variable not declared anywhere before.")

########################################################################################

#8) TYPE ERROR
# OPERATION ON DIFFERENT DATA TYPES
try:
    x = 5
    y = "COEP"
    z = x + y
except TypeError:
    print("Operation on different types")
else:
    print("Success !!")

########################################################################################

# 9) VALUE ERROR
# INVALID CONVERSION OF DATA TYPES
try :
    x = int("Atharv")
except ValueError:
    print("Could not convert \"Atharv\" to int.")
else:
    print(x)

########################################################################################
