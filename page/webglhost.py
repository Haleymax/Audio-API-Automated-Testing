import time

from page.BasePage import BasePage


class WebglhostPage(BasePage):
    def start_app(self, package):
        self.client.app_start(package)
        print("star app")

    def stop_app(self, package):
        self.client.app_stop(package)
        print("stop app")

    def click_SDK_Sample(self, resourceId="com.u3d.webglhost:id/sdkSampleBt"):
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
    webgl = WebglhostPage()
    webgl.start_app("com.u3d.webglhost")
    webgl.click_SDK_Sample()
    webgl.input_url("http://127.0.0.1:8000")
    webgl.click_testscript_btn()
    webgl.click_start_btn()
    webgl.click_play_btn()
    webgl.click_v_console_btn()
    webgl.stop_app("com.u3d.webglhost")
