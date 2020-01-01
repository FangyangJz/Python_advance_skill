import socket
import threading

bind_host = "0.0.0.0"
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_host, bind_port))
server.listen(5)
print(f"[*] Listing on {bind_host, bind_port}")


def handle_client(client_socket):
    request = client_socket.recv(1024)
    print(f"[*] Received :{request}")
    client_socket.send("ACK!".encode("utf-8"))
    client_socket.close()


while True:
    client, addr = server.accept()
    print(f"[*] Accepted connection from : {addr[0]}:{addr[1]}")
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()
