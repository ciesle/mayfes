import numpy as np
from PIL import Image, ImageDraw

# 画像サイズ
width, height = 800, 600

# 正弦波のパラメータ
amplitude = 30
offset = 300
carrier_freq = 8         # キャリア周波数 f_c
mod_freq = 2             # モジュレーション周波数 f_m
mod_index = 2            # 周波数変調係数 β

# 固定グラデーションの高さ（px）
y_fixed = 220  # ← ここを固定値にしたのが重要
border = 180

# 画像生成
img = Image.new('RGB', (width, height))
pixels = img.load()

y_wave_array1 = []
y_wave_array2 = []

for x in range(width):
    # 白くなる高さ：正弦波
    x_norm = x / width
    # FM信号で高さを決定
    y_wave = int(offset + amplitude * np.sin(
        2 * np.pi * carrier_freq * x_norm + mod_index * np.sin(2 * np.pi * mod_freq * x_norm)
    ))
    y_wave_array1.append(int(offset + 10 * np.sin(
        2 * np.pi * carrier_freq * x_norm + 3 * np.sin(2 * np.pi * 1 * x_norm)
    ) + 20 * np.sin(2 * np.pi * 5 * x_norm)))
    y_wave_array2.append(int(offset + 10 * np.sin(
        2 * np.pi * carrier_freq * x_norm + 1 * np.sin(2 * np.pi * 2 * x_norm)
    ) + 10 * np.sin(2 * np.pi * 2 * x_norm)))

    for y in range(height):
        if y < y_fixed:
            # 上部：固定グラデーション
            t = y / y_fixed
            r = g = int(border * t)
            b = 255
        elif y < y_wave:
            # 中間部：各xに応じたグラデーション
            t = (y - y_fixed) / (y_wave - y_fixed)
            r = g = border+int(border * t)
            b = 255
        else:
            # 完全な白
            r = g = b = 255

        pixels[x, y] = (r, g, b)

# 描画オブジェクト作成
draw = ImageDraw.Draw(img)

# --- FM波に沿った線を2本描画 ---

line2 = []
count = 0
for x in range(0, width):
    if count % 30 < 15:
        line2.append((x, max(0, y_wave_array2[x] - 250)))
    elif count % 30 == 15:
        draw.line(line2, fill=(50,50,200), width=5)
        line2 = []
    count += 1


# 1. 薄い黒色の実線（y_waveより20px上）
line1 = [(x, max(0, y_wave_array1[x] - 120)) for x in range(width)]
draw.line(line1, fill=(150,150,250), width=2)


# 画像を保存
img.save('background.png')