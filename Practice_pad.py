input_num_list = input("숫자들을 쉼표로 구분하여 입력하세요: ")

num_list = input_num_list.split(",")

sum = 0
output_list = []
over_100_flag = False

for num_str in num_list:
    num = int(num_str)
    sum += num
    output_list.append(num)
    
    
    if sum > 100:
        over_100_flag = True # break가 동작했는지 안했는지 확인 식
        break
    
if over_100_flag:
    print("총합이 100을 초과하였습니다.")
    print("현재까지의 입력값들: ", output_list)
    print("현재까지의 총합: ", sum)
else:
    print("총합이 100을 초과하지 않았습니다.")
    print("입력된 모든 숫자들: ",output_list)
    print("최총 총합: ", sum)

