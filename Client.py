import socket
T_PORT = 12345
TCP_IP = '127.0.0.1'
BUF_SIZE = 30

sock = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
sock.connect((TCP_IP, T_PORT))
MSG = "Hello karl"
sock.send(MSG.encode())
while True:
	data = sock.recv(BUF_SIZE)
