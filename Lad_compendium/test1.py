a = input("첫 번째 값을 입력 하세요:\n")
if "." in a:
    a = float(a)
else:
    a = int(a)
    
b = input("두 번째 값을 입력 하세요:\n")
if "." in b:
    b = float(b)
else:
    b = int(b)
c = input("연산자를 선택 하세요 (+, -, *, / 중 하나 입력):\n")
if c == "+": # 연산자에 따라 if문 설정
    f = a + b
    m = input("결과 값 자료형 (integer, float, string 중 하나 입력)\n")
    if m == "integer": # 자료형 선택한거에 따라 f 자료형 변경
        f = int(f)
    elif m == "float":
        f = float(f)
    else:
        f = str(f)
    print(f"결과 값은 아래와 같습니다.\n{a} {"+"} {b} {"="} {f}")
elif c == "-": # 위에 주석 반복
    f = a - b
    m = input("결과 값 자료형 (integer, float, string 중 하나 입력)\n")
    if m == "integer":
        f = int(f)
    elif m == "float":
        f = float(f)
    else:
        f = str(f)
    print(f"결과 값은 아래와 같습니다.\n{a} {"-"} {b} {"="} {f}")
elif c == "*":
    f = a * b
    m = input("결과 값 자료형 (integer, float, string 중 하나 입력)\n")
    if m == "integer":
        f = int(f)
    elif m == "float":
        f = float(f)
    else:
        f = str(f)
    print( f"결과 값은 아래와 같습니다.\n{a} {"*"} {b} {"="} {f}")
else:
    f = a // b
    m = input("결과 값 자료형 (integer, float, string 중 하나 입력)\n")
    if m == "integer":
        f = int(f)
    elif m == "float":
        f = float(f)
    else:
        f = str(f)
    print(f"결과 값은 아래와 같습니다.\n{a} {"/"} {b} {"="} {f} ")