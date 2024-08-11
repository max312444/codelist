# 문제 5073

while True:
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        break
    if a + b + c - max((a, b, c)) <= max((a, b, c)):
        print("Invalid")
    elif a == b == c:
        print("Equilateral")
    elif a == b or b == c or a == c:
        print("Isosceles")
    elif a != b != c:
        print("Scalene")