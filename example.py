from qrcodegen import QrCode, QrSegment

def to_svg_str(qr: QrCode, border: int) -> str:
    """Returns a string of SVG code for an image depicting the given QR Code, with the given number
    of border modules. The string always uses Unix newlines (\n), regardless of the platform."""
    if border < 0:
        raise ValueError("Border must be non-negative")
    parts: list[str] = []
    parts.append('<?xml version="1.0" encoding="UTF-8"?>\n')
    parts.append('<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">\n')
    dimension = qr.get_size() + border * 2
    parts.append(f'<svg xmlns="http://www.w3.org/2000/svg" version="1.1" viewBox="0 0 {dimension} {dimension}" stroke="none">\n')
    parts.append('\t<rect width="100%" height="100%" fill="#FFFFFF"/>\n')
    parts.append('\t<path d="')
    for y in range(qr.get_size()):
        for x in range(qr.get_size()):
            if qr.get_module(x, y):
                parts.append(f'M{x+border},{y+border}h1v1h-1z ')
    parts.append('" fill="#000000"/>\n')
    parts.append('</svg>\n')
    return "".join(parts)

# Create a simple QR code with medium error correction
qr = QrCode.encode_text("Hello from Python!", QrCode.Ecc.MEDIUM)

# Convert to SVG string with a border of 4 modules
svg = to_svg_str(qr, 4)

# Save the SVG to a file
with open("qr_code.svg", "w") as f:
    f.write(svg)

# Also print the QR code as text (just for fun!)
print("\nQR Code as text:")
for y in range(qr.get_size()):
    # Each module (pixel) is represented as █ or space
    line = ""
    for x in range(qr.get_size()):
        line += "██" if qr.get_module(x, y) else "  "
    print(line)
