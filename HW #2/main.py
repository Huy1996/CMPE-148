#import socket module
from socket import *
import sys # In order to terminate the program
serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
#Fill in start
serverHost = '192.168.1.4'
serverPort = 9999   #port less than 65535
serverSocket.bind((serverHost, serverPort))
serverSocket.listen(1)

#Fill in end
while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:
        print("about to receive data")
        message = connectionSocket.recv(4096) #buffer size

        print("received ", message)
        filename = message.split()[1] #get "hello.html" from b'GET /hello.html HTTP/1.1\r\nHost..'
        f = open(filename[1:])
        outputdata = f.read() #Fill in start #Fill in end
        print("outputdata", outputdata)

        #Send one HTTP header line into socket
        #Fill in start
        connectionSocket.send(b"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n") #respone to client
        connectionSocket.send(b"\r\n")  # Empty line-Data termination
        print("sent HTTP/1.x 200 OK")
        #Fill in end

        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
            # print("sent ", outputdata[i])
        connectionSocket.send(b"\r\n") #Data termination

        connectionSocket.close()
    except IOError as e:
        print("IOE exception ", e)
        #Send response message for file not found
        #Fill in start
        connectionSocket.send(b"HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n")
        connectionSocket.send(b"<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n")
        # connectionSocket.send(b"\r\n") #Data termination
        #Fill in end

        #Close client socket
        #Fill in start
        connectionSocket.close()
        #Fill in end

serverSocket.close()
sys.exit()