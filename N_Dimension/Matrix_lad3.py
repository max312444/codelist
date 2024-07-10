# 학생 성적 관리 프로그램
# 성적을 입력받아 리스트에 저장하고 입력값을 출력하는 프로그램을 함수를 이용하여 작성

# count = 0
# students = []

# while True:
#     print("=" * 23)
#     print("  1. 학생 성적 입력")
#     print("  2. 학생 목록 출력(입력 순)")
#     print("  3. 프로그램 종료")
#     print(" " * 10)
#     print(f"현 입력데이터 갯수 : {count}")
#     if count > 0:
#         total_avg = sum([student['avg'] for student in students]) / count
#         print(f"전체 학생 평균 값 : {total_avg:.2f}")
#     else:
#         print("전체 학생 평균 값 : 0.00")
#     print("=" * 23)
#     user_input = int(input())
    
#     if user_input == 1:
#         std_id = int(input("학번을 입력하세요\t"))
#         name = input("이름을 입력하세요\t")
#         score_kor = int(input("국어 성적을 입력하세요\t"))
#         score_eng = int(input("영어 성적을 입력하세요\t"))
#         score_math = int(input("수학 성적을 입력하세요\t"))

#         sum_score = score_kor + score_eng + score_math
#         avg = sum_score / 3
#         # 딕셔너리
#         student = {'id' : std_id, 'name' : name, 'kor' : score_kor, 'eng' : score_eng, 'math' : score_math, 'sum' : sum_score, 'avg' : avg}

#         students.append(student)
#         count += 1
        
#     elif user_input == 2:
#         for student in students:
#             print(f"[ id : {student['id']} name : {student['name']} kor : {student['kor']} eng : {student['eng']} math : {student['math']} sum : {student['sum']} avg : {student['avg']:.2f} ]")
    
#     elif user_input == 3:
#         break

# 딕셔너리 사용 안한 버전
# 학생 성적 관리 프로그램
# 성적을 입력받아 리스트에 저장하고 입력값을 출력하는 프로그램을 함수를 이용하여 작성

count = 0
students = []
id_list = []
name_list = []
kor_list = []
eng_list = []
math_list = []
sum_list = []
avg_list = []

while True:
    print("=" * 23)
    print("  1. 학생 성적 입력")
    print("  2. 학생 목록 출력(입력 순)")
    print("  3. 프로그램 종료")
    print(" " * 10)
    print(f"현 입력데이터 갯수 : {count}")
    if count > 0:
        total_avg = sum(avg_list) / count
        print(f"전체 학생 평균 값 : {total_avg:.2f}")
    else:
        print("전체 학생 평균 값 : 0.00")
    print("=" * 23)
    user_input = int(input())
    
    if user_input == 1:
        std_id = int(input("학번을 입력하세요\n"))
        id_list.append(std_id)
        name = input("이름을 입력하세요\n")
        name_list.append(name)
        score_kor = int(input("국어 성적을 입력하세요\n"))
        kor_list.append(score_kor)
        score_eng = int(input("영어 성적을 입력하세요\n"))
        eng_list.append(score_eng)
        score_math = int(input("수학 성적을 입력하세요\n"))
        math_list.append(score_math)

        sum_score = score_kor + score_eng + score_math
        sum_list.append(sum_score)
        avg = sum_score / 3
        avg_list.append(avg)

        count += 1
        
    elif user_input == 2:
        for i in students:
            print(f"[ id : {id_list[i]} name : {name_list[i]} kor : {kor_list[i]} eng : {eng_list[i]} math : {math_list[i]} sum : {sum_list[i]} avg : {avg_list[i]:.2f} ]")
    
    elif user_input == 3:
        break

# 함수 사용한 버전
