"""
base文件
"""
import os
import ctypes
from dataclasses import dataclass


def load_lib(lib_name: str, path: str = None) -> ctypes.CDLL:
    """
    从path加载库，如果没有指定path就从默认位置寻找
    :param path:
    :param lib_name:
    :return:
    """
    specified_lib = os.path.join(path, lib_name) if path else None
    usr_lib = os.path.join("/usr/lib", lib_name)
    usr_lib_x86 = os.path.join("/usr/lib/x86_64-linux-gnu", lib_name)
    if specified_lib and os.path.isfile(specified_lib):
        return ctypes.CDLL(specified_lib, mode=ctypes.RTLD_GLOBAL)
    elif os.path.isfile(usr_lib):
        return ctypes.CDLL(usr_lib, mode=ctypes.RTLD_GLOBAL)
    elif os.path.isfile(usr_lib_x86):
        return ctypes.CDLL(usr_lib_x86, mode=ctypes.RTLD_GLOBAL)
    else:
        raise Exception(f"找不到{lib_name}")


@dataclass
class RobotLib:
    dl: ctypes.CDLL = load_lib("libdl.so")
    m: ctypes.CDLL = load_lib("libm.so")
    rt: ctypes.CDLL = load_lib("librt.so")
    modbus: ctypes.CDLL = load_lib("libmodbus.so")
    nlopt: ctypes.CDLL = load_lib("libnlopt.so")
    RobotIQLib: ctypes.CDLL = load_lib("libRobotIQLib.so")
    ExtraLib2: ctypes.CDLL = load_lib("libExtraLib2.so")
    ExtraLib: ctypes.CDLL = load_lib("libExtraLib.so")
    TorqueSensor: ctypes.CDLL = load_lib("libTorqueSensor.so")
    KinematicLibCustom: ctypes.CDLL = load_lib("libKinematicLibCustom.so")
    KinematicLib: ctypes.CDLL = load_lib("libKinematicLib.so")
    KinematicCalibrationLib: ctypes.CDLL = load_lib("libKinematicCalibrationLib.so")
    AdditionAxisLib: ctypes.CDLL = load_lib("libAdditionAxisLib.so")
    InterpolateLib: ctypes.CDLL = load_lib("libInterpolateLib.so")
    EtherCATLib: ctypes.CDLL = load_lib("libEtherCATLib.so")
    GripLib: ctypes.CDLL = load_lib("libGripLib.so")
    DynamicsLib: ctypes.CDLL = load_lib("libDynamicsLib.so")
    BaseLib: ctypes.CDLL = load_lib("libBaseLib.so")
    TorqueSensorLib: ctypes.CDLL = load_lib("libTorqueSensorLib.so")
    ExternallyGuidedMotion: ctypes.CDLL = load_lib("libExternallyGuidedMotion.so")
    RobotInterface: ctypes.CDLL = load_lib("libRobotInterface.so")
    RobotControlLib: ctypes.CDLL = load_lib("libRobotControlLib.so")
    RobotControlerAPI: ctypes.CDLL = load_lib("libRobotControlerAPI.so")
    RobotLib: ctypes.CDLL = load_lib("libRobotLib.so")

robot_lib = RobotLib()
