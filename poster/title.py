import numpy as np
from PIL import Image, ImageDraw

# 元のサイズ
base_width, base_height = 800, 800
scale = 5
width, height = base_width * scale, base_height * scale

# 正弦波のパラメータ
amplitude = 30 * scale
offset1 = 650 * scale
offset2 = 250 * scale
offset3 = 720 * scale
carrier_freq = 8
mod_freq = 2
mod_index = 2

# 固定グラデーションの高さ（px）
y_fixed = 550 * scale
border = 200
minimum = 50

# 画像生成
img = Image.new('RGB', (width, height))
pixels = img.load()

y_wave_array1 = []
y_wave_array2 = []

for x in range(width):
    x_norm = x / width  # 正規化

    y_wave = int(offset1 + amplitude * np.sin(
        2 * np.pi * carrier_freq * x_norm + mod_index * np.sin(2 * np.pi * mod_freq * x_norm)
    ))

    y_wave_array1.append(int(offset2 + 10 * scale * np.sin(
        2 * np.pi * carrier_freq * x_norm + 3 * np.sin(2 * np.pi * 1 * x_norm)
    ) + 20 * scale * np.sin(2 * np.pi * 3 * x_norm)))

    y_wave_array2.append(int(offset3 + 10 * scale * np.sin(
        2 * np.pi * carrier_freq * x_norm + 1 * np.sin(2 * np.pi * 2 * x_norm)
    ) + 10 * scale * np.sin(2 * np.pi * 2 * x_norm)))

    for y in range(height):
        if y < y_fixed:
            t = y / y_fixed
            r = g = minimum + int((border - minimum) * t)
            b = 255
        elif y < y_wave:
            t = (y - y_fixed) / (y_wave - y_fixed)
            r = g = border + int(border * t)
            b = 255
        else:
            r = g = b = 255

        pixels[x, y] = (r, g, b)

draw = ImageDraw.Draw(img)

# 波に沿った線を描画（y_wave_array2）
line2 = []
count = 0
for x in range(width):
    if count % (30 * scale) < (15 * scale):
        line2.append((x, max(0, y_wave_array2[x] - 250 * scale - 4 * scale // 2 + (count % 2) * scale * 4)))
    elif count % (30 * scale) == (15 * scale):
        draw.line(line2, fill=(50, 50, 200), width = 2 * scale)
        line2 = []
    count += 1

# y_wave_array1 に沿った線を描画（実線）
line1 = [(x, max(0, y_wave_array1[x] - 120 * scale)) for x in range(width)]
draw.line(line1, fill=(150, 150, 250), width=2 * scale)

# 保存
img.save('title.png')