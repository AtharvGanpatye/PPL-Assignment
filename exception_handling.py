
#KEYBOARD INTERRUPT ERROR
def keyboard_interrupt():
    try:
    	x = input("Enter Ctrl + C to interrupt OR Enter anything :\n")

    except KeyboardInterrupt:
    	print("\nKeyboardInterrupt Detected.")

    else:
    	print("KeyboardInterrupt didn't occur.")

keyboard_interrupt()
########################################################################################

#STANDARD ERRORS

#1) ZERO DIVISION ERROR
# DIVISION BY ZERO
def divide():
    try:
        print("Division of 2 numbers:")
        x = int(input("\nEnter first number\n"))
        y = int(input("\nEnter second number\n"))
        z = x / y
    except ZeroDivisionError:
        print("\nDivision by zero not possible !!!")
    else:
        print(z)

divide()
########################################################################################

#2) ATTRIBUTE ERROR
# RAISED WHEN ATTRIBUTE DOESN'T EXIST IN CLASS
class animal():
    legs = 4 
    tail = 1
    species = "Tiger"

def try_animal():
    try:
        print("In 'animal' class.")
        x = animal()
        print(x.legs, "legs, ", x.tail, "tail.")
        print(x.color)
    except AttributeError:
        print("\nThis Attribute doesn't exist")

try_animal()
########################################################################################

#3) IMPORT ERROR
# WHEN IT IS UNABLE TO LOAD THE MODULE / PACKAGE
def import_function():
    try:
        import beautifulsoup4
        
    except ModuleNotFoundError:
        print("\nUnable to import the module.")
    else:
        print("\nModule imported successfully !")

import_function()
########################################################################################

#4) INDEX ERROR
# INDEX OUT OF RANGE
def index():
    try :
        l = ['i','n','d','i','a']
        print(l[6])

    except IndexError:
        print("\nArray index out of range.")

index()
########################################################################################

#5) NAME ERROR
# WHEN THE NAME OF A VARIABLE IS NOT FOUND
def name_err():
    try :
        print(new_var)

    except NameError:
        print("\nVariable not declared anywhere before.")

name_err()
########################################################################################

#6) TYPE ERROR
# OPERATION ON DIFFERENT DATA TYPES
def type_err():
    try:
        x = 5
        y = "COEP"
        z = x + y

    except TypeError:
        print("\nOperation on different data types.")

    else:
        print("\nSuccess !!")

type_err()
########################################################################################

#7) VALUE ERROR
# INVALID CONVERSION OF DATA TYPES
def value_err():
    try :
        x = int("Pune")

    except ValueError:
        print("\nCould not convert \"Pune\" to int.")

    else:
        print(x)

#value_err()
########################################################################################

#8) IO ERROR
#   Error while reading and wrting in a file
def files():
    try:
        f = open("demo.txt", "r")

    except IOError:
        print("\nError : Can't open the file.")

    else:
        print("\nFile opened successfully.") 

files()
########################################################################################
