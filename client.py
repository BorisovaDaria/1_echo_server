import socket
import time
from enum import Enum

def main():

    sock = socket.socket()
    sock.setblocking(True)
    sock.connect(('localhost', 9090))
    log(LogType.CONNECTED)

    msg = ''

    while msg != 'exit':
        msg = input()
        sock.send(msg.encode())
        log(LogType.DATA_SENT)

        data = sock.recv(1024)
        log(LogType.DATA_RECEIVED)

        print(data.decode())


    sock.close()
    log(LogType.DISCONNECTED)



class LogType(Enum):
    CONNECTED = "Connected to server"
    DISCONNECTED = "Disconnected from server"
    DATA_SENT = "Data sent to server"
    DATA_RECEIVED = "Data received from server"

def log(log_type: LogType):
    print("[" + log_type.value + "; " + str(time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime())) + "]")

main()
