# usb_gamepak_toggle.py
import time
import sys

# Simulated USB GamePak connection (since actual USB library may not be available)
# In a real implementation, you would use pyusb or similar

# Change these to your Game PAK's Vendor ID and Product ID
VENDOR_ID = 0x1234  # Example: 0x057E for Nintendo
PRODUCT_ID = 0xABCD  # Example: 0x0306 for specific device

class GamePakUSB:
    def __init__(self):
        self.connected = False
        self.connection_count = 0
    
    def simulate_detection(self):
        """Simulate GamePak detection for demo purposes"""
        import random
        # Randomly simulate connection/disconnection for demo
        return random.choice([True, False]) if self.connection_count < 5 else False
    
    def find_device(self):
        """Simulate finding USB device"""
        # In real implementation, this would use:
        # import usb.core
        # dev = usb.core.find(idVendor=VENDOR_ID, idProduct=PRODUCT_ID)
        # return dev is not None
        
        return self.simulate_detection()
    
    def monitor(self):
        print("🕹️  GamePak USB Monitor")
        print("=" * 25)
        print(f"Looking for device: VID={hex(VENDOR_ID)}, PID={hex(PRODUCT_ID)}")
        print("Waiting for Game PAK...\n")
        
        try:
            while True:
                device_present = self.find_device()
                
                if device_present and not self.connected:
                    self.connected = True
                    self.connection_count += 1
                    print(f"✅ Connected to GamePak (Connection #{self.connection_count})")
                    print("   Status: READY")
                    
                elif not device_present and self.connected:
                    self.connected = False
                    print("❌ Disconnected from GamePak")
                    print("   Status: WAITING")
                
                time.sleep(1)
                
        except KeyboardInterrupt:
            print("\n\n🛑 Monitoring stopped by user")
            print("GamePak USB Monitor terminated.")
            sys.exit(0)

def main():
    monitor = GamePakUSB()
    
    print("Note: This is a simulation. For real USB functionality,")
    print("install pyusb: pip install pyusb\n")
    
    monitor.monitor()

if __name__ == "__main__":
    main()