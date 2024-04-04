from socket import *
serverPort = 12000
serverSocket = socket(IF_INET, SOCK_DGRAM)

# Associate the server socket with its port
serverSocket.bind(('', serverPort))
print "The server is ready to receive"
while 1:
    # Get the message send from the client and the client IP address
    # It knows the message reached its end when a /0 char is read
    message, clientAddress = ServerSocket.recvfrom(2048)
    modifiedMessage = message.upper()

    # Uses the client IP address to send the modified message
    serverSocket.sendto(modifiedMessage, clientAdress)
