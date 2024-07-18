# 문제 : 10430
a, b, c = map(int,(input().split()))
A = (a + b) % c
print(A)
B = ((a % c) + (b % c)) % c
print(B)
C = (a * b) % c
print(C)
D = ((a % c) * (b % c)) % c
print(D)
