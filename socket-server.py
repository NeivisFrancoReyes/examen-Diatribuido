"""
Created and adapted on Fri Nov 4 14:44:26 2021
@author: Willian
"""
import socket
import json
import base64

from bson.objectid import ObjectId
from urllib.parse import quote_plus
from pymongo import MongoClient
# Bind the socket to the port


HOST = '10.0.0.53'                 # Symbolic name meaning all available interfaces
PORT = 50007  
mBuffer=1024
ExamenDis = "examen"
client = MongoClient ("mongodb://127.0.0.1:27017/?readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false")
BD = client [ExamenDis]



# Create TCP Socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print('Iniciando el servidor up on {} port {}'.format(HOST, PORT))
sock.bind((HOST, PORT))
# Listen for incoming connections
sock.listen(1)


while True:
    # espera la conn.
    print('Esperando conectar con un cliente')
    connection, client_address = sock.accept()
    try:
        print('Conectado desde', client_address)

        # Receive the data in small chunks and retransmit it
        while True:
            print('espererando respuestas')
            data = connection.recv(mBuffer)#16
            
            print('Recibiendo dato: {!r}'.format(data), "Typo:", type (data))
            estudiantes = BD.Alumnos.find_one({'_id': ObjectId(data.decode("utf-8"))})
            message=str(estudiantes["cedula"])
            print("output_byte", message)
            
            datamen=str.encode(message)
            
            
            if data:
                print('Enviando respuesta al cliente')
                connection.sendall(datamen)
            else:#No existe datos, client_address
                break
    except KeyboardInterrupt:
        break
    finally:
        # Clean up the connection
        connection.close()

  