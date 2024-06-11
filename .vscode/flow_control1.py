
# M3, M5, M7 -> BMW,
# Y, X -> Tesla
# ES, LS -> Lexus
# G80, G90 -> Hyundai
# 이외 모델 -> "알수 없는 모델입니다."

BMW_model_list = ["M1", "M2", "M3", "M4", "M5", "M6", "M7"]
Tesla_model_list = ["Y", "X"]
Lexus_model_list = ["ES", "LS"]
Hyundai_model_list = ["G80", "G90"]

maker = ""

model = input("모델 선택:")
## in 연산자 사용
# if model in BMW_model_list:
#     maker = "BMW"
# elif model in Tesla_model_list:
#     maker = "Tesla"
# elif model in Lexus_model_list:
#     maker = "Lexus"
# elif model in Hyundai_model_list:
#     maker = "Hyundai"
# else:
#     maker = "알수 없는 모델입니다."
  
# print(maker)


# bmw
for modle_in_list in BMW_model_list:
    if model == modle_in_list:
        maker = "BMW"
        break
#tesla
if maker == "":
    for modle_in_list in Tesla_model_list:
        if model == modle_in_list:
            maker = "Tesla"
            break
#lexus
if maker == "":
    for modle_in_list in Lexus_model_list:
        if model == modle_in_list:
            maker = "Lexus"
            break
#hyundai
if maker == "":
    for modle_in_list in Hyundai_model_list:
        if model == modle_in_list:
            maker = "Hyundai"
            break
        
maker = maker if maker != "" else "알수 없는 모델입니다."
print(maker)

# 리스트 안에 리스트 넣어서 이차원 적으로 관리 가능
list_model = [BMW_model_list, Tesla_model_list, Lexus_model_list, Hyundai_model_list]

# 회사 목록을 가지고 온다. 반복 -> 4회 (BMW -> Tesla -> Lexus -> Hyundai)
# 세로 반복 
maker_name_list = ["BMW", "Tesla", "Lexus", "Hyundai"]
index_count = 0


for maker_list in list_model:
    # 회사별 자동차 모델을 가지고 온다. -> 반복 -> 회사별 모델 개수에 따라 다름.
    # 가로 반복
    for model_in_list in maker_list:
        if model == model_in_list:
            maker = maker_name_list[index_count]
            break
            
            
    if maker != "":
        break
    
    index_count += 1