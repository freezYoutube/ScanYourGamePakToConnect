import time
import random
import os

CONSOLES = [
    "Nintendo 64",
    "Ultra 64", 
    "Nintendo DS",
    "Game Boy Advance",
    "Super Nintendo"
]

OUT_DIR = "output"

def slow_print(text, delay=0.01):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def progress(duration):
    steps = 20
    for i in range(steps + 1):
        percent = (i / steps) * 100
        bar = '█' * i + '░' * (steps - i)
        print(f'\r[{bar}] {percent:.0f}%', end='', flush=True)
        time.sleep(duration / steps)
    print()

def create_gamepak(name, console, size_kb):
    filename = f"{name}_{console.replace(' ', '_')}.pak"
    metadata = {
        'name': name,
        'console': console,
        'size': f"{size_kb}KB",
        'created': time.strftime('%Y-%m-%d %H:%M:%S'),
        'checksum': hex(random.randint(0x1000, 0xFFFF))
    }
    
    # Create output directory
    os.makedirs(OUT_DIR, exist_ok=True)
    
    # Write GamePak file
    filepath = os.path.join(OUT_DIR, filename)
    with open(filepath, 'w') as f:
        f.write(f"GamePak: {name}\n")
        f.write(f"Console: {console}\n")
        f.write(f"Size: {size_kb}KB\n")
        f.write(f"Created: {metadata['created']}\n")
        f.write(f"Checksum: {metadata['checksum']}\n")
    
    return filename, metadata, metadata['checksum']

def save_savefile(name, metadata):
    save_filename = f"{name}.sav"
    save_path = os.path.join(OUT_DIR, save_filename)
    with open(save_path, 'w') as f:
        f.write("# GamePak Save File\n")
        f.write(f"# Generated: {metadata['created']}\n")
        f.write("# No save data yet\n")
    return save_filename

def write_readme(pak_filename, metadata, checksum):
    readme_filename = "README_GamePak.txt"
    readme_path = os.path.join(OUT_DIR, readme_filename)
    with open(readme_path, 'w') as f:
        f.write("GamePak Information\n")
        f.write("==================\n\n")
        f.write(f"File: {pak_filename}\n")
        f.write(f"Console: {metadata['console']}\n")
        f.write(f"Size: {metadata['size']}\n")
        f.write(f"Created: {metadata['created']}\n")
        f.write(f"Checksum: {checksum}\n\n")
        f.write("To connect via USB:\n")
        f.write("1. Run usb_gamepak_toggle.py\n")
        f.write("2. Insert GamePak into USB port\n")
        f.write("3. Wait for connection confirmation\n")
    return readme_filename

def main():
    slow_print("🕹️  GamePak Console Selector", 0.02)
    slow_print("=" * 30, 0.005)
    slow_print("Available consoles:", 0.01)

    for i, c in enumerate(CONSOLES):
        slow_print(f" {i+1}. {c}", 0.005)

    choice = None
    while choice is None:
        try:
            sel = int(input("Select a console number: "))
            if 1 <= sel <= len(CONSOLES):
                choice = CONSOLES[sel-1]
            else:
                slow_print("Invalid choice. Try again.", 0.005)
        except ValueError:
            slow_print("Please enter a number.", 0.005)

    name = input("Enter game pak name: ").strip() or "MyGamePak"
    size_kb = random.choice([128, 256, 512, 1024])

    slow_print(f"Creating '{name}' for {choice} ({size_kb}KB)...", 0.01)
    progress(3.0)

    filename, metadata, checksum = create_gamepak(name, choice, size_kb)
    save_path = save_savefile(name, metadata)
    readme_path = write_readme(filename, metadata, checksum)

    slow_print(f"Done! Generated files in '{OUT_DIR}':", 0.01)
    slow_print(f" - {filename}", 0.005)
    slow_print(f" - {save_path}", 0.005)
    slow_print(f" - {readme_path}", 0.005)

if __name__ == "__main__":
    main()