import random
import turtle

# 화면을 설정합니다.
screen = turtle.Screen()
screen.title("Turtle 키보드 이벤트 처리 예제")

width = screen.window_width() // 2
height = screen.window_height() // 2

print("윈도우 가로X세로", width, height)
# 거북이를 생성합니다.
t = turtle.Turtle()

# 거북이가 움직이는 함수를 정의합니다.
def move_forward():
    t.forward(100)
    
    x, y = t.position()
    print(x, y)
    
    if x >= width or x <= -width or y >= height or y <= -height:
        t.right(180)
    
    
def move_backward():
    t.backward(100)
    
def turn_left():
    t.left(15)
    
def turn_right():
    t.right(15)
    
# 펜 색깔을 검은색으로 변경 - > "b" key를 누를 때 호출
def change_color_to_black():
    color = "black"
    t.pencolor(color)

# 펜 색깔 변경 함수를 정의
def move_random():
    colors = ["red", "green", "blue", "yellow", "purple", "orange"]
    t.pencolor(random.choice(colors))
    
# 펜 색깔 빨간색으로 변경 - > "r"key를 누를 때 호출
def change_color_red():
    color = "red"
    t.pencolor(color)
    
# i를 누르면 색깔이 빨간색에서 -> 검은색 또는 검은색 -> 빨간색
# 현재 펜 색깔이 빨간색 또는 검은 색인 경우에만 반전
# def change_color_red_black_exchange():
#     if t.pencolor() == "black":
#         t.pencolor("red")    
#     elif t.pencolor() == "red":
#         t.pencolor("black")

# 위에꺼랑 같긴함 
def change_color_red_black_exchange():
    cerrent_pen_color = t.pencolor()
    
    if cerrent_pen_color == "black":
        t.pencolor("red")    
    elif cerrent_pen_color == "red":
        t.pencolor("black")

# 펜 색깔 선택 함수
def change_color():
    print("색깔 선택: ")
    input_value = -1
    while True:
        print("1. 파란색")
        print("2. 검정색")
        print("3. 노란색")
    # 사용자 입력
        input_value = int(input("숫자 입력: "))
        # 만약 1, 2, 3 이 입력되면 각각에 해당하는 색깔로 변경
        # 1,2,3, 이외의 값 입력시 재입력 -> 언제까지? 1-3 값이 입력 될때 까지
        if 1 <= input_value <= 3: # 중첩 if문 바깥쪽 if 문과 안쪽 if 문은 and 가 활성화 된다.
            if input_value == 1:
                t.pencolor("blue")
            elif input_value == 2:
                t.pencolor("black")
            elif input_value == 3:
                t.pencolor("yellow")
            break
        else:
            print("색깔을 다시 선택 하십시오")
            
    # while not (1 <= input_value <= 3):
    #     input_value = int(input("숫자 입력: "))
        
    #     if input_value == 1:
    #         t.pencolor("blue")
    #     elif input_value == 2:
    #         t.pencolor("black")
    #     elif input_value == 3:
    #         t.pencolor("yellow")
        

# 키보드 이벤트를 설정합니다.
screen.listen()
screen.onkey(move_forward, "Up") # 화살표 위 key 누를시 위로 이동
screen.onkey(move_backward, "Down") # 화살표 위 key 누를시 위로 이동
screen.onkey(turn_left, "Left") # 화살표 위 key 누를시 위로 이동
screen.onkey(turn_right, "Right") # 화살표 위 key 누를시 위로 이동
screen.onkey(move_random, "c") # 화살표 위 key 누를시 위로 이동
screen.onkey(change_color_to_black, "b") # 화살표 위 key 누를시 위로 이동
screen.onkey(change_color_red, "r") # 화살표 위 key 누를시 위로 이동
screen.onkey(change_color_red_black_exchange, "i") # 화살표 위 key 누를시 위로 이동
screen.onkey(change_color, "t") # t key 누를시 

# 이벤트 루프를 시작합니다.
screen.mainloop()