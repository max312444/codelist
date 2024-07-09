import random
# 중복되지 않은 난수 값 3개 생성(0 ~ 9)
random_list = []
count = 0

while count < 3:
    random_value = random.randint(0, 10)
    
    for index in range(count):
        if random_list[index] == random_value:
            break
        
        else: # 중복 값이 없다.
            random_list.append[random_value]
            count += 1
            
print(random_list)
# 또 다른 풀이(이건 쓰지 않는게 좋을듯)
# random_list = [value for value in range(0, 10)]

# for _ in range(7):
#     del random_list[random.randint(0, len(random_list) - 1)]
    
# print(random_list)

    # 사용자로 부터 정수 3개 입력
input_values = input()

input_list = [int(value) for value in input_values.split()] # split을 사용하면 공백이 삭제 된다. 

print(input_list)

count_trial = 0
count_strike_out = 0

while True:
    count_strike = 0
    count_ball = 0
    
    # strike, ball 판별 - 숫자가 들어가있으면  ball, 숫자랑 자리가 맞으면 strike
    for i in range(3):
        for j in range(3):
            if random_list[i] == input_list[j]:
                if i == j:
                    count_strike += 1
                else:
                    count_ball += 1
    
    # strike_out 판별 - 아무것도 안 맞을 때    
    if count_strike == 0 and count_ball == 0:
        count_strike_out += 1
        print(f"스트라이크 아웃; {count_strike_out}")
    # 게임 종료 조건 
    # - strike 3개 
    if count_strike >= 3:
        print(f"사용자 승리")
        break
    # - strike_out 2번 
    if count_strike_out >= 2 or count_trial >= 5:
        print(f"사용자 패배")
        break
    # - 시도 횟수가 5번이상
    count_trial += 1
