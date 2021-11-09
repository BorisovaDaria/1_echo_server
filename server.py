import socket, time
from enum import Enum


def main():
	sock = socket.socket()
	sock.bind(('', 9090))
	log(LogType.SERVER_STARTED)

	sock.listen(0)
	log(LogType.START_LISTEN)

	conn, addr = sock.accept()
	log(LogType.CLIENT_CONNECTED, addr)

	msg = ''

	while True:
		data = conn.recv(1024)
		if not data:
			break
		log(LogType.DATA_RECEIVED)
		msg += data.decode()
		conn.send(data)
		log(LogType.DATA_SENT)

	print(msg)

	conn.close()
	log(LogType.CLIENT_DISCONNECTED)


class LogType(Enum):
	SERVER_STARTED = "Server started"
	START_LISTEN = "Start listening"
	CLIENT_CONNECTED = "Client connected"
	DATA_RECEIVED = "Data received"
	DATA_SENT = "Data sent"
	CLIENT_DISCONNECTED = "Client disconnected"
	SERVER_STOPPED = "Server stopped"


def log(log_type: LogType, ip: tuple = None):
	if ip != None:
		print("[" + log_type.value + "; " + str(time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime())) + "; " + str(ip) + "]")
	else:
		print("[" + log_type.value + "; " + str(time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime())) + "]")



if __name__ == '__main__':
	main()
