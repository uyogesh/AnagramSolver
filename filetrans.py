import socket
import os
import struct

file_to_send = 'avi.jpg'
path = os.path.join(os.environ['HOME'], '/Desktop/weeding of parash')
filename = os.path.join(path, file_to_send)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('192.168.1.101', 9998))
# server.setsockopt(socket.SO_REUSEADDR,socket.SO)
server.listen(4)


def send(sock, msg):
    msg = struct.pack('>I',len(msg)) + msg
    sock.sendall(msg)

try:
    client = server.accept()
    with open(filename, 'r') as f:
        d = f.read()
        # data = len(d)
        # total_sent = 0
        # while total_sent < data:
        #     sent = client.send(d[total_sent:])
        #     if sent == 0:
        #         raise RuntimeError('Error at the socket...')
        #     total_sent += sent
        send(server, d)
    server.close()
    print 'Finished Successfully'
except Exception:
    server.close()
    raise Exception(str(Exception.message))