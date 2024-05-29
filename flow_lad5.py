# 성적의 총합, 평균, 학생 수 출력 프로그램 
# for 문을 사용하여 아래 학생들의 성적에 대한 총합, 평균, 학생 수를 출력하는 프로그램 작성

score = [99, 29, 30, 40, 20, 60]
# 학생 수 구함
student_num = len(score)
# 초기 총점은 0으로 지정
sum = 0
# 점수 더하는 식
for i in range(0, student_num):
    sum += score[i]
# 총점을 나눔
avg = sum / student_num

print("학생 수 : ", student_num, ", 총점 : ", sum, ", 평균 : ", avg)