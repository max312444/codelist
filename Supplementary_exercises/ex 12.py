# 문제 12- 1 가위,바위, 보 게임 만들기(1)
# 컴퓨터가 난수를 사용해 가위 바위 보 중 하나를 무작위로 선택
# 사용자는 가위바위보 중하나를 입력하고 컴퓨터의 선택과 비교하여 승리,패배,무승부를 결정하는 프로그램 작성

import random # 내장함수 random 불러옴

player_choices = input("가위, 바위, 보 중 하나를 선택하세요: ") # 사용자로 부터 입력받음

choices = ['가위', '바위', '보'] # 선택 범위
computer_choices = random.choice(choices) # 컴퓨터가 랜덤하게 고르는 식
print("컴퓨터의 선택:",computer_choices) 
if player_choices in ('가위', '바위', '보'): # 만약 사용자의 입력이 가위바위보 안에 있다면
    if computer_choices > player_choices: # 컴퓨터의 선택이 사용자의 선택을 이긴다면
        print("결과: 당신이 졌습니다!") 
    elif computer_choices < player_choices: # 컴퓨터의 선택이 사용자의 선택에 진다면
        print("결과: 당신이 이겼습니다!")
    elif computer_choices == player_choices: # 컴퓨터와 사용자의 선택이 같다면
        print("결과: 무승부입니다!")
else:
    print("잘못된 입력입니다. 가위, 바위, 보 중에서 선택해주세요") # 가위바위보 외의 값 입력시