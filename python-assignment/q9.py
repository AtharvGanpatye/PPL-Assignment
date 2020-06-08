# FIRST 10 HARMONIC DIVISOR NUMBERS / ORE NUMBERS.
#n = input("Enter a number\n")
def divisor(n):
    l = []
    for i in range(1, int(n ** 0.5) + 1):
        # FOR DIVISIORS, RUN THE LOOP TILL SQRT(N) BASED ON THAT INSERT IN LIST
        if n % i == 0:
            if n / i == i:
                l.append(i)
            else:
                l.append(i)
                l.append(n / i)
    return l

def HM(n):
    list = divisor(n)
    size = len(list)
    sum = 0
    for i in range(0, size):
        sum = sum + n / list[i]
    sum = float(sum) / n
    m = size / sum
    if m - int(m) != 0:
        return False
    else:
        return True
L = []
i = 1
while(len(L) < 10):
    if(HM(i)):
        L.append(i)
    i = i + 1
print("First 10 Harmonic Divisors are:")
for i in L : print(i)
