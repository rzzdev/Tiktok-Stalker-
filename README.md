# TikTok Stalker - Termux Edition

<p align="center">
  <strong>Tiktok Stalker - By [R]zzdeV</strong>
</p>

<p align="center">
  Sebuah alat command-line yang powerful dan kaya fitur untuk mengambil data profil publik TikTok, dirancang khusus untuk berjalan di lingkungan Termux Android.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue.svg" alt="Python 3.x">
  <img src="https://img.shields.io/badge/Platform-Termux%20%7C%20Linux-lightgrey.svg" alt="Platform">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
</p>

---

## 📸 Preview Tampilan

Berikut adalah tampilan menu utama dari skrip ini:

```
╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                                                                                                                      ║
║                           ████████╗███████╗██████╗ ███╗   ███╗██╗███╗   ██╗ █████╗ ██╗                              ║
║                           ╚══██╔══╝██╔════╝██╔══██╗████╗ ████║██║████╗  ██║██╔══██╗██║                              ║
║                              ██║   █████╗  ██████╔╝██╔████╔██║██║██╔██╗ ██║███████║██║                              ║
║                              ██║   ██╔══╝  ██╔══██╗██║╚██╔╝██║██║██║╚██╗██║██╔══██║██║                              ║
║                              ██║   ███████╗██║  ██║██║ ╚═╝ ██║██║██║ ╚████║██║  ██║███████╗                           ║
║                              ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝                           ║
║                           ███████╗██████╗  █████╗  ██████╗███████╗███████╗███████╗                              ║
║                           ██╔════╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝██╔════╝                              ║
║                           ██████╗ ██████╔╝███████║██║     █████╗  ███████╗███████╗                              ║
║                           ██╔══╝  ██╔══██╗██╔══██║██║     ██╔══╝  ╚════██║╚════██║                              ║
║                           ██║     ██║  ██║██║  ██║╚██████╗███████╗███████║███████║                              ║
║                           ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚══════╝╚══════╝╚══════╝                              ║
║                                                                                                                      ║
║                                        >>>>>>>>>> Created By [R]zzdeV <<<<<<<<<<                                         ║
║                                                                                                                      ║
║                                           Jumat, 27 Oktober 2023 - 16:05:30                                            ║
║                                                                                                                      ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════╝

--- MENU UTAMA ---
1. Stalk Username TikTok
2. Tampilkan Hasil Terakhir
3. Simpan Hasil Terakhir ke File (JSON)
4. Cek Status API
5. Masuk ke Mode Premium
6. Keluar

Pilih menu (1-6):
```

---

## ✨ Fitur-Fitur

-   🎨 **Tampilan Keren & Interaktif**: Banner ASCII Art yang menarik, output berwarna, dan menu yang mudah digunakan.
-   📊 **Data Profil Lengkap**: Mengambil semua informasi publik seperti username, nickname, bio, verifikasi, region, dan statistik (pengikut, suka, video).
-   💾 **Simpan & Ekspor Data**: Simpan hasil stalking ke file JSON atau ekspor ke file CSV untuk analisis lebih lanjut.
-   🚀 **Mode Premium (Demo)**: Nikmati fitur eksklusif dengan login sederhana.
    -   **Batch Stalking**: Stalk beberapa username sekaligus dalam satu kali proses.
    -   **Export ke CSV**: Ekspor hasil (single atau batch) ke format CSV yang kompatibel dengan spreadsheet.
    -   **Riwayat Stalking**: Lihat daftar username yang pernah Anda stalk beserta waktunya.
-   🛡️ **Penanganan Error yang Baik**: Menangani berbagai masalah seperti jaringan gagal, username tidak ditemukan, atau error dari server dengan pesan yang jelas.
-   📜 **Info Waktu Real-time**: Menampilkan hari, tanggal, dan jam saat ini di dalam banner.

---

## 📋 Prerequisites

Sebelum menjalankan skrip ini, pastikan Anda telah menginstal:

-   Aplikasi **Termux** (disarankan install dari F-Droid).
-   **Python 3**
-   Library Python: `requests` dan `colorama`.

---

## 🚀 Installation & Setup

Ikuti langkah-langkah berikut di Termux Anda:

1.  **Update dan Upgrade Termux**
    ```bash
    pkg update && pkg upgrade
    ```

2.  **Instal Python**
    ```bash
    pkg install python
    ```

3.  **Instal Library yang Dibutuhkan**
    ```bash
    pip install requests colorama
    ```

4.  **Unduh Skrip**
    -   **Cara 1: Menggunakan Git**
        ```bash
        git clone https://github.com/username-anda/nama-repo.git
        cd nama-repo
        ```
    -   **Cara 2: Unduh Manual**
        Unduh file `tiktok_stalker.py` dan pindahkan ke folder Termux Anda.

---

## 💻 Usage

Setelah semua langkah instalasi selesai, jalankan skrip dengan perintah:

```bash
python tiktok_stalker.py
```

Ikuti menu interaktif yang tersedia:
1.  **Stalk Username TikTok**: Masukkan username untuk diambil datanya.
2.  **Tampilkan Hasil Terakhir**: Menampilkan kembali hasil stalking terakhir tanpa perlu koneksi internet.
3.  **Simpan Hasil**: Menyimpan hasil terakhir ke file JSON.
4.  **Cek Status API**: Memeriksa apakah server API sedang online.
5.  **Mode Premium**: Masuk ke fitur eksklusif.
6.  **Keluar**: Menutup program.

---

## 🔑 Mode Premium (Demo)

**Catatan: Mode Premium adalah fitur demo untuk menunjukkan kemampuan skrip.**

-   **Password Default**: `rzzdev`
-   **Fitur di Dalamnya**:
    1.  **Batch Stalking**: Masukkan beberapa username yang dipisahkan dengan koma (misal: `user1,user2,user3`).
    2.  **Export ke CSV**: Menyimpan data profil ke file `tiktok_export_[timestamp].csv`.
    3.  **Lihat Riwayat**: Menampilkan riwayat stalking yang tersimpan di `stalking_history.json`.

---

## 📂 Output Files

Skrip ini akan membuat beberapa file di direktori yang sama:
-   `tiktok_[username]_[timestamp].json`: File JSON untuk setiap hasil stalking yang Anda simpan.
-   `tiktok_export_[timestamp].csv`: File CSV yang dihasilkan dari fitur export premium.
-   `stalking_history.json`: File yang menyimpan riwayat semua username yang pernah di-stalk.

---

## ⚠️ Disclaimer

Skrip ini dibuat untuk tujuan pembelajaran dan edukasi. Pengguna bertanggung jawab penuh atas cara mereka menggunakan alat ini. Harap hormati privasi pengguna lain dan jangan gunakan untuk tujuan yang merugikan. Saya (pembuat) tidak bertanggung jawab atas penyalahgunaan skrip ini.

---

## 🙏 Credits

-   API yang digunakan bersumber dari **https://api.siputzx.my.id/**
-   Dibuat dengan ❤️ menggunakan Python.

---

## 📜 License

Proyek ini dilisensikan di bawah **MIT License** - lihat file [LICENSE](LICENSE) untuk detailnya.
```
