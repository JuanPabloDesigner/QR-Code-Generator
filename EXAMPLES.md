# Examples and Templates

## Basic Examples

### 1. Simple QR Code (`example.py`)
Generates a basic QR code with white background and black modules.

```python
from qrcodegen import QrCode
qr = QrCode.encode_text("Hello from Python!", QrCode.Ecc.MEDIUM)
```

### 2. Dark Mode QR Code (`dark_mode_example.py`)
Generates a QR code with dark background and white modules.

```python
qr = QrCode.encode_text("Hello from Dark Mode!", QrCode.Ecc.MEDIUM)
```

## Advanced Examples

### Error Correction Levels
- `QrCode.Ecc.LOW` - ~7% error correction
- `QrCode.Ecc.MEDIUM` - ~15% error correction  
- `QrCode.Ecc.QUARTILE` - ~25% error correction
- `QrCode.Ecc.HIGH` - ~30% error correction

### Custom Colors
You can modify the SVG generation function to use custom colors:

```python
# Change background color
parts.append('\t<rect width="100%" height="100%" fill="#FF6B6B"/>\n')

# Change module color  
parts.append('" fill="#4ECDC4"/>\n')
```

## Template Structure

Each template includes:
- QR code generation
- SVG export functionality
- Console text display
- Error handling

## Running the Examples

```bash
# Basic example
python example.py

# Dark mode example
python dark_mode_example.py
```
