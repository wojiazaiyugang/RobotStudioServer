"""
文件读写相关
"""
import json
from typing import Optional
from configparser import ConfigParser, Error

RUN_PARAMETER_CONFIG = "/hanbing/runParameterConfig.ini"
BUS_CONFIG = "/hanbing/busConfig.ini"


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


def set_ini_config(file: str, data: dict):
    """
    设置ini文件中的配置
    :param file: ini文件
    :param data: dict，key是section，value是dict，key是key，value是value
    :return:
    """
    config_parser = ConfigParser()
    config_parser.read(file)
    try:
        for section in data:
            for key in data.get(section):
                config_parser.set(section=section, option=key, value=data.get(section).get(key))
        with open(file, "w") as f:
            config_parser.write(f)
    except Error as err:
        print(err)
        ...


def get_all_config(arg: list) -> str:
    """
    获取所有的配置项
    跟这个接口对应的是设置所有配置项，这里返回的配置在IDE里配置完之后都会再返回来进行配置，所以更改这个函数要同步更改设置的函数，见set_all_config
    :param arg:
    :return:
    """
    data = {
        "data_data_path": get_ini_config([RUN_PARAMETER_CONFIG, "data_path", "value"]),
        "data_robot_type": get_ini_config([RUN_PARAMETER_CONFIG, "robot_type", "value"]),
        "bus_ec_di": get_ini_config([BUS_CONFIG, "ec", "ec_di"]),
        "bus_ec_do": get_ini_config([BUS_CONFIG, "ec", "ec_do"]),
        "bus_ec_ai": get_ini_config([BUS_CONFIG, "ec", "ec_ai"]),
        "bus_ec_ao": get_ini_config([BUS_CONFIG, "ec", "ec_ao"]),
        "bus_ec_li": get_ini_config([BUS_CONFIG, "ec", "ec_li"]),
        "bus_ec_lo": get_ini_config([BUS_CONFIG, "ec", "ec_lo"]),
    }
    return json.dumps(data)


def set_all_config(args: list):
    """
    设置所有的配置
    所有的配置项见get_all_config
    :param args:
    :return:
    """
    data = json.loads(args[0])
    set_ini_config(RUN_PARAMETER_CONFIG, {"data_path": {"value": data.get("data_data_path")},
                                          "robot_type": {"value": data.get("data_robot_type")}})
    set_ini_config(BUS_CONFIG, {
        "ec": {"ec_di": data.get("bus_ec_di"),
               "ec_do": data.get("bus_ec_do"),
               "ec_ai": data.get("bus_ec_ai"),
               "ec_ao": data.get("bus_ec_ao"),
               "ec_li": data.get("bus_ec_li"),
               "ec_lo": data.get("bus_ec_lo")}})


if __name__ == '__main__':
    exec('print(get_ini_config("/hanbing/runParameterConfig.ini", "data_path", "value"))')

    # print(get_ini_config("/hanbing/runParameterConfig.ini", "data_path", "value"))
    # set_ini_config("/hanbing/runParameterConfig.ini", "data_path", "value", "/hanbing/data")
    # print(get_ini_config("/hanbing/runParameterConfig.ini", "data_path", "value"))
