#coding:utf-8
#P26_构建自己的Windows调试器

from ctypes import *

WORD     = c_ushort
DWORD    = c_ulong
LPBYTE   = POINTER(c_ubyte)
LPTSTR   = POINTER(c_char)
HANDLE   = c_void_p

#常值定义
DEBUG_PROCESS           = 0x00000001
CREATE_NEW_CONSOLE      = 0x00000001

#定义函数CreateProcessA()所需的结构体
