import time
import sys

sys.path.append("/root/RobotPython")
from robot_python.robot.constant import SPEED_VERY_FAST, SPEED_SLOW, SPEED_FAST, ZONE_SMALL
from robot_python.robot.data_structure import Pose, Joint
from robot_python.robot.robot import Robot

if __name__ == '__main__':
    robot = Robot()
    robot.system_initialize()
    print(f"运动库版本{robot.get_sdk_version()}")
    print(f"当前使用的工具{robot.get_tool()}")
    time.sleep(3)
    robot.move_start()
    for i in range(2):
        print(f"机械臂回零")
        robot.move_joint(Joint((0, 0, 0, 0, 0, 0, 0, 0, 0, 0)), SPEED_VERY_FAST)
        pose = robot.get_pose()
        print(f"机械臂当前的关节是{robot.get_joint()}")
        robot.move_pose(Pose(xyz=(379, 309, 351), kps=(-3.13, 0.3, 0.19999986792500643)), SPEED_VERY_FAST)
        current_pose = robot.get_pose()
        offset_pose = robot.get_offset_pose(current_pose, 0, 0, -30, 0, 0, 0)
        robot.move_pose(offset_pose, SPEED_VERY_FAST)
        print(f"机械臂当前的位姿是{robot.get_pose()}")
        print(f"机械臂当前运动状态是{robot.get_run_status()}")
        new_pose = robot.get_offset_pose(robot.get_pose(), 50, 0, 0, 0, 0, 0)
        robot.move_line(new_pose, SPEED_SLOW)
        pose2 = robot.get_offset_pose(new_pose, 0, 10, 0, 0, 0, 0)
        pose3 = robot.get_offset_pose(pose2, 0, 30, 0, 0, 0, 0)
        print(f"机械臂圆弧运动")
        robot.move_circle(pose3, pose2, SPEED_FAST, zone=ZONE_SMALL)
    robot.move_stop()
