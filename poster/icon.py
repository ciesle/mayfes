import matplotlib.pyplot as plt
import numpy as np

# 描画設定
fig, ax = plt.subplots()
fig.set_size_inches(3, 3)
ax.set_aspect('equal')
ax.axis('off')  # 軸を非表示
fig.patch.set_alpha(0.0)  # 背景透明

# 波のパラメータ
num_arcs = 3
colors = (0, 0, 150/255)
linewidth = 13  # 線を太く

# 弧を描く関数（上下反転を含む）
def draw_arc(radius, width):
    theta = np.linspace(np.pi/2 + np.pi/6, np.pi/2 - np.pi/6, 100)  # 上下反転
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)
    ax.plot(x, y, color=colors, lw=width, solid_capstyle='round')

# 描画範囲を調整して線が飛び出さないように
padding = 0.2  # 少し余裕を持たせる
max_radius = num_arcs * 0.5 + padding
ax.set_xlim(-max_radius, max_radius)
ax.set_ylim(-0.5, max_radius + 0.2)  # 反転後、上方向へアークが広がる

# 波を描画
for i in range(1, num_arcs + 1):
    draw_arc(0.5 + (i-1) * 0.4, linewidth)

# 中心の点（Wi-Fiの起点）
ax.plot(0, 0.1, 'o', color=colors, markersize=14)  # 点も上に移動

# 保存（背景透明）
plt.savefig("icon.png", dpi=300, transparent=True, bbox_inches='tight', pad_inches=0)
plt.close()
