from config import setting
from data.generate_case import generate_case

audio_case = generate_case(setting.YAML_FILE_PATH)['audio']
