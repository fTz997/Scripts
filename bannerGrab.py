#!/usr/bin/python
import socket
ip = raw_input("Digite o IP: ")
porta = input("Digite a porta:")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(ip,porta)
banner = s.recv(1024)

print (banner)

