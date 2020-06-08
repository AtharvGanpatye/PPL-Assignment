#max = input("Enter maximum value\n")
#Amicable Numbers
def sum_of_divisors(n):
    l = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            if n / i == i:
                l.append(i)
            else:
                l.append(i)
                l.append(n / i)
    return sum(l) - n

L = []
num1 = 1
while(len(L) < 10):
    num2 = sum_of_divisors(num1)
    if( num1 < num2 and num1 == sum_of_divisors(num2) ):
        a = (num1, num2)
        L.append(a)
    num1 = num1 + 1
print(L)
