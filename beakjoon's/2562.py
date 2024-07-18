# 문제 2562
# 9개의 서로다른 자연수 주어질 때, 최댓값 찾고 몇 번째 수인지 구하는 프로그램 작성하시오
numbers = [] # 변수 지정
for i in range(9): # 9개 정수 입력하는 범위 설정
    i = int(input()) # i 의 값은 정수 입력값이다.
    numbers.append(i) # 마지막에 인덱스 값을 추가한다.

print(max(numbers)) # 가장 큰수 
print(numbers.index(max(numbers)) + 1) # 그 수가 몇번째에 있는지