# 리스트와 타겟 숫자를 매개변수로 받아, 타겟 숫자가 리스트 내에 있는지 여부를
# 반환하는 함수 작성
def contains(arg_a, arg_b):
    for i in arg_a:
        if i == arg_b:
            return True
    else:
        return False
            
            


print(contains([1, 2, 3, 4], 3))
print(contains([1, 2, 3, 4], 8))