import webview

# Konfigurasi Utama
URL_UJIAN = "https://simcantiq.my.id/ujian/"
JUDUL_APP = "Exambro SIMCANTIQ"
KODE_KELUAR = "12345"

# Variabel untuk menampung ketikan
buffer_ketikan = ""

def on_keydown(key):
    global buffer_ketikan
    
    # Hanya tangkap karakter string/angka
    if len(key) == 1:
        buffer_ketikan += key
    
    # Jaga panjang buffer agar tidak kepanjangan
    if len(buffer_ketikan) > len(KODE_KELUAR):
        buffer_ketikan = buffer_ketikan[-len(KODE_KELUAR):]
    
    # Cek kode rahasia
    if buffer_ketikan == KODE_KELUAR:
        active_window = webview.active_window()
        if active_window:
            active_window.destroy()

def buka_ujian():
    # Membuat jendela Fullscreen dan Selalu di Depan (On Top)
    window = webview.create_window(
        JUDUL_APP, 
        URL_UJIAN, 
        fullscreen=True, 
        on_top=True
    )
    
    # Daftarkan fungsi deteksi keyboard
    window.events.keydown += on_keydown
    webview.start()

if __name__ == '__main__':
    buka_ujian()
