# 🖨️ Epson EcoTank L5290 Suite & Control Center for Linux (Fedora / RHEL)

[![License: GPL v2](https://img.shields.io/badge/License-GPLv2-blue.svg)](https://gnu.org/licenses/gpl-2.0.html)
[![Platform: Linux Fedora](https://img.shields.io/badge/Platform-Fedora%20%7C%20RHEL-informational.svg)](https://fedoraproject.org)
[![Python: 3.x](https://img.shields.io/badge/Python-3.x-green.svg)](https://python.org)

Solusi **Instant Install** dan **Control Center GUI** serbaguna untuk printer **Epson EcoTank L5290** di Linux Fedora dan RedHat Enterprise Linux (RHEL). 

Proyek ini dibuat untuk mengatasi kendala printer yang berstatus *"Need Driver"* di Linux serta menyediakan antarmuka pemeliharaan modern (Head Cleaning & Nozzle Check) tanpa perlu menghafal perintah terminal.

---

## 🌟 Fitur Utama

- ⚡ **Instant RPM Installer**: Mengunduh dan memasang satu file `.rpm` langsung mengonfigurasi driver resmi Epson ESC/P-R dan layanan sistem CUPS.
- 🎨 **Modern Dark-Mode GUI Control Center**: Antarmuka grafis yang elegan, responsif, dan mudah digunakan.
- 🧽 **Auto Head Cleaning**: Melakukan pembersihan kepala cetak secara mendalam (*Head Cleaning*) hanya dengan 1-klik.
- 📝 **Nozzle Check Pattern**: Mencetak pola tes nozzle untuk memeriksa garis putus atau hasil cetak yang bergaris.
- 📋 **Live Activity Log**: Menampilkan log aktivitas dan status koneksi printer secara real-time langsung di dalam aplikasi.
- 🔄 **Auto CUPS Integration**: Mengatur printer secara otomatis sebagai printer utama sistem.

---

## 📦 1. Tata Cara Instalasi Instant (Untuk Pengguna)

Jika Anda ingin langsung menggunakan printer tanpa perlu melakukan kompilasi dari source code, ikuti langkah berikut:

### Langkah A: Unduh Paket `.rpm`
Unduh file installer versi terbaru `epson-l5290-suite-1.0.0-1.fc43.x86_64.rpm` dari menu **[Releases](https://github.com/dosq/epson-l5290-suite/releases)** repositori ini.

### Langkah B: Jalankan Instalasi di Terminal
Buka terminal di folder tempat Anda mengunduh file tersebut, lalu jalankan:

```bash
sudo dnf install -y ./epson-l5290-suite-1.0.0-1.fc43.x86_64.rpm
```

*Selesai! Driver, layanan CUPS, dan Aplikasi GUI secara otomatis sudah terpasang dan siap digunakan.*

---

## 🚀 2. Panduan Penggunaan Aplikasi GUI Control Center

Setelah instalasi selesai, Anda dapat membuka aplikasi **Epson L5290 Utility** dengan 3 cara:

1. **Menu Aplikasi Linux**: Buka launcher aplikasi Fedora (tekan tombol `Super` / Windows) dan cari **"Epson L5290 Utility"**.
2. **Pintasan Desktop**: Klik dua kali (*double-click*) pada ikon **Epson L5290 Utility** di Desktop komputer Anda.
3. **Melalui Terminal**:
   ```bash
   epson-l5290-utility
   ```

### Fungsi Menu di Dalam Aplikasi GUI:
- 🧽 **Head Cleaning**: Klik kartu ini jika hasil cetak Anda samar atau bergaris. Aplikasi akan mengirimkan perintah pembersihan kepala cetak secara otomatis.
- 📝 **Nozzle Check Pattern**: Klik kartu ini untuk mencetak lembar tes warna (Cyan, Magenta, Yellow, Black) guna memastikan semua lubang tinta terbuka lancar.
- 📄 **Print Test Page**: Menguji sistem pencetakan CUPS dengan mencetak halaman tes standar.
- 🔄 **Refresh Connection & Status**: Memeriksa kembali status koneksi printer (Online / Offline / Pending).

---

## ❓ 3. Troubleshooting & Tanya Jawab Umum (FAQ)

### Q: Mengapa muncul peringatan *"Black ink appears to be low (14%)"* padahal tabung tinta sudah saya isi penuh dari botol?
**Jawaban:**  
Printer Epson EcoTank **TIDAK memiliki sensor fisik/elektronik** di dalam tabung tinta. Indikator di komputer hanyalah **perkiraan matematis (software counter)**. 

Untuk mereset indikator menjadi 100% kembali, Anda harus memberitahu printer secara manual melalui panel fisiknya:
1. Tekan tombol **Home** (gambar rumah) di panel layar printer Epson L5290.
2. Pilih menu **Maintenance (Pemeliharaan)** -> **Fill Ink (Isi Tinta)** atau **Reset Ink Levels**.
3. Tekan **Start** dan pilih warna tinta yang telah Anda isi penuh.

---

## 🛠️ 4. Panduan Build Paket `.rpm` (Untuk Pengembang)

Jika Anda ingin mengompilasi ulang file paket `.rpm` ini dari source code:

### 1. Cloning Repositori
```bash
git clone https://github.com/dosq/epson-l5290-suite.git
cd epson-l5290-suite
```

### 2. Install Dependency Pembangun
```bash
sudo dnf install -y rpm-build
```

### 3. Jalankan Skrip Build
```bash
./build.sh
```
File `.rpm` yang baru dikompilasi akan secara otomatis tersimpan di dalam folder `output/`.

---

## 📜 Lisensi & Kontribusi

Proyek ini didistribusikan di bawah lisensi **GPLv2**. Kontribusi berupa bug report, pull request, atau saran perbaikan antarmuka sangat disambut hangat!
