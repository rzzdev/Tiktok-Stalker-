import requests
import json
import os
import sys
import time
import csv
from datetime import datetime

# --- Instalasi library colorama untuk output berwarna ---
# pip install colorama
try:
    from colorama import init, Fore, Style
    init(autoreset=True)
except ImportError:
    print("[!] Modul 'colorama' tidak ditemukan. Silakan install dengan: pip install colorama")
    sys.exit(1)

# --- Konfigurasi ---
API_URL = "https://api.siputzx.my.id/api/stalk/tiktok"
last_profile_data = None
HISTORY_FILE = "stalking_history.json"
# --- KONFIGURASI PREMIUM ---
PREMIUM_PASSWORD = "rzzdev" # Password untuk masuk ke mode premium

# Mapping hari dan bulan ke Bahasa Indonesia
HARI_INDO = {'Monday': 'Senin', 'Tuesday': 'Selasa', 'Wednesday': 'Rabu', 'Thursday': 'Kamis', 'Friday': 'Jumat', 'Saturday': 'Sabtu', 'Sunday': 'Minggu'}
BULAN_INDO = {'January': 'Januari', 'February': 'Februari', 'March': 'Maret', 'April': 'April', 'May': 'Mei', 'June': 'Juni', 'July': 'Juli', 'August': 'Agustus', 'September': 'September', 'October': 'Oktober', 'November': 'November', 'December': 'Desember'}

# --- Fungsi-Fungsi Pendukung ---

