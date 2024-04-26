# 문제 2-2 평균 점수와 학점 등급 계산 프로그램
# 학생들의 세 과목 점수를 입력 받아 평균 점수를 계산하고, 평균에 따른 학점 등급을 부여하는 프로그램 제작

# 함수 정의 수학 과학 영어 평균 값
def calculate_average(math_score, science_score, english_score):
    a = (math_score + science_score + english_score) / 3
    return a
# 수학 과학 영어 점수 기입
math_score = float(input("수학 점수를 입력하세요: "))
science_score = float(input("과학 점수를 입력하세요: "))
english_score = float(input("영어 점수를 입력하세요: "))

if (calculate_average(math_score, science_score, english_score))  >= 90: # 평균이 90점 이상일 때
    print("평균 점수는",(calculate_average(math_score, science_score, english_score)) ,"점이고,","학점은 A입니다.")
elif (calculate_average(math_score, science_score, english_score))  >= 80: # 평균이 80점 이상일 때
    print("평균 점수는",(calculate_average(math_score, science_score, english_score)) ,"점이고,","학점은 B입니다.")
elif (calculate_average(math_score, science_score, english_score))  >= 70: # 평균이 70점 이상일 때
    print("평균 점수는",(calculate_average(math_score, science_score, english_score)) ,"점이고,","학점은 C입니다.")
elif (calculate_average(math_score, science_score, english_score))  >= 60: # 평균이 60점 이상일 때
    print("평균 점수는",(calculate_average(math_score, science_score, english_score)) ,"점이고,","학점은 D입니다.")
elif (calculate_average(math_score, science_score, english_score))  >= 50: # 평균이 50점 이상일 때
    print("평균 점수는",(calculate_average(math_score, science_score, english_score)) ,"점이고,","학점은 E입니다.")
else: # 그외 점수
    print("평균 점수는",(calculate_average(math_score, science_score, english_score)) ,"점이고,","학점은 F입니다.")
   
# 교수님 문제 2-2 풀이