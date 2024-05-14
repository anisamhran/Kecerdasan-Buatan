import wmi
import time
from pynput.mouse import Controller

# Inisialisasi posisi mouse awal
initial_position = None

def is_idle():
    global initial_position

    # Inisialisasi objek mouse
    mouse = Controller()

    # Jika posisi awal belum ditetapkan, set posisi awal dan kembalikan False
    if initial_position is None:
        initial_position = mouse.position
        return False
     
    # Bandingkan posisi mouse sekarang dengan posisi awal
    if mouse.position == initial_position:
        return True
    else:
        # Jika posisi mouse telah berubah, atur ulang posisi awal
        initial_position = mouse.position
        return False

def decrease_brightness():
    # Membuat objek WMI (Windows Management Instrumentation)
    wmi_obj = wmi.WMI(namespace='wmi')

    # Mendapatkan instance objek kecerahan layar
    brightness = wmi_obj.WmiMonitorBrightnessMethods()[0]

    # Mengatur kecerahan layar menjadi 5%
    brightness.WmiSetBrightness(5, 0)  

def increase_brightness():
    # Membuat objek WMI (Windows Management Instrumentation)
    wmi_obj = wmi.WMI(namespace='wmi')

    # Mendapatkan instance objek kecerahan layar
    brightness = wmi_obj.WmiMonitorBrightnessMethods()[0]

    # Mengatur kecerahan layar menjadi 50%
    brightness.WmiSetBrightness(50, 0)  

def main():
    while True:
        if is_idle():
            print("Idle")
            decrease_brightness()
        else:
            print("Not Idle")
            increase_brightness()
        # Tunggu selama 5 detik sebelum memeriksa status lagi
        time.sleep(5)

if __name__ == "__main__":
    main()
