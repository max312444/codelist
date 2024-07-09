# 범위 내의 난수 리스트 생성
# start : 난수의 시작범위 - 0이상 end 보다 작아야함
# end : 난수의 끝 범위 - start 보다 커야함
# N : 생성할 난수의 수 - start와 end 사이 가능한 최대 수 이하
# 모든 입력 값은 유효할 때까지 재입력 요구
# 생성된 난수 값은 1차원 리스트에 저장 되어야 한다.
# 출력 - 생성된 중복되지 않은 N개의 난수를 포함한 리스트를 출력한다.

import random

N_list = []
N_count = 0

while True:
    start_value = int(input("Start (0 이상의 정수): "))
    end_value = int(input(f"End (Start({start_value})보다 큰 정수): "))
    N = int(input("N (생성할 난수의 개수): "))
    if start_value >= 0 and end_value > start_value and start_value <= N <= end_value:
        break

while N_count < 2:      
    N_value = random.randint(start_value, end_value)
    if N_value not in  N_list:
        N_list.append(N_value)
        N_count += 1
    if len(N_list) - 1 == N:
        break
print(N_list)