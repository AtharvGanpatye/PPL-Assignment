L = input("Enter the list of page numbers :\n")
L = L.split(',')
for i in range(len(L)):
	L[i] = int(L[i])
L2 = []
for i in range(1, 27):
    if i in L:
        continue
    else:
        L2.append(i)
print("Missing Elements : ",sorted(L2))
# 2,3,4,5,8,10,13,15,17,21