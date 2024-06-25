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