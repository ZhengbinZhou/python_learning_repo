import tkinter as tk
from tkinter import messagebox, simpledialog
import threading
import time
import random
import datetime
import os
import sys


class StudyMonitor:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("学习监督器")
        self.root.geometry("400x300")
        self.root.resizable(False, False)

        # 设置窗口图标
        try:
            self.root.iconbitmap("study_icon.ico")  # 如果有图标文件
        except:
            pass

        # 创建UI元素
        self.create_widgets()

        # 初始化变量
        self.study_time = 0
        self.remaining_time = 0
        self.is_studying = False
        self.is_resting = False
        self.notification_thread = None
        self.stop_event = threading.Event()

        # 启动主循环
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

    def create_widgets(self):
        # 标题
        title_label = tk.Label(self.root, text="学习监督器", font=("Arial", 20, "bold"))
        title_label.pack(pady=10)

        # 设置学习时间
        time_frame = tk.Frame(self.root)
        time_frame.pack(pady=10)

        tk.Label(time_frame, text="设置学习时间(分钟):").pack(side=tk.LEFT)
        self.time_entry = tk.Entry(time_frame, width=10)
        self.time_entry.pack(side=tk.LEFT, padx=5)
        self.time_entry.insert(0, "60")

        # 按钮框架
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=20)

        self.start_button = tk.Button(button_frame, text="开始学习", command=self.start_study, width=15, height=2)
        self.start_button.pack(side=tk.LEFT, padx=10)

        self.pause_button = tk.Button(button_frame, text="暂停", command=self.pause_study, width=15, height=2,
                                      state=tk.DISABLED)
        self.pause_button.pack(side=tk.LEFT, padx=10)

        # 状态显示
        self.status_label = tk.Label(self.root, text="准备开始学习", font=("Arial", 12))
        self.status_label.pack(pady=10)

        self.time_label = tk.Label(self.root, text="剩余时间: --:--", font=("Arial", 14))
        self.time_label.pack(pady=5)

        # 进度条
        self.progress = tk.DoubleVar()
        self.progress_bar = tk.Scale(self.root, from_=0, to=100, orient=tk.HORIZONTAL,
                                     length=350, showvalue=False, variable=self.progress,
                                     state=tk.DISABLED)
        self.progress_bar.pack(pady=10)

        # 底部状态栏
        self.bottom_status = tk.Label(self.root, text="程序已就绪", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.bottom_status.pack(side=tk.BOTTOM, fill=tk.X)

    def start_study(self):
        try:
            self.study_time = int(self.time_entry.get()) * 60  # 转换为秒
            if self.study_time <= 0:
                messagebox.showerror("错误", "学习时间必须大于0")
                return
        except ValueError:
            messagebox.showerror("错误", "请输入有效的数字")
            return

        self.remaining_time = self.study_time
        self.is_studying = True
        self.is_resting = False
        self.stop_event.clear()

        # 更新UI
        self.start_button.config(state=tk.DISABLED)
        self.pause_button.config(state=tk.NORMAL)
        self.time_entry.config(state=tk.DISABLED)
        self.status_label.config(text="学习中...")
        self.update_time_label()
        self.progress.set(0)
        self.progress_bar.config(state=tk.NORMAL)
        self.bottom_status.config(text="学习已开始 - {}".format(datetime.datetime.now().strftime("%H:%M:%S")))

        # 启动通知线程
        self.notification_thread = threading.Thread(target=self.run_notifications)
        self.notification_thread.daemon = True
        self.notification_thread.start()

        # 启动计时线程
        threading.Thread(target=self.run_timer).start()

    def pause_study(self):
        if self.is_studying:
            self.is_studying = False
            self.pause_button.config(text="继续")
            self.status_label.config(text="已暂停")
            self.bottom_status.config(text="学习已暂停")
        else:
            self.is_studying = True
            self.pause_button.config(text="暂停")
            self.status_label.config(text="学习中...")
            self.bottom_status.config(text="学习已继续")
            # 重新启动计时线程
            threading.Thread(target=self.run_timer).start()

    def run_timer(self):
        start_time = time.time()
        elapsed = 0

        while self.is_studying and elapsed < self.study_time:
            if self.stop_event.is_set():
                break

            time.sleep(1)
            elapsed = time.time() - start_time
            self.remaining_time = max(0, self.study_time - elapsed)
            self.progress.set((elapsed / self.study_time) * 100)
            self.update_time_label()

            # 检查是否需要休息（每50分钟）
            if not self.is_resting and elapsed >= 50 * 60 and (elapsed - 50 * 60) % (60 * 60) < 1:
                self.start_rest()

        if elapsed >= self.study_time:
            self.complete_study()

    def start_rest(self):
        self.is_resting = True
        self.status_label.config(text="休息中...")
        self.bottom_status.config(text="休息时间 - {}".format(datetime.datetime.now().strftime("%H:%M:%S")))

        # 休息10分钟
        rest_start = time.time()
        while time.time() - rest_start < 600 and self.is_studying and not self.stop_event.is_set():
            time.sleep(1)

        if self.is_studying and not self.stop_event.is_set():
            self.show_notification("休息结束", "10分钟休息时间已结束，请继续学习！")
            self.is_resting = False
            self.status_label.config(text="学习中...")
            self.bottom_status.config(text="学习已继续")

    def run_notifications(self):
        segment_start = time.time()

        while self.is_studying and not self.stop_event.is_set():
            # 如果正在休息，不发送通知
            if self.is_resting:
                time.sleep(1)
                continue

            # 计算当前学习段的时间
            segment_elapsed = time.time() - segment_start

            # 每10分钟一个段
            if segment_elapsed >= 600:
                segment_start = time.time()
                continue

            # 在10分钟内随机选择一个时间点发送通知
            if segment_elapsed >= random.randint(60, 540):  # 1-9分钟之间
                self.show_notification("坚持学习", "加油！继续保持专注，坚持学习！")
                segment_start = time.time()  # 重置段开始时间
                time.sleep(60)  # 避免短时间内多次通知
            else:
                time.sleep(1)

    def show_notification(self, title, message):
        # 创建全屏提醒窗口
        def create_popup():
            popup = tk.Toplevel(self.root)
            popup.title(title)
            popup.attributes("-fullscreen", True)  # 全屏
            popup.attributes("-topmost", True)  # 置顶

            # 添加关闭按钮
            close_button = tk.Button(popup, text="知道了", command=popup.destroy,
                                     font=("Arial", 16), bg="#4CAF50", fg="white",
                                     height=2, width=20)
            close_button.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

            # 添加消息
            message_label = tk.Label(popup, text=message, font=("Arial", 24),
                                     wraplength=popup.winfo_screenwidth() - 100)
            message_label.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

            # 添加时间信息
            time_label = tk.Label(popup, text=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                                  font=("Arial", 14))
            time_label.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

            # 添加图标
            try:
                icon = tk.PhotoImage(file="study_icon.png")
                icon_label = tk.Label(popup, image=icon)
                icon_label.image = icon
                icon_label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
            except:
                pass

        # 在主线程中创建GUI元素
        self.root.after(0, create_popup)

    def update_time_label(self):
        minutes, seconds = divmod(int(self.remaining_time), 60)
        self.time_label.config(text=f"剩余时间: {minutes:02d}:{seconds:02d}")
        self.root.update()

    def complete_study(self):
        self.is_studying = False
        self.stop_event.set()

        # 更新UI
        self.start_button.config(state=tk.NORMAL)
        self.pause_button.config(state=tk.DISABLED, text="暂停")
        self.time_entry.config(state=tk.NORMAL)
        self.status_label.config(text="学习完成！")
        self.time_label.config(text="剩余时间: 00:00")
        self.progress.set(100)
        self.bottom_status.config(text="学习已完成 - {}".format(datetime.datetime.now().strftime("%H:%M:%S")))

        # 显示完成通知
        self.show_notification("学习完成", f"恭喜！您已完成 {int(self.study_time / 60)} 分钟的学习！")

    def on_closing(self):
        if self.is_studying:
            if messagebox.askyesno("确认", "学习仍在进行中，确定要退出吗？"):
                self.stop_event.set()
                self.root.destroy()
        else:
            self.root.destroy()


# 运行程序
if __name__ == "__main__":
    StudyMonitor()