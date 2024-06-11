# 야구 게임
import random
# 함수 정의 랜덤값 추출 위해
def get_rand_list(rand_value, startvalue, endvalue):
    # 랜덤으로 뽑은 값 저장 리스트 
    random_list = []
    # 중복되지 않은 랜덤값이 들어가 때만 카운트를 올려 다음 과정으로 넘어감
    random_count = 0

# 컴퓨터 랜덤 선택
    while random_count < rand_value: # 랜덤값이 3개 들어갈 때 까지 반복
        # 시작값과 마지막값사이의 무작위 정수 선택
        random_choice = random.randint(startvalue, endvalue)
        # 중복값 검사를 위해 플레그 함수 사용
        found_value = False
        # 중복 값이 있으면 정지하고 다시 위로 올라가 재시작
        for index in range(random_count): 
            if random_list[index] == random_choice: # 만약 랜덤값을 저장한 리스트 안의 값과 뽑은 값이 같으면
                found_value = True 
                break # 다시 반복을 위해서 정지
            
        if not found_value: # 만약 중복되지 않는다면
            random_list.append(random_choice) # 랜덤 리스트에 저장
            random_count += 1 # 그리고 카운트 증가
            
    return random_list # 3개의 정수를 모두 뽑았다면 리스트 값 반환

com_random_list = get_rand_list(3, 1, 10) # 앞에서 부터 정수의 개수, 시작값, 마지막값

print("컴퓨터 랜덤 값: ", com_random_list) # 뽑은 리스트 확인

count_game = 0 # 게임 횟수 
count_strike_out = 0 # 스트라이크 아웃 횟수

while True: # 반복 시작
    count_strike = 0 # 스트라이크 횟수
    count_ball = 0 # 볼 횟수
    
    count_game += 1 # 시도 횟수
    print("사용자 입력: ") 
    user_input = [int(input()) for _ in range(3)] # 사용자가 정수 3개를 입력
    
    for i in range(3): # 각 리스트에 인덱스를 넣어서 그 값이 같은지 확인
        for j in range(3):
            if com_random_list[i] == user_input[j]: # 만약 같으면 스트라이크
                if i == j:
                    count_strike += 1
                else: # 같지 않으면 볼
                    count_ball += 1
                
                break # break를 써서 반복
            
    if count_strike == 0 and count_ball == 0: # 만약 스트라이크도 볼도없으면 스트라이크 아웃
        count_strike_out += 1 # 스트라이크 횟수 증가
        print("스트라이크 아웃")
    else: # 둘중 하나라도 있다면 몇번 있는지 표시
        print("strike: ", count_strike, "\tball: ", count_ball)
    # 만약 시도를 5번 이상하거나 스트라이크 아웃이 2번이상 나오면 게임종료 (패배 조건)
    if count_game >= 5 or count_strike_out >= 2:
        msg = "5회 이상 실행" if count_game >= 5 else "스트라이크 아웃 2회 이상"
        print(msg, "\t게임 종료")
        break
    # 만약 스트라이크 아웃이 3번이상이면 게임 종료(승리 조건)
    if count_strike >= 3:
        print("승리\t게임 종료")
        break