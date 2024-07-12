# bar = { "name" : "ycjung", "age" : 20, "phone" : 123-456 }
# bar = { "영어" : 20, "수학" : 30, "국어" : 40 }
bar = {
        "ycj" :{"name" : "정영철", "age" : 20},
        "lny" :{"name" : "이나영", "age" : 30}
        }

foo = [d for d in bar.values()]

print(foo)

# for item in bar.values():
#     print(item)
    
# for item in bar.values():
#     for e in item.values():
#         print(e)



# 딕셔너리에서 브라켓의 개수는 층을 의미한다.
# 이차원 리스트랑 똑같이 생각하면 된다.
# print(bar["ycj"]) # ycj 딕셔너리의 주소 값을가진다.
# print(bar["ycj"]["name"]) # ycj 딕셔너리의 name의 value 값을 출력한다.
# print(bar["ycj"]["age"]) # ycj 딕셔너리의 age의 value 값을 출력한다.
# print(bar["lny"]["name"]) # lny 딕셔너리의 name의 value 값을 출력한다.
# print(bar["lny"]["age"]) # lny 딕셔너리의 age의 value 값을 출력한다.

# sum = 0
# for value in bar.values():
#     sum += value
# print(sum)

# print(sum(bar.values())) # sum(20 30 40)

# 순회 할때 사용
# keys() : 키 값. 키들이 뭐가 있는지 확인할 때 사용
# values() : 데이터 값. 그안의 값에 관심이 있을 때 사용
# items() : 키 + 데이터

# for sud in bar.keys(): 
#     print(sud, "\t", end="")

# print(bar.items()) # key 값과 value 값을 튜플로 붙여서 반환한다.

# for key, value in bar.items(): # [('영어', 20), ('수학', 30), ('국어', 40)] for문이 한번 돌 때 마다, 원소가 2개인 튜플로 넘어온다
#     print(key, "\t", value)

# for key in bar.keys(): # key 값만 있어도 된다. 왜냐 bar[key]를 입력하면 해당 value값이 나오기 때문이다. 
#     print(key, "\t", bar[key])


# print(bar.keys()) # key값들을 출력한다. 객체형으로 넘어온다. 튜플형태로 들어있다.

# for key in bar.keys():
#     print(key)

# print(bar["name"])

# bar['email'] = "max12max@daum.net"
# # print(bar['email'])

# if "email" in bar: # key. ['name', 'age', 'phone'] 딕셔너리 그래도 넣으면 key값을 가져오도록 세팅되어있다. 예외 처리시 사용
#     print("True")
# else:
#     print("False")
    
# if "mobile" in bar.keys(): # 10번이랑 똑같음 key값들이 넘어옴 듀플값으로. ['name', 'age', 'phone']
#     print("True")
# else:
#     print("False")


# std_grades = {} # Ditctional
#                     # 이름     국어 영어 수학 총점 평균
# std_grades[240001] = ["홍길동", 10, 20, 30, 60, 30]
# std_grades[240002] = ["홍길삼", 100, 200, 300, 600, 300]
# std_grades[240003] = ["홍길사", 1000, 2000, 3000, 6000, 3000]
# std_grades[240004] = ["홍길오", {"국어" : 100, "수학" : 20, "영어" : 10}]

# print(sum(std_grades[240004][1].values()))

# # 리스트 컴프리헨션에서 중첩 for문이 작동하는 원리 및 사용방법
# foo = [value for g in range(2) for value in range(3)]
# for g in range(2):
#     for value in range(3):
#         value 
        
# print(foo)

# # 리스트 컴프리헨션을 이용해서 이차원 배열을 만드는것
# foo = [[value for g in range(2)] for value in range(3)]

# print(foo)