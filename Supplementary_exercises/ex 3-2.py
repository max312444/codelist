#문제 3-2 출석 점수 프로그램
#만점 20점에서 결석시간에 비례하는 점수 차감. 식 : 20 - (20* 결석시간 수 / 총 수업시간 수). 총수업시간 계산 : 시수/주 *15
#지각 처리 : 지각 3회 = 결석 1시간
#결석 처리 : 결석 시수가 총 수업시수의 1/4초과할 경우 f처리

# 함수 정의 점수 내는 식
def score(week, hours, count):
    n = count // 3 # 지각 처리 식
    score = 20 - ((20 * (hours + n)) /( week * 15)) # 점수 구하는 식
    return score 
# 조건에 맞는 값 입력
week = float(input("주당 수업시간을 입력하세요: "))
hours = float(input("결석한 총 시간을 입력하세요: "))
count = float(input("지각 횟수를 입력하세요: "))

if hours * 4 > week * 15 : # 만약 결석 시수가 총수업시수에 1/4을 초과할 경우
    print("당신의 출석 점수는 F (학점 미부여)점입니다.")

elif score(week, hours, count): 
    print("당신의 출석 점수는",format(score(week, hours, count),".2f"),"점입니다.")