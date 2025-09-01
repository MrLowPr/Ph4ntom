# Phantom – Stealth Network Scanner

**Versi:** 1.0  
**Author:** Solfegio T.P 

## Deskripsi
**Phantom** adalah alat stealth network scanner untuk pemetaan subnet dan port.  
Mendukung berbagai mode scan: **root SYN scan**, **non-root TCP connect scan**, dan mode **efisien + stealth** untuk meminimalkan deteksi firewall.  
Hasil scan bisa disimpan dalam **TXT** dan **JSON** untuk analisis atau integrasi lebih lanjut.

## Fitur
- Scan subnet lengkap dengan berbagai mode (root/non-root, stealth/cepat)  
- Output hasil scan ke terminal maupun file (TXT & JSON)    
- Mendukung root/non-root execution sesuai hak akses pengguna  
- Efisien dan fleksibel untuk berbagai skenario pengintaian jaringan legal  

## Instalasi
1. Pastikan Python 3.x terinstall  
2. Install dependencies:
   ```bash
   pip install python-nmap
