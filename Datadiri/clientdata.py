import socket

if __name__ == "__main__":
    
    ip = "localhost"
    port = 9806

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ip, port))

    nama = input("Nama: ")
    nim = input("NIM: ")
    tahun = input("Tahun Lahir: ")

    client.send(bytes(f"{nama}, {nim}, {tahun}", "utf-8"))

    buffer = client.recv(1024)
    buffer = buffer.decode("utf-8")

    print("Server:", buffer)
