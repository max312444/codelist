# 야구 게임 만들기
import random
# 컴퓨터 난수 생성 - 0 ~ 9 사이의 중복되지 않은 수 3개
def get_random_list(rand_value, start_value, end_value):
    
    random_list = []
    random_count = 0
    
    while random_count < rand_value:
        random_num = random.randint(start_value, end_value)
        found_value = False
        for index in range(random_count):
            if random_list[index] == random_num:
                found_value = True
                break
        if not found_value:
            random_list.append(random_num)
            random_count += 1
            
    return random_list

com_random_list = get_random_list(3, 0, 9)
print("컴퓨터 랜덤 값: ", com_random_list)
        
# 플레이어 입력 - 0 ~ 9 사이의 수
count_game = 0
count_strike_out = 0

while True:
    count_strike = 0
    count_ball = 0
    count_game += 1
    print("사용자 입력")
    user_input = [int(input()) for _ in range(3)]
    
    for i in range(3):
        for j in range(3):
            if com_random_list[i] == user_input[j]:
                if i == j:
                    count_strike += 1
                else:
                    count_ball += 1
                break
            
    if count_strike == 0 and count_ball == 0:
        count_strike_out += 1
        print("스트라이크 아웃")
    else:
        print("strike : ", count_strike, "ball : ", count_ball)
# 게임 패배 조건 - 스트라이크 아웃 2회 이상, 시도 횟수 5번 이상
    if count_strike_out >= 2:
        print("게임 종료 스트라이크 아웃 2회 이상")
    elif count_game >= 5:
        print("게임 종료 시도 횟수 5번 이상")
        break
# 게임 승리 조건 - 모든 숫자와 자리 까지 맞출경우
    if count_strike >= 3:
        print("승리\t 게임종료")
        break 