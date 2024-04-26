# 사용자 나이대를 영어로 표현하기

# 사용자로부터 나이를 입력받는다.(정수형으로 가정)
# 입력된 나이에 따라 사용자를 "청소년(Teenager)", "성인(Adult)", "노년(Senior)"중 하나로 분류
age = int(input("나이를 입력하세요: "))
# 13세에서 19세 사이는 "Teenger"를 출력
if 13 <= age <= 19:
    print("You are in the 'Teenger' age group.")
# 20세에서 64세 사이는 "Adult"를 출력
elif 20 <= age <= 64:
    print("You are in the 'Adult' age group.")
# 65세 이상은 "Senior"를 출력
elif 65 <= age:
    print("You are in the 'Senior' age group.")
# 범위에 맞지 않는 입력값에 대해서는 "Unknown age group"
else:
    print("You are in the 'Unknown age group' age group.")