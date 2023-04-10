import socket
import logging
import threading

logging.basicConfig(level=logging.DEBUG)

services = ['djxmmx.net', 'time.nist.gov']
ports = [17, 13]


for i in range(2):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((services[i], ports[i]))
    logging.debug("Connecting to service: {} on port (${})".format(services[i], ports[i]))
    if(services[i] == 'tcpbin.com'):
        s.send("Can you hear me?".encode())
    data = s.recv(1024)
    logging.debug("Receiving data")
    s.close()
    logging.debug("Closing connection")
    print("received data:", data.decode())
    logging.debug("Printing data")