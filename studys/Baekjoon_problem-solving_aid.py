'''
문제 : 18108
a = input()
b = int(a) - 543
print(b)

문제 : 10430
a, b, c = map(int,(input().split()))
A = (a + b) % c
print(A)
B = ((a % c) + (b % c)) % c
print(B)
C = (a * b) % c
print(C)
D = ((a % c) * (b % c)) % c
print(D)

문제 : 2884
a, b = map(int,input().split())
if b < 45:
    if a == 0 :
        a = 23
        b = b + 60
    else :
        a = a - 1
        b = b + 60
print(a, b-45)

문제 : 2525
시작하는 시각과 필요한 시간이 분단위로 주어졌을 떄, 끝나는 시각을 계산하는 프로그램을 작성하시오.

a, b = map(int,input().split())
c = int(input())
a = a + (c // 60)
b = b + (c % 60)

if b >=60:
    a = a + 1
    b = b - 60
if a >= 24:
    a = a - 24
    
print(a, b)

문제 : 2480 주사위 던지기
같은 눈이 3개 나오면 10000+ 같은 눈*1000
같은 눈이 2개만 나오면 1000+ 같은 눈*100
모두 다른 눈 그중 가장 큰눈 * 100

a, b, c = map(int,input().split())
if a == b == c:
    print(10000 +  a * 1000)
elif a == b or b == c or a == c:
    print(1000 + a * 100) if a == c else print(1000 + b * 100)
else:
    print(max(a, b, c)*100)

문제 : 2739 구구단

a = int(input())
for b in range(1,10):
    print(a,'*', b, '=', a*b)    

문제 : 10950
두 정수 a, b를 입력받은 다음, a+b를 출력하는 프로그램을 작성하시오

t = int(input())
for i in range(t):     #i는 순서를 나타냄
    a, b = map(int,input().split())
    print(a + b)

문제 : 8393
n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오

n = int(input())
t = 0 # t 초기화
for i in range(1, n + 1):
    t += i
print(t)

문제 : 25304
구매한 각 물건의 가격과 개수, 구매한 물건들의 총 금액 을 보고 구매한 물건의 가격과 개수로
계산한 총 금액이 영수증에 적힌 총 금액과 일치하는지 검사해보자.

t = int(input()) # 구매한 물건 총 금액
n = int(input()) # 구매한 물건 총 개수
s = 0 # 총 금액
for i in range(1, n + 1): 
    a, b = map(int,input().split())
    s += a*b 
if t == s:  # 총 금액과 구매 한 물건 총금액 일치 하는지
    print('Yes')
else:
    print('No')


문제 : 25314
 long lnt 4바이트까지, long long int 8바이트 까지 저장. 

n = int(input())
answer = 'int' # 뒤에 int를 붙인다.
for i in range(n // 4): # 범위는 n 을 4로 나눈 몫이다.
    answer = 'long ' + answer # n을 4로 나눈 몫의 값 만큼 long 를 추가함.
print(answer) # 출력시엔 long int로 출력


문제 : 15552
 input 대신 sys.stdin.readline 을 사용할 수 있다. 단, 맨 끝의 개행문자까지 같이 입력받기 때문에 문자열을 저장하고 싶을 경우 .rstrip
 때문에 문자열을 저장하고 싶을 경우 .rstrip을 추가한다.

import sys # import : 다른 모듈에서 (sys) 값을 가져온다. 

n = int(input())
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)


문제 : 11021
두 정수 a, b 를 입력받은 다음, a + b 를 출력하는 프로그램을 작성하시오.

n = int(input())
for i in range(1,n+ 1):
    a, b = map(int,input().split())
    s = (f"Case #{i}:") # "" 사용하는거 잊지 않기.
    print(s ,a + b)

문제 11022
두 정수 a와 b를 입력받은 다음, a + b 를 출력하는 프로그램을 작성하시오

n = int(input())
for i in range(1, n + 1):
    a, b = map(int,input().split())
    c = a + b
    print(f"Case #{i}: {a} + {b} = {c}")
    
문제 2438
첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제
n = int(input())
for i in range(1, 1+ n):
    print("*" * i ) # *을 i 만큼 곱한것(ex : i = 2, **. i = 3, *** ) 문자열에서 *은 문자를 n 번 반복하라는 소리이다.
      
문제 2439
첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번쨰 줄에는 별 N개를 찍는 문제. 하지만, 오른쪽을 기준으로 정렬한 별을 출력하시오

n = int(input())
for i in range(1, 1 + n):
    print(' ' * (n - i) + "*" * i)

문제 10952
두 정수 a, b를 입력받은 다음, a + b를 출력하는 프로그램을 작성하시오.

while 1: # while을 사용하여 계속 반복되게 한후 시작
    a, b = map(int,input().split())
    if (a == 0 and b == 0): # a와 b가 0일때 
        break # 멈춤
    else:
        print(a + b) # 그 외의 경우에는 출력

문제 10951
두 정수 a 와b를 입력받은 다음, a + b를 출력하는 프로그램을 작성하시오

while True:
    try:
        a, b = map(int,input().split())
        print(a + b)
    except:
        break 
    패스 너무 빨리 나온 문제

문제 2588
세자리수 * 세자리수

a = int(input())
b = input()

print(a * int(b[2]))
print(a * int(b[1]))
print(a * int(b[0]))
print(a * int(b))

문제 11382
꼬마 정민이는 이제 a + b 정도는 쉽게 계산할 수 있다. 이제 a + b + c 는?

a, b, c = map(int,input().split())
print(a + b + c)

문제 10171
고양이를 출력하시오

print("\\    /\\")
print(" )  ( ')")
print("(  /  )")
print(" \\(__)|")

문제 10172
개를 출력하시오

print("|\\_/|")
print("|q p|   /}")
print('( 0 )"""\\') #""을 연속해서 넣어 그대로 출력하고 싶으면 바깥 ""을 ''로 변경해서 입력한다.
print('|"^"`    |')
print("||_/=\\\__|")

문제 10807
총 n 개의 정수가 주어졌을 때, 정수 v가 몇 개인지 구하는 프로그램을 작성하시오

n = input()
n_list = list(map(int,input().split())) # list를 사용해 목록을 만들고 목록 내용은 입력값을 차례대로 들어가게 
# map(int,input(split())) 을 사용한다
v = int(input())
# v 는 갯수를 세고 싶은 값을 입력하고 출력할 때 count를 사용한다.
print(n_list.count(v))

문제 10871
정수 n개로 이루어진 수열 a와 정수 x가 주어진다. 이때, a에서 x보다 작은 수를 모두 출력하는 프로그램을 작성하시오.

n, x = map(int,input().split()) # n과 x의 수 입력
a = list(map(int,input().split())) # a의 목록을 입력. list는 목록을 작성할 때 사용된다.
for i in range(n): # 범위 n 을 설정
    if a[i] < x: # 만약 a에 입력한 수 중, i 번째 수가 x 보다 작은지 판별
        print(a[i], end = " ") # 작은 수를 출력하고 " "을 양끝에 입력하고 프로그램 중지.

문제 10818
n개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.


n = int(input()) # 정수의 개수를 입력. 의미 없음 다른데 쓰이는 게 없음
a = list(map(int,input().split())) # 정수를 입력받음
print(min(a),max(a)) # 정수 들 중 최소값과 최대값을 구함.

문제 2562
9개의 서로다른 자연수 주어질 때, 최댓값 찾고 몇 번째 수인지 구하는 프로그램 작성하시오
numbers = [] # 변수 지정
for i in range(9): # 9개 정수 입력하는 범위 설정
    i = int(input()) # i 의 값은 정수 입력값이다.
    numbers.append(i) # 마지막에 인덱스 값을 추가한다.

print(max(numbers)) # 가장 큰수 
print(numbers.index(max(numbers)) + 1) # 그 수가 몇번째에 있는지
'''

   