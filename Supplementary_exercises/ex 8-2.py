# 문제 8-2 사칙연산 계산기 - 전역변수와 지역변수 사용
# 사용자로부터 초기값(baseValue)을 입력받아 전역 변수로 선언
# 프로그램은 더하기 뺴기 곱하기 나누기 중 하나의 연산을 수행할 수 있음
# 사용자가 연산을 선택하고 숫자를 입력하면, selectOperaion() 함수에서 선택한 연산을 (baseValue)에 적용
# 나누기 연산에서 분모가 0일 경우, "에러: 0으로 나눌 수 없습니다."라는 메시지를 출력 - 이 경우 연산 결과 출력 안함
# 에러 메시지가 출력되지 않은 경우에만, 연산 결과를 출력
baseValue = float(input("기본값을 입력하세요: "))
print("1. 더하기")
print("2. 빼기")
print("3. 곱하기")
print("4. 나누기")
choice = int(input("선택:"))
inputValue = float(input("숫자 입력:"))

def selectOperation():
    global baseValue
if inputValue != 0:
    if choice == 1:    
        baseValue = baseValue + inputValue
        print("연산 결과: ",baseValue)
    elif choice == 2:
        baseValue = baseValue - inputValue
        print("연산 결과: ",baseValue)
    elif choice == 3:
        baseValue = baseValue * inputValue
        print("연산 결과: ",baseValue)
    elif choice == 4:
        baseValue = baseValue / inputValue
        print("연산 결과: ", baseValue)
    else:
        print(" ")
else:
    print("에러: 0으로 나눌 수 없습니다.")
selectOperation()