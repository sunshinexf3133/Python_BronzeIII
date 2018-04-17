#coding:utf-8
#P6_使用动态链接库

from ctypes import *
msvcrt = cdll.msvcrt
message_string = "Hello World!\n"
msvcrt.printf("Testing : %s",message_string)
