import sys # 파이썬 인터프리터와 상호작용 기능 제공

# sysy.path 변수의 자료형 출력
print(type(sys.path))

# sys.path 리스트에 있는 각 경로를 출력
for path in sys.path:
    print(path)