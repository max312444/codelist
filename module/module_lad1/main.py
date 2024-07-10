import utilities # 다른 파일로 정의한 것을 가져옴

def main(): # main 정의
    num1 = float(input("Enter the first number: ")) # 사용자 입력 1
    num2 = float(input("Enter the first number: ")) # 사용자 입력 2
    operation = input("Choose the operation (add, subtract, multiply, divide)") # 4개의 함수중에 하나 결정
    
    if operation == 'add': # 만약 고른게 add면 불러온 함수에서 add 실행
        result = utilities.add(num1, num2)
    elif operation == 'subtract': # 만약 고른게 subtract 이면 불러운 함수에서 subtract 실행
        result = utilities.subtract(num1, num2)
    elif operation == 'multiply':# 만약 고른게 multiply이면 불러온 함수에서 multiply 실행
        result = utilities.multiply(num1, num2)
    elif operation == 'divide': # 만약 고른게 divide이면 불러온 함수에서 divide 실행
        result = utilities.divide(num1, num2)
    else: # 위 4개 중에 없는걸 결정하면 오류 메시지 출력후 정지
        print("Invalid oprtation")
        return
    # 실행한 값 출력
    print(f"The result is {result}")
# 만약 이름이 main이면 main함수 실행 아니면 실행안함
if __name__ == '__main__':
    main()