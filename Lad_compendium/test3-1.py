# 1. for문을 사용하여 다섯 개의 정수를 입력받아 합계의 평균을 출력하는 프로그램 작성
numbers = [] # 다섯 개의 정수 리스트

for i in range(5): # 범위 지정
    num = int(input(f"{i+1}번째 입력:")) # 입력 식 생성 - 5번 출력해야하고 출력하면 할수록 n번째 의 n이 1씩 커져야함
    numbers.append(num) # numbers 리스트에 추가

total = sum(numbers) # 합계 구하는 식

average = float(total // 5) # 평균 구하는 식 - 이때 평균은 소수점이 나올 수 있으니 float 으로 지정한다. 

print("합계 :",total)
print("평균 :", average)