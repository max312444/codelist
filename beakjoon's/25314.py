# 문제 : 25314
#  long lnt 4바이트까지, long long int 8바이트 까지 저장. 

n = int(input())
answer = 'int' # 뒤에 int를 붙인다.
for i in range(n // 4): # 범위는 n 을 4로 나눈 몫이다.
    answer = 'long ' + answer # n을 4로 나눈 몫의 값 만큼 long 를 추가함.
print(answer) # 출력시엔 long int로 출력

