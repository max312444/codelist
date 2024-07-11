count = 0
avg_list = []
students = []
id_list = []
name_list = []
kor_list = []
eng_list = []
math_list = []
sum_list = []

def score(arg_a):
    global name_list
    global kor_list
    global eng_list
    global math_list
    global sum_list
    global id_list
    global students
    global avg_list
    global count
    if arg_a == "1":
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
    menu_input = input()
    if menu_input == "1":
        score(menu_input)
    elif menu_input == "2":
        for i in students:
            print(f"[ id : {id_list[i]} name : {name_list[i]} kor : {kor_list[i]} eng : {eng_list[i]} math : {math_list[i]} sum : {sum_list[i]} avg : {avg_list[i]:.2f} ]")
    elif menu_input == "3":
        break