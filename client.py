#!/usr/bin/python3

import socket

HOST = "www.google.com"
PORT = 80
BUFFER_SIZE = 1024

payload = f"GET / HTTP/1.0 \r\nHOST: {HOST}\r\n\r\n"


def getRequest(addr):
    (family, socktype, proto, canonname, sockaddr) = addr
    try:
        s = socket.socket(family, socktype, proto)
        s.connect(sockaddr)
        s.sendall(payload.encode())
        s.shutdown(socket.SHUT_WR)

        fulldata = b''
        while True:
            data = s.recv(BUFFER_SIZE)
            fulldata += data
            if not data: 
                break

        print(fulldata)

    except Exception as e:
        print(e)
    finally:
        s.close()


def main():
    addr_info = socket.getaddrinfo(HOST, PORT)

    for addr in addr_info:
        (family, socktype, proto, canonname, sockaddr) = addr 
        if family == socket.AF_INET and socktype == socket.SOCK_STREAM:
            print(addr)
            getRequest(addr)


if __name__ == "__main__":
    main()
