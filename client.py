import socket
import struct

server_addr = '192.168.1.101'
server_port = 9998
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((server_addr, server_port))


def recvall(sock, n):
    data = ''
    while len(data)<n:
        packet = sock.recv(n-len(data))
        if not packet:
            return None
        data += packet
    return data


def receive(sock):
    raw_msglen =  recvall(sock,4)
    if not raw_msglen:
        return None
    msglen = struct.unpack('>I',raw_msglen)[0]
    return recvall(sock,msglen)


r = receive(client)
print r


