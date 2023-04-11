import socket
import logging
import threading

logging.basicConfig(level=logging.DEBUG)

services = ['djxmmx.net', 'time.nist.gov', 'tcpbin.com']
ports = [17, 13, 4242]


for i in range(3):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((services[i], ports[i]))
    logging.info("Connecting to service: {} on port (${})".format(services[i], ports[i]))
    if(services[i] == 'tcpbin.com'):
        s.send("Can you hear me?\n".encode())
        s.settimeout(5)
    data = s.recv(1024)
    logging.debug("Receiving data")
    s.close()
    logging.debug("Closing connection")
    print("received data:", data.decode())
    logging.info("Printing data")
