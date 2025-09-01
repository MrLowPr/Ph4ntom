## Instalasi
Pastikan Python 3.x sudah terinstall, buat virtual environment opsional, install dependencies, dan Nmap:  

```bash
# Cek versi Python
python --version

# Buat virtual environment (opsional tapi disarankan)
python -m venv venv
# Aktifkan:
# Windows
venv\Scripts\activate
# Linux/macOS
source venv/bin/activate

# Install dependency python-nmap
pip install python-nmap

# Install Nmap
# Windows: download dari https://nmap.org/download.html
# Linux (Debian/Ubuntu):
sudo apt install nmap
# macOS (Homebrew):
brew install nmap

# JALANKAN!
python3 phantom.py
# Cek instalasi Nmap
nmap --version
