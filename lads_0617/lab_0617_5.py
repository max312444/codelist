# 주어진 수가 짝수인지 홀수인지 판별하는 함수 is_even을 작성
def is_even(arg_1):
    if arg_1 % 2 == 0:
        return "True"
    else:
        return "False"

print(is_even(4))
print(is_even(5))