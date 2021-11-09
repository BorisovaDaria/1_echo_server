import socket

sock = socket.socket()
sock.setblocking(True)
sock.connect(('localhost', 9090))

msg = input()

sock.send(msg.encode())

data = sock.recv(1024)

sock.close()

print(data.decode())
