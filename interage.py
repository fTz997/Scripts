#!/usr/bin/python
# banner grabbing script exemplo em um serviço ftp

import socket
print ("Interagindo com o FTP Server")
ip = raw_input("Digite o IP:")
porta = 21

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip,porta))
banner = s.recv(1024)
print (banner)

print ("Enviando usuario")
s.send("USER victor \r\n")
banner = s.recv(1024)
print (banner)

print ("Enviando senha")
s.send("PASS victor \r\n")
banner = s.recv(1024)
print (banner)
