# 구구단과 삼각형 출력 프로그램
# 사용자에게 입력을 받아 해당 기능 실행 후 다시 메뉴로 돌아옴
# 입력이 1~3 범위 외의 값일 경우 에러 메시지출력후 재입력
# 각각의 예외 처리 있음
import random
while True:
# 메뉴 선택
    print("----------------")
    print("1. 구구단 출력")
    print("2. 랜덤값 삼각형 출력")
    print("3. 종료")
    print("----------------")
    # user_dan_list = []
    user_choice = int(input("원하는 메뉴 번호를 입력하세요: "))
    # 프로그램 종료
    if user_choice == 3:
        print("프로그램 종료")
        break
# 사용자 메뉴 입력
    while True:
        if user_choice < 4:
            # 구구단 출력 
            if user_choice == 1:
                user_dan = input("출력할 구구단을 아래 형식으로 입력하세요 (예: 2, 2~5)\n")
                user_dan_list = [value for value in user_dan]
                if "~" in user_dan_list:
                    user_dan_list.remove("~")
                for i in user_dan_list:
                    for j in range(1, 10):
                        print(f"{int(i)} X {j} = {int(i) * j}")
                    print(" " * 10)
                if 1 >=  user_choice or user_choice >= 10:
                    print("2에서 9사이의 값을 입력하세요")
                break
            # 랜덤값 삼각형 출력
            elif user_choice == 2:
                line_count = int(input("삼각형의 높이 줄 수를 입력하세요 (2이상 3이하)\n"))
                random_num_list = []
                if line_count != 2 or 3:
                    print("2이상 3이하 값을 넣으십시오")
                    break

                while len(random_num_list) < line_count:
                    random_num = random.randint(0, 9)
                    if random_num not in random_num_list:
                        random_num_list.append(random_num)

                print(random_num_list)     
                n = random.choice(random_num_list)
                for j in range(line_count):    
                    print((" " *(j)) * n)
        #     elif user_input2 == 3:
        #         n = [s for s in range(0,10)]
        #         for _ in range(user_input2):
        #             del n[random.randint(0,len(n)-1)]
        #         #삼각형을빈칸 3 랜덤숫자
        #         #빈칸 2 랜덤숫자* 
        #         #랜덤숫자 
        #         user_input2 =2
        #         n = [s for s in range(0,10)]
        #         for _ in range(4):
        #             del n[random.randint(0,len(n)-1)]
        #         print(" "*2,    n[0])
        #         print(" ", n[1],n[2])
        #         print(n[3],n[4],n[5])
        # else:
            print("1~3 사이의 값을 입력하세요")
            break


