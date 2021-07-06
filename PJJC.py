#在角色配队中的编组1、3、4、5配好换防的队伍
#点开公主竞技场，然后运行,模拟器分辨率要调成1600*900

import os
import time
import random

def connect():
    try:
        os.system("adb kill-server && adb start-server")
        os.system("adb remount")     # 此处端口号为mumu模拟器，其他模拟器需更换端口号
    except:
        print('连接失败')

def disconnect():
    os.system("adb kill-server")

def click(x, y):
    print(x, y)
    os.system('adb shell input tap %s %s' % (x, y))


def change1():
    click(1440, 160) #防止刷新网络卡顿
    time.sleep(10)
    
    click(450, 700)   # 防守设定
    time.sleep(0.5)

    # 队伍1 清空
    click(900, 750)  # 移除五号位
    time.sleep(0.5)
    click(900, 750)  # 移除五号位
    time.sleep(0.5)
    click(900, 750)  # 移除五号位
    time.sleep(0.5)
    click(900, 750)  # 移除五号位
    time.sleep(0.5)
    click(900, 750)  # 移除五号位
    time.sleep(0.5)


    click(1400, 750)  # 队伍2
    time.sleep(0.5)
    click(900, 750)   # 移除五号位
    time.sleep(0.5)
    click(900, 750)  # 移除五号位
    time.sleep(0.5)
    click(900, 750)  # 移除五号位
    time.sleep(0.5)
    click(900, 750)  # 移除五号位
    time.sleep(0.5)
    click(900, 750)  # 移除五号位
    time.sleep(0.5)

    click(1400, 750)  # 队伍3
    time.sleep(0.5)
    click(900, 750)  # 移除五号位
    time.sleep(0.5)
    click(900, 750)  # 移除五号位
    time.sleep(0.5)
    click(900, 750)  # 移除五号位
    time.sleep(0.5)
    click(900, 750)  # 移除五号位
    time.sleep(0.5)
    click(900, 750)  # 移除五号位
    time.sleep(0.5)

    click(150, 150)  # 队伍1
    time.sleep(0.5)

    click(1450, 250)  # 我的队伍
    time.sleep(0.5)
    click(1300, 300)  # 呼出此编制1
    time.sleep(0.5)


    click(350, 150)   # 队伍2
    time.sleep(0.5)

    click(1450, 250)  # 我的队伍
    time.sleep(0.5)
    click(1300, 500)  # 呼出此编制2
    time.sleep(0.5)

    click(1400, 750)  # 队伍3
    time.sleep(0.5)

    click(1450, 250)  # 我的队伍
    time.sleep(0.5)
    click(1300, 700)  # 呼出此编制3
    time.sleep(0.5)

    click(1400, 750)  # 编组完毕
    time.sleep(1)


def change2():
    click(1440, 160) #防止刷新网络卡顿
    time.sleep(10)
    
    click(450, 700)   # 防守设定
    time.sleep(0.5)

    # 队伍1 清空
    click(900, 750)  # 移除五号位
    time.sleep(0.5)
    click(900, 750)  # 移除五号位
    time.sleep(0.5)
    click(900, 750)  # 移除五号位
    time.sleep(0.5)
    click(900, 750)  # 移除五号位
    time.sleep(0.5)
    click(900, 750)  # 移除五号位
    time.sleep(0.5)

    click(1400, 750)  # 队伍2
    time.sleep(0.5)
    click(900, 750)   # 移除五号位
    time.sleep(0.5)
    click(900, 750)  # 移除五号位
    time.sleep(0.5)
    click(900, 750)  # 移除五号位
    time.sleep(0.5)
    click(900, 750)  # 移除五号位
    time.sleep(0.5)
    click(900, 750)  # 移除五号位
    time.sleep(0.5)

    click(1400, 750)  # 队伍3
    time.sleep(0.5)
    click(900, 750)  # 移除五号位
    time.sleep(0.5)
    click(900, 750)  # 移除五号位
    time.sleep(0.5)
    click(900, 750)  # 移除五号位
    time.sleep(0.5)
    click(900, 750)  # 移除五号位
    time.sleep(0.5)
    click(900, 750)  # 移除五号位
    time.sleep(0.5)

    click(150, 150)  # 队伍1
    time.sleep(0.5)

    click(1450, 250)  # 我的队伍
    time.sleep(0.5)
    click(700, 150)  # 编组3
    time.sleep(0.5)
    click(1300, 300)  # 呼出此编制1
    time.sleep(0.5)

    click(350, 150)   # 队伍2
    time.sleep(0.5)

    click(1450, 250)  # 我的队伍
    time.sleep(0.5)
    click(700, 150)  # 编组3
    time.sleep(0.5)
    click(1300, 500)  # 呼出此编制2
    time.sleep(0.5)

    click(1400, 750)  # 队伍3
    time.sleep(0.5)

    click(1450, 250)  # 我的队伍
    time.sleep(0.5)
    click(700, 150)  # 编组3
    time.sleep(0.5)
    click(1300, 700)  # 呼出此编制3
    time.sleep(0.5)

    click(1400, 750)  # 编组完毕
    time.sleep(1)


def change3():
    click(1440, 160) #防止刷新网络卡顿
    time.sleep(10)

    click(450, 700)   # 防守设定
    time.sleep(0.5)

    # 队伍1 清空
    click(900, 750)  # 移除五号位
    time.sleep(0.5)
    click(900, 750)  # 移除五号位
    time.sleep(0.5)
    click(900, 750)  # 移除五号位
    time.sleep(0.5)
    click(900, 750)  # 移除五号位
    time.sleep(0.5)
    click(900, 750)  # 移除五号位
    time.sleep(0.5)

    click(1400, 750)  # 队伍2
    time.sleep(0.5)
    click(900, 750)   # 移除五号位
    time.sleep(0.5)
    click(900, 750)  # 移除五号位
    time.sleep(0.5)
    click(900, 750)  # 移除五号位
    time.sleep(0.5)
    click(900, 750)  # 移除五号位
    time.sleep(0.5)
    click(900, 750)  # 移除五号位
    time.sleep(0.5)

    click(1400, 750)  # 队伍3
    time.sleep(0.5)
    click(900, 750)  # 移除五号位
    time.sleep(0.5)
    click(900, 750)  # 移除五号位
    time.sleep(0.5)
    click(900, 750)  # 移除五号位
    time.sleep(0.5)
    click(900, 750)  # 移除五号位
    time.sleep(0.5)
    click(900, 750)  # 移除五号位
    time.sleep(0.5)

    click(150, 150)  # 队伍1
    time.sleep(0.5)

    click(1450, 250)  # 我的队伍
    time.sleep(0.5)
    click(900, 150)  # pjjc3
    time.sleep(0.5)
    click(1300, 300)  # 呼出此编制1
    time.sleep(0.5)

    click(350, 150)   # 队伍2
    time.sleep(0.5)

    click(1450, 250)  # 我的队伍
    time.sleep(0.5)
    click(900, 150)  # pjjc3
    time.sleep(0.5)
    click(1300, 500)  # 呼出此编制2
    time.sleep(0.5)

    click(1400, 750)  # 队伍3
    time.sleep(0.5)

    click(1450, 250)  # 我的队伍
    time.sleep(0.5)
    click(900, 150)  # pjjc3
    time.sleep(0.5)
    click(1300, 700)  # 呼出此编制3
    time.sleep(0.5)

    click(1400, 750)  # 编组完毕
    time.sleep(1)


def change4():
    click(1440, 160) #防止刷新网络卡顿
    time.sleep(10)

    click(450, 700)   # 防守设定
    time.sleep(0.5)

    # 队伍1 清空
    click(900, 750)  # 移除五号位
    time.sleep(0.5)
    click(900, 750)  # 移除五号位
    time.sleep(0.5)
    click(900, 750)  # 移除五号位
    time.sleep(0.5)
    click(900, 750)  # 移除五号位
    time.sleep(0.5)
    click(900, 750)  # 移除五号位
    time.sleep(0.5)

    click(1400, 750)  # 队伍2
    time.sleep(0.5)
    click(900, 750)   # 移除五号位
    time.sleep(0.5)
    click(900, 750)  # 移除五号位
    time.sleep(0.5)
    click(900, 750)  # 移除五号位
    time.sleep(0.5)
    click(900, 750)  # 移除五号位
    time.sleep(0.5)
    click(900, 750)  # 移除五号位
    time.sleep(0.5)

    click(1400, 750)  # 队伍3
    time.sleep(0.5)
    click(900, 750)  # 移除五号位
    time.sleep(0.5)
    click(900, 750)  # 移除五号位
    time.sleep(0.5)
    click(900, 750)  # 移除五号位
    time.sleep(0.5)
    click(900, 750)  # 移除五号位
    time.sleep(0.5)
    click(900, 750)  # 移除五号位
    time.sleep(0.5)

    click(150, 150)  # 队伍1
    time.sleep(0.5)

    click(1450, 250)  # 我的队伍
    time.sleep(0.5)
    click(1100, 150)  # pjjc4
    time.sleep(0.5)
    click(1300, 300)  # 呼出此编制1
    time.sleep(0.5)

    click(350, 150)   # 队伍2
    time.sleep(0.5)

    click(1450, 250)  # 我的队伍
    time.sleep(0.5)
    click(1100, 150)  # pjjc4
    time.sleep(0.5)
    click(1300, 500)  # 呼出此编制2
    time.sleep(0.5)

    click(1400, 750)  # 队伍3
    time.sleep(0.5)

    click(1450, 250)  # 我的队伍
    time.sleep(0.5)
    click(1100, 150)  # pjjc4
    time.sleep(0.5)
    click(1300, 700)  # 呼出此编制3
    time.sleep(0.5)

    click(1400, 750)  # 编组完毕
    time.sleep(1)


if __name__ == '__main__':

    connect()

    while True:
        change1()
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        print("阵容1")
        time.sleep(random.randint(120,300))
        change2()
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        print("阵容2")
        time.sleep(random.randint(120,300))
        change3()
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        print("阵容3")
        time.sleep(random.randint(120,300))
        change4()
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        print("阵容4")
        time.sleep(random.randint(120,300))