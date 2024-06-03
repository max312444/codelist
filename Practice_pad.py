import random
# 범위: 번호는 1부터 45까지의 숫자 중에서 선택해야 합니다.
# 고유성: 선택된 6개의 번호는 중복되지 않아야 합니다.
# 정렬: 선택된 번호는 오름차순으로 정렬하여 출력해야 합니다.
# 사용자 입력: 몇 세트를 생성할지 사용자로부터 입력받을 수 있어야 합니다
random_list = [random.randint(1, 46) for _ in range(6)]
random_list.sort()
print(random_list)

