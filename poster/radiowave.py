import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 4周期分のt
# 変更後（4周期、1周期 = 4π の長さ → 2倍に拡大）
t = np.linspace(0, 4 * 2 * np.pi, 500)
x = t
y_red = -np.sin(t) / 3
z_blue = np.sin(t + np.pi / 2) / 3

# プロット準備
fig = plt.figure(figsize=(20, 6))
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(
    np.array([x, x]),
    np.array([y_red, np.zeros_like(y_red)]),
    np.array([[0] * len(x), [0] * len(x)]),
    color='red', alpha=1.0
)
ax.plot_surface(
    np.array([x, x]),
    np.array([[0] * len(x), [0] * len(x)]),
    np.array([z_blue, np.zeros_like(z_blue)]),
    color='blue', alpha=1.0
)

# 赤い波（Y方向）と塗り面
#ax.plot(x, y_red, zs=0, zdir='z', color='red')
# 青い波（Z方向）と塗り面
#ax.plot(x, z_blue, zs=0, zdir='y', color='blue')

ax.set_xlim(0, 4 * 2 * np.pi)  # ← x軸の表示範囲を2倍に
ax.set_ylim(-1, 1)  # ← x軸の表示範囲を2倍に
ax.set_zlim(-1, 1)  # ← x軸の表示範囲を2倍に

ax.view_init(elev=30, azim=60)

# 軸・背景パネルを非表示
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])
ax.set_axis_off()
for axis in [ax.xaxis, ax.yaxis, ax.zaxis]:
    axis.set_pane_color((1.0, 1.0, 1.0, 0.0))
    axis._axinfo["grid"]['color'] = (1, 1, 1, 0)



# 背景を透明にして保存
plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
fig.patch.set_alpha(0)
plt.savefig("radiowave.png", dpi=300, transparent=True)
plt.close()
