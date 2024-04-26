# 문제 2-1  면적 단위 변환기
# 사용자가 제곱미터 단위로 입력한 토지의 면적을 평방피트와 에이커 단위로 변환해주는 프로그램 작성
# 변환식 : 1제곱미터 = 10.7639 평방피트. 1에이커 = 4046.86 제곱미터

# 함수 정의 제곱 미터당 평방피트
def convert_to_square_feet(square_meters):
    square_meters * 10.7639
# 함수 정의 에이커당 제곱 미터
def convert_to_acres(square_meters):
    square_meters / 4046.86
square_meters = float(input("토지의 면적을 제곱미터(m*2) 단위로 입력하세요: "))
if square_meters < 0 : # 만약 제곱 미터가 음수일 떄
    print("잘못된 입력입니다.") 
else:
    print(f"{square_meters} 제곱미터는",square_meters * 10.7639,"평방피트 입니다.")
    print(f"{square_meters} 제곱미터는",square_meters / 4046.86,"에이커입니다.")
    
# 교수님 문제 2-1 풀이