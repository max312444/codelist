# 구구단 
# 2단 ~ 9단
# 2 X 1
# 2 X 2
# 
# 2 X 9 = 18
# ------------
#
# 9 X 9 = 81

for i in range(2, 10):# 5단 7단 제외
    if i == 5 or i == 7:
        continue
    for j in range(1, 10):
        print(f"{i} X {j} = {i * j}")
    print("-----------------")
    # if i != 5 or i != 7:
    #     for j in range(1, 10):
    #         print(f"{i} X {j} = {i * j}")
    # print("-----------------")