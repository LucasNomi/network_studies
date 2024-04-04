from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('',serverPort))

# Server listen to its welcome port for any client
# the parameter specifies the maximum number of queued connections
serverSocket.listen(1)
print 'The server is ready to receive'
while 1:
    # Server accepts the connection and creates a exclusive TCP connection
    connectionSocket, addr = serverSocket.accept()
    
    # Sentence send by the client arrives at the exclusive TCP connection socket
    sentence = connectionSocket.recv(1024)
    capitalizedSentence = sentence.upper()

    # The modified sentence is send using the connection socket
    connectionSocket.send(capitalizedSentence)

    # The connection socket is closed
    connectionSocket.close()
