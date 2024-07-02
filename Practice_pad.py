# 야구 게임 만들기
import random
# 컴퓨터 난수 생성 - 0 ~ 9 사이의 중복되지 않은 수 3개
# 함수 설정 
def get_random_list(rand_value, start_value, end_value):
    # 빈 리스트 생성
    random_list = []
    # 리스트안에 3개의 난수가 들어가면 반복을 멈춰야하니 카운트를 해줌
    random_count = 0
    
    while random_count < rand_value:
        # 랜덤 난수 생성    
        random_num = random.randint(start_value, end_value)
        # 플레그 변수 
        found_value = False 
        # 인덱스 번호를 카운트 범위 만큼 반복
        for index in range(random_count):
            # 리스트 안의 인덱스에 해당하는 숫자가 이번에 랜덤으로 뽑은 숫자와 같으면
            if random_list[index] == random_num:
                # 플레그 변수 변경
                found_value = True
                # 정지
                break
            # 만약 플레그 변수가 변하지 않을 때
        if not found_value:
            # 리스트에 랜덤 숫자 추가
            random_list.append(random_num)
            # 카운트 올림
            random_count += 1
    # 리스트 값 반환
    return random_list
# 함수 호출. 참조 변수 지정
com_random_list = get_random_list(3, 0, 9)
# 뽑은 랜덤 값 리스트 출력
print("컴퓨터 랜덤 값: ", com_random_list)
# 플레이어 입력 - 0 ~ 9 사이의 수
count_game = 0
count_strike_out = 0

while True:
    count_strike = 0
    count_ball = 0
    # 반복 할 때마다 시도 횟수 증가해야함
    count_game += 1
    print("사용자 입력: ")
    # 사용자 입력을 바로 리스트에 넣음 3번 반복해서
    user_input = [int(input()) for _ in range(3)]
    # 리스트 내에서의 반복
    for i in range(3):
        # 리스트 내에서의 반복
        for j in range(3):
            # 만약 랜덤 리스트의 i번째가 사용자가 입력 리스트의 j번째와 같다면
            if com_random_list[i] == user_input[j]:
                # 랜덤 리스트의 자리와 사용자 입력 리스트의 자리가 같으면
                if i == j:
                    # 스트라이크임
                    count_strike += 1
                else:
                    # 아니면 볼
                    count_ball += 1
                break
    # 만약 스트라이크랑 볼이 없으면
    if count_strike == 0 and count_ball == 0:
        # 스트라이크 아웃 1개 올라감
        count_strike_out += 1
        print("스트라이크 아웃")
    else:
        # 아니면 스트라이크와 볼의  횟수를 출력
        print("strike : ", count_strike, "ball : ", count_ball)
    
    

# 게임 패배 조건 - 스트라이크 아웃 2회 이상, 시도 횟수 5번 이상
    # 만약 스트라이크 아웃이 2번이상이면
    if count_strike_out >= 2:
        # 패배 조건 달성
        print("종료 스트라이크 아웃 2회 이상")
    # 만약 시도 횟수가 5번 이상이면 
    elif count_game >= 5:
        # 패배 조건 달성
        print("종료 시도 횟수 5회 이상")
        # 종료
        break
# 게임 승리 조건 - 모든 숫자와 자리 까지 맞출경우
    # 만약 스트라이크가 3번 이상이면
    if count_strike >= 3:
        # 승리 조건 달성
       print("승리 게임 종료")
        # 종료
       break