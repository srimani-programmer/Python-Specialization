import socket

# Creating a Connection Object
conn = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# Connecting to the Required Server
conn.connect(('data.pr4e.org', 80))

# Our Required URL
url = 'GET http://data.pr4e.org/cover.jpg HTTP/1.0\r\n\r\n'.encode()

# Sending the request
conn.send(url)

# Now Revceiving the data

while True:
    data = conn.recv(512)

    if(len(data) < 1):
        break
    print(data.decode())

conn.close()