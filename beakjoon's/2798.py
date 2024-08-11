a, b = map(int, input().split())
num_list = list(map(int, input().split()))

sum = 0

for i in range(a):
    for j in range(i + 1, a):
        for k in range(j + 1, a):
            if num_list[i] + num_list[j] + num_list[k] > b:
                continue
            else:
                sum = max(sum, num_list[i] + num_list[j] + num_list[k])
print(sum)