# 단어 맞추기 게임
# 50% 블라인드 처리 하고 사용자가 입력하는 문자가 포함 되면 블라인드 해제
# 해제할때 몇개 해제했는지 출력, 없으면 없다고 출력
import random
# 3개의 단어 입력을 위한 count
count = ["첫", "두", "세"]
# 빈 리스트 생성 - 사용자가 입력한 단어를 저장
user_list = []
# 카운트 리스트의 i번째 - "첫" 부터 시작
for i in count:
    while True:
        # 사용자 입력
        user1 = input(f"{i}번째 단어를 입력하세요")
        # 만약 사용자가 입력한 단어의 길이가 3이상 20이하일 때
        if 3 <= len(user1) <= 20:
            # 리스트에 추가
            user_list.append(user1)
            break
        else:
            # 아니면 추가 안하고 다시 입력
            print("재입력")
# 입력한 3개의 단어중 랜덤으로 고름
user_choice = random.choice(user_list)
# 위에서 랜덤으로 고른 단어를 한 문자씩 리스트에 저장
user_choice_list = [value for value in user_choice]
# 위의 리스트를 하나더 복사
s_list = user_choice_list[:]
# 50% 블라인드 해야하니 리스트의 길이를 구함
count_word = len(user_choice_list)
# 구한 리스트를 반으로 나눔
half_word = count_word // 2
# 만약 구한 길이가 짝수가 아니면 
if count_word % 2 != 0:
    # 블라인드 할 단어 수에 1개 추가
    half_word += 1
# 블라인드 했는지 확인용 카운트 추가
count = 0
# 블라인드한 위치 인덱스 저장
rest_list = []
# 반복문 
while count < half_word:
    # 0부터 블라인드 할 
    random_num = random.randint(0, count_word - 1)
    # 만약 문자 리스트의 인덱스 번호가 "_"가 아니라면
    if s_list[random_num] != "_":
        # "_"로 변환
        s_list[random_num] = "_"
        # 바꾼 문자의 인덱스 번호를 빈리스트에 추가
        rest_list.append(random_num)
        # 카운트 증가
        count += 1
# 시도 횟수 카운트
count = 0
while True:
    # 단어에 몇개가 들어갔는지 확인용 카운트
    count_1 = 0
    # 시도 횟수 올라감
    count += 1
    print(f"단어 선택 완료 게임 시작 선택된 단어 : {user_choice}")
    print(f"{count}번째 시도, 아래 단어를 구성하는 문자를 입력하세요")
    print(s_list)
    user_input = input()
    # 블라인드 한 인덱스 위치중에서
    for i in rest_list:
        # 만약 사용자가 입력한 문자가 블라인드 처리한 문자와 같으면
        if user_input == user_choice_list[i]:
            # 
            s_list[i] = user_input 
            count_1 += 1 
    print(f"{s_list}, 입력한 문자 단어 내 포함 글자: {count_1}개")
    
    if "_" not in s_list: 
        print(f"게임 종료 선택된 단어 {user_choice}, 총 시도 횟수 {count}")
        break 