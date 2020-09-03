"""
重启Server
"""
import os

from system import kill_by_port

kill_by_port(8000)
os.system("/usr/bin/python /root/server/main.py")
