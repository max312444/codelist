# 함수 구현 - 섭씨 -> 화씨 온도 변환
# 섭씨를 화씨로 바꾸는 식을 넣은 함수 작성한다.
def convert_celsius_to_fahrenheit(celsius):
    F = (celsius * 9/5) + 32 
    return F
    
# 섭씨 온도를 입력 한다.
C = int(input("섭씨 온도를 입력하세요: "))

# 함수에 변수 C 값을 넣고 출력한다.
print("화씨 온도는",convert_celsius_to_fahrenheit(C),"입니다.")