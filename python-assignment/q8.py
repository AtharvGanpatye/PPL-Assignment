from sympy import Matrix
from sympy import init_printing
L = []
print("LU Decomposition of n*n matrix.")
n = int(input("Enter value of n :\n"))
print("Enter the matrix elements :")
for i in range(n):
    l = []
    for j in range(n):
        x = int(input())
        l.append(x)
    L.append(l)
A = Matrix(L)
L, U, _ = A.LUdecomposition()
print("L = ", L, "\n")
print("U = ", U)
