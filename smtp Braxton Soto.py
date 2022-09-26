from socket import *
import logging
logging.basicConfig(filename="Braxton's smtp.txt", level=logging.INFO) # Creates the logging file

# This is not a well formed email message (see RFC2822)
msg = "\r\n I love computer networks!"

# This -is- the correct way to end a message after the data command
endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = "simplesmtp.thought.net"
mailport = 8025 # "fill me in"


# Create socket called clientSocket and establish a TCP connection with mailserver
#Fill in start
clientSocket = socket(AF_INET, SOCK_STREAM) #Creates the client socket
clientSocket.connect((mailserver, mailport)) #Creates the TCP connection to the mailserver
logging.info("clientSocket.connect((simplesmtp.thought.net, 8025))") # This and all subsequent logging.info commands writes to the logging file
#Fill in end

# NOTE: you should write better handling for return messages. The
# code below might work, but it does NOT handle multiline responses.
# Please consult RFC5321 for details.

recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')
logging.info(recv)

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
logging.info("HELO Alice\r\n")
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')
logging.info(recv1)

# Send MAIL FROM command and print server response.
# Fill in start
mailFrom = 'MAIL FROM:<test>\r\n' # Stores the MAIL FROM: command
clientSocket.send(mailFrom.encode()) # Sends the MAIL FROM: command
logging.info("MAIL FROM:<test>\r\n")
recv1 = clientSocket.recv(1024).decode() # Stores the return message from the server
print(recv1) # Prints the return message from the server
if recv1[:3] != '250': # Handles the event that we do not receive a 250 response
    print('250 reply not received from server.')
logging.info(recv1)
    
# Fill in end

# Send RCPT TO command and print server response.
# Fill in start
mailTo = 'RCPT TO: <jasonwright>\r\n' # Stores the RCPT TO: command
clientSocket.send(mailTo.encode()) # Sends the RCPT TO: command
logging.info("RCPT TO: <jasonwright>\r\n")
recv1 = clientSocket.recv(1024).decode() # Stores the return message from the server
print(recv1) # Prints the return message from the server
if recv1[:3] != '250': # Handles the event that we do not receive a 250 response
    print('250 reply not received from server.')
logging.info(recv1)
# Fill in end

# Send DATA command and print server response.
# Fill in start
data = 'DATA \r\n' # Stores the DATA command
clientSocket.send(data.encode()) # Sends the DATA command
logging.info("DATA \r\n")
recv1 = clientSocket.recv(1024).decode() # Stores the return message from the server
print(recv1) # Prints the return message from the server
if recv1[:3] != '354': # Handles the event that we do not receive a 354 response
    print('354 reply not received from server.')
logging.info(recv1)
# Fill in end

# Send message data.
# Fill in start
msg1 = 'Subject: Test <test>\nDate: Sun, 18 Sep 2022 13:16:01\nMessage-ID: <test@test.net> \n\nI am currently testing my smtp client.;' # String I will send containing subject and body of email'
print(msg1)
clientSocket.send(msg1.encode()) # Sends msg1 to the server
logging.info(msg1)

# Fill in end

# Message ends with a single period.
# Fill in start
clientSocket.send(endmsg.encode()) # Sends endmsg to the server, signalling the end of the msg
print(endmsg)
logging.info(endmsg)
recv1 = clientSocket.recv(1024).decode() # Stores the return message from the server
print(recv1) # Prints the return message from the server
if recv1[:3] != '250': # Handles the event that we do not receive a 250 response
  print('250 reply not received from server.')
logging.info(recv1)
# Fill in end

# Send QUIT command and get server response.
# Fill in start
clientSocket.send('QUIT \r\n'.encode()) # Sends the quite command that terminates connection
logging.info("QUIT \r\n")
recv1 = clientSocket.recv(1024).decode() # Stores the return message from the server
print(recv1)
if recv1[:3] != '221': # Handles the event that we do not receive a 221 response
    print('221 reply not received from server.')
logging.info(recv1)
# Fill in end

