# 2차원 리스트 조작

# 사용자에게 row 값과 col 값을 입력받음 
user_row = int(input("Enter the number of rows : "))
user_col = int(input("Enter the number of columns : "))
# bar 초기화하여 행렬 만큼의 매트릭스 작성
bar = [[0 for _ in range(user_col)] for _ in range(user_row)]
# 입력한 row, col 만큼 반복
for i in range(user_row):
    for j in range(user_col):
        # bar의 값을 입력한 값으로 바꿔줌
        bar[i][j] = int(input(f"Enter value for [{i}][{j}]: "))
# 하나씩 출력 
for row in bar:
    for col in row:
        print(col, "\t", end=' ')
    print()