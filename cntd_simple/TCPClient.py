from socket import *
serverName = 'hostname'
serverPort = 12000

# The socket is created as TCP
clientSocket = socket(AF_INET, SOCK_STREAM)

# The client 'knocks' on the server welcome port
# Here a handshake process occurs
clientSocket.connect((serverName, serverPort))
sentence = input('Input lowercase sentence:')

# Client send its message to the server exclusive TCP connection
clientSocket.send(sentence)

# Client awaits for the modified message
modifiedSentence = clientSocket.recv(1024)
print 'From Server:', modifiedSentence

# Non-persistent TCP connection
clientSocket.close()
