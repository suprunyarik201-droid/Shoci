import socket
import threading

import sock
from customtkinter import *


# HOST = "localhost"
# PORT = 8080
#
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sock.connect((HOST, PORT))


win = CTk()
win.geometry("400x350")


menu = CTkFrame(win, width=140)
set_appearance_mode("dark")

name_label = CTkLabel(menu, text="Ім'я")
name_label.pack(pady=5)


name_entry = CTkEntry(menu)
name_entry.insert(0, "JoJo")
name_entry.pack(padx=10)

all_buttons = []

def set_theme(val):
  if val == "синій":
      btn_color = "#292f8f"
      box_color = "#0d1480"
      theme_menu.configure(fg_color=btn_color)
      menu.configure(fg_color=box_color)
      for btn in all_buttons:
          btn.configure(fg_color=btn_color)
          chat_box.configure(fg_color=box_color)

  elif val == "фіолетовий":
      btn_color = "#7f3eb8"
      box_color = "#47097d"
      theme_menu.configure(fg_color=btn_color)
      menu.configure(fg_color=box_color)
      for btn in all_buttons:
          btn.configure(fg_color=btn_color)
          chat_box.configure(fg_color=box_color)

  elif val == "зелений":
      btn_color = "#4f9c51"
      box_color = "#264726"
      theme_menu.configure(fg_color=btn_color)
      menu.configure(fg_color=box_color)
      for btn in all_buttons:
          btn.configure(fg_color=btn_color)
          chat_box.configure(fg_color=box_color)


theme_menu = CTkOptionMenu(menu, values=["фіолетовий", "синій", "зелений"], command=set_theme)
theme_menu.pack(side="bottom", pady=10)




def toggle_menu():
  if menu.winfo_ismapped():
      menu.pack_forget()
  else:
      menu.pack(side="left", fill="y")




main_frame = CTkFrame(win, fg_color="transparent")
main_frame.pack(side="right", expand=True, fill="both", padx=5, pady=5)


menu_btn = CTkButton(main_frame, text="☰", width=30, command=toggle_menu)
menu_btn.pack(anchor="w")
all_buttons.append(menu_btn)


chat_box = CTkTextbox(main_frame)
chat_box.pack(expand=True, fill="both", pady=5)




def send_message():
  text = msg_entry.get()
  name = name_entry.get()
  full_text = name + ": " + text


  chat_box.insert("end", "Я: " + text + "\n")
  sock.sendall(full_text.encode())
  msg_entry.delete(0, "end")




input_frame = CTkFrame(main_frame, fg_color="transparent")
input_frame.pack(fill="x")


msg_entry = CTkEntry(input_frame, placeholder_text="Повідомлення...")
msg_entry.pack(side="left", expand=True, fill="x", padx=(0, 5))


send_btn = CTkButton(input_frame, text=">", width=40, command=send_message)
send_btn.pack(side="right")
all_buttons.append(send_btn)


# def receive():
#    while True:
#        data = sock.recv(1024)
#        chat_box.insert("end", data.decode() + "\n")




# threading.Thread(target=receive, daemon=True).start()
win.mainloop()

