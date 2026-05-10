import webview

# Konfigurasi Utama
URL_UJIAN = "https://simcantiq.my.id/ujian/"
JUDUL_APP = "Exambro SIMCANTIG"
KODE_KELUAR = "12345"

# Variabel untuk menampung ketikan
buffer_ketikan = ""

def check_kode(window):
    global buffer_ketikan
    
    # Ambil karakter yang ditekan lewat eksekusi JavaScript sederhana
    # Ini cara paling ampuh dan kompatibel untuk webview terbaru
    def get_key(key):
        global buffer_ketikan
        if len(key) == 1:
            buffer_ketikan += key
        
        if len(buffer_ketikan) > len(KODE_KELUAR):
            buffer_ketikan = buffer_ketikan[-len(KODE_KELUAR):]
            
        if buffer_ketikan == KODE_KELUAR:
            window.destroy()

    # Menambahkan event listener ke halaman web
    window.expose(get_key)
    window.evaluate_js("""
        document.onkeydown = function(e) {
            get_key(e.key);
        };
    """)

def buka_ujian():
    window = webview.create_window(
        JUDUL_APP, 
        URL_UJIAN, 
        fullscreen=True, 
        on_top=True
    )
    
    # Jalankan pengecekan setelah halaman selesai dimuat
    webview.start(check_kode, window)

if __name__ == '__main__':
    buka_ujian()
