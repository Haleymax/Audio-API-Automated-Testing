import subprocess
import sys
import time


def capture_filtered_logs(package_name, tag_filter):
    """
    持续捕获并过滤adb logcat日志
    :param package_name: 目标包名（如 com.u3d.webglhost）
    :param tag_filter: 目标日志标签（如 [INFO:CONSOLE(1)]）
    """
    adb_cmd = [
        "adb", "logcat",
        "-v", "brief",
        f"{package_name}:I",  # 仅显示该包名的INFO及以上级别日志
        "*:S"  # 静默其他所有日志
    ]

    try:
        print(f"开始捕获日志 - 包名: {package_name}, 过滤标签: {tag_filter}")
        print("按 Ctrl+C 停止...\n")

        # 启动adb logcat进程（实时流式读取）
        process = subprocess.Popen(
            adb_cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=1,  # 行缓冲
            universal_newlines=True
        )

        # 持续读取输出流
        while True:
            line = process.stdout.readline()
            if not line:
                time.sleep(0.1)  # 避免CPU空转
                continue

            # 检查是否包含目标标签
            if tag_filter in line:
                print(line.strip())  # 打印符合条件的日志

    except KeyboardInterrupt:
        print("\n捕获已停止")
    except Exception as e:
        print(f"发生错误: {e}", file=sys.stderr)
    finally:
        if process:
            process.terminate()


if __name__ == "__main__":
    # 配置目标包名和标签
    TARGET_PACKAGE = "com.u3d.webglhost"
    TARGET_TAG = "[INFO:CONSOLE(1)]"

    # 开始捕获
    capture_filtered_logs(TARGET_PACKAGE, TARGET_TAG)