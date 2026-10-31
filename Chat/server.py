from socket import *
import threading

from customtkinter import CTkTextbox

client_socket = socket(AF_INET, SOCK_STREAM)
name = input("Введіть ім'я: ")
client_socket.connect(('4.tcp.eu.ngrok.io', 20450))
client_socket.send(name.encode())

chat_box = CTkTextbox(main_frame)
chat_box.pack(expand='true', fill='both', pady=(5))

def send_message():
   while True:
       client_message = input()
       if client_message.lower() == 'exit':
           client_socket.close()
           break
       client_socket.send(client_message.encode())


threading.Thread(target=send_message).start()
while True:
   try:
       message = client_socket.recv(1024).decode().strip()
       if message:
           print(message)
   except:
       break