"""
系统工具相关
"""
from signal import SIGKILL

import psutil


def kill_by_port(port: int):
    """
    杀死占用端口的进程
    查找所有进程，看占用的端口，然后杀死
    :param port:
    :return:
    """
    for proc in psutil.process_iter():
        for conns in proc.connections(kind='inet'):
            if conns.laddr.port == port:
                try:
                    proc.send_signal(SIGKILL)
                except psutil.NoSuchProcess as err:
                    pass
