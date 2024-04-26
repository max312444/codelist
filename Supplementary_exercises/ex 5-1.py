# 문제 5-1 세 수의 비교 - 유사성과 차이점 찾기
# 사용자로부터 세 개의 정수를 입력 받는다.
# 세 수의 관계에 따라 다음과 같이 출력한다.
# 1. 모든 수가 같으면, "모든 수가 같습니다.", 
# 2. 두 수가 같으면, "두 수가 같습니다."와 같은 두 수도 출력
# 3. 모든 수가 다르면,"모든 수가 다릅니다. 가장 큰 수는 x입니다."x는 가장 큰 수

value1 = int(input("첫 번째 수 입력: "))
value2 = int(input("두 번째 수 입력: "))
value3 = int(input("세 번째 수 입력: "))

x = value1 # if 문으로 최댓 값 구하는 식(변수가 3개일 때)
if x < value2:
    x = value2
    
if x < value3:
    x = value3

if value1 == value2 == value3: # 세 수가 모두 같을 때
    print("모든 수가 같습니다.")
elif value1 == value2 or value1 == value3 or value2 == value3: # 세 수 중 두개만 같을 때
    if value1 == value2: # value1과 value2가 같을 때
        print(f"두 수가 같습니다.{value1}와 {value2}")
    elif value1 == value3:# value1과 value3가 같을 때
        print(f"두 수가 같습니다.{value1}와 {value3}")
    else: # value2와 value3가 같을 때
        print(f"두 수가 같습니다.{value2}와 {value3}")
else: # 모든 수가 다를 때 x는 가장 큰 수 (위에서 구하는 식 작성 완료)
    print(f"모든 수가 다릅니다. 가장 큰 수는 {x}입니다.")

