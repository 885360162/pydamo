#imports
from time import time,sleep

class DM:
    def __init__(self):
        try:
            from win32com.client import Dispatch
            #dm = Dispatch('dm.dmsoft')  # 调用大漠插件
            self.dm = Dispatch('dm.dmsoft')  # 调用大漠插件
        except:
            import os
            os.system('regsvr32 dm.dll /s')
            print('注册dm.dll')
            self.dm = Dispatch('dm.dmsoft')  # 调用大漠插件

        print('版本：', self.ver(),'，ID：',self.GetID())

    def reg(self):  #重名Reg报错，原因不明
        return self.dm.Reg('albin7a7a6b9740b219fb4db62c7865e00437', '123')
    # def Reg(self):
    #     return self.dm.Reg('albin7a7a6b9740b219fb4db62c7865e00437', '123')

        #print('reg: ', self.dm.Reg('albin7a7a6b9740b219fb4db62c7865e00437', '123'))
        # print('reg: ',dm.Reg('xxhongdev4dd3dddabe56dfb834fb3b70f0cea8ee', '123'))
        # dm.Reg('fzdxwhl20070b412e2fa2fc4462a6c25de3826e859e','147')
        # dm.Reg('xxhongdev4dd3dddabe56dfb834fb3b70f0cea8ee','Oa0UhMx5rC')

    def GetDmCount(self):
        return self.dm.GetDmCount()
    def GetID(self):
        return self.dm.GetID()

    # base
    if (1):
        def ver(self):
            return self.dm.ver()

        def Reg(self, reg_code, ver_info):
            return self.dm.Reg(reg_code, ver_info)

        def GetDir(self, type):
            return self.GetDir(type)

        def GetBasePath(self):
            return self.dm.GetBasePath()

        def GetPath(self):
            return self.dm.GetPath()

        def GetID(self):
            return self.dm.GetID()

        def SetDisplayInput(self, mode):
            return self.dm.SetDisplayInput(mode)

        def SetShowErrorMsg(self, show):
            return self.dm.SetShowErrorMsg(show)

        1

    # color
    if (1):
        def Capture(self, x1, y1, x2, y2, file):
            return self.dm.Capture(x1, y1, x2, y2, file)

        def FindPic(self, x1, y1, x2, y2, pic_name, delta_color='101010', sim=0.9, dir=0, intX=0, intY=0):
            return self.dm.FindPic(x1, y1, x2, y2, pic_name, delta_color='101010', sim=0.9, dir=0, intX=0, intY=0)

        def FindColor(self, x1, y1, x2, y2, color, sim, dir, intX, intY):
            return self.dm.FindColor(x1, y1, x2, y2, color, sim, dir, intX, intY)

        def LoadPic(self, pic_name):
            return self.dm.LoadPic(pic_name)

        def LoadPic(self, pic_name):
            return self.dm.LoadPic(pic_name)

        def FreePic(self, pic_name):
            return self.dm.FreePic(pic_name)

        def GetColor(self, x, y):
            return self.dm.GetColor(x, y)

        def GetPicSize(self, pic_name):
            return self.dm.GetPicSize(pic_name)

        def BGR2RGB(self, bgr_color):
            return self.dm.BGR2RGB(bgr_color)

        def CmpColor(self, x, y, color, sim):
            return self.dm.CmpColor(x, y, color, sim)

        1

    # window
    if (1):
        def BindWindow(self, hwnd, display=['normal', 'gdi', 'gdi2', 'dx', 'dx2'][1],
                       mouse=['normal', 'windows', 'windows2', 'windows3', 'dx', 'dx2'][1],
                       keypad=['normal', 'windows', 'dx'][1],
                       mode=[0, 1, 2, 3, 4, 5, 6, 7, 101, 103][0]):
            return self.dm.BindWindow(hwnd, display, mouse, keypad, mode)

        def UnBindWindow(self):
            return self.dm.UnBindWindow()

        def IsBind(self, hwnd):
            return self.dm.IsBind(hwnd)

        def MoveWindow(self, hwnd, x, y):
            return self.dm.MoveWindow(hwnd, x, y)

        def FindWindow(self, class_name='', title_name=''):
            return self.dm.FindWindow(class_name, title_name)

        def ClientToScreen(self, hwnd, x, y):
            return self.dm.ClientToScreen(hwnd, x, y)

        def ScreenToClient(self, hwnd, x, y):
            return self.dm.ScreenToClient(hwnd, x, y)

        def FindWindowByProcess(self, process_name, class_name, title_name):
            return self.dm.FindWindowByProcess(process_name, class_name, title_name)

        def FindWindowByProcessId(self, process_id, class_, title):
            return self.dm.FindWindowByProcessId(process_id, class_, title)

        def GetClientRect(self, hwnd, x1, y1, x2, y2):
            return self.dm.GetClientRect(hwnd, x1, y1, x2, y2)

        def GetClientSize(self, hwnd, width, height):
            return self.dm.GetClientSize(hwnd, width, height)

        def GetWindowRect(self, hwnd, x1, y1, x2, y2):
            return self.dm.GetWindowRect(hwnd, x1, y1, x2, y2)

        def GetWindow(self, hwnd, flag):
            return self.dm.GetWindow(hwnd, flag)

        def GetWindowProcessPath(self, hwnd):
            return self.dm.GetWindowProcessPath(hwnd)

        def SetWindowSize(self, hwnd, width, height):
            return self.dm.SetWindowSize(hwnd, width, height)

        def SetWindowState(self, hwnd, flag):
            return self.dm.SetWindowState(hwnd, flag)

        def SetWindowText(self, hwnd, title):
            return self.dm.SetWindowText(hwnd, title)

        def SetWindowTransparent(self, hwnd, trans):
            return self.dm.SetWindowTransparent(hwnd, trans)

        def EnumWindow(self, parent, title, class_name, filter):
            return self.dm.EnumWindow(parent, title, class_name, filter)

        def EnumWindowByProcess(self, process_name, title, class_name, filter):
            return self.dm.EnumWindowByProcess(process_name, title, class_name, filter)

        def EnumWindowSuper(self, spec1, flag1, type1, spec2, flag2, type2, sort):
            return self.dm.EnumWindowSuper(spec1, flag1, type1, spec2, flag2, type2, sort)

        1

    # key_mouse
    if (1):
        def GetCursorPos(self, x=0, y=0):
            return self.dm.GetCursorPos(x, y)

        def GetKeyState(self, vk_code):
            return self.dm.GetKeyState(vk_code)

        def SetKeypadDelay(self, type=['normal', 'windows', 'dx'][-1], delay=[0.03, 0.01, 0.05][-1]):
            return self.dm.SetKeypadDelay(type, delay)

        def SetMouseDelay(self, delay=[0.03, 0.01, 0.04][-1], type=['normal', 'windows', 'dx'][-1]):
            return self.dm.SetMouseDelay(type, delay)

        def WaitKey(self, vk_code, time_out=0):
            # vk_code = 'a'
            # vk_code.__class__.__name__ == 'str'
            # vk_code.upper()
            # kk
            # if(vk_code.__class__.)
            return self.dm.WaitKey(vk_code, time_out)

        # def WaitKey(vk_code,time_out = 0):
        #     # vk_code = 'a'
        #     # vk_code.__class__.__name__ == 'str'
        #     # vk_code.upper()
        #     # kk
        #     # if(vk_code.__class__.)
        #
        #     return print(vk_code, time_out)
        # WaitKey('a')

        def KeyDown(self, vk_code):
            return self.dm.KeyDown(vk_code)

        def KeyDownChar(self, key_str):
            return self.dm.KeyDownChar(key_str)

        def KeyPress(self, vk_code):
            return self.dm.KeyPress(vk_code)

        def KeyPressChar(self, key_str):
            return self.dm.KeyPressChar(key_str)

        def KeyPressStr(self, key_str, delay):
            return self.dm.KeyPressStr(key_str, delay)

        def KeyUp(self, vk_code):
            return self.dm.KeyUp(vk_code)

        def KeyUpChar(self, key_str):
            return self.dm.KeyUpChar(key_str)

        def LeftClick(self, ):
            return self.dm.LeftClick()

        def LeftDoubleClick(self, ):
            return self.dm.LeftDoubleClick()

        def LeftDown(self, ):
            return self.dm.LeftDown()

        def LeftUp(self, ):
            return self.dm.LeftUp()

        def MiddleClick(self, ):
            return self.dm.MiddleClick()

        def MoveR(self, rx, ry):
            return self.dm.MoveR(rx, ry)

        def MoveTo(self, x, y):
            return self.dm.MoveTo(x, y)

        def MoveToEx(self, x, y, w, h):
            return self.dm.MoveToEx(x, y, w, h)

        def RightClick(self, ):
            return self.dm.RightClick()

        def RightDown(self, ):
            return self.dm.RightDown()

        def RightUp(self, ):
            return self.dm.RightUp()

        def SetKeypadDelay(self, type, delay):
            return self.dm.SetKeypadDelay(type, delay)

        def SetMouseDelay(self, type, delay):
            return self.dm.SetMouseDelay(type, delay)

        def WaitKey(self, vk_code, time_out):
            return self.dm.WaitKey(vk_code, time_out)

        def WheelDown(self, ):
            return self.dm.WheelDown()

        def WheelUp(self, ):
            return self.dm.WheelUp()

        1

    # memmory
    if (1):
        def FindData(self, hwnd, addr_range, data):
            return self.dm.FindData( hwnd, addr_range, data)
        def FindDataEx(self, hwnd, addr_range, data, step, multi_thread, mode):
            return self.dm.FindDataEx(hwnd, addr_range, data, step, multi_thread, mode)

        def DoubleToData(self, value):
            return self.dm.DoubleToData(value)

        def FloatToData(self, value):
            return self.dm.FloatToData(value)

        def GetModuleBaseAddr(self, hwnd, module):
            return self.dm.GetModuleBaseAddr(hwnd, module)

        def IntToData(self, value, type):
            return self.dm.IntToData(value, type)

        def ReadData(self, hwnd, addr, len):
            return self.dm.ReadData(hwnd, addr, len)

        def ReadDouble(self, hwnd, addr):
            return self.dm.ReadDouble(hwnd, addr)

        def ReadFloat(self, hwnd, addr):
            return self.dm.ReadFloat(hwnd, addr)

        def ReadInt(self, hwnd, addr, type):
            return self.dm.ReadInt(hwnd, addr, type)

        def ReadString(self, hwnd, addr, type, len):
            return self.dm.ReadString(hwnd, addr, type, len)

        def StringToData(self, value, type):
            return self.dm.StringToData(value, type)

        def WriteData(self, hwnd, addr, data):
            return self.dm.WriteData(hwnd, addr, data)

        def WriteDouble(self, hwnd, addr, v):
            return self.dm.WriteDouble(hwnd, addr, v)

        def WriteFloat(self, hwnd, addr, v):
            return self.dm.WriteFloat(hwnd, addr, v)

        def WriteInt(self, hwnd, addr, type, v):
            return self.dm.WriteInt(hwnd, addr, type, v)

        def WriteString(self, hwnd, addr, type, v):
            return self.dm.WriteString(hwnd, addr, type, v)

        1

    # file
    if (1):
        def CopyFile(self, src_file, dst_file, over):
            return self.dm.CopyFile(src_file, dst_file, over)

        def CreateFolder(self, folder):
            return self.dm.CreateFolder(folder)

        def DecodeFile(self, file, pwd):
            return self.dm.DecodeFile(file, pwd)

        def DeleteFile(self, file):
            return self.dm.DeleteFile(file)

        def DeleteFolder(self, folder):
            return self.dm.DeleteFolder(folder)

        def DeleteIni(self, section, key, file):
            return self.dm.DeleteIni(section, key, file)

        def DeleteIniPwd(self, section, key, file, pwd):
            return self.dm.DeleteIniPwd(section, key, file, pwd)

        def DownloadFile(self, url, save_file, timeout):
            return self.dm.DownloadFile(url, save_file, timeout)

        def EncodeFile(self, file, pwd):
            return self.dm.EncodeFile(file, pwd)

        def GetFileLength(self, file):
            return self.dm.GetFileLength(file)

        def IsFileExist(self, file):
            return self.dm.IsFileExist(file)

        def MoveFile(self, src_file, dst_file):
            return self.dm.MoveFile(src_file, dst_file)

        def ReadFile(self, file):
            return self.dm.ReadFile(file)

        def ReadIni(self, section, key, file):
            return self.dm.ReadIni(section, key, file)

        def ReadIniPwd(self, section, key, file, pwd):
            return self.dm.ReadIniPwd(section, key, file, pwd)

        def SelectDirectory(self, ):
            return self.dm.SelectDirectory()

        def SelectFile(self, ):
            return self.dm.SelectFile()

        def WriteFile(self, file, content):
            return self.dm.WriteFile(file, content)

        def WriteIni(self, section, key, value, file):
            return self.dm.WriteIni(section, key, value, file)

        def WriteIniPwd(self, section, key, value, file, pwd):
            return self.dm.WriteIniPwd(section, key, value, file, pwd)

    # system
    if (1):
        def GetNetTime(self, ):
            return self.dm.GetNetTime()

        def GetOsType(self, ):
            return self.dm.GetOsType()

        def GetScreenHeight(self, ):
            return self.dm.GetScreenHeight()

        def GetScreenWidth(self, ):
            return self.dm.GetScreenWidth()

        def GetTime(self, ):
            return self.dm.GetTime()

        def Is64Bit(self, ):
            return self.dm.Is64Bit()

        def RunApp(self, app_path, mode):
            return self.dm.RunApp(app_path, mode)

        def Play(self, media_file):
            return self.dm.Play(media_file)

        def Stop(self, id):
            return self.dm.Stop(id)

        def Delay(self, mis):
            return self.dm.Delay(mis)

        def ExitOs(self, type):
            return self.dm.ExitOs(type)

        def Beep(self, duration=500, f=500):
            return self.dm.Beep(f, duration)

    # My function
    def stop_0(self, ch='p', continue_key='p'):
        # ch = 'a'
        break0 = 0
        ch = ch.upper()

        if (self.dm.GetKeyState(ord(ch))):
            print('------- Stop! --------')
            from win32gui import MessageBox
            # 'A'.upper()
            break0 = (MessageBox(0, 'Do you continue?', 'Stop!', 1) - 1)
            # break0 = self.WaitKey(ord(continue_key.upper()),0)

            if (break0 == 1):
                print('------ Break!!! ---------')
            # return break0
        return break0
    1

