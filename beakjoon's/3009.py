# 문제 3009

x_list = []
y_list = []

for _ in range(3):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)
for i in x_list:
    x_list.count(i)
for j in y_list:
    y_list.count(j)
    
    