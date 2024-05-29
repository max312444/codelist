# for 문과 continue 문을 사용하여 1부터 20까지의 숫자 중 홀수를 건너 뛰고 짝수의 합계를 계산

total = 0
# 1부터 20까지 범위 지정
for i in range(1, 21):
    if i % 2 != 0:
        continue # continue을 사용해 홀수를 건너 뛴다.
        # 짝수의 합계
    total += i
print("1부터 20까지의 짝수 합계 (홀수 건너뜀):",total)