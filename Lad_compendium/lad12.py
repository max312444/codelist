# 함수 구현 - 개인 소득세 계산 프로그램

# 소득세 계산 함수를 작성한다. 경우의 수가 3가지 있으므로 3가지 경우의 Tax값을 구하는 식을 작성한다.
def calculate_Tax(income):
    if 10000 >= income:
        Tax = income * 0.1
        
    elif 20000 >= income > 10000:
        Tax = (income - 10000) * 0.15 + 1000

    elif income > 20000:
    
           Tax = (income - 20000) * 0.2 + 2500

    return Tax
# 계산할 소득 금액을 입력한다.
income = int(input("소득 금액을 입력하세요: "))

# 사용하기 쉽게 Tax 변수 값으로 지정한다.
Tax = calculate_Tax(income)

# 함수에 변수 Tax을 넣어 결과를 출력한다.
print(f"소득세는 {Tax}달러입니다.")