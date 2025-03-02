import socket
import threading

def receive_messages(client):
    """Menerima pesan dari server dan menampilkannya."""
    while True:
        try:
            pesan = client.recv(1024).decode("utf-8")
            if not pesan:
                break
            print(f"\n{pesan}", flush=True)
        except:
            break

ip = "localhost"
port = 9806

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((ip, port))

nama = input(client.recv(1024).decode("utf-8"))  # Pastikan input dieksekusi
client.send(nama.encode("utf-8"))

thread = threading.Thread(target=receive_messages, args=(client,))
thread.start()

while True:
    pesan = input()  
    client.send(pesan.encode("utf-8"))
    if pesan.lower() == "exit":
        break

client.close()
