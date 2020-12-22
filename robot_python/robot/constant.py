"""
常量
"""

from robot_python.robot.data_structure import Speed, Joint, Zone

JOINT_ZERO = Joint((0, 0, 0, 0, 0, 0, 0, 0, 0, 0))  # 零点
JOINT_MOVE = Joint((0, 0.6, 0, 0, 1, 0, 0, 0, 0, 0))  # 运动准备
JOINT_CARRY = Joint((0, -0.1, 0.8, 0, 1, 0, 0, 0, 0, 0))  # 搬运姿态

SPEED_SLOW = Speed((0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1), 1, 10, 0.1, 1, 6)  # 慢
SPEED_FAST = Speed((0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5), 1, 100, 0.5, 1, 6)  # 快
SPEED_VERY_FAST = Speed((1, 1, 1, 1, 1, 1, 1, 1, 1, 1), 1, 200, 1, 1, 6)  # 很快啊，啪的一下

ZONE_NONE = Zone(0, 0)  # 没有转弯区
ZONE_SMALL = Zone(1, 0.1)  # 小转弯区
ZONE_BIG = Zone(1, 0.2)  # 大转弯区
