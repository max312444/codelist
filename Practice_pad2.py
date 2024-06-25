# 단어 맞추기 게임
# 50% 블라인드 처리 하고 사용자가 입력하는 문자가 포함 되면 블라인드 해제
# 해제할때 몇개 해제했는지 출력, 없으면 없다고 출력
import random
# 단어 입력 파트
count = ["첫", "두", "세"]
user_list = []
# 단어 3개 입력
for i in count:
    while True:
        user1 = input(f"{i}번째 단어를 입력하세요")
        # 단어 조건
        if 3 <= len(user1) <= 20:
            user_list.append(user1)
        else:
            print("재입력")
# 입력한 단어중 랜덤으로 하나 선택
user_choice = random.choice(user_list)
# 선택한 단어 리스트화
user_choice_list = [value for value in user_choice]
s_list = user_choice_list[:]

count_word = len(user_choice_list)
half_word = count_word // 2
# 리스트 길이가 짝수가 아니면 반으로 나눈거에 1 더해줘서 50%이상 블라인드 조건에 충족 시킴
if count_word % 2 != 0:
    half_word += 1
# 새로운 카운트 생성
count = 0
rest_list = [] # 블라인드 처리할 인덱스 번호 저장
while count < half_word: # count가 half-word보다 작을 때 까지만 반복
    random_num = random.randint(0, half_word) # 범위는 0부터 half_word까지
    if s_list[random_num] != "_": # 만약 랜덤으로 뽑은 인덱스의 인덱스가 "_"가 아니라면
        s_list[random_num] = "_" # "_"로 변경
        rest_list.append(random_num) # 그 변경했다면 그 인덱스 rest_list에 저장
        count += 1 # 카운트올림
        
count = 0 # 시도 횟수 세는 카운트
while True:
    count_1 = 0 # 단어 내 입력한 문자가 몇개 해당하는지 확인용
    count += 1
    print(f"단어 선택 완료 게임 시작 선택된 단어 : {user_choice}")
    print(f"{count}번째 시도, 아래 단어를 구성하는 문자를 입력하세요")
    print(s_list)
    user_input = input() # 사용자 입력
    for i in rest_list: # 블라인드된 단어의 인덱스 리스트중
        if user_input == user_choice_list[i]: # 원래 단어리스트에 사용자가 입력한 단어가 들어있다면
            s_list[i] = user_input # 그 인덱스를 입력한 단어로 바꿈
            count_1 += 1 # 몇개 들어있는지 카운트
    print(f"{s_list}, 입력한 문자 단어 내 포함 글자: {count_1}개")
    
    if "_" not in s_list: # 만약 "_"가 블라인드된 인덱스 리스트에 없다면 
        print(f"게임 종료 선택된 단어 {user_choice}, 총 시도 횟수 {count}")
        break # 게임종료