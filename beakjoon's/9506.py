# 문제 9506

while True:
    n = int(input())
    num_list = []
    if n == -1:
            break
    for i in range(1, n):
        if n % i == 0:
            num_list.append(i)
            
    if sum(num_list) == n:
        print(n, " = ", " + ".join(str(i) for i in num_list), sep="")
    else:
        print(n, "is NOT perfrct.")
            
    
# 이게 정답이래 왜지?
# while True:
#     n = int(input())
#     if n == -1:
#         break
#     arr = []
#     for i in range(1, n):
#         if n % i == 0:
#             arr.append(i)
#     if sum(arr) == n:
#         print(n, "=", end=" ")
#         print(*arr, sep=" + ")
#     else:
#         print(n, "is NOT perfect.")