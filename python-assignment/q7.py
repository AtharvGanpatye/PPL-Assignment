# Angstrong number = sum of power of each number to the number of digits in it.
m = int(input("Enter maximum number\n"))
L = []
def digits(n):
    l = []
    while(int(n / 10) != 0):
        l.append(n%10)
        n = (n/10)
        n = int(n)
    if(int(n/10) == 0):
        l.append(int(n))
    return l

for i in range(m + 1):
    l = digits(i)
    n = len(l)
    sum = 0
    for j in range(len(l)):
        sum = sum + (l[j] ** n)
    if sum == i:
        L.append(i)
print(L)

