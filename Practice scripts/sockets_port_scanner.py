
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

target = '192.168.0.5'

def pscan(port):
    try:
        con = s.connect((target,port))
        return True
    except:
        return False


for x in range(25):
    if pscan(x):
        print('Port',x,'is open')
    else:
        print('Port Closed')