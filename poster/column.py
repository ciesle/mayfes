import numpy as np
from PIL import Image, ImageDraw
from scipy.ndimage import distance_transform_edt

# 画像サイズ・矩形サイズ
width, height = 1000, 500
rect_w, rect_h = 750, 300
margin_x = (width - rect_w) // 2
margin_y = (height - rect_h) // 2

# 正弦波設定
amplitude = 5
period_px = 150  # 1周期の長さ（px）
points_per_edge = 300

# 正弦波関数（位相調整なし、整数周期数で高さ連続を確保）
def sine_wave(length_px, num_points, amp, base_pos, axis="x"):
    num_cycles = round(length_px / period_px)
    cycle_length = length_px / num_cycles
    points = []
    for i in range(num_points):
        t = i / (num_points - 1)
        s = t * length_px
        angle = 2 * np.pi * (s / cycle_length)
        offset = amp * np.sin(angle)
        if axis == "x":
            points.append((int(base_pos[0] + s), int(base_pos[1] + offset)))
        else:
            points.append((int(base_pos[0] + offset), int(base_pos[1] + s)))
    return points

# 各辺を生成（始点と終点の高さを合わせる）
top = sine_wave(rect_w, points_per_edge, amplitude, (margin_x, margin_y), axis="x")
right = sine_wave(rect_h, points_per_edge, amplitude, (margin_x + rect_w, margin_y), axis="y")
bottom = list(reversed(sine_wave(rect_w, points_per_edge, amplitude, (margin_x, margin_y + rect_h), axis="x")))
left = list(reversed(sine_wave(rect_h, points_per_edge, amplitude, (margin_x, margin_y), axis="y")))

# すべて結合して多角形
points = top + right + bottom + left

# グラデーションマスク生成
mask = Image.new("L", (width, height), 0)
draw_mask = ImageDraw.Draw(mask)
draw_mask.polygon(points, fill=255)

# グラデーション（内向きに透明）
mask_np = np.array(mask)
inv_mask = 255 - mask_np
dist = distance_transform_edt(inv_mask)
fade_range = 10
alpha = np.clip((fade_range - dist) / fade_range * 255, 0, 255).astype(np.uint8)

# RGBA出力
rgba = np.zeros((height, width, 4), dtype=np.uint8)
rgba[..., 0] = 180     # R
rgba[..., 1] = 255     # G
rgba[..., 2] = 180     # B
rgba[..., 3] = alpha   # A

# PIL画像に変換して上下反転
img = Image.fromarray(rgba, mode="RGBA")
img = img.transpose(Image.FLIP_TOP_BOTTOM)

img.save("column.png")