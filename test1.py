# Membership operator
# in, not in
# A in B
# A rkqt, B sequential Object
# 결과 값은 Boolean

# def myInOperator(argValue, argSeqObj):
#     for value in argSeqObj: # 범위 설정 argSeqObj 내에 value 가 있는데 
#         if value == argValue: # 만약 value 가 argValue가 같다면
#             return True # 참
        
#     return False # 아니면 거짓

# def myInOperator(argValue, argSeqObj):
#     for value in argSeqObj:
#         if value == argValue:
#             return False
    
#     return True

# print("a" in "abc")

# bar = [3, 4, 5, 6]

# print(4 in bar)
# print(4 not in bar)
# print(myInOperator(3, [2, 3, 4]))


# bar = [2, 3, 4]

# foo = [2, 3, 4]

# pos = bar

# if bar == foo:
#     print("참")
# else:
#     print("거짓")
    
# if bar is foo:
#     print("참")
# else:
#     print("거짓")

# if bar is pos:
#     print("참")
# else:
#     print("거짓")
    
# bar = [2, 3, 4]
# pos = bar # pos 는 bar랑 같다. 같은 객체를 가르킨다.

# if bar == (foo := list((2, 3, 4))): # (2, 3, 4)의 튜플 값을 리스트로 변환하고 bar 랑 foo 가 같은지 확인 
#     print("참")
# else:
#     print("거짓")
    
# 위에 식을 한줄로 정리    
# print("참" if bar == (foo := list((2, 3, 4)))else "거짓")

