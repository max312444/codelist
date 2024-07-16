# 컴퓨터가 1부터 100사이의 숫자 랜덤 선택
# 사용자는 10번의 기회를 얻고 숫자를 맞춤
# 사용자의 숫자가 컴퓨터 숫자보다 크거나 작다 출력
# 맞추면 정답입니다 출력후 게임 종료
# 기회 10번이 끝나면 모든기회를 사용하였습니다. 정답은 [숫자]입니다. 라고 출력
# 사용자가 0을 입력하면 게임 종료
import random

count = 1
# 랜덤 정수 뽑아냄!
computer_num = random.randint(1, 100)
# print(computer_num)
# count가 10 이하일 때
while count < 10:
    player_num = int(input(f"기회{count} - 1부터 100 사이의 숫자를 맞춰보세요 (종료하려면 0 입력) : "))
    # 만약 컴퓨터 정수가 더 작을 때 count + 1하고 더 작은 숫자입니다 출력
    if player_num > computer_num:
        count += 1
        print("더 작은 숫자 입니다.")
    # 만약 컴퓨터 정수가 더 클 때 count + 1하고 더 큰 숫자입니다 출력
    elif player_num < computer_num:
        count += 1
        print("더 큰 숫자 입니다.")
    # 만약 0을 입력한다면 바로 종료
    elif player_num == 0:
        print("게임이 끝났습니다.")
        break
    else: # 컴퓨터 정수와 사용자가 입력한 정수가 같다면 정답입니다, 게임이 끝났습니다. 출력 후 게임 종료
        print("정답입니다!")
        print("게임이 끝났습니다.")
        break
# 만약 count가 10을넘어간다면 기회를 다 썻다고 출력후 정답 알려주고 게임 종료        
if count >= 10:    
    print(f"기회를 모두 사용하였습니다. 정답은 {computer_num}입니다.")
    print("게임이 끝났습니다.")