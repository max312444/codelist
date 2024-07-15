# 리스트 컴플리헨션 -> 리스트 내 원소를 동적으로 생성하는 방법
# 수식 for 선택항목 in 선택 리스트 if 조건식

#
# for else
# while else
# done_break = False # Flag 변수 True or False
# for value in range(5): # N번 반복, 0 -> N - 1, 5번 반복, 0 -> 4
# # 왜 0부터 시작하나 : 리스트를 많이 사용하여서 인덱스를 나타내기 쉽게 하기 위해

#     input_value = int(input("입력 값 : "))
#     # for문의 반복이 비정상적으로 종료 됨
#     if input_value <= 0:
#         done_break = True
#         msg = "break 사용"
#         break
    
#     print(value)
# else: # for 문의 반복이 정상적으로 종료 됨
#     msg = "break 미사용"
# # msg = "break 사용" if done_break else "break 미사용"

# print(msg)

# 반복이 정상적으로 종료되었나? 아니면 중간에 break 사용해서 정지 되었나?

# break
# continue
# pass (Python)

# for k in range(1, 5):
#     for i in range(1, 3):
#         for j in range(1, 4):
#             if i == 2:
#                 break
#             print(k, ":", i, ":", j)
            
# break 동작 절차:
# 1) 위로 올라간다.
# 2) 첫 번째 만나는 반복을 종료한다.

# j = 1,2,3 / i = 1,2 / k = 1,2,3,4
# i == 2 면 정지
# k = 1 and i = 1 and j = 1 or 2 or 3
# k = 2 and i = 1 and j = 1 or 2 or 3
# k = 3 and i = 1 and j = 1 or 2 or 3
# k = 4 and i = 1 and j = 1 or 2 or 3
# i가 2 일때만 출력 안함

# for i in range(4): = for i in range(1, 5): # 세로 출력 횟수
#     for j in range(3): = for j in range(1, 4): # 가로 별 3개 출력
#         print("*",end="")
#     print()

# ex)
# 맨위에 for 문은 break가 걸리면 그대로 프로그램 종료한다.
for l in range(1, 4):
    if l == 2:
        continue
    for k in range(1, 5): # k가 3일때 다음 반복으로 넘어간다.
        if k == 3:
            continue
        for i in range(1, 3): # i가 2일 때를 제외하고 가능
            if i == 2:
                break
            # j가 3일 때를 제외하고 가능. 만약 j를 시작 값으로 두면 아무것도 출력되지 않는다.
            for j in range(1, 4): 
                if j == 3:
                    break
                print(l, ":", k, ":", i, ":", j)