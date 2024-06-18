# 문제 9-2 주민번호 유효성 검사
# 주민번호는 13자리로 구성. 앞의 6자리 생년월일, 뒤 7자리 성별 출생등록지, 일련번호 및 검증번호로 구성
# 주민번호 앞 12자리를 각각 234567892345 로 곱한 후 모두 더한다. 
# 더한 결과에서 11로 나눈 나머지 구한 후 11에서 이 나머지를 뺀다.
# 결과가 두 자리일 경우 10의 자리는 버리고 1의 자리만 사용
# 최종 결과가 주민번호의 마지막 숫자와 일치하면 유효한 주민번호

# numbers1 = list(input("주민번호를 입력하세요: "))

# numbers1.remove("-") # 주민번호에 - 를 제거하는 식
# numbers2 = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5] # 곱할 수 지정

# sum = 0 # 곱한 값들의 합산 을 넣을 변수 지정

# for i in range(12): # 주민번호 13자리 중 마지막 검증번호를 제외한 수의 범위 지정
#     sum += int(numbers1[i]) * numbers2[i] # 주민번호와 곱하는 수를 의 결과를 전부 더해 sum에 입력 

# if (11 - (sum % 11)) % 10 == int(numbers1[-1]): # 만약 계산 한 값이 검증번호와 같다면. 여기서 int(number1[-1])은 int(numbers1[12])과 같다.
#     print("유효한 주민번호입니다.") # 유효한 주민번호입니다 출력
# else:
#     print("유효하지 않은 주민번호입니다.") # 아니면 유효하지 않은 주민번호입니다. 출력
    
# 문제 9-2 주민번호 유효성 검사
# 주민번호는 13자리로 구성. 앞의 6자리 생년월일, 뒤 7자리 성별 출생등록지, 일련번호 및 검증번호로 구성
# 주민번호 앞 12자리를 각각 234567892345 로 곱한 후 모두 더한다. 
# 더한 결과에서 11로 나눈 나머지 구한 후 11에서 이 나머지를 뺀다.
# 결과가 두 자리일 경우 10의 자리는 버리고 1의 자리만 사용
# 최종 결과가 주민번호의 마지막 숫자와 일치하면 유효한 주민번호
    
def get_check_dight(arg_ssid):
    weight = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]
    weight = [(value % 8 ) + 2 for value in range(12)]
    
    ssid = [int(value) for value in arg_ssid]
    
    sum_value = sum([ssid[index] * weight[index] for index in range(12)])
    
    return (11 - (sum_value % 11) ) % 10
    
    
# 유효한 주민번호 -> True and False
def is_valid_ssid(arg_ssid):
    
    arg_ssid = arg_ssid.replace("-", "")
    
    if len(arg_ssid) != 13:
        return False
    
    # 체크값 계산 알고리즘 구현 필요
    check_dight = get_check_dight(arg_ssid[:-1])
    
    if check_dight == int(arg_ssid[-1]):
        return True
    else:
        return False


print(is_valid_ssid("650212-2871727"))