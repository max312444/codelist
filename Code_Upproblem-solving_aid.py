'''
# 문제 6049
# 정수 2개 입력받아 비교하기2

a, b = map(int,input().split())

if a == b:
    print("True")
else:
    print("False")

# 문제 6050
# 정수 2개 입력받아 비교하기3

a, b = map(int,input().split())

if a <= b:
    print("True")
else:
    print("False")

# 문제 6051
# 정수 2개 입력받아 비교하기4

a, b = map(int,input().split())

if a != b:
    print("True")
else:
    print("False")

# 문제 6052
# 정수 입력받아 참 거짓 평가하기

n = int(input())
print(bool(n))

# 문제 6053
# 참 거짓 바꾸기

a = bool(int(input()))
print(not a)

# 문제 6054
# 둘 다 참일 경우만 참 출력하기

a, b = input().split()
print(bool(int(a)) and bool(int(b)))

# 문제 6055
# 하나라도 참이면 참 출력하기

a, b = input().split()
print(bool(int(a)) or bool(int(b)))

# 문제 6056
# 참/거짓이 서로 다를 때에만 참 출력하기

a, b = input().split()
A = bool(int(a))
B = bool(int(b))
print((A and (not B)) or (B and (not A)))

# 문제 6057
# 참/거짓이 서로 같을 때에만 참 출력하기

a, b = input().split()

A = bool(int(a))
B = bool(int(b))
print((A and B) or ((not A) and (not B)))

# 문제 6058
# 둘 다 거짓일 경우만 참 출력하기

a, b = map(int,input().split())

A = bool(a)
B = bool(b)
print(not A and not B)
'''

# 문제 6059
# 비트단위로 not하며 출력하기
