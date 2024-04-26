# incrementCount 함수 정의:
# - 전역 변수 count의 값을 1 증가
def incrementCount():
    global count;
    count = count + 1
    
# decrementCount 함수 정의:
# - 전역 변수 count의 값을 1 감소
def decrementCount():
    global count;
    count = count - 1
    
# 전역 변수 count를 1로 초기화
count = 1

incrementCount()
print(count)

decrementCount()
print(count)

incrementCount()
print(count)
incrementCount()
print(count)