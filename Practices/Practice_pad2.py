# 학생 성적 관리 프로그램
# 성적을 입력받아 리스트에 저장하고 입력값을 출력하는 프로그램을 함수를 이용하여 작성

count = 0
students = []

while True:
    print("=" * 23)
    print("  1. 학생 성적 입력")
    print("  2. 학생 목록 출력(입력 순)")
    print("  3. 프로그램 종료")
    print(" " * 10)
    print(f"현 입력데이터 갯수 : {count}")
    if count > 0:
        total_avg = sum([students for student_list in students]) / count # 여기를 수정해야함 마지막 입력한 평균이 나옴 평균들의 평균이 나와야함.
        print(f"전체 학생 평균 값 : {total_avg:.2f}")
    else:
        print("전체 학생 평균 값 : 0.00")
    print("=" * 23)
    user_input = int(input())
    
    if user_input == 1:
        std_id = int(input("학번을 입력하세요\t"))
        name = input("이름을 입력하세요\t")
        score_kor = int(input("국어 성적을 입력하세요\t"))
        score_eng = int(input("영어 성적을 입력하세요\t"))
        score_math = int(input("수학 성적을 입력하세요\t"))

        sum_score = score_kor + score_eng + score_math
        avg = sum_score / 3
        # 딕셔너리
        student_list = [std_id, name, score_kor, score_eng, score_math, sum_score, avg]
        student = {'total' : student_list} # 여기서 키가 중복되서 위에 평균의 평균구하는거에서 마지막 평균이 출력이 되는듯
        
        students.append(student)
        count += 1
        
    elif user_input == 2:
        for student in students:
            print("  id  name kor eng math sum  avg")
            print(f"{student['total']}")
            
    elif user_input == 3:
        break
    