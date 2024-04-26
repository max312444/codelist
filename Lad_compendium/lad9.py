# 방향 명령어 해석기
# inputValue에 방향 입력한다.
inputValue = input("방향을 입력하세요(left, right, up, down): ")
# 입력한 값이 해당하면 해당되는 입력값을 출력하고, 해당하지 않는다면 알 수 없는 명령입니다.를 출력
if inputValue == "left":
    print("왼쪽으로 이동합니다.")
elif inputValue == "right":
    print("오른쪽으로 이동합니다.")
elif inputValue == "up":
    print("위로 이동합니다.")
elif inputValue == "down":
    print("아래로 이동합니다.")
else:
    print("알 수 없는 명령입니다.")  
    