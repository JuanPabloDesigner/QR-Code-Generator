# Installation Guide

## Prerequisites

- Python 3.x
- pip package manager

## Step-by-Step Installation

1. Clone the repository:
```bash
git clone https://github.com/JuanPabloDesigner/QR-Code-Generator.git
cd QR-Code-Generator
```

2. Create a virtual environment:
```bash
python -m venv venv
```

3. Activate the virtual environment:
```bash
# Windows
.\venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

4. Install dependencies:
```bash
pip install setuptools
python setup.py develop
```

## Verification

Test the installation by running:
```bash
python example.py
```

You should see a QR code printed in the console and a `qr_code.svg` file created.
