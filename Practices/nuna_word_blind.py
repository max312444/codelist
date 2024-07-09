import random
#단어입력
count = ["첫", "둘", "셋"]
user_list = []
for i in count:
    while True:
        user1 = input(f"{i}번째 단어를 입력하세여")
        if 3 <= len(user1) <= 20:
            user_list.append(user1)
            break
        else:
            print("재입력")
#단어선택      
user_choice = random.choice(user_list)

user_choice_list = [value for value in user_choice]
s_list = user_choice_list[:]
#블라인드글자수
count_word = len(user_choice_list)
#블라인드 글자수 블라인드 추가 
half_word = count_word // 2
if count_word % 2 != 0:
    half_word += 1
    
count = 0
rest_list = []
while count < half_word:
    random_num = random.randint(0, half_word)
    if s_list[random_num] != "_":
        s_list[random_num] = "_"
        rest_list.append(random_num)
        count += 1
        
count = 0
while True:
    count_1 = 0
    count += 1
    print(f"단어 선택 완료 게임 시작 선택 단어;{user_choice}")
    print(f"{count}번째 시도, 아래 단어를 구성하는 알파벳 한개 입력")
    print(s_list)
    user_input = input()
    for i in rest_list:
        if user_input == user_choice_list[i]:
            s_list[i] = user_input
            count_1 += 1
    print(f"{s_list}, 입력한 알파벳 단어 내 포함 글자:{count_1}개")
    

    if "_" not in s_list:
        print(f"게임 종료, 선택된 단어: {user_choice}, 총 시도 횟수{count}")
        break
        