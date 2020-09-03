"""
文件读写相关
"""
from typing import Optional
from configparser import ConfigParser, Error


def get_ini_config(arg: list) -> Optional[str]:
    """
    读ini文件中的配置
    :param arg: 读取的文件、section、key
    :return:
    """
    file, section, key = arg
    config_parser = ConfigParser()
    config_parser.read(file)
    try:
        config = config_parser.get(section=section, option=key)
    except Error:
        config = None
    return config


def set_ini_config(arg: list):
    """
    设置ini文件中的配置
    :return:
    """
    file, section, key, value = arg
    config_parser = ConfigParser()
    config_parser.read(file)
    try:
        config_parser.set(section=section, option=key, value=value)
        with open(file, "w") as f:
            config_parser.write(f)
    except Error as err:
        print(err)
        ...


if __name__ == '__main__':
    exec('print(get_ini_config("/hanbing/runParameterConfig.ini", "data_path", "value"))')

    # print(get_ini_config("/hanbing/runParameterConfig.ini", "data_path", "value"))
    # set_ini_config("/hanbing/runParameterConfig.ini", "data_path", "value", "/hanbing/data")
    # print(get_ini_config("/hanbing/runParameterConfig.ini", "data_path", "value"))
