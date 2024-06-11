import random

def get_random_list(random_value, start_value, end_value):
    
    random_list = []
    
    randcom_count = 0
    
    while randcom_count < random_value:
        
        random_choice = random.randint(start_value, end_value)
        
        found_value = False
        
        for index in range(randcom_count):
            if random_list[index] == random_choice:
                found_value = True
                break
        if not found_value:
            random_list.append(random_choice)
            randcom_count += 1
            
    return random_list
            
com_random_list = get_random_list(3, 1, 10)

print("컴퓨터 선택: ",com_random_list)

count_game = 0
count_strike_out = 0

while True:
    count_strike = 0
    count_ball = 0
    
    count_game += 1
    print("사용자 입력: ")
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
        print("strike: ", count_strike, "ball: ", count_ball)
        
    if count_game >= 5 or count_strike_out >= 2:
        msg = "시도 횟수 5회 이상" if count_game >= 5 else "스트라이크 아웃 2회 이상"
        print(msg, "\t게임 종료")
        break
        
    if count_strike >= 3:
        print("승리\t게임 종료")
        break