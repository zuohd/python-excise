''''
used in windows operation system
'''
import win32api
import win32con
import win32gui


def setWallPaper(path):
    reg_key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,"Control Pannel\\Desktop", 0, win32con.KEY_SET_VALUE)
