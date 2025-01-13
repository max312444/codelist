import socket

# 서버 소켓 생성
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 서버 IP와 포트 바인딩
server_socket.bind(('210.101.236.189', 12345))  # 서버의 IP 주소와 포트
server_socket.listen(1)  # 최대 1개의 클라이언트 대기
print("서버가 실행 중입니다. 클라이언트를 기다리는 중...")

# 클라이언트 연결 수락
client_socket, addr = server_socket.accept()
print(f"클라이언트가 연결되었습니다: {addr}")

# 데이터 송수신
while True:
    try:
        data = client_socket.recv(1024).decode()  # 클라이언트로부터 데이터 수신
        if not data:  # 데이터가 없으면 연결 종료
            break
        print(f"클라이언트로부터 받은 메시지: {data}")
        client_socket.sendall(f"서버 응답: {data}".encode())  # 클라이언트로 응답
    except ConnectionResetError:
        print("클라이언트와의 연결이 종료되었습니다.")
        break

# 연결 종료
client_socket.close()
server_socket.close()
