import json
import os

config_file_path = os.path.join(os.path.dirname(__file__), 'config.json')
with open(config_file_path) as fr:
    globalConfig = json.load(fr)


def configModifier(key, value):
    globalConfig[key] = value
    with open(config_file_path, 'w') as fw:
        json.dump(globalConfig, fw)
