# 문제 1 가위 바위 보 게임 확장 버전
# 사용자로부터 가위 바위 보 중 하나 입력 받고 컴퓨터가 선택한 값과 대결하여 승패무를 판단하고 결과 출력
# 게임은 3판 2선승제. 매 게임마다 승패무의 결과 출력
# 게임이 종료되면 전체 승 무 패의 결과와 최종 승자 출력
# 가위 바위 보 이외의 값이 입력되면 다시 입력
# in, not in 연산자 사용금지


# 첫번째 문제 풀이 chat gpt 참고
# import random # 내장함수 랜덤 가져오가

# choice_list = ["가위", "바위", "보"] # 가위바위보 리스트 작성
# W = 0 # 승리 횟수
# L = 0 # 패배 횟수
# D = 0 # 무승부 횟수

# while W < 2 and L < 2 and D < 2: # 승리 2번이나 패배 2번 할 때 까지 반복
#     choice = input("가위, 바위, 보 중 하나를 입력하세요: ") # 가위바위보 입력
#     if choice == "가위" or choice == "바위" or choice == "보": # 만약 입력한 게 가위바위보이면 진행
#         computer_choice = random.choice(choice_list) # 컴퓨터는 가위바위보중 랜덤으로 선택
#         print("컴퓨터:", computer_choice) 
#         if choice == "가위" and computer_choice == "보": # 만약 사용자는 가위 컴퓨터가 보이면 
#             W += 1 # 1승 추가
#             print("승리! 현재 전적:",W,"승",L,"패",D,"무")
#         elif choice == "바위" and computer_choice == "가위": # 사용자가 바위 컴퓨터가 가위이면
#             W += 1 # 1승 추가
#             print("승리! 현재 전적:",W,"승",L,"패",D,"무")
#         elif choice == "보" and computer_choice == "바위": # 사용자가 보 컴퓨터가 바위이면
#             W += 1 # 1승 추가
#             print("승리! 현재 전적:",W,"승",L,"패",D,"무")
#         elif choice == computer_choice: # 만약 사용자랑 컴퓨터가 같은 거라면
#             D += 1 # 무승부 추가
#             print("무승부! 현재 전적:",W,"승",L,"패",D,"무")
#         else: # 그외 나머지 경우는 패배하는 경우이기 때문에 한번에 else로 묶어서 표현
#             L += 1  # 패배 추가
#             print("패배! 현재 전적:",W,"승",L,"패",D,"무")
#     else: # 가위바위보 중에서 입력 안했을시
#         print("가위, 바위, 보 중에서 선택하세요.")
            
# if W >= 2: # 승리가 2번 이상이면 사용자가 이김
#     print("최종 승자: 사용자")
# elif D >= 2:
#     print("최종 결과: 무승부")
# else: # 나머지 경우인데 한마디로 패배가 2번이상이면 컴퓨터 승리
#     print("최종 승자: 컴퓨터")
    
    
# 두번째 문제 풀이
# import random

# choice_list = ["가위", "바위", "보"]

# W = 0
# L = 0
# D = 0

# while W < 2 and L < 2:
#     choice = input("가위, 바위, 보 중에 하나를 입력하세요:")
#     computer_choice = random.choice(choice_list)
#     print("컴퓨터의 선택:",computer_choice)
#     if choice == "가위" or choice == "바위" or choice == "보":
#         if choice == "가위" and computer_choice == "보":
#             W += 1 
#             print("승리! 현재 전적:",W,"승",L,"패",D,"무")
#         elif choice == "바위" and computer_choice == "가위":
#             W += 1
#             print("승리! 현재 전적:",W,"승",L,"패",D,"무")
#         elif choice == "보" and computer_choice == "바위":
#             W += 1
#             print("승리! 현재 전적:",W,"승",L,"패",D,"무")
#         elif choice == computer_choice:
#             D += 1
#             print("무승부! 현재 전적:",W,"승",L,"패",D,"무")
#         else:
#             L += 1
#             print("패배! 현재 전적:",W,"승",L,"패",D,"무")
#     else:
#         print("가위, 바위, 보 중에서 선택하세요")
    
    
# if W >= 2:
#     print("전적: ",W,"승",L,"패",D,"무")
#     print("최종 승자: 사용자")
# else:
#     print("전적: ",W,"승",L,"패",D,"무")
#     print("최종 승자: 컴퓨터")


# 교수님 풀이
import random

# 가위 바위 보 게임 만들기
count_win = 0
count_lose = 0
count_draw = 0

# count_win, count_lose, count_draw = 0, 0, 0 위에 처럼 변수를 여러게 설정하고 정의 할 수있다.

while True:
# 승리 횟수가 2번 이상 또는 패배 횟수가 2번 이상이면, 프로그램 종료
    if count_win >= 2 or count_lose >= 2:
        print("승리 : ", "사용자" if count_win >= 2 else "컴퓨터") # if 가 참이면 앞에꺼 선택 거짓이면 뒤에꺼 선택
        
        # if count_win >= 2:
        #     print("사용자")
        # else:
        #     print("컴퓨터")

        break


# 사용자로부터 입력받기
    input_user = input("가위 바위 보 중 입력:")

# 컴퓨터 랜덤 선택
# random -> 정수 (integer)
    rsp = ["가위", "바위", "보"]
    input_computer = rsp[random.randint(0, 2)] # 랜덤 인데스 번호 골라 출력

    msg_result = ""
# 결과 판별
# 1) 무승부
    if input_user == input_computer:
        msg_result = "무승부"
        count_draw += 1
# 2) 승
    elif input_user == "가위" and input_computer == "보" or \
        input_user == "바위" and input_computer == "가위" or \
        input_user == "보" and input_computer == "바위":
        msg_result = "승리"
        count_win += 1
# 3) 패
    else:
        msg_result = "패"
        count_lose += 1
# 출력
    print("사용자:", input_user, "\t컴퓨터:", input_computer)
    print(msg_result)
    print(f"전적 :{count_win}승 {count_lose}패 {count_draw}무")
