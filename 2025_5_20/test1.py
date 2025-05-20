N = int(input())
p = []

for i in range(N):
    a = list(map(int, input().split()))
    p.append(a)
    
b = (N + 1) // 2

for b in range(b):
    for i in range(N):
        for j in range(N):
                p[i][j] -= (b + 1)

print(p)