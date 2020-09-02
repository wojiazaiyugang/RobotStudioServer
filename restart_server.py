"""
重启Server
"""
import os

from util.system import kill_by_port

kill_by_port(8001)
os.system("/usr/bin/python /root/server/socket_.py")
