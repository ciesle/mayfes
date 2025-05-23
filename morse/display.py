import serial
import threading
import tkinter as tk

# ===== シリアルポート設定 =====
SERIAL_PORT = 'COM3'  # 適切なポート名に変更（例: '/dev/ttyUSB0'）
BAUD_RATE = 9600      # 通信速度（デバイスに合わせて変更）

# グローバル変数
latest_data = ""

# ===== データ受信スレッド =====
def read_serial():
    global latest_data
    try:
        with serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1) as ser:
            while True:
                line = ser.readline().decode('utf-8', errors='ignore').strip()
                if line:
                    latest_data = line
    except serial.SerialException as e:
        print(f"シリアルエラー: {e}")

# ===== GUI表示設定 =====
def update_label():
    label.config(text=latest_data)
    root.after(100, update_label)  # 100ミリ秒ごとに更新

# ===== メイン処理 =====
if __name__ == '__main__':
    # シリアル受信スレッドの開始
    thread = threading.Thread(target=read_serial, daemon=True)
    thread.start()

    # GUIの初期化
    root = tk.Tk()
    root.title("シリアルモニター")

    label = tk.Label(root, text="", font=("Arial", 100), fg="black")
    label.pack(expand=True)

    # ラベルの更新ループ
    update_label()

    # GUIのメインループ開始
    root.mainloop()
