# 문제 25083
# 아래 예제와 같이 새싹을 출력하시오.
print("         ,r\'\"7")
print("r`-_   ,\'  ,/")
print(" \\. \". L_r\'")
print("   `~\\/")
print("      |")
print("      |")

# 문제 2444
N = int(input())
for i in range(1, N):
    print(" " * (N - i) + "*" *(2 * i - 1))
for i in range(N, 0, -1):
    print(" " * (N - i) + "*" *(2 * i - 1))