class Time:

    def __init__(self):

        self.t0 = time()
        self.t1 = time()
        self.now()

    def now(self):

        self.t1 = time()
        return self.t1 - self.t0

    def exceed(self, T):
        if (self.now() >= T):
            return 1
        else:
            return 0

    1

class VK:
        Time = 0.1
        Constant = 800

        ctrl = 17
        alt = 18
        shift = 16

        f1 = 112
        f2 = 113
        f3 = 114
        f4 = 116
        f5 = 117

        enter = 13
        space = 32
        back = 8


        #小键盘数字
        n0, n1, n2, n3, n4, n5, n6, n7, n8, n9 = 96, 97, 98, 99, 100, 101, 102, 103, 104, 105

        left, up, right, down = 37, 38, 39, 40

class Key:
    def __init__(self,dm = 0, key='k'):
        if(dm == 0):
            self.dm = DM()
        else:
            self.dm = dm

        
        if (key.__class__.__name__ == 'str'):
            self.chr = key.upper()
        else:
            self.chr = 'None'
        self.ord = self.conv_ord(key)

    def get_ord(self, key):
        key = key.upper()
        return ord(key)

    def __main__(self):
        return self.ord

    def conv_ord(self, key0):
        key = key0
        if (key.__class__.__name__ == 'str'):
            # key = key.upper()
            key = ord(key.upper())
        elif (key.__class__.__name__ == 'int'):
            if (key >= 0 and key <= 9):
                key = str(key)
                key = ord(key)
        return key

    def conv_chr(self, key):
        key = chr(key)
        return key

    def conv(self, key0):
        key = key0
        if (key == VK.Constant):
            key = self.ord
        else:
            key = self.conv_ord(key)
        return key

    def state(self, key=VK.Constant):
        key = self.conv(key)
        return self.dm.GetKeyState(key)

    def press(self, key0=VK.Constant):
        key = self.conv_ord(key0)

        return self.dm.KeyPress(key)

    def down(self, key0=VK.Constant):
        key = self.conv_ord(key0)

        return self.dm.KeyDown(key)

    def up(self, key0=VK.Constant):
        key = self.conv_ord(key0)

        return self.dm.KeyUp(key)

    def down_up(self, key0=VK.Constant, t=VK.Time):
        key = self.conv_ord(key0)
        self.down(key)
        sleep(t)
        self.up(key)

    def dp(self, key=VK.Constant, t=VK.Time):
        self.down_up(key, t)

    def test_dp(self, key, delay=1, t=VK.Time):
        sleep(delay)
        self.dp(key, t)

    1

    1

