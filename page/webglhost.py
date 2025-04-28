import time
from time import sleep

from page.BasePage import BasePage


class WebglhostPage(BasePage):
    def start_app(self, package):
        self.client.app_start(package)
        print("star app")

    def stop_app(self, package):
        self.client.app_stop(package)
        print("stop app")

    def install_app(self, package):
        self.client.app_install(package)
        print("install app")

    def uninstall_app(self, package):
        try:
            # 检查应用是否存在
            app_info = self.client.app_info(package)
            if app_info:
                print(f"应用 {package} 存在，准备卸载...")
                result = self.client.app_uninstall(package)
                if result:
                    print(f"应用 {package} 已成功卸载。")
                else:
                    print(f"应用 {package} 卸载失败，请检查权限或手动卸载。")
            else:
                print(f"应用 {package} 不存在，跳过卸载。")
        except Exception as e:
            print(f"在卸载应用 {package} 时发生错误: {e}")
            print("尝试手动卸载应用...")
            print(f"请运行以下命令：adb shell pm uninstall {package}")

    def start_watcher(self):
        self.client.watcher("INSTALL").when(
            xpath='//*[@resource-id="com.oplus.appdetail:id/view_bottom_guide_continue_install_btn"]'
        ).click()

        self.client.watcher("ALLOW_PERMISSION").when(
            xpath='//*[@resource-id="com.android.permissioncontroller:id/permission_allow_foreground_only_button"]'
        ).click()

        self.client.watcher("SUCCESS").when(
            xpath='//*[@resource-id="com.oplus.appdetail:id/launch_button"]'
        ).click()

        self.client.watcher.start(interval=1.0)  # 设置检测间隔为 1 秒

        print("所有 Watcher 已启动")

    def stop_watcher(self):
        sleep(2)
        self.client.watcher.stop()

    def click_SDK_Sample(self, resourceId="com.u3d.webglhost:id/sdkSampleBt"):
        sleep(2)
        SDK_Sample = self.client(resourceId=resourceId)
        SDK_Sample.click()
        print("click SDK Sample")
        time.sleep(1.5)

    def input_url(self, url, resourceId="com.u3d.webglhost:id/server_address_et"):
        address_et = self.client(resourceId=resourceId)
        address_et.set_text(url)
        print("input url")
        time.sleep(1.5)
        self.client.click(0.909, 0.675)
        print("back")

    def click_testscript_btn(self, resourceId="com.u3d.webglhost:id/btnTestscript"):
        TestScript_btn = self.client(resourceId=resourceId)
        TestScript_btn.click()
        print("click testscript")
        time.sleep(1.5)

    def click_start_btn(self, resourceId="com.u3d.webglhost:id/start_btn"):
        start_btn = self.client(resourceId=resourceId)
        start_btn.click()
        print("click start")
        time.sleep(1.5)

    def click_play_btn(self, resourceId="com.u3d.webglhost:id/play_btn"):
        play_btn = self.client(resourceId=resourceId)
        play_btn.click()
        print("click play")
        time.sleep(1.5)

    def click_v_console_btn(self, resourceId="com.u3d.webglhost:id/v_console_txt"):
        v_console_btn = self.client(resourceId=resourceId)
        v_console_btn.click()
        print("click vconsole")
        time.sleep(1.5)

if __name__ == '__main__':
    i = True
    timestamp1 = time.time()
    try:
        while True:
            webgl = WebglhostPage()
            if i :
                webgl.start_watcher()
                webgl.uninstall_app("com.u3d.webglhost")
                webgl.install_app("D:\project\python\Audio-API-Automated-Testing\\app\\app-debug.apk")
                sleep(6)
            webgl.stop_app("com.u3d.webglhost")
            webgl.start_app("com.u3d.webglhost")
            webgl.click_SDK_Sample()
            webgl.input_url("http://127.0.0.1:8000")
            webgl.click_testscript_btn()
            webgl.click_start_btn()
            webgl.click_play_btn()
            webgl.click_v_console_btn()
            webgl.stop_app("com.u3d.webglhost")
            if i :
                webgl.stop_watcher()
    except Exception as e:
        print(e)
        timestamp2 = time.time()

        # 计算时间差（秒），然后转换为分钟
        time_diff_seconds = timestamp2 - timestamp1
        time_diff_minutes = time_diff_seconds / 60
        print(f"{time_diff_seconds} min")
