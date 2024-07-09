# bar = [10, 20, 30, 40]

# print(bar)
# # bar = [10, 20, 30, 40]

# # del bar[2] # 2번째 인덱스의 값을 삭제해라. 삭제할 때 마다 원소의 개수는 줄어든다.

# # print(bar.pop(2)) # del과 같은 건데 해당 리스트의 값(좌표 : 인덱스 번호)을 가져오고 삭제한다.

# # print(bar)
# # bar = [10, 20, 40]

# # while len(bar) > 0:
# #     item = bar.pop(0) # 제일 왼쪽의 값을 하나씩 빼오고 삭제를 함. 리스트안의 원소값이 없어질 때 까지
# #     print(item)

# bar.append(100)

# bar.insert(2, 70)

# print(bar)

# bar = [[1, 2], [2, 3], [3, 4]]
# print(bar)

# bar = [[0 for _ in range(5)] for _ in range(3)]
# print(bar)

# bar = [[0] * 4 for _ in range(3)]
# print(bar)

# bar = [[input() for _ in range(3)] for _ in range(3)]
# print(bar)

# bar = [[10, 20], [30, 40], [50, 60]]
# print(bar[2][1])
# # 해당 위치의 원소값을 100으로 바꿈
# bar[0][1] = 100
# print(bar[0][1])

# bar = [[10, 20, 30], [40, 50], [60, 70, 80, 90]]

# for col in bar:
#     for item in col:
#         print(item, end=' ') # end를 쓰는 이유 : 줄바꿈 및 줄바꿈 대신 공백으로 바꿈
#     print()

# # 행을 삭제
# bar = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# del bar[1]

# print(bar)

# # 열을 삭제
# bar = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# del bar[1][1]

# print(bar)

# # 모든 행에서 동일한 위치의 인덱스 삭제 방법
# bar = [[1,2,3], [4,5,6], [7,8,9]]

# for row in bar:
#     del row[1]
# print(bar)

# 바로 위에꺼 함수로 만들면
# def print_matrix(arg_list):
#     for row in arg_list:
#         for col in row:
#             print(col, "\t", end="")
#         print()
#     print("-" * 20)

# def del_col(arg_list, col_num):
#     for index in range(len(arg_list)):
#         del arg_list[index][col_num]

# matrix = [[1, 2], [3, 4, 5], [6, 7, 8, 9]]

# print_matrix(matrix)

# del_col(matrix, 1)

# print(len(matrix))
# print(len(matrix[0]))
# print(len(matrix[1]))
# print(len(matrix[2]))

# matrix = [[1,2,3], [4,5], [6,7]]
# # matrix의 2번째 인덱스에 해당하는 리스트에 100을 추가한다. 추가 할때 맨뒤에 붙는다.
# matrix[1].append(100)
# print(matrix)

# matrix = [[1,2,3], [4,5], [6,7]]
# # matrix리스트 자체에 리스트를 추가하면 됨
# matrix.append([8, 9, 10, 11])
# print(matrix)

# matrix.insert(2, [100, 200, 300])
# print(matrix)