def clear_screen():
    """Membersihkan layar terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_current_time_info():
    now = datetime.now()
    day_name_id = HARI_INDO.get(now.strftime('%A'), now.strftime('%A'))
    month_name_id = BULAN_INDO.get(now.strftime('%B'), now.strftime('%B'))
    return f"{day_name_id}, {now.day} {month_name_id} {now.year} - {now.strftime('%H:%M:%S')}"

def display_banner(time_info: str):
    """Menampilkan banner keren, rapi, dengan info waktu (VERSI DIPERBAIKI)."""
    border_width = 118
    
    # Definisi setiap baris banner
    line1 = f"{Fore.CYAN} ████████╗███████╗██████╗ ███╗   ███╗██╗███╗   ██╗ █████╗ ██╗     "
    line2 = f"{Fore.CYAN} ╚══██╔══╝██╔════╝██╔══██╗████╗ ████║██║████╗  ██║██╔══██╗██║     "
    line3 = f"{Fore.CYAN}    ██║   █████╗  ██████╔╝██╔████╔██║██║██╔██╗ ██║███████║██║     "
    line4 = f"{Fore.CYAN}    ██║   ██╔══╝  ██╔══██╗██║╚██╔╝██║██║██║╚██╗██║██╔══██║██║     "
    line5 = f"{Fore.CYAN}    ██║   ███████╗██║  ██║██║ ╚═╝ ██║██║██║ ╚████║██║  ██║███████╗"
    line6 = f"{Fore.CYAN}    ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝"
    line7 = f"{Fore.YELLOW}███████╗██████╗  █████╗  ██████╗███████╗███████╗███████╗"
    line8 = f"{Fore.YELLOW}██╔════╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝██╔════╝"
    line9 = f"{Fore.YELLOW}█████╗  ██████╔╝███████║██║     █████╗  ███████╗███████╗"
    line10 = f"{Fore.YELLOW}██╔══╝  ██╔══██╗██╔══██║██║     ██╔══╝  ╚════██║╚════██║"
    line11 = f"{Fore.YELLOW}██║     ██║  ██║██║  ██║╚██████╗███████╗███████║███████║"
    line12 = f"{Fore.YELLOW}╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚══════╝╚══════╝╚══════╝"
    author_line = f"{Fore.GREEN}                                        >>>>>>>>>> Created By [R]zzdeV <<<<<<<<<<                                         "
    time_line = f"{Fore.MAGENTA}                                           {time_info}                                            "

    # --- BAGIAN YANG DIPERBAIKI: Mencetak baris per baris tanpa loop globals() ---
    print(f"{Fore.CYAN}╔{'═' * (border_width - 2)}╗")
    print(f"║{' ' * (border_width - 2)}║")
    print(f"║{line1.center(border_width - 2)}║")
    print(f"║{line2.center(border_width - 2)}║")
    print(f"║{line3.center(border_width - 2)}║")
    print(f"║{line4.center(border_width - 2)}║")
    print(f"║{line5.center(border_width - 2)}║")
    print(f"║{line6.center(border_width - 2)}║")
    print(f"║{line7.center(border_width - 2)}║")
    print(f"║{line8.center(border_width - 2)}║")
    print(f"║{line9.center(border_width - 2)}║")
    print(f"║{line10.center(border_width - 2)}║")
    print(f"║{line11.center(border_width - 2)}║")
    print(f"║{line12.center(border_width - 2)}║")
    print(f"║{' ' * (border_width - 2)}║")
    print(f"║{author_line.center(border_width - 2)}║")
    print(f"║{' ' * (border_width - 2)}║")
    print(f"║{time_line.center(border_width - 2)}║")
    print(f"║{' ' * (border_width - 2)}║")
    print(f"╚{'═' * (border_width - 2)}╝{Style.RESET_ALL}")

def show_spinner(message="Mengambil data", delay=0.1):
    spinner = ['|', '/', '-', '\\']
    for _ in range(10):
        for char in spinner:
            sys.stdout.write(f'\r{Fore.YELLOW}[INFO] {message}... {char}')
            sys.stdout.flush()
            time.sleep(delay)
    sys.stdout.write('\r' + ' ' * (len(message) + 10) + '\r')

def save_to_history(data: dict, username: str):
    history_entry = {"timestamp": datetime.now().isoformat(), "username": username, "nickname": data.get('data', {}).get('nickname', 'N/A')}
    try: 
        with open(HISTORY_FILE, 'a', encoding='utf-8') as f: f.write(json.dumps(history_entry) + '\n')
    except IOError: pass

def get_tiktok_profile(username: str) -> dict | None:
    global last_profile_data
    payload = {'username': username}
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36', 'Content-Type': 'application/x-www-form-urlencoded'}
    try:
        show_spinner(f"Mengambil data untuk @{username}")
        response = requests.post(API_URL, data=payload, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
        if not data.get('status', False):
            error_message = data.get('message', 'Kesalahan tidak diketahui dari API.')
            print(f"{Fore.RED}[!] Error dari API: {error_message}")
            return None
        print(f"{Fore.GREEN}[+] Berhasil mengambil data.")
        last_profile_data = data
        save_to_history(data, username)
        return data
    except requests.exceptions.HTTPError as http_err: print(f"{Fore.RED}[!] Error HTTP: {http_err} (Status: {response.status_code})")
    except requests.exceptions.ConnectionError: print(f"{Fore.RED}[!] Error: Gagal terhubung ke API.")
    except requests.exceptions.Timeout: print(f"{Fore.RED}[!] Error: Permintaan ke API timeout.")
    except requests.exceptions.RequestException as err: print(f"{Fore.RED}[!] Terjadi error: {err}")
    except json.JSONDecodeError: print(f"{Fore.RED}[!] Error: Respons dari API bukan JSON yang valid.")
    return None

def display_summary(data: dict):
    user_info = data.get('data', {})
    stats = user_info.get('stats', {})
    print(f"\n{Fore.CYAN}╔══════════════════════════════════════════════════════════════╗")
    print(f"║{Fore.CYAN}                    INFORMASI PROFIL                          ║")
    print(f"╚══════════════════════════════════════════════════════════════╝")
    print(f"{Fore.GREEN}Username       : {Fore.WHITE}@{user_info.get('username', 'N/A')}")
    print(f"{Fore.GREEN}Nickname       : {Fore.WHITE}{user_info.get('nickname', 'N/A')}")
    print(f"{Fore.GREEN}Bio/Signature  : {Fore.WHITE}{user_info.get('signature', 'N/A')}")
    print(f"{Fore.GREEN}Region         : {Fore.WHITE}{user_info.get('region', 'N/A')}")
    print(f"{Fore.GREEN}Verified       : {Fore.WHITE}{'Ya' if user_info.get('verified') else 'Tidak'}")
    print(f"{Fore.GREEN}Akun Privat    : {Fore.WHITE}{'Ya' if user_info.get('isPrivate') else 'Tidak'}")
    print(f"\n{Fore.YELLOW}╔══════════════════════════════════════════════════════════════╗")
    print(f"║{Fore.YELLOW}                    STATISTIK AKUN                            ║")
    print(f"╚══════════════════════════════════════════════════════════════╝")
    print(f"{Fore.GREEN}Pengikut       : {Fore.WHITE}{stats.get('followerCount', 0):,}")
    print(f"{Fore.GREEN}Mengikuti      : {Fore.WHITE}{stats.get('followingCount', 0):,}")
    print(f"{Fore.GREEN}Suka/Likes     : {Fore.WHITE}{stats.get('heartCount', 0):,}")
    print(f"{Fore.GREEN}Total Video    : {Fore.WHITE}{stats.get('videoCount', 0):,}")
    print(f"{Fore.CYAN}----------------------------------------------------------\n")

# --- FITUR PREMIUM ---

def premium_login():
    attempts = 3
    while attempts > 0:
        password = input(f"{Fore.YELLOW}[PREMIUM] Masukkan password (kesempatan {attempts}): {Style.RESET_ALL}")
        if password == PREMIUM_PASSWORD:
            print(f"{Fore.GREEN}[+] Login berhasil! Selamat datang di Mode Premium.")
            time.sleep(1.5)
            return True
        else:
            attempts -= 1
            print(f"{Fore.RED}[!] Password salah!")
            time.sleep(1)
    print(f"{Fore.RED}[!] Kesempatan habis. Kembali ke menu utama.")
    time.sleep(2)
    return False

def batch_stalk():
    usernames_input = input(f"{Fore.CYAN}[PREMIUM] Masukkan username dipisahkan dengan koma (,): {Style.RESET_ALL}")
    usernames = [u.strip() for u in usernames_input.split(',') if u.strip()]
    if not usernames:
        print(f"{Fore.RED}[!] Tidak ada username yang dimasukkan.")
        return
    all_results = []
    print(f"\n{Fore.MAGENTA}--- MEMULAI BATCH STALKING ---")
    for user in usernames:
        print(f"\n{Fore.CYAN}Memproses @{user}...")
        data = get_tiktok_profile(user)
        if data:
            all_results.append(data)
            display_summary(data)
        else:
            print(f"{Fore.RED}Gagal mengambil data untuk @{user}.")
        time.sleep(1)
    if all_results:
        global last_profile_data
        last_profile_data = {"batch_results": all_results, "batch_mode": True}
        print(f"{Fore.GREEN}\n[+] Batch stalking selesai. {len(all_results)} profil berhasil diambil.")
    else:
        print(f"{Fore.RED}\n[!] Tidak ada profil yang berhasil diambil selama batch stalking.")

def export_to_csv():
    if not last_profile_data:
        print(f"{Fore.RED}[!] Tidak ada data untuk diekspor. Lakukan stalking terlebih dahulu.")
        return
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"tiktok_export_{timestamp}.csv"
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['username', 'nickname', 'signature', 'verified', 'region', 'isPrivate', 'followerCount', 'followingCount', 'heartCount', 'videoCount']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            if last_profile_data.get("batch_mode"): results = last_profile_data.get("batch_results", [])
            else: results = [last_profile_data]
            for item in results:
                user_info = item.get('data', {})
                stats = user_info.get('stats', {})
                writer.writerow({'username': user_info.get('username'), 'nickname': user_info.get('nickname'), 'signature': user_info.get('signature'), 'verified': user_info.get('verified'), 'region': user_info.get('region'), 'isPrivate': user_info.get('isPrivate'), 'followerCount': stats.get('followerCount'), 'followingCount': stats.get('followingCount'), 'heartCount': stats.get('heartCount'), 'videoCount': stats.get('videoCount'),})
        print(f"{Fore.GREEN}[+] Berhasil mengekspor data ke file: {filename}")
    except IOError as e:
        print(f"{Fore.RED}[!] Gagal mengekspor file: {e}")

def view_history():
    if not os.path.exists(HISTORY_FILE):
        print(f"{Fore.YELLOW}[!] Belum ada riwayat stalking.")
        return
    try:
        with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
            print(f"\n{Fore.CYAN}--- RIWAYAT STALKING ---")
            for line in f:
                entry = json.loads(line)
                dt_obj = datetime.fromisoformat(entry['timestamp'])
                formatted_time = dt_obj.strftime('%d %b %Y %H:%M')
                print(f"{Fore.WHITE}> {Fore.GREEN}@{entry['username']} ({Fore.CYAN}{entry['nickname']}{Fore.WHITE}) - {Fore.MAGENTA}{formatted_time}")
            print("-------------------------\n")
    except (IOError, json.JSONDecodeError):
        print(f"{Fore.RED}[!] Gagal membaca file riwayat.")

def premium_menu():
    while True:
        clear_screen()
        current_time = get_current_time_info()
        display_banner(current_time)
        print(f"{Fore.YELLOW}{'='*20} MODE PREMIUM {'='*20}")
        print("1. Batch Stalking (Multi Username)")
        print("2. Export Hasil Terakhir ke CSV")
        print("3. Lihat Riwayat Stalking")
        print("4. Kembali ke Menu Utama")
        choice = input(f"{Fore.CYAN}\nPilih menu premium (1-4): {Style.RESET_ALL}").strip()
        if choice == '1': batch_stalk()
        elif choice == '2': export_to_csv()
        elif choice == '3': view_history()
        elif choice == '4': break
        else: print(f"{Fore.RED}[!] Pilihan tidak valid."); time.sleep(1.5)
        input(f"{Fore.YELLOW}Tekan Enter untuk melanjutkan...")

# --- MENU UTAMA ---

def main_menu():
    while True:
        clear_screen()
        current_time = get_current_time_info()
        display_banner(current_time)
        print(f"{Fore.MAGENTA}\n--- MENU UTAMA ---")
        print("1. Stalk Username TikTok")
        print("2. Tampilkan Hasil Terakhir")
        print("3. Simpan Hasil Terakhir ke File (JSON)")
        print("4. Cek Status API")
        print(f"{Fore.YELLOW}5. Masuk ke Mode Premium")
        print("6. Keluar")
        choice = input(f"{Fore.CYAN}\nPilih menu (1-6): {Style.RESET_ALL}").strip()
        if choice == '1':
            target_username = input(f"{Fore.CYAN}Masukkan username TikTok: {Style.RESET_ALL}").strip()
            if target_username:
                profile_data = get_tiktok_profile(target_username)
                if profile_data:
                    view_choice = input(f"{Fore.CYAN}Tampilkan (r)ingkasan atau (j)son lengkap? [r/j]: {Style.RESET_ALL}").strip().lower()
                    if view_choice == 'r': display_summary(profile_data)
                    else: print("\n--- DATA LENGKAP (JSON) ---\n" + json.dumps(profile_data, indent=4, ensure_ascii=False) + "\n---------------------------\n")
                input(f"{Fore.YELLOW}Tekan Enter untuk kembali ke menu...")
            else: print(f"{Fore.RED}[!] Username tidak boleh kosong."); time.sleep(1.5)
        elif choice == '2':
            if last_profile_data: print(f"{Fore.GREEN}[+] Menampilkan hasil stalking terakhir."); display_summary(last_profile_data)
            else: print(f"{Fore.YELLOW}[!] Belum ada hasil stalking yang tersimpan.")
            input(f"{Fore.YELLOW}Tekan Enter untuk kembali ke menu...")
        elif choice == '3':
            if last_profile_data:
                username = last_profile_data.get('data', {}).get('username', 'unknown')
                timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                filename = f"tiktok_{username}_{timestamp}.json"
                try:
                    with open(filename, 'w', encoding='utf-8') as f: json.dump(last_profile_data, f, indent=4, ensure_ascii=False)
                    print(f"{Fore.GREEN}[+] Berhasil menyimpan data ke file: {filename}")
                except IOError as e: print(f"{Fore.RED}[!] Gagal menyimpan file: {e}")
            else: print(f"{Fore.YELLOW}[!] Belum ada hasil stalking yang tersimpan.")
            input(f"{Fore.YELLOW}Tekan Enter untuk kembali ke menu...")
        elif choice == '4':
            print(f"\n{Fore.CYAN}[*] Memeriksa status API...")
            try:
                response = requests.head(API_URL, timeout=5)
                if response.status_code == 200: print(f"{Fore.GREEN}[+] API ONLINE dan merespon dengan baik (Status: {response.status_code}).")
                else: print(f"{Fore.YELLOW}[!] API merespon, tapi dengan status tidak biasa (Status: {response.status_code}).")
            except requests.exceptions.ConnectionError: print(f"{Fore.RED}[!] API OFFLINE atau tidak dapat dijangkau.")
            except requests.exceptions.Timeout: print(f"{Fore.RED}[!] Gagal memeriksa status, permintaan timeout.")
            except requests.exceptions.RequestException as e: print(f"{Fore.RED}[!] Terjadi error saat mengecek status API: {e}")
            print("-" * 60); input(f"{Fore.YELLOW}Tekan Enter untuk kembali ke menu...")
        elif choice == '5':
            if premium_login(): premium_menu()
        elif choice == '6':
            print(f"{Fore.GREEN}Terima kasih telah menggunakan Tiktok Stalker!")
            break
        else:
            print(f"{Fore.RED}[!] Pilihan tidak valid. Silakan coba lagi.")
            time.sleep(1.5)

if __name__ == "__main__":
    main_menu()