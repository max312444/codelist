# 문제 9063

n = int(input())
x_list = []
y_list = []

for _ in range(n):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)
    
a = max(x_list)
b = max(y_list)
c = min(x_list)
d = min(y_list)
print((a - c) * (b - d))
