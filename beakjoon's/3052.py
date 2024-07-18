# 문제 3052
# 두 자연수 A와 B가 있을 때, A%B는 A를 B로 나눈 나머지이다. 예를 들어 7, 14, 27, 38을 나눈 나머지는 1,2,0,2 이다.
# 수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다. 그 다음 서로 다른 값이 몇 개 있는지 출력한느 프로그램 작성
# 첫째 줄부터 열번째 줄 까지 숫자가 한 줄에 하나씩 주어진다. 이 숫자는 1,000보다 작거나 같고, 음이 아닌 정수이다.

input_list = []
last_list = []

for j in range(10):
    input_num = int(input())
    input_list.append(input_num)
    
for num in input_list:
    last_num = num % 42 
    if last_num not in last_list:
        last_list.append(last_num)
        
print(len(last_list))