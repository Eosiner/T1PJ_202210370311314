import socket
import threading

clients = {}
lock = threading.Lock()


def broadcast(message, sender_conn=None):
    """Mengirim pesan ke semua client kecuali pengirimnya."""
    with lock:
        for conn in clients.values():
            if conn != sender_conn:
                try:
                    conn.send(message.encode("utf-8"))
                except:
                    pass


def handle_client(conn, addr):
    """Mengelola komunikasi dengan satu client"""
    conn.send("Masukkan nama Anda: ".encode("utf-8"))
    nama_client = conn.recv(1024).decode("utf-8")

    with lock:
        clients[nama_client] = conn
    print(f"\n{nama_client} ({addr}) bergabung dalam chat.")
    broadcast(f"{nama_client} telah bergabung dalam chat.", conn)
    try:
        while True:
            buffer = conn.recv(1024).decode("utf-8")
            if not buffer:
                break
            if buffer.lower() == "exit":
                print(f"\n{nama_client} keluar...")
                conn.send("Sesi chat selesai.".encode("utf-8"))
                break
            pesan = f"[{nama_client}]: {buffer}"
            print(pesan)
            broadcast(pesan, conn)
    except:
        pass

    conn.close()
    with lock:
        del clients[nama_client]

    print(f"{nama_client} keluar dari chat.")
    broadcast(f"{nama_client} telah keluar dari chat.")


def server_chat():
    """Memungkinkan server untuk mengirim pesan ke client."""
    while True:
        pesan = input()
        if pesan.lower() == "exit":
            print("Server keluar...")
            broadcast("Server telah keluar.")
            break
        broadcast(f"[Server]: {pesan}")


if __name__ == "__main__":
    ip = "localhost"
    port = 9806

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((ip, port))
    server.listen()
    print(f"Server berjalan di {ip}:{port}\nMenunggu client...")
    threading.Thread(target=server_chat, daemon=True).start()
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
