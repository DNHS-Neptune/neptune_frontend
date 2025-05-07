---
layout: post
title: Base64 HW
description: Final Check
type: issues 
comments: true
permalink: /navigation/arya_blog/base64
---


# Binary Icon & Color Encoding Project

This markdown document includes:
- A 2×2 icon color design
- 24-bit image storage calculation
- Base64 encoding of a string
- Embedded Base64 PNG
- RGB/RGBA color conversions

---

## 🎨 2×2 Icon Colors

```python
# 2x2 Icon Colors
colors = {
    "Blue": "#1E90FF",
    "LimeGreen": "#32CD32",
    "Gold": "#FFD700",
    "Red": "#FF0000"
}

for name, hex_code in colors.items():
    print(f"{name}: {hex_code}")
```

---

## 💾 Storage Calculation for 2×2 Image at 24-bit Depth

- Bits per pixel: 24  
- Number of pixels: 2 × 2 = 4  
- Total bits: 24 × 4 = **96 bits**  
- Total bytes: 96 ÷ 8 = **12 bytes**

---

## 🐱 Base64 Encode the String "Cat"

```python
import base64

# Encode "Cat"
encoded = base64.b64encode("Cat".encode()).decode()
print(f"Base64-encoded 'Cat': {encoded}")
```

---

## 🖼️ 1×1 Red PNG (Base64 Embedded)

Below is a red pixel (1×1 PNG) embedded as a Base64 image:

```python
from IPython.display import HTML

# 1x1 red PNG image in base64
red_pixel_base64 = (
    "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAIAAACQd1PeAAAADUlEQVR42mP8z8BQDwAFiQL/"
    "qW8iWwAAAABJRU5ErkJggg=="
)

# Embed it in HTML
HTML(f'<img src="data:image/png;base64,{red_pixel_base64}" />')
```

---

## 🎨 Hex to RGB & RGBA

```python
def hex_to_rgb(hex_code):
    h = hex_code.lstrip('#')
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

# Colors
hex_codes = ["#1E90FF", "#32CD32", "#FFD700"]
for code in hex_codes:
    rgb = hex_to_rgb(code)
    rgba = rgb + (1,)
    print(f"{code} → rgb{rgb}, rgba{rgba}")
```

---

## 🧊 50% Transparent Teal (RGBA)

```css
rgba(0, 128, 128, 0.5)
```
