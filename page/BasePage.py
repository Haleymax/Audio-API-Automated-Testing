import uiautomator2 as u2

class BasePage:
    def __init__(self):
        self.client = u2.connect()


