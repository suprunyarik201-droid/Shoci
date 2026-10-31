from customtkinter import *
import socket
import threading

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("localhost", 8080))


win = CTk()
win.geometry("400x350")
win.title("Tusk ACT 4")
menu = CTkFrame(win, width=140)

name_label = CTkLabel(menu, text="Ім'я")
name_label.pack()

name_entry = CTkEntry(menu, width=140)
name_entry.pack()

def set_theme(val):
    if val == "Артьомка":
        set_appearance_mode("dark")
    else:
        set_appearance_mode("light")



themes = CTkOptionMenu(menu, values=["Артьомка", "Свєта"], command=set_theme)
themes.pack()

main_frame = CTkFrame(win, width=140)

def toggle_menu():
    if menu.winfo_ismapped():
        menu.pack_forget()
    else:
        menu.pack(side="left", fill="y")

menu_btn = CTkButton(win, text="^_^", width=30, command=toggle_menu)
menu_btn.pack(anchor="w")

main_frame = CTkFrame(win, width=140)
main_frame.pack(side="right", fill="both", expand=True, padx=5, pady=5)

entry_message = CTkEntry(main_frame)
entry_message.pack(side="left", expand=True, fill="x")

chat_box = CTkTextbox(main_frame)
chat_box.pack(expand='true', fill='both', pady=(5))

def send_message():
    text = entry_message.get()
    name = name_entry.get()
    full_text = name + ": " + text

    chat_box.insert("END", full_text + "\n")
    sock.sendall(full_text.encode())
    entry_message.delete(0, 'end')


send_btn = CTkButton(main_frame, text=">", width=30, command=send_message)
send_btn.pack(side="right",)

def receive_message():
    while True:
        data = sock.recv(1024)
        chat_box.insert("end", data.decode()+ "\n")

threading.Thread(target=receive_message).start()



win.mainloop()


