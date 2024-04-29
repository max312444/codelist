'''
bar = [] # 리스트 생성
# []

for value in range(1, 20): # 총 19회 [1 -> 19, 1 증가]
    bar.append(value) # [1, 2, 3, 4 .... 19]

print(bar)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

# 첫 번째 원소의 값은?
print(baar[0]) # 1

foo = []

foo.append(10)
foo.append(20)
foo.append(30)
foo.append(5)

for index in range(0, 4):
    print(foo[index])
    # 1) foo[0] -> 10
    # 2) foo[1] -> 20
    # 3) foo[2] -> 30
    # 4) foo[3] -> 5

print("foo list의 사이즈는: ", len(foo))
# 리스트 생성
# 리스트의 메모리상 주소를 foo에 저장
# foo를 이용하여 각 리스트의 원소에 접근 가능
# 그냥 [7, 8, 6, 3, 4]를 입력하면 접근할 방법이 없어 사용할 수 없다.
foo = [7, 8, 6, 3, 4]

print(foo[0])

foo = [10, 20, 30]

bar = [100, 200, 300]

pos = [60, 30, 50]

bar = foo

pos = bar

bar[0] = 900

print(foo[0], bar[0], pos[0])

bar = [90, 10, 20]

def test(argValue):
    for index in range(0, len(argValue)):
        argValue[index] += 1
        
test(bar)

print(bar)

# 좀비 메모리 - 메모리만 잡아먹음
# 참조 변수가 있는지 확인하고 없으면 삭제해야함
bar = [1, 2, 3, 4]

bar = []

foo = bar

foo = []

foo.append(10) # foo에 10의 값을 가지는 원소 추가

print(bar[0])

bar = [1, 3, 6, 7]

bar.insert(2, 4)

print(bar)

bar = [3, 10 ,20]

foo = [100, 200]

bar = bar + foo

print(bar)

bar = []

foo = list()

foo.append(100)
bar.append(200)
bar.append(300)
foo.append(400)
bar.insert(0, 70)

print(foo)
print(bar)

# pos = foo + bar # foo + bar를 하면 새로운 메모리 공간을 만든다
# foo += bar
foo.extend(bar)

print(foo)
print(bar)
print(pos)

import random

bar = list()

for _ in range(0, 5):
    bar.append(random.randint(1, 100)) 
# random.randint = 1 이상 100 이하의 정수 중 난수를 한 개 선택    
print(bar)

print(bar[4], bar[-1], bar[len(bar) - 1])

bar = [10, 20, 30, 40, 50]

print(bar[0])
print(bar[1])
print(bar[2])
print(bar[3])
print(bar[4])
print(bar[5]) # 인덱스 5번째 값이 존재 하지 않는다

print(bar[-1])
print(bar[-2])
print(bar[-3])
print(bar[-4])
print(bar[-5])
print(bar[-6]) # 인덱스 -6은 전체 원소 길이보다 긴 범위를 지정하기 때문에 에러가 일어난다.

bar = [10, 20, 30]
foo = [1, 2, 3,]
pos = [-1, -2, -3]

kin = pos

pos = bar

pos[-1] = 100

pos = kin
print(bar[-1], pos[-1])

bar = [10, 20, 30 ,40]

foo = bar[0:0:1]
print(foo)
foo = bar[0:1:1]
print(foo)
foo = bar[0:2:1]
print(foo)
foo = bar[0:3:1]
print(foo)
foo = bar[0:4:1]
print(foo)
foo = bar[1:4:1]
print(foo)

bar = [10 ,20 ,30 ,40]

foo = bar[:]
print(foo)

foo = bar[2:]
print(foo)

foo = bar[:3]
print(foo)

bar = [10, 20 ,30 ,40]

foo = bar[-1::-1]
print(foo)

# 770225-3983813
# 3개로 구분해서 문자열로 저장
# 첫 번째 : 생년월일 6자리 -> 770225
# 두 번째 : 지역 코드값 6자리 -> 398381
# 세 번째 : 패리티 체크값 1자리 -> 3

bar = [7,7,0,2,2,5,'-',3,9,8,3,8,1,3]

foo = bar[:6]
print(foo)

foo = bar[7:13]
print(foo)

foo = bar[-1]
print(foo)

# 리스트를 사용하기 위해서는 리스트를 생성
bar = []
foo = list()

# CRUD
# create : 원소 삽입
bar.append(10) # bar -> [10]
bar.append(20) # bar -> [10 ,20]

# index     0    1    2
# bar      [10, 100, 20]
#          index   value
bar.insert(1,      100)

# Read
# bar [10, 100, 20]

for index in range(0, len(bar)):  # 0, 3 : len(리스트) -> 리스트의 원소 개수
    print(bar[index]) # index 0 -> 2

bar = [value for value in range(0, 10)]

# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# slicing
# 참조 변수 [start, stop. step]
# start : 0 -> stop : 4 - 1
foo = bar[ 0 : 4 : 1 ]
print("foo", foo)
print("bar", bar)

# CRUD : Update
# Befor : [2, 3, 4, 5, 6]
bar = []

CRUD : Delete
원소 삭제 : 원소 한 개 삭제, 리스트 내 전체 원소 삭제
원소 한 개 삭제 : 세 가지 방법
1) del 명령어를 사용해서 해당 index의 원소를 삭제
2) remove 함수를 이용해서 값을 이용해서 해당 원소를 삭제
3) pop 함수를 이용, 해당 index의 원소를 삭제하고, 삭제된 값을 반환

bar = [10, 20, 30, 40, 50, 60]
print("befor :", bar, len(bar)) # [10, 20, 30 ,40 , 50, 60]
del bar[1]
print("after : ", bar, len(bar)) # [10, 30, 40, 50, 60]

bar = [10, 50, 30, 40, 50, 60]
print("befor :", bar, len(bar)) # [10, 50, 30 ,40 , 50, 60]
bar.remove(50)
print("after", bar, len(bar)) # [10, 30, 40, 50, 60]

print(bar.pop(2)) # 30
print("after :", bar, len(bar)) # [10, 50, 40 , 50, 60] 5

print(bar.pop()) # 60 pop에 아무 값도 넣지 않으면 마지막 값을 삭제한다.
print("after :", bar, len(bar)) # [10, 50, 40 , 50] 4

import random # 내장함수 random 불러옴
n = 5 # 범위 
max_num = 6 # 최대 값 지정

sample_list = [ value for value in range(1, max_num) ]
# 주어진 범위 내의 리스트 생성. value for value 리스트 내에서 원소들을 자동적으로 생산하게 하는 것
# sample_list -> [1, 2, 3, 4, 5]

random_list = [] 
# 새로운 리스트 생성
for trial_count in range(0, n): # 범위 반복
    # 무작위 인덱스 번호를 지정 (인덱스를 구하는 것 이기 때문에 길이에서 1을 빼는 것이다. )
    random_index = random.randint(0, len(sample_list) - 1)
    # 무작위 숫자 뽑아냄 
    random_num = sample_list.pop(random_index)
    # 주어진 리스트의 인덱스 번호를 입력해 제거하고 수를 뽑아낸 후 random_num에 넣는다.
    random_list.append(random_num)    
    # 위에서 실행해 나온 수를 새로생성한 리스트에 넣는다.
print(random_list)

List comprehension

bar = [1, 2, 3, 4, 5, 6]

print(bar)

bar.clear() # 리스트 내의 원소를 삭제

print(bar)

foo = [1, 2, 3, 4, 5, 6]
del foo # 리스트는 살아있지만 참조 변수를 지워서 리스트에 접근할 수 없다.
'''