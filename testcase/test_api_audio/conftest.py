import logging

import pytest

from config import setting
from data.generate_case import generate_case
from reportportal_client import RPLogger


@pytest.fixture(scope="session")
def rp_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logging.setLoggerClass(RPLogger)
    return logger

@pytest.fixture(scope="session")
def url():
    url = f'testscripts/audio/test.js'
    return url

audio_case = generate_case(setting.YAML_FILE_PATH)['audio']
