# 가변 개수의 숫자를 매개변수로 받아 평균을 반환하는 함수
def calculate_average(*arg_a):
    sum = 0
    for i in arg_a:
        sum += i   
    
    return sum / len(arg_a)


print(calculate_average(1, 2, 3, 4, 5))
print(calculate_average(6, 7, 8))
print(calculate_average(10, 20))