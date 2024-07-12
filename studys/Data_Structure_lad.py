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
        total_avg = sum([student['avg'] for student in students]) / count
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
        student = {'id' : std_id, 'name' : name, 'kor' : score_kor, 'eng' : score_eng, 'math' : score_math, 'sum' : sum_score, 'avg' : avg}
        
        students.append(student)
        count += 1
        
    elif user_input == 2:
        for student in students:
            print(f"[ id : {student['id']} name : {student['name']} kor : {student['kor']} eng : {student['eng']} math : {student['math']} sum : {student['sum']} avg : {student['avg']:.2f} ]")
            
    elif user_input == 3:
        break