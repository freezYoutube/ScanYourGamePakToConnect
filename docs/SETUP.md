# GamePak System Setup Guide

## 🚀 Quick Start

1. **Clone or download this repository**
2. **Open the main interface**: Open `index.html` in your browser
3. **Run Python scripts**: Use the scripts in the `scripts/` folder

## 📁 Project Structure

```
gamepak-system/
├── index.html                    # Main web interface
├── GamePak_BIOS.html            # BIOS simulation interface
├── HelperAssiant.Advanced.html  # AI assistant interface
├── scripts/
│   ├── MakeGamePak.py           # GamePak creation tool
│   ├── PickAConsole.py          # Console selection utility
│   └── usb_gamepak_toggle.py    # USB connection manager
├── docs/
│   └── SETUP.md                 # This file
└── README.md                    # Main documentation
```

## 🎮 Using the System

### Web Interface
- Open `index.html` for the main dashboard
- Click cards to access different tools
- BIOS and Helper Assistant run in separate windows

### Python Scripts

#### Creating GamePaks
```bash
python scripts/MakeGamePak.py
```
- Choose from Nintendo 64, Ultra 64, or Nintendo DS
- Confirm your selection
- GamePak will be created automatically

#### Advanced Console Selection
```bash
python scripts/PickAConsole.py
```
- More console options available
- Generates complete GamePak files with metadata
- Creates save files and documentation

#### USB Management
```bash
python scripts/usb_gamepak_toggle.py
```
- Monitors USB GamePak connections
- Real-time status updates
- Automatic detection and disconnection

## 🔧 Requirements

### For Web Interface
- Modern web browser (Chrome, Firefox, Safari, Edge)
- No additional dependencies required

### For Python Scripts
- Python 3.6 or higher
- For real USB functionality: `pip install pyusb`

## 🆘 Troubleshooting

### GamePak Not Working?
1. Check the README file for tips
2. Use the Helper Assistant (HelperAssiant.Advanced.html)
3. Ask: "help me, I scanned the game pak and it isn't working!"

### USB Connection Issues
1. Verify GamePak is properly inserted
2. Check USB port functionality
3. Run the USB toggle script for diagnostics

### Python Script Errors
1. Ensure Python 3.6+ is installed
2. Check file permissions
3. Install required dependencies if needed

## 🎯 Tips

- **Quick GamePak Help**: Use the exact phrase "help me, I scanned the game pak and it isn't working!" in the Helper Assistant
- **USB Toggle**: Scan the same GamePak again to disconnect
- **Console Selection**: Type "no" if you pick the wrong console during setup
- **File Organization**: Generated files are saved in the `output/` directory

## 🔄 Development

To run the web interface with a development server:

```bash
npm install
npm run dev
```

This will start a local server with hot reloading for development.