import pytest

from testcase.test_api_audio.conftest import audio_case


class TestRunAudioApi:
    @pytest.mark.audio_api
    @pytest.mark.parametrize("name, api", audio_case)
    def test_audio(self, name, api, monkeypatch):
        print(f"Running test for {name} with API {api}")



        # 模拟用户交互
        user_input = input("请输入数字: ")
        print(f"Received input: {user_input}")

        # 实际测试逻辑（示例）
        # 这里应该是您的API测试代码，例如：
        # response = requests.get(api)
        # assert response.status_code == 200

        # 有意义的断言
        assert user_input == "999"  # 验证模拟输入是否生效
# pytest -s test_01_audio.py::TestRunAudioApi::test_audio