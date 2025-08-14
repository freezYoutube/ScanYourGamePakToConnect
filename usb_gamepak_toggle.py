# usb_gamepak_toggle.py
import usb.core
import usb.util
import time

# Change these to your Game PAK's Vendor ID and Product ID
VENDOR_ID = 0x1234  # Example: 0x057E
PRODUCT_ID = 0xABCD  # Example: 0x0306

connected = False

print("Waiting for Game PAK...")

while True:
    dev = usb.core.find(idVendor=VENDOR_ID, idProduct=PRODUCT_ID)
    if dev is not None and not connected:
        connected = True
        print("Connected to game pak")
    elif dev is None and connected:
        connected = False
        print("Disconnected from game pak")
    time.sleep(1)
