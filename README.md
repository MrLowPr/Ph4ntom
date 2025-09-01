## Instalasi
Pastikan Python 3.x sudah terinstall, buat virtual environment opsional, dan install dependencies requirement:  

```bash
# Persiapan
sudo apt update && sudo apt upgrade -y

# Buat virtual environment (opsional tapi disarankan)
python -m venv venv

Aktifkan:
# Windows
venv\Scripts\activate
# Linux/macOS
source venv/bin/activate

# Penggunaan
1. Masuk ke direktori tempat script berada (Misal: C:/Admin/Tools/Ph4ntom)
lalu lakukan "ls", Temukan file bernama "phantom.py".
2. Install dependency
pip install -r requirements.txt
2. Setelah itu:
python/python3 phantom.py
