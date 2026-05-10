import webview

# Konfigurasi Exambro
URL_UJIAN = "https://simcantiq.my.id/ujian/index/" # GANTI dengan link ujian Anda
JUDUL_APP = "Exambro Portable"

def buka_ujian():
    window = webview.create_window(
        JUDUL_APP, 
        URL_UJIAN, 
        fullscreen=True, 
        confirm_close=True
    )
    webview.start()

if __name__ == '__main__':
    buka_ujian()
