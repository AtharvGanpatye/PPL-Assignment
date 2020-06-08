# PRINTS FIRST 10 NUMBERS OF GP. FIRST TERM AND RATIO IS INPUT FROM USER.
a = int(input("Enter first term in GP\n"))
x = int(input("Enter common ratio in GP\n"))
l = []
for i in range(10):
    l.append(a * (x**i))
print("Fisrt 10 numbers of G.P are ")
print(l)
