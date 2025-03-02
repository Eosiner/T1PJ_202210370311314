from datetime import datetime

def hitung_umur(tahun_lahir):
    return datetime.now().year - tahun_lahir

if __name__ == "__main__":
    tahun = int(input("Tahun Lahir: "))
    print(f"Umur Anda: {hitung_umur(tahun)} tahun")
