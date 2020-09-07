import ctypes
from ctypes import c_char_p, c_int, POINTER

from robot.base import robot_lib
from robot.data_structure import CommandArg

command_arg = CommandArg(c_char_p(bytes("/hanbing", encoding="utf8")), 1, 0, 0, 0, 6666, 1)

fn_command = robot_lib.ExtraLib.commandLineParser
fn_command.argtypes = c_int, POINTER(c_char_p), CommandArg
fn_command.restype = c_int
resp = fn_command(c_int(1), (c_char_p * 1)(b"./robot"), command_arg)
fn = robot_lib.RobotLib.system_initialize
fn.argtypes = POINTER(CommandArg),
fn.restype = c_int
resp = fn(command_arg)

ff = robot_lib.RobotControlerAPI.start_robot_c_project
ff.argtypes = ctypes.c_char_p,
ff.restype = c_int
resp = ff("move_test".encode("utf-8"))
print(resp)

f2 = robot_lib.ExtraLib.get_robot_busy_state
f2.restype = c_int
resp = f2()
print(resp)
