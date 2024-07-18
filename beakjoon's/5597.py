# 문제 5597
# X대학 M교수님은 프로그래밍 수업을 맡고 있다. 교실엔 학생이 30명이 있는데, 학생 명부엔 각 학생별로 1번부터 30번까지 출석번호가 붙어있다.
# 교수님이 내준 특별과제를 28명이 제출했는데 그 중에서 제출 안 한 학생 2명의 출석번호를 구하는 프로그램 작성

# 입력은 총 28줄로 각 제출자의 출석번호가 한 줄에 하나씩 주어진다. 출석번호에 중복은 없다.

student_num_list = [value for value in range(1, 31)]
count = 0
while count < 28:
    check_num = int(input())
    if check_num in student_num_list:
        student_num_list.remove(check_num)
        count += 1
        
print(student_num_list[0])
print(student_num_list[1])