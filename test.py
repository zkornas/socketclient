import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('tcpbin.com', 4242))
s.send('Hello'.encode())
data = s.recv(1024)
s.close()
print("received data:", data.decode())