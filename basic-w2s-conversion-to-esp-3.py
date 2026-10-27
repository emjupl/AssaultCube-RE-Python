import pymem
import os
import struct
import win32gui
import win32api

pm = pymem.Pymem("ac_client.exe")

module = pymem.process.module_from_name(
    pm.process_handle, "ac_client.exe"
)
base = module.lpBaseOfDll

ObjectList = base + 0x0018AC04
oXcoord = 0x004
oYcoord = 0x008
oZcoord = 0x00C

def set_pixel(x, y, color):
    hdc = win32gui.GetDC(0)
    win32gui.SetPixel(hdc, x, y, color)
    win32gui.ReleaseDC(0, hdc)

def read_matrix():
    matrixAddress = 0x57DFD0
    matrix = pm.read_bytes(matrixAddress, 64)
    matrix = struct.unpack("16f", matrix)
    return matrix

def get_window_info(title="AssaultCube"):
    hwnd = win32gui.FindWindow(None, title)
    if not hwnd:
        return None
    l, t, r, b = win32gui.GetClientRect(hwnd)
    X, Y = win32gui.ClientToScreen(hwnd, (0, 0))
    return r - l, b - t, X, Y

def world_to_screen(pos, m, W, H):
    x, y, z = pos
    clip_x = x * m[0] + y * m[4] + z * m[8] + m[12]
    clip_y = x * m[1] + y * m[5] + z * m[9] + m[13]
    clip_w = x * m[3] + y * m[7] + z * m[11] + m[15]
    if clip_w < 0.1:
        return None
    ndc_x = clip_x / clip_w
    ndc_y = clip_y / clip_w
    return (W / 2) * ndc_x + W / 2, H / 2 - (H / 2) * ndc_y

def main():
    if (module):
        while True:
            playerCount = pm.read_uint(pm.read_uint(base + 0x0005C434))

            for i in range(1, playerCount):
                ObjectListStart = pm.read_uint(ObjectList)
                entityAddress = ObjectListStart + 4*i

                entityXcoord = pm.read_float(pm.read_uint(entityAddress) + oXcoord)
                entityYcoord = pm.read_float(pm.read_uint(entityAddress) + oYcoord)
                entityZcoord = pm.read_float(pm.read_uint(entityAddress) + oZcoord)

                acWindowInfo = get_window_info()
                acWindowWidth, acWindowHeight, acWindowPositionX, acWindowPositionY = acWindowInfo

                viewMatrix = read_matrix()
                entityPosition = (entityXcoord, entityYcoord, entityZcoord)
                try:
                    W2SscreenX, W2SscreenY = world_to_screen(entityPosition, viewMatrix, acWindowWidth, acWindowHeight)
                    set_pixel(round(W2SscreenX)+acWindowPositionX, round(W2SscreenY)+acWindowPositionY, win32api.RGB(255, 0, 0))
                except Exception:
                    pass
main()






