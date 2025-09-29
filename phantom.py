import nmap
import json
import getpass
import os
import time

# Helper untuk convert bytes ke string
def bytes_to_str(obj):
    if isinstance(obj, bytes):
        return obj.decode(errors="replace")
    elif isinstance(obj, dict):
        return {k: bytes_to_str(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [bytes_to_str(i) for i in obj]
    else:
        return obj

ascii_art = r"""
______ _   _   ___  _   _ _____ ________  ___
| ___ \ | | | /   || \ | |_   _|  _  |  \/  |
| |_/ / |_| |/ /| ||  \| | | | | | | | .  . |
|  __/|  _  / /_| || . ` | | | | | | | |\/| |
| |   | | | \___  || |\  | | | \ \_/ / |  | |
\_|   \_| |_/   |_/\_| \_/ \_/  \___/\_|  |_/
                                             
                                                             
                                --Ph4ntom Network
Recon Tool v1.0 by MrLowPr
"""
print(ascii_art)

print("Pilih mode scan:")
print("1. Recon subnet + root (SYN scan stealth)")
print("2. Efisien non-root (TCP connect scan)")
print("3. Efisien + root (SYN scan cepat)")
print("4. Recon subnet + root stealth + minim deteksi firewall")

choice = input("Masukkan pilihan (1-4): ").strip()

mode_descriptions = {
    "1": "Opsi 1: SYN scan stealth (root required) – cepat dan stealth, cocok untuk subnet besar.",
    "2": "Opsi 2: TCP connect scan (non-root) – aman tanpa root, tapi lebih mudah terdeteksi firewall.",
    "3": "Opsi 3: SYN scan cepat (root) – cepat, membutuhkan root, tidak terlalu stealth.",
    "4": "Opsi 4: Stealth + minim deteksi firewall (root) – paling stealth, lebih lambat, membutuhkan root."
}
if choice not in mode_descriptions:
    print("Pilihan tidak valid!")
    exit()
print("\nInfo Mode Scan:")
print(mode_descriptions[choice])


log_file = "subnet_history.txt"
if os.path.exists(log_file):
    with open(log_file, "r") as f:
        history = [line.strip() for line in f.readlines()]
else:
    history = []

if history:
    print("\nHistory subnet:")
    for idx, h in enumerate(history, 1):
        print(f"{idx}. {h}")
    print("0. Masukkan subnet baru")

history_choice = input("Pilih subnet dari history atau 0 untuk baru: ").strip()
if history_choice == "0":
    subnet = getpass.getpass("Masukkan subnet target (input tersembunyi): ").strip()
    if subnet not in history:
        with open(log_file, "a") as f:
            f.write(subnet + "\n")
else:
    try:
        subnet = history[int(history_choice)-1]
    except:
        print("Pilihan tidak valid")
        exit()

scan_args_map = {
    "1": "-sS -T3 -Pn",
    "2": "-sT -T4 -Pn",
    "3": "-sS -T4 -Pn",
    "4": "-sS -T2 -Pn --min-rate 50"
}
scan_args = scan_args_map[choice]

nm = nmap.PortScanner()
print(f"\nMemulai scan subnet {subnet} ...\n")
start_time = time.time()

try:
    nm.scan(hosts=subnet, arguments=scan_args)
    end_time = time.time()
    duration = end_time - start_time
    print(f"\nScan selesai dalam {duration:.2f} detik")
    if duration > 60:
        print("⚠️ Scan lama karena banyak host/port atau mode stealth")

    
    for host in nm.all_hosts():
        print(f"Host: {host} ({nm[host].hostname()})")
        print("Status:", nm[host].state())
        if 'tcp' in nm[host]:
            for port in nm[host]['tcp']:
                print(f"Port {port}: {nm[host]['tcp'][port]['state']}")
        print("")

    save_flag = input("Ingin simpan hasil scan? (yes/no): ").strip().lower()
    if save_flag == "yes":
        # TXT
        with open("hasil_scan.txt", "w") as f:
            for host in nm.all_hosts():
                f.write(f"Host: {host} ({nm[host].hostname()})\n")
                f.write(f"Status: {nm[host].state()}\n")
                if 'tcp' in nm[host]:
                    for port in nm[host]['tcp']:
                        f.write(f"Port {port}: {nm[host]['tcp'][port]['state']}\n")
                f.write("\n")
        # JSON
        with open("hasil_scan.json", "w") as f:
            output = nm.get_nmap_last_output()
            json.dump(bytes_to_str(output), f, indent=2)
        print("Hasil scan tersimpan di hasil_scan.txt dan hasil_scan.json")
    else:
        print("Hasil scan tidak disimpan.")

except Exception as e:

    print("Terjadi error saat scan:", e)
