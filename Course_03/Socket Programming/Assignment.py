import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

conn.connect(('data.pr4e.org',80))

url = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()

conn.send(url)

while True:
    data = conn.recv(512)

    if(len(data) < 1):
        break
    print(data.decode())

conn.close()