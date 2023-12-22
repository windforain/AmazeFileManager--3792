# bug reproduction script for bug #3792 of AFM
import sys
import time
import uiautomator2 as u2


def wait(seconds=2):
    for i in range(0, seconds):
        print("wait 1 second ..")
        time.sleep(1)


if __name__ == '__main__':
    avd_serial = sys.argv[1]
    d = u2.connect(avd_serial)
    d.app_start("com.amaze.filemanager")
    wait()

    current_app = d.app_current()
    print(current_app)

    while True:
        if current_app['package'] == "com.amaze.filemanager":
            break
        time.sleep(2)
    wait()

    out = d(resourceId="com.amaze.filemanager:id/sd_main_fab").click()
    if not out:
        print("Success: 点击右下角加号 ")
    wait()


    out = d(resourceId="com.amaze.filemanager:id/sd_label", text="网盘").click()
    if not out:
        print("Success: 点击网盘 ")
    wait()

    out = d(text="SCP/SFTP 连接").click()
    if not out:
        print("Success: 点击SCP/SFTP ")
    wait()


    out = d(text="服务器 IP 地址").set_text("106.15.75.216")
    if not out:
        print("Success: 输入服务器 IP 地址")
    wait()

    width, height = d.window_size()
    d.swipe(0.5*width, 0.8*height, 0.5*width,0.3*height, 0.5)

    out = d(text="用户名").set_text("root")
    if not out:
        print("Success: 输入服务器用户名")
    wait()

    out = d(text="密码").set_text("55039260abcZ?")
    if not out:
        print("Success: 输入服务器密码")
    wait()

    out = d(resourceId="com.amaze.filemanager:id/md_buttonDefaultPositive").click()
    if not out:
        print("Success: 点击连接")
    wait()

    out = d(resourceId="android:id/button1").click()
    if not out:
        print("Success: 建立远端，点击 是 ")
    wait()

    d.swipe(0.5*width, 0.8*height, 0.5*width,0.3*height, 0.5)

    d.swipe(0.5*width, 0.8*height, 0.5*width,0.3*height, 0.5)

    out = d(resourceId="com.amaze.filemanager:id/firstline", text="root").click()
    if not out:
        print("Success: 点击root文件夹")
    wait()

    out = d(resourceId="com.amaze.filemanager:id/firstline", text="go").click()
    if not out:
        print("Success: 点击go文件夹")
    wait()

    out = d(resourceId="com.amaze.filemanager:id/firstline", text="@test").click()
    if not out:
        print("Success: 点击@test文件夹")
    wait()
