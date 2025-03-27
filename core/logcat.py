import threading

import uiautomator2 as u2


class LogcatMonitor:
    """日志监控器，用于抓取特定日志"""
    def __init__(self, package_name, tag_filter):
        self.package_name = package_name
        self.tag_filter = tag_filter
        self.logs = []
        self._stop_event = threading.Event()
        self._thread = None

    def start(self):
        """启动日志监控线程"""
        self._thread = threading.Thread(target=self._capture_logs, daemon=True)
        self._thread.start()

    def stop(self):
        """停止日志监控"""
        self._stop_event.set()
        if self._thread:
            self._thread.join()

    def _capture_logs(self):
        """实际抓取日志的方法"""
        d = u2.connect()
        cmd = f"logcat -v brief {self.package_name}:I *:S"
        for line in d.shell(cmd, stream=True):
            if self._stop_event.is_set():
                break
            if self.tag_filter in line:
                self.logs.append(line.strip())
                print(f"[LOGCAT] {line.strip()}")