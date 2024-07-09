#     *  
#    *** 
#   *****
#  *******
# *********
# row_count = 5
# star_count = 1

# # 세로 반복 
# for i in range(row_count):
#     # 가로 반복 - 세로줄이 늘어나면 별의 개수가 양옆으로 하나씩 늘고 공백은 양쪽으로 하나씩 줄어든다.
#     for _ in range(row_count - i - 1):
#         print(" ", end = "")
    
#     for _ in range(star_count):
#         print("*", end = "")
        
#     print()
    
#     star_count += 2
    
row_count = 5
star_count = 1    

# 세로 반복
for _ in range(row_count):
    # print for blank
    for _ in range(row_count):
        print(" ", end = "")
    # print for "*"
    for _ in range(star_count):
        print("*", end = "")
    # print "\n" 
    print()
    row_count -= 1
    star_count += 2
     # 가독성이 쉽게 만들도록 노력하자 
     # 단순 문자로 입력하지 말고 어떤 값에 대한 것인지 이름 지정
     # 연산자 사이에 공백을 넣어 가독성이 좋게 만들자