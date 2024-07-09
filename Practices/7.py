# 10이상 20 이하 정수 중 짝수의 합을 계산하라
# sum = 0

# for i in range(10, 21):
#     if i % 2 == 0:
#        sum += i

# print(sum)

sum = 0

for value in range(10, 21, 2):
    sum += value
    
print(sum)