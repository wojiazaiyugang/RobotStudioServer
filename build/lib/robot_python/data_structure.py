from ctypes import Structure, c_int, c_char_p, c_double
from typing import List, Tuple
from dataclasses import dataclass

MAX_DOF = 10  # 最大DOF
DOF = 6  # DOF
BUFFER_SIZE = 2048  # 读字符串的BUFFER 辣鸡C语言

Tuple3Float = Tuple[float, float, float]
Tuple6Float = Tuple[float, float, float, float, float, float]
Tuple10Float = Tuple[float, float, float, float, float, float, float, float, float, float]


class CommandArg(Structure):
    _fields_ = [
        ("path", c_char_p),
        ("mode", c_int),
        ("dete_background", c_int),
        ("EtherCATonly", c_int),
        ("server_modbus", c_int),
        ("port", c_int),
        ("iscopy", c_int)]


class SdkVersion(Structure):
    _fields_ = [
        ("major", c_int),
        ("minor", c_int),
        ("build", c_int)
    ]


class CJoint(Structure):
    _fields_ = [
        ("angle", c_double * MAX_DOF),
        ("dof", c_int)
    ]


class CPose(Structure):
    _fields_ = [
        ("xyz", c_double * 3),
        ("kps", c_double * 3)
    ]


class CSpeed(Structure):
    _fields_ = [
        ("per", c_double * MAX_DOF),
        ("per_flag", c_int),
        ("tcp", c_double),
        ("orl", c_double),
        ("tcp_flag", c_int),
        ("dof", c_int)
    ]


class CPayLoad(Structure):
    _fields_ = [
        ("m", c_double),
        ("cm", c_double * 3),
        ("I", (c_double * 3) * 3),
        ("I2", (c_double * 3) * 3)
    ]


class CZone(Structure):
    _fields_ = [("zone_flag", c_int),
                ("zone_size", c_double)]


class CWobj(Structure):
    _fields_ = [("robhold", c_int),
                ("ufprog", c_int),
                ("ufmec", c_int),
                ("uframe", CPose),
                ("oframe", CPose)]


class CTool(Structure):
    _fields_ = [
        ("robhold", c_int),
        ("tframe", CPose),
        ("payload", CPayLoad)
    ]


@dataclass
class Joint:
    angle: Tuple10Float
    dof: int = DOF

    @property
    def c(self):
        return CJoint((c_double * MAX_DOF)(*self.angle), self.dof)


@dataclass
class Speed:
    per: Tuple10Float
    per_flag: int
    tcp: float
    orl: float
    tcp_flag: int
    dof: int = DOF

    @property
    def c(self):
        return CSpeed((c_double * MAX_DOF)(*self.per), self.per_flag, self.tcp, self.orl, self.tcp_flag, self.dof)


@dataclass
class Pose:
    xyz: Tuple3Float
    kps: Tuple3Float

    @property
    def c(self):
        return CPose((c_double * 3)(*self.xyz), (c_double * 3)(*self.kps))


@dataclass
class PayLoad:
    m: float
    cm: Tuple3Float
    i: Tuple6Float
    i2: Tuple6Float

    @property
    def c(self):
        return CPayLoad(self.m, (c_double * 3)(*self.cm), (c_double * 6)(*self.i), (c_double * 6)(*self.i2))


@dataclass
class Tool:
    robhold: int
    tframe: Pose
    payload: PayLoad

    @property
    def c(self):
        return CTool(self.robhold, self.tframe.c, self.payload.c)


@dataclass
class Zone:
    zone_flag: int
    zone_size: float

    @property
    def c(self):
        return CZone(self.zone_flag, self.zone_size)


@dataclass
class Wobj:
    robhold: int
    ufprog: int
    ufmec: int
    uframe: Pose
    oframe: Pose

    @property
    def c(self):
        return CWobj(self.robhold, self.ufprog, self.ufmec, self.uframe.c, self.oframe)


if __name__ == '__main__':
    j = Joint(angle=(0, 0, 0, 0, 0, 0, 0, 0, 0, 0), dof=4)
    print(j.c)
