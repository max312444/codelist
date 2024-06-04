# 학생 점수 분석 및 등급 분포 시각화
# 90 이상 a 80이상 90미만 b 70이상 80미만 c 60이상 70미만 d 60미만 f
# 등급별 학생수 계산하고, 등급별 학생수를 '*'문자를 사용하고, 각 등급의 평균 점수도 계산하여 출력

scores = [92, 85, 34, 76, 58, 90, 61, 70, 45, 99, 82, 67, 50, 77, 89]

# 등급 별 합을 저장하기 위해 변수 생성
# a_sum, b_sum, c_sum, d_sum, f_sum = 0, 0, 0, 0, 0

# 등급별 점수 구분 
# a_list = [i for i in scores if i >= 90]
# for q in a_list:
#     a_sum += q
# A등급 평균 점수 및 포함된 인원 및 별 출력
# print(f"A등급: 평균 점수 = {format(a_sum / len(a_list), ".2f")}\n {len(a_list) * "*"} ({len(a_list)}명")
# b_list = [i for i in scores if 90> i >= 80]
# for q in b_list:
#     b_sum += q
# B등급 평균 점수 및 포함된 인원 및 별 출력
# print(f"B등급: 평균 점수 = {format(b_sum / len(b_list), ".2f")}\n {len(b_list) * "*"} ({len(b_list)}명")
# c_list = [i for i in scores if 80 > i >= 70]
# for q in c_list:
#     c_sum += q
# C등급 평균 점수 및 포함된 인원 및 별 출력
# print(f"C등급: 평균 점수 = {format(c_sum / len(c_list), ".2f")}\n {len(c_list) * "*"} ({len(c_list)}명")
# d_list = [i for i in scores if 70 > i >= 60]
# for q in d_list:
#     d_sum += q
# D등급 평균 점수 및 포함된 인원 및 별 출력
# print(f"D등급: 평균 점수 = {format(d_sum / len(d_list), ".2f")}\n {len(d_list) * "*"} ({len(d_list)}명")
# f_list = [i for i in scores if 60 > i]
# for q in f_list:
#     f_sum += q
# F등급 평균 점수 및 포함된 인원 및 별 출력
# print(f"F등급: 평균 점수 = {format(f_sum / len(f_list), ".2f")}\n {len(f_list) * "*"} ({len(f_list)}명)")


# sum 함수 사용
a_list = [i for i in scores if i >= 90]
print(f"A등급: 평균 점수 = {format(sum(a_list) / len(a_list), ".2f")}\n {len(a_list) * "*"} ({len(a_list)}명")

b_list = [i for i in scores if 90> i >= 80]
print(f"B등급: 평균 점수 = {format(sum(b_list) / len(b_list), ".2f")}\n {len(b_list) * "*"} ({len(b_list)}명")

c_list = [i for i in scores if 80 > i >= 70]
print(f"C등급: 평균 점수 = {format(sum(c_list) / len(c_list), ".2f")}\n {len(c_list) * "*"} ({len(c_list)}명")

d_list = [i for i in scores if 70 > i >= 60]
print(f"D등급: 평균 점수 = {format(sum(d_list) / len(d_list), ".2f")}\n {len(d_list) * "*"} ({len(d_list)}명")

f_list = [i for i in scores if 60 > i]
print(f"F등급: 평균 점수 = {format(sum(f_list) / len(f_list), ".2f")}\n {len(f_list) * "*"} ({len(f_list)}명)")
