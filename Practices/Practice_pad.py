# 파일 읽기 예제
# with open('example.txt', 'r') as file:
#     content = file.read()
#     print(content)

# 파일 쓰기 예제
# with open('example.txt', 'w') as file:
#     file.write("Hello, world!")

# 파일에 내용 추가 예제
# with open('example.txt', 'a') as file:
#     file.write("\nHello, world!")

# 파일 읽고 수정하기 예제
# with open('example.txt', 'r+') as file:
#     content = file.read()
#     print('Original Content:', content)
#     file.seek(0) # 파일의 시작 위치로 포인터 이동
#     file.write('Updated Content')
    
# 파일 쓰고 읽기 예제
with open('example.txt', 'w+') as file:
    file.write('New Content')
    file.seek(0)
    print(file.read())