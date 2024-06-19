# 코드를 짤때 일단 예외는 제외하고 먼저 요구사항에 맞게 출력되는 것 부터 시작한다.



def print_menu():
    width = 15
    print("-" * width)
    print("1. 구구단 출력")
    print("2. 삼각형 출력")
    print("3. 종료")
    print("-" * width)

def print_mul_table(): 
    while True:
        isValid = False
        input_value = input("출력할 단을 입력하세요: ")
        
        
        input_list = input_value.split("~")
        input_list = [int(value) for value in input_list]

        
        for value in input_list:
            if not (2 <= value <= 9):
                isValid = False
                break
            
        if isValid:
            break
                
            
        print("2~9 사이의 정수를 입력하세요")
        
        start = 2
        end = 5
        
        for dan in range(start, end + 1):
            for num in range(1, 10):
                print(f"{dan} X {num} = {dan * num}")
            print()
def print_triangel():
    row = 2
    
    
    
    
    
while True:   
    print_menu()

    input_value  = int(input("메뉴를 선택해주세요: "))

    if not (1 <= input_value <= 3):
        print("1에서 3사이의 정수를 입력해주세요")
        continue
    # 구구단 실행
    if input_value == 1:
        print_mul_table()
    # 삼각형 출력
    elif input_value == 2:
        print_triangel()
    # 프로그램 종료
    elif input_value == 3:
        print("종료")
        break