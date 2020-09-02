import os
import time
import ctypes
from ctypes import c_char_p, Structure, c_int, POINTER


class CommandArg(Structure):
    _fields_ = [
        ("path", c_char_p),
        ("mode", c_int),
        ("dete_background", c_int),
        ("EtherCATonly", c_int),
        ("server_modbus", c_int),
        ("port", c_int),
        ("iscopy", c_int)]


command_arg = CommandArg(c_char_p(bytes("/hanbing", encoding="utf8")), 1, 0, 0,0, 6666, 0)


lib_dict = {}
for lib_name in ["libdl.so", "libm.so", "librt.so", "libmodbus.so", "libnlopt.so", "libRobotIQLib.so",
                 "libExtraLib2.so", "libExtraLib.so", "libTorqueSensor.so", "libKinematicLibCustom.so",
                 "libKinematicLib.so", "libKinematicCalibrationLib.so", "libAdditionAxisLib.so",
                 "libInterpolateLib.so", "libEtherCATLib.so", "libGripLib.so", "libDynamicsLib.so", "libBaseLib.so",
                 "libTorqueSensorLib.so", "libExternallyGuidedMotion.so", "libRobotInterface.so"
    , "libRobotControlLib.so", "libRobotControlerAPI.so", "libRobotLib.so"]:
    usr_lib = os.path.join("/usr/lib", lib_name)
    usr_lib_x86 = os.path.join("/usr/lib/x86_64-linux-gnu", lib_name)
    if os.path.isfile(usr_lib):
        lib_dict[lib_name] = ctypes.CDLL(usr_lib, mode=ctypes.RTLD_GLOBAL)
    elif os.path.isfile(usr_lib_x86):
        lib_dict[lib_name] = ctypes.CDLL(usr_lib_x86, mode=ctypes.RTLD_GLOBAL)
    else:
        raise Exception(f"找不到{lib_name}")
fn_command = lib_dict["libExtraLib.so"].commandLineParser
fn_command.argtypes = c_int, POINTER(c_char_p),  CommandArg
fn_command.restype = c_int
resp = fn_command(c_int(1), (c_char_p*1)(b"./robot"), command_arg)
fn = lib_dict["libRobotLib.so"].system_initialize
fn.argtypes = POINTER(CommandArg),
fn.restype = c_int
resp = fn(command_arg)
while True:
    time.sleep(10)