class Mouse:
    def __init__(self,dm = 0):
        if (dm == 0):
            self.dm = DM()
        else:
            self.dm = dm

    def position(self):
        return self.dm.GetCursorPos(x=0, y=0)[1:]

    def set_delay(self, delay, type='dx'):
        return self.dm.SetMouseDelay(type, delay)

    def move_to(self, x, y):
        return self.dm.MoveTo(x, y)

    def click_left(self,x, y, t=0.5):
        self.dm.MoveTo(x, y)
        return self.dm.LeftClick()

    def test_click_left(self,x, y, t=0.5, delay=1):
        sleep(delay)
        return self.click_left(x, y, t)

    def click_right(self,x, y, t=0.5):
        self.dm.MoveTo(x, y)
        return self.dm.RightClick()

    def test_click_right(self,x, y, t=0.5, delay=1):
        sleep(delay)
        return self.click_right(x, y, t)
    #大漠对象的直接转换
    if(1):
        def LeftClick(self, ):
            return self.dm.LeftClick()

        def LeftDoubleClick(self, ):
            return self.dm.LeftDoubleClick()

        def MiddleClick(self, ):
            return self.dm.MiddleClick()

        def LeftDown(self, ):
            return self.dm.LeftDown()

        def LeftUp(self, ):
            return self.dm.LeftUp()

        def RightClick(self, ):
            return self.dm.RightClick()

        def SetMouseDelay(self, type, delay):
            return self.dm.SetMouseDelay(type, delay)

        def MoveR(self, rx, ry):
            return self.dm.MoveR(rx, ry)

        def RightDown(self, ):
            return self.dm.RightDown()

        def RightUp(self, ):
            return self.dm.RightUp()

        def WheelDown(self, ):
            return self.dm.WheelDown()

        def WheelUp(self, ):
            return self.dm.WheelUp()

        def GetCursorShape(self, ):
            return self.dm.GetCursorShape()

        def GetCursorShapeEx(self, int_type):
            return self.dm.GetCursorShapeEx(int_type)
    1


#增加大漠函数时可以简化操作

# #将公有函数转换为dm对象里面的私有函数
# def f0_to_f1(f0):
#     f0_name, f0_para = f0.split(')')[0].split('(')
#     f0_name, f0_para
#     str = 'def {0}(self,{1}):\n\treturn self.dm.{2}'.format(f0_name, f0_para, f0)
#     print(str)
#
#
# ff = '''LeftClick()
# LeftDoubleClick()
# MiddleClick()
# LeftDown()
# LeftUp()
# RightClick()
# SetMouseDelay(type,delay)
# MoveR(rx,ry)
# RightDown()
# RightUp()
# WheelDown()
# WheelUp()
# GetCursorShape()
# GetCursorShapeEx(int_type)'''
#
# #多个一起转换,最好ff向左缩进至顶格再转换！
# def ff0_to_ff1(ff):
#     ff_0 = ff.split('\n')
#     for f0 in ff_0: f0_to_f1(f0)
# ff0_to_ff1(ff)
