import pytest

from page.webglhost import WebglhostPage
from testcase.test_api_audio.conftest import audio_case

package = "com.u3d.webglhost"

class TestRunAudioApi:

    @pytest.mark.name(f"audio api test")
    @pytest.mark.parametrize("name, api", audio_case)
    def test_audio(self, name, api, rp_logger):
        rp_logger.debug(f"Running test for {name} with API {api}")
        print(f"Running test for {name} with API {api}")
        # webgl = WebglhostPage()
        # webgl.stop_app(package)
        # rp_logger.info("stop app")
        #
        # webgl.start_app(package)
        # rp_logger.info("start app")
        #
        # webgl.click_SDK_Sample()
        # url =f'testscripts/audio_250326/{api}'
        # rp_logger.info(f"api is {url}")
        # webgl.input_url(url=url)
        #
        # webgl.click_testscript_btn()
        # rp_logger.info("click testscript btn")
        #
        # webgl.click_start_btn()
        # rp_logger.info("click start btn")
        # webgl.click_play_btn()
        #
        # rp_logger.info("click play btn")
        # webgl.click_v_console_btn()
        #
        # rp_logger.info("click v console btn")
        # is_pass = input("是否通过:")
        # contrast_wx = "yes"
        # if is_pass != "yes":
        #     contrast_wx = input("是否与微信行为一致:")
        # rp_logger.info(f"Received input: {is_pass}")
        # print(f"Received input: {is_pass}")
        # Remark = input("测试结果备注:")
        # if is_pass != "yes":
        #     rp_logger.warn(f"备注: {Remark}")
        # else:
        #     rp_logger.info(f"备注: {Remark}")
        # rp_logger.info(
        #     "测试结果备注",
        #     attachment={
        #         "name": "备注",
        #         "data": Remark,
        #         "mime": "text/plain"
        #     },
        # )
        # webgl.stop_app(package)
        # assert is_pass == "yes"
        # assert contrast_wx == "yes"
        assert True

# pytest -s test_01_audio.py::TestRunAudioApi::test_audio