import socket
from sense_hat import SenseHat
import time

try:
    sense = SenseHat()
except:
    print("Sense HAT not found, using emulator")
    sense = None

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip_address = s.getsockname()[0]
    s.close()
    return ip_address

def display_ip(ip_address):
    if sense:
        sense.show_message(ip_address, scroll_speed=0.05, text_colour=[255, 255, 255], back_colour=[0, 0, 0])
        time.sleep(2)  # Display for 2 seconds
    else:
        print(f"Emulator: IP Address: {ip_address}")

if __name__ == "__main__":
    ip = get_ip_address()
    display_ip(ip)
