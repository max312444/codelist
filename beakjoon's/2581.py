# 문제 2581

m = int(input())
n = int(input())

num_list = []

for i in range(m, n + 1):
    count = 0 # 나눠지는 수 카운트
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                count += 1
                break
        if count == 0:
            num_list.append(i)

if len(num_list) > 0:
    print(sum(num_list))
    print(min(num_list))
else:
    print("-1")
            