# 점수 분류 및 평균 계산
# 학생들의 점수 리스트가 주어졌을 때, 각 점수를 분류하고 분류된 점수들의 평균을 계산하는 프로그램을 작성
# 90이상 우수, 70이상 90미만 양호, 50이상 70미만 보통, 50미만 미흡
# 각 분류에 따른 점수의 평균을 계산하고, 분류된 점수 리스트와 각 분류의 평균 점수를 출력

# 학생들의 점수 리스트
scores = [92, 85, 34, 76, 58, 90, 61, 70, 45, 99]

a_list = []
b_list = []
c_list = []
d_list = []

a_sum, b_sum, c_sum, d_sum = 0, 0, 0, 0

for i in scores:
    if i >= 90:
        a_list.append(i)
for y in a_list:
    a_sum += y
print(f"우수 : {a_list} 평균 : {a_sum / len(a_list)}")        
for i in scores:
    if 90 > i >= 70:
        b_list.append(i)
for t in b_list:
    b_sum += t
print(f"양호 : {b_list} 평균 : {b_sum / len(b_list)}") 
for i in scores:
    if 70 > i >= 50:
        c_list.append(i)
for u in c_list:
    c_sum += u
print(f"보통 : {c_list} 평균 : {c_sum / len(c_list)}") 
for i in scores:
    if 50 > i:
        d_list.append(i)
for o in d_list:
    d_sum += o
print(f"미흡 : {d_list} 평균 : {d_sum / len(d_list)}") 

# a_list = [i for i in scores if i >= 90]
# print(a_list)


