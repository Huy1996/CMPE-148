from socket import *
import base64
import ssl
import time

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

username =  "breakoutroom.spring2022@gmail.com"
password = "thisispassword"
email_to = "*******@sjsu.edu" # recepient email account


def main():

# Choose a mail server (e.g. Google mail server) and call it mail server
    #Fill in start
    # google mail server: https://support.google.com/mail/answer/7126229?hl=en
    mailServer = "smtp.gmail.com" #loop back address 127.0.0.1
    mailPort = 465
    # Fill in end


    context = ssl.create_default_context()

    with create_connection((mailServer, mailPort)) as sock:
        clientSocket = context.wrap_socket(sock, server_hostname=mailServer)

# Create socket called clientSocket and establish a TCP connection with mailserver
    #Fill in start

    recv = clientSocket.recv(1024).decode()
    print(recv)
    if recv[:3] != '220':
        print('220 reply not received from server.')

 #Fill in end

# Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    print(recv1)
    if recv1[:3] != '250':
         print('250 reply not received from server.')


    #Info for username and password
    base64_str = ("\x00"+username+"\x00"+password).encode()
    base64_str = base64.b64encode(base64_str)
    authMsg = "AUTH PLAIN ".encode()+base64_str+"\r\n".encode()
    clientSocket.send(authMsg)
    recv_auth = clientSocket.recv(1024)
    print(recv_auth.decode())

# Send MAIL FROM command and print server response.
    mailFrom = "MAIL FROM:<{}>\r\n".format(username)
    clientSocket.send(mailFrom.encode())
    recv2 = clientSocket.recv(1024)
    recv2 = recv2.decode()
    print("Server respond to MAIL FROM: "+recv2)

# Send RCPT TO command and print server response.
    rcptTo = "RCPT TO:<{}>\r\n".format(email_to)
    clientSocket.send(rcptTo.encode())
    recv3 = clientSocket.recv(1024)
    recv3 = recv3.decode()
    print("Server respond to RCPT TO: "+recv3)

# Send DATA command and print server response.
    data = "DATA\r\n"
    clientSocket.send(data.encode())
    recv4 = clientSocket.recv(1024)
    recv4 = recv4.decode()
    print("Server respond to DATA: "+recv4)

    # Send message data.
    # Message ends with a single period.
    subject = "Subject: testing my client\r\n\r\n"
    clientSocket.send(subject.encode())

    date = time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime())
    date = date + "\r\n\r\n"
    clientSocket.send(date.encode())
    clientSocket.send(msg.encode())
    clientSocket.send(endmsg.encode())
    recv_msg = clientSocket.recv(1024)
    print("Response after sending message body:"+recv_msg.decode())

# Send QUIT command and get server response.
    quit = "QUIT\r\n"
    clientSocket.send(quit.encode())
    recv5 = clientSocket.recv(1024)
    print(recv5.decode())
    clientSocket.close()

if __name__ == '__main__':
     main()
