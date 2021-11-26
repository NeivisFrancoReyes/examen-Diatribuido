# -*- coding: utf-8 -*-
"""
Created and adapted on Fri Nov 4 14:44:26 2021
@author: Willian
"""


import socket
import sys


HOST = '10.0.0.53'                 # Symbolic name meaning all available interfaces
PORT = 50007  
mBuffer=1024


# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect the socket to the port where the server is listening


print('Conectando con el servidor up on {} port {}'.format(HOST, PORT))

sock.connect((HOST, PORT))

try:

    # Send data
    message = ' '.join(sys.argv[1:]) or 'Mensaje de prueba que se envia al servidor y retorna al cliente'
    
    print('Enviando {!r}'.format(message))
    sock.sendall(str.encode(message))
    
    # Look for the response
    amount_received = 0
    amount_expected = len(message)
    print("Longitud del mensaje:",amount_expected )
    while amount_received < amount_expected:
         data = sock.recv(mBuffer)
         amount_received += len(data)
         print('received {!r}'.format(data))
    
finally:
    print('closing socket')
    sock.close()

