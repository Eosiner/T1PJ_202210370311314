import socket

if __name__ == "__main__":
    
    ip = "localhost"
    port = 9806

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip, port))
    server.listen(1)

    print("Menunggu koneksi...")

    conn, addr = server.accept()
    print("Terhubung dengan:", addr)

    data = conn.recv(1024)
    data = data.decode("utf-8")

    print("Data diterima:", data)

    conn.send(bytes("Data diterima oleh server", "utf-8"))
    conn.close()
