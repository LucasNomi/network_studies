# import everything from python's socket method
from socket import *

# define the server's address (IP:PORT)
serverName = 'hostname'
serverPort = 12000

# creates the client's socket
# AF_INET defines the address family (IPv4)
# SOCK_DGRAM defines the protocol used for the socket (UDP)
clientSocket = socket(socket.AF_INET, socket.SOCK_DGRAM)
message = input('Input lowercase sentence:')

# Encapsulate the message with the server's address
# Sends the message in the client socket
clientSocket.sendto(message,(serverName, serverPort)

# Waits for server's response
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print modifiedMessage

# Close the socket
clientSocket.close()
