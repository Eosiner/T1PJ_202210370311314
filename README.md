# Socket Programming & Chat Application

## 1. Pengiriman Data ke Socket Server
Program ini mengimplementasikan komunikasi antara **client** dan **server** menggunakan **socket programming** di Python. Data yang dikirim meliputi:

- **Nama**
- **NIM**
- **Tahun Lahir**

Server akan menerima data tersebut dan menampilkannya di terminal.

### **Cara Menjalankan Server**
```bash
python server.py
```

### **Cara Menjalankan Client**
```bash
python client.py
```

---

## 2. Fungsi Menghitung Umur
Program ini juga memiliki fungsi untuk menghitung umur berdasarkan tahun lahir yang dikirimkan oleh client.

Fungsi ini akan menghitung umur berdasarkan tahun lahir yang diberikan.

---

## 3. Aplikasi Chat (Client-Server) dengan Banyak Client
Program ini memungkinkan **banyak client** untuk terhubung ke satu server dan saling mengirim pesan dalam sebuah grup chat.

### **Cara Kerja**
1. **Server** menunggu koneksi dari beberapa client.
2. **Client** menghubungkan diri ke server dan mulai mengirim pesan.
3. Server menerima pesan dari satu client dan menyebarkannya ke semua client yang terhubung.

### **Menjalankan Server**
```bash
python chat_server.py
```

### **Menjalankan Client**
```bash
python chat_client.py
```

Setiap client yang terhubung dapat mengirim dan menerima pesan secara real-time.

---

## **Teknologi yang Digunakan**
- Python 3
- Socket Programming
- Multithreading untuk menangani banyak client

## **Fitur Utama**
✔️ **Pengiriman Data ke Server** (Nama, NIM, Tahun Lahir)  
✔️ **Fungsi Penghitung Umur**  
✔️ **Chat Room dengan Banyak Client**  
✔️ **Pesan Real-Time**  

---

## **Catatan**
Pastikan firewall atau antivirus tidak memblokir port yang digunakan agar komunikasi socket berjalan lancar. Jika terjadi error, coba jalankan ulang server sebelum menjalankan client.

