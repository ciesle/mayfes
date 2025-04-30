import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
import japanize_matplotlib

# WAVファイルの読み込み
sampling_rate, data = wavfile.read("sample.wav")

# モノラルに変換（ステレオの場合）
if len(data.shape) == 2:
    data = data[:, 0]  # 左チャンネルを使用

# 1秒後から1秒間のデータを切り出す
start_sample = sampling_rate * 1  # 1秒後
end_sample = start_sample + sampling_rate//10  # さらに1秒分

segment = data[start_sample:end_sample]

# 正規化（振幅を[-1, 1]に）
if data.dtype == np.int16:
    segment = segment / 32768.0
elif data.dtype == np.int32:
    segment = segment / 2147483648.0

# 時間軸
time = np.linspace(0, 1/10, len(segment))

# 波形表示
plt.figure(figsize=(10, 3))
plt.plot(time, segment, color='black')
plt.xlabel("時間 [s]")
plt.ylabel("振幅 [V]")
plt.grid()
plt.tight_layout()
plt.show()
