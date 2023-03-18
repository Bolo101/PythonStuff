import socket
from tkinter import *
from cryptography.fernet import Fernet
import threading


key = Fernet.generate_key()
fernet = Fernet(key)


HOST = '255.255.255.255'
PORT = 1234
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('', PORT))
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)


def send_message1():
    message = entry1.get()
    encrypted_message = fernet.encrypt(message.encode())
    s.sendto(encrypted_message, (HOST, PORT))
    entry1.delete(0, END)

def receive_message1():
    while True:
        data, address = s.recvfrom(1024)
        decrypted_message = fernet.decrypt(data).decode()
        label.config(text=label.cget("text") + "\n" + decrypted_message)

root = Tk()
root.title('Encrypted communication')
clientC = Canvas(root, width = 200, height = 200,bg ='red')
clientC.grid(row = 1, column = 1)
serverC = Canvas(root, width = 200, height = 200, bg = 'green')
serverC.grid(row =1, column =0)
nameC = Label(root, text = 'Client side').grid(row = 0, column = 1)
nameS = Label(root, text = 'Server side').grid(row = 0, column = 0)
label = Label(root, text="Message reçu :")
label.grid(row = 1, column = 0)
output = Label(root, text="").grid(row = 1, column =0)
entry1 = Entry(root)
entry1.grid(row = 1, column =1)
send_button = Button(root, text="Envoyer", command=send_message1)
send_button.grid(row = 2,column =1)
disconnect_button = Button(root, text="Déconnecter", command=root.quit)
disconnect_button.grid(row = 3, column = 1)

t = threading.Thread(target=receive_message1)
t.daemon = True
t.start()


root.mainloop()
s.close()