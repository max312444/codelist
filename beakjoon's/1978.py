# 문제 1978

n = int(input())
num_list = list(map(int, input().split()))
count = 0

for i in num_list:
    m = 0
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                m += 1
        if m == 0:
            count += 1
print(count)    