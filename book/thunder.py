from PIL import Image, ImageDraw

# 画像サイズ
width, height = 256, 256

# 透明背景のRGBA画像を作成
img = Image.new("RGBA", (width, height), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)

# 稲妻マークの形（適当なスケーリングあり）
# ポイントは (x, y) で表現
lightning_shape = [
    (width * 0.45, height * 0.10),   # 上端
    (width * 0.70, height * 0.10),
    (width * 0.40, height * 0.50),   # 中央まで落ちる
    (width * 0.60, height * 0.50),
    (width * 0.35, height * 0.85),   # 下端
    (width * 0.45, height * 0.55),
    (width * 0.33, height * 0.55),
]

# ポリゴンで稲妻マークを描画
draw.polygon(lightning_shape, fill=(0, 0, 150))  # 青色

# 保存
img.save("thunder.png")