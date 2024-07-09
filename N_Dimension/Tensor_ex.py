# 3차원 리스트
# bar = [[[1,2,3], [4,5,6], [7,8,9]], [[10,11,12], [13,14,15], [16,17,18]]]
# print(len(bar)) # 2
# print(len(bar[0])) # 3
# print(len(bar[0][2])) # 3

bar = [\
    [[1,2,3], [4,5,6], [7,8,9]]\
    , [[10,11,12], [13,14,15], [16,17,18]]\
      ]
# [2][3][3]
# 3 X 3 Matrix가 2장


# 첫번째 : 1번째 Matrix가 반환
# 두번째 : 2번째 Matrix가 반환
# for matrix in bar:
#     print(matrix)

# 각 matrix의 열을 반환
# for matrix in bar:
#     for row in matrix:
#         print(row)
        
# 각 matrix의 열마다의 행을 출력
# for matrix in bar:
#     for row in matrix:
#         for col in row:
#             print(col)
            
# bar 리스트 안에 있는 각 행렬의 내부 원소를 순서대로 출력한다
# for matrix in bar:
#     for row in matrix:
#         for col in row:
#             print(col, "\t", end="")
#         print()
#     print("-" * 10)

# 별 출력하는거도 매트릭스와 같다.
