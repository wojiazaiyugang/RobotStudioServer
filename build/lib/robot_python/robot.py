from ctypes import POINTER, c_int, c_char_p, pointer, c_double, c_char

from robot_python.robot.robot_lib import RobotLib
from robot_python.robot.data_structure import CommandArg, Speed, Joint, Pose, Tool, Zone, Wobj, DOF, BUFFER_SIZE, CPose, SdkVersion, MAX_DOF


class Robot:

    def __init__(self):
        """
        机器人初始化
        """
        self.lib = RobotLib()
        self.encoding = "utf-8"

    def system_initialize(self):
        """
        系统初始化
        :return:
        """
        command_arg = CommandArg(c_char_p(bytes("/hanbing", encoding=self.encoding)), 0, 0, 0, 0, 6666, 0)
        fn = self.lib.RobotLib.system_initialize
        fn.argtypes = POINTER(CommandArg),
        fn.restype = c_int
        fn(command_arg)

    def move_start(self):
        """
        机器人上使能
        :return:
        """
        self.lib.RobotInterface.move_start()

    def move_stop(self):
        """
        机器人下使能
        :return:
        """
        self.lib.RobotInterface.move_stop()

    def move_joint(self, joint: Joint, speed: Speed, zone: Zone = None, tool: Tool = None, wobj: Wobj = None) -> None:
        """
        机器人关节运动
        :param joint:
        :param speed:
        :param zone:
        :param tool:
        :param wobj:
        :return:
        """
        self.lib.BaseLib.MoveA(self._c_pointer(joint), self._c_pointer(speed), self._c_pointer(zone), self._c_pointer(tool), self._c_pointer(wobj))

    def move_pose(self, pose: Pose, speed: Speed, zone: Zone = None, tool: Tool = None, wobj: Wobj = None) -> None:
        """
        笛卡尔空间运动
        :param pose:
        :param speed:
        :param zone:
        :param tool:
        :param wobj:
        :return:
        """
        self.lib.BaseLib.MoveJ(self._c_pointer(pose), self._c_pointer(speed), self._c_pointer(zone), self._c_pointer(tool), self._c_pointer(wobj))

    def move_line(self, pose: Pose, speed: Speed, zone: Zone = None, tool: Tool = None, wobj: Wobj = None):
        """
        末端直线运动
        :param pose:
        :param speed:
        :param zone:
        :param tool:
        :param wobj:
        :return:
        """
        self.lib.BaseLib.MoveL(self._c_pointer(pose), self._c_pointer(speed), self._c_pointer(zone), self._c_pointer(tool), self._c_pointer(wobj))

    def move_circle(self, pose: Pose, pose_mid: Pose, speed: Speed, zone: Zone = None, tool: Tool = None, wobj: Wobj = None):
        """
        圆弧运动
        :param wobj: 工件
        :param zone: 转弯区
        :param speed: 速度
        :param pose: 起始位姿
        :param pose_mid: 轨迹中经过的位姿
        :return:
        """
        self.lib.BaseLib.MoveC(self._c_pointer(pose), self._c_pointer(pose_mid), self._c_pointer(speed), self._c_pointer(zone), self._c_pointer(tool), self._c_pointer(wobj))

    def get_data_path(self) -> str:
        """
        获取数据文件夹
        :return:
        """
        func = self.lib.RobotControlerAPI.get_robot_data_path
        func.restype = POINTER(c_char * BUFFER_SIZE)
        resp = func()
        return str(resp.contents.value, encoding=self.encoding)

    def get_joint(self) -> Joint:
        """
        获取当前关节角度
        :return:
        """
        joint = (c_double * DOF)()
        self.lib.RobotControlerAPI.get_robot_joint(joint)
        return Joint(angle=tuple(joint))

    def get_pose(self) -> Pose:
        """
        获取当前位姿
        :return:
        """
        pose = (c_double * 6)()
        self.lib.RobotControlerAPI.get_robot_cartesian(pose)
        pose = list(pose)
        return Pose(xyz=(pose[0], pose[1], pose[2]), kps=(pose[3], pose[4], pose[5]))

    def get_offset_pose(self, pose: Pose, x: float, y: float, z: float, k: float, p: float, s: float) -> Pose:
        """
        给定一个初始pose和一个offset，计算offset之后的pose
        :param pose:
        :param x: x
        :param y: y
        :param z: z
        :param k: k
        :param p: p
        :param s: s
        :return:
        """
        func = self.lib.BaseLib.Offs
        func.argtypes = (POINTER(CPose), c_double, c_double, c_double, c_double, c_double, c_double)
        func.restype = CPose
        offset_pose = func(self._c_pointer(pose), x, y, z, k, p, s)
        return Pose(xyz=tuple(offset_pose.xyz), kps=tuple(offset_pose.kps))

    def get_tool(self) -> str:
        """
        获取当前的工具
        :return:
        """
        func = self.lib.RobotControlerAPI.get_robot_tool
        func.restype = POINTER(c_char * BUFFER_SIZE)
        resp = func()
        return str(resp.contents.value, encoding=self.encoding)

    def get_wobj(self) -> str:
        """
        获取当前的工件
        :return:
        """
        func = self.lib.RobotControlerAPI.get_robot_wobj
        func.restype = POINTER(c_char * BUFFER_SIZE)
        resp = func()
        return str(resp.contents.value, encoding=self.encoding)

    def get_run_status(self) -> int:
        """
        获取运动状态
        :return:
        """
        func = self.lib.RobotControlerAPI.get_robot_run_state
        return func()

    def get_sdk_version(self) -> str:
        """
        获取SDK版本
        :return:
        """
        func = self.lib.ExtraLib.getSystemVerison
        func.restype = SdkVersion
        resp = func()
        return f"{resp.major}-{resp.minor}-{resp.build}"

    def sleep(self, n):
        """
        机器人休眠
        :param n: 毫秒
        :return:
        """
        self.lib.BaseLib.Rsleep(n)

    def start_project(self, file_name):
        """
        启动C项目
        :param file_name:
        :return:
        """
        func = self.lib.RobotControlerAPI.start_robot_c_project
        func.argtypes = (POINTER(c_char),)
        func.restype = c_int
        func(c_char_p(bytes(file_name, encoding=self.encoding)))

    def stop_project(self):
        """
        停止C项目
        :return:
        """
        func = self.lib.RobotControlerAPI.close_robot_project
        func.restype = c_int
        func()

    def teach_set_robot_index(self, index):
        """
        设置要操作的机器人的索引
        :param index:
        :return:
        """
        func = self.lib.RobotControlerAPI.set_robot_index
        func.argtypes = (c_int,)
        func.restype = c_int
        func(index)

    def teach_get_robot_index(self) -> int:
        """
        获取当前操作的机器人
        :return:
        """
        func = self.lib.RobotControlerAPI.get_robot_index
        func.argtypes = None
        func.restype = c_int
        return func()

    def teach_set_tool(self, tool_name) -> int:
        """
        设置工具
        :param tool_name:
        :return:
        """
        func = self.lib.RobotControlerAPI.set_robot_tool
        func.argtypes = (POINTER(c_char),)
        func.restype = c_int
        return func(bytes(tool_name, encoding=self.encoding))

    def teach_get_tool(self) -> str:
        """
        获取当前工具
        :return:
        """
        func = self.lib.RobotControlerAPI.get_robot_tool
        func.argtypes = None
        func.restype = POINTER(c_char * BUFFER_SIZE)
        resp = func()
        return str(resp.contents.value, encoding=self.encoding)

    def teach_set_wobj(self, wobj_name) -> int:
        """
        设置工件
        :param wobj_name:
        :return:
        """
        func = self.lib.RobotControlerAPI.set_robot_wobj
        func.argtypes = (POINTER(c_char),)
        func.restype = c_int
        return func(bytes(wobj_name, encoding=self.encoding))

    def teach_get_wobj(self) -> str:
        """
        获取工件
        :return:
        """
        func = self.lib.RobotControlerAPI.get_robot_wobj
        func.restype = POINTER(c_char * BUFFER_SIZE)
        resp = func()
        return str(resp.contents.value, encoding=self.encoding)

    def teach_set_coordinate(self, frame) -> int:
        """
        设置坐标系
        :param frame:
        :return:
        """
        func = self.lib.RobotControlerAPI.set_robot_teach_coordinate
        func.argtypes = (c_int,)
        func.restype = c_int
        return func(frame)

    def teach_get_coordinate(self) -> int:
        """
        获取坐标系
        :return:
        """
        func = self.lib.RobotControlerAPI.get_robot_teach_coordinate
        func.argtypes = None
        func.restype = c_int
        return func()

    def teach_get_num(self) -> int:
        """
        获取机器人数量
        :return:
        """
        func = self.lib.RobotControlerAPI.get_robot_num
        func.argtypes = None
        func.restype = c_int
        return func()

    def teach_get_dof(self) -> int:
        """
        获取DOF
        :return:
        """
        func = self.lib.RobotControlerAPI.get_robot_dof
        func.argtypes = None
        func.restype = c_int
        return func()

    def teach_get_joint(self) -> Joint:
        """
        获取当前关节
        :return:
        """
        func = self.lib.RobotControlerAPI.get_robot_joint
        func.argtypes = (POINTER(c_double * MAX_DOF),)
        func.restype = c_int
        joint = (c_double * MAX_DOF)()
        func(joint)
        return Joint(tuple(joint))

    def teach_get_pose(self) -> Pose:
        """
        获取笛卡尔位置
        :return:
        """
        func = self.lib.RobotControlerAPI.get_robot_cartesian
        func.argtypes = (POINTER(c_double * MAX_DOF),)
        func.restype = c_int
        pose = (c_double * MAX_DOF)()
        func(pose)
        pose = list(pose)
        return Pose(xyz=(pose[0], pose[1], pose[2]), kps=(pose[3], pose[4], pose[5]))

    def teach_set_velocity(self, vel_percent):
        """
        设置示教速度
        :param vel_percent:
        :return:
        """
        func = self.lib.RobotControlerAPI.set_robot_teach_velocity
        func.argtypes = (c_double,)
        func.restype = None
        func(vel_percent)

    def teach_get_velocity(self) -> float:
        """
        获取示教速度
        :return:
        """
        func = self.lib.RobotControlerAPI.get_robot_teach_velocity
        func.argtypes = None
        func.restype = c_double
        return func()

    def teach_set_run_type(self, is_simulation: bool):
        """
        设置是否开启仿真
        :param is_simulation:
        :return:
        """
        func = self.lib.RobotControlerAPI.set_robot_run_type
        func.argtypes = (c_int,)
        func.restype = None
        func(int(is_simulation))

    def teach_get_run_type(self) -> int:
        """
        获取是否开启仿真
        :return:
        """
        func = self.lib.RobotControlerAPI.get_robot_run_type
        func.argtypes = None
        func.restype = c_int
        return func()

    def teach_get_run_state(self) -> int:
        """
        获取运行状态
        :return:
        """
        func = self.lib.RobotControlerAPI.get_robot_run_state
        func.argtypes = None
        func.restype = c_int
        return func()

    def teach_clear_move_error(self):
        """
        清除运动错误
        :return:
        """
        func = self.lib.RobotControlerAPI.robot_move_error_clear
        func.argtypes = None
        func.restype = None
        func()

    def teach_move_start(self) -> int:
        """
        使能
        :return:
        """
        func = self.lib.RobotControlerAPI.robot_teach_enable
        func.argtypes = None
        func.restype = c_int
        return func()

    def teach_move_stop(self) -> int:
        """
        下使能
        :return:
        """
        func = self.lib.RobotControlerAPI.robot_teach_enable
        func.argtypes = None
        func.restype = c_int
        return func()

    def teach_stop(self) -> int:
        """
        停止示教动作
        :return:
        """
        func = self.lib.RobotControlerAPI.robot_teach_stop
        func.argtypes = None
        func.restype = c_int
        return func()

    def teach_move_home(self) -> int:
        """
        示教回零
        :return:
        """
        func = self.lib.RobotControlerAPI.robot_home
        func.argtypes = None
        func.restype = c_int
        return func()

    def teach_move(self, axis: int, dir: int):
        """
        示教
        :param axis: 轴
        :param dir: 方向
        :return:
        """
        func = self.lib.RobotControlerAPI.robot_teach_move
        func.argtypes = (c_int, c_int)
        func.restype = c_int
        return func(axis, dir)

    def teach_calibrate_axis(self, axis: int) -> int:
        """
        某个轴标零点
        :param axis:
        :return:
        """
        func = self.lib.RobotControlerAPI.calibrate_robot_zero_axis_position
        func.argtypes = (c_int,)
        func.restype = c_int
        return func(axis)

    def teach_calibrate(self) -> int:
        """
        所有轴标零
        :return:
        """
        func = self.lib.RobotControlerAPI.calibrate_robot_zero_position
        func.argtypes = None
        func.restype = c_int
        return func()

    @staticmethod
    def _c_pointer(data):
        """
        获取C结构体
        :param data:
        :return:
        """
        return pointer(data.c) if data else None


if __name__ == '__main__':
    robot = Robot()
    robot.system_initialize()
    print(robot.get_run_status())
    # robot.system_initialize()
    # print(robot.teach_get_joint())
    # print(robot.teach_get_velocity())
    # print(robot.get_run_status())
    # pose = robot.get_pose()
    # print("1111")
    # off = robot.get_offset_pose(pose, 100, 0, 0, 0, 0, 0)
    # print("111221")
    # print(pose)
    # print(off)
    # print(robot.get_data_path())
    # robot.start_project("gohome")
    # robot.stop_project()
    # robot.stop_project()
    # print(robot.get_tool())
    # robot.move_start()
    # robot_pose = robot.get_pose()
    # print(robot_pose)
    # p = Pose(xyz=(robot_pose[0], robot_pose[1], robot_pose[2]), kps=(robot_pose[3], robot_pose[4], robot_pose[5]))
    # robot.move_pose(p, Speed((1, 1, 1, 1, 1, 1, 1, 1, 1, 1), 1, 200, 1, 1, 6))
    # robot.move_circle(p ,p,Speed((1, 1, 1, 1, 1, 1, 1, 1, 1, 1), 1, 200, 1, 1, 6))
