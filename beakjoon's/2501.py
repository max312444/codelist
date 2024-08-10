# 문제 2501

p, q = map(int, input().split())
num_list = []
for i in range(1, p + 1):
    if p % i == 0:
        num_list.append(i)

if len(num_list) < q:
    print(0)
else:
    print(num_list[q - 1])
