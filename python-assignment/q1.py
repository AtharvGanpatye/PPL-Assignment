
print("Man rides the boat. How can he cross the river with Tiger, Goat, Grass in minimum rounds ??\n")
print("NOTE : Tiger, Goat and Goat, Grass should not be on the shore at same time.\n")
print("NOTE : For no one in the boat, type : none.\n")
shore1 = ['tiger', 'goat', 'grass']
shore2 = []
set = ['tiger','goat', 'grass','none']
i = 2

def isvalid(n, shore1, shore2):
    l1 = ['goat', 'grass']
    l2 = ['goat', 'tiger']
    if n == 0:
        shore1 = sorted(shore1)
        if l1 == shore1 or l2 == shore1:
            return False
        else:
            return True
    else:
        shore2 = sorted(shore2)
        if l1 == shore2 or l2 == shore2:
            return False
        else:
            return True

while(len(shore2) != 3):
    if i%2 == 0:
        print("Shore 1")
    else:
        print("Shore 2")
    print(shore1,"\t",shore2)
    x = input("Enter the other member:\n")
    x = x.lower()
    if not(x in set):
        print("Invalid Input !")
        break
    elif x == 'none':
        if i%2 == 0:
            b = isvalid(0, shore1, shore2)
            if not b:
                print("Try Again !!")
                break
        else:
            b = isvalid(1, shore1, shore2)
            if not b:
                print("Try Again !")
                break
    elif i%2 == 0:
        shore1.remove(x)
        shore2.append(x)
        b = isvalid(0, shore1, shore2)
        if not b:
            print("Try Again !!")
            break
    else:
        shore1.append(x)
        shore2.remove(x)
        b = isvalid(1, shore1, shore2)
        if not b:
            print("Try Again !!")
            break
    i = i + 1
if(len(shore2) == 3):
    print(shore1,"\t",shore2)
    print("\nCorrect !!")