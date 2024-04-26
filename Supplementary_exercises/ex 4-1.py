#문제 4-1 가상 주식 거래 시뮬레이션
#가격 변동 후 주식 판매하여 얻느 손익 계산 
#초기 자본금, 주식의 구매 가격, 구매할 주식의 수, 판매할 떄의 주식 가격 입력
#주식구매 비용 계산 : 구매가격 * 주식수
#남의 자본금 계산 : 초기 자본금 - 총 구매 비용
#판매 예상 이익 계산 : 판매할 떄의 주식가격 * 주식 수 - 총 구매 비용
#결과 출력 : 이익 발생시 "예상되는 이익입니다.", 손실 발생시 "예상되는 손실입니다." 출력

# 조건에 맞는 값 입력
money = int(input("초기 자본금을 입력하세요: "))
price = int(input("주식 가격을 입력하세요: "))
count = int(input("구매할 주식 수를 입력하세요: "))
change_price = int(input("판매할 때의 주식 가격을 입력하세요: "))
# 최종 금액 계산 식
total_money = money - price * count 

if total_money < 0: # 최종 금액이 음수 일 때
    print("자본금이 부족합니다.")
else: 
    M = change_price * count - price * count
    
    print(f"구매 후 남은 자본 : {float(total_money):.2f}")
    print(f"예상 이익: {float(M):.2f}")
    
    if M > 0:
        print("예상되는 이익입니다.")
    elif M < 0:
        print("예상되는 손실입니다.")