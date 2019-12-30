import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 8000))
server.listen()



def handle_sock(sock, addr):
    while True:
        data = sock.recv(1024)
        print(data.decode('utf-8'))
        re_data = input()
        sock.send(re_data.encode('utf-8'))



# 获取从客户端发送的数据
while True:
    sock, addr = server.accept()  # 接收到一个用户后, 启动一个多线程
    client_thread = threading.Thread(target=handle_sock, args=(sock, addr))
    client_thread.start()

    # data = sock.recv(1024)  # 一次接收1k的数据
    # print(data.decode('utf-8'))
    # # encode, str -> bytes
    # # decode, bytes -> str
    # re_data = input()
    # sock.send(re_data.encode('utf-8'))
    # server.close()
    # sock.close()