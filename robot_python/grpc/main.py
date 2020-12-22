import time
import sys

sys.path.append("/root/RobotStudioServer")
from concurrent import futures

import grpc
import robot_pb2
import robot_pb2_grpc
from robot_python.robot.robot import Robot
from robot_python.util.system import kill_by_port

power_on = False  # 是否已经上电


class RobotService(robot_pb2_grpc.RobotServiceServicer):
    def HelloWorld(self, request, context):
        print("看到我说明环境配置成功了！")
        return robot_pb2.ResponseS(data1=f"hello1 world{request.arg1}")

    def GetSDKVersion(self, request, context):
        return robot_pb2.ResponseS(data1=robot.get_sdk_version())

    def TeachSetIndex(self, request, context):
        return robot.teach_set_robot_index(request.arg1)

    def TeachGetIndex(self, request, context):
        return robot_pb2.ResponseI(data1=robot.teach_get_robot_index())

    def TeachSetTool(self, request, context):
        return robot_pb2.ResponseI(data1=robot.teach_set_tool(request.arg1))

    def TeachGetTool(self, request, context):
        return robot_pb2.ResponseS(data1=robot.teach_get_tool())

    def TeachSetWobj(self, request, context):
        return robot_pb2.ResponseI(data1=robot.teach_set_wobj(request.arg1))

    def TeachGetWobj(self, request, context):
        return robot_pb2.ResponseS(data1=robot.teach_get_wobj())

    def TeachSetCoordinate(self, request, context):
        return robot_pb2.ResponseI(data1=robot.teach_set_coordinate(request.arg1))

    def TeachGetCoordinate(self, request, context):
        return robot_pb2.ResponseI(data1=robot.teach_get_coordinate())

    def TeachGetNum(self, request, context):
        return robot_pb2.ResponseI(data1=robot.teach_get_num())

    def TeachGetDof(self, request, context):
        return robot_pb2.ResponseI(data1=robot.teach_get_dof())

    def TeachGetJoint(self, request, context):
        return robot_pb2.ResponseRD(data1=robot.teach_get_joint().angle)

    def TeachStreamGetJoint(self, request, context):
        global power_on
        while power_on:
            time.sleep(0.1)
            yield robot_pb2.ResponseRD(data1=robot.teach_get_joint().angle)

    def TeachGetCartesian(self, request, context):
        pose = robot.teach_get_pose()
        return robot_pb2.ResponseRD(data1=list(pose.xyz) + list(pose.kps))

    def TeachStreamGetCartesian(self, request, context):
        global power_on
        while power_on:
            time.sleep(0.1)
            pose = robot.teach_get_pose()
            yield robot_pb2.ResponseRD(data1=list(pose.xyz) + list(pose.kps))

    def TeachSetVelocity(self, request, context):
        robot.teach_set_velocity(request.arg1)

    def TeachGetVelocity(self, request, context):
        return robot_pb2.ResponseD(data1=robot.teach_get_velocity())

    def TeachSetRunType(self, request, context):
        robot.teach_set_run_type(request.arg1)

    def TeachGetRunType(self, request, context):
        return robot_pb2.ResponseI(data1=robot.teach_get_run_type())

    def TeachClearMoveError(self, request, context):
        robot.teach_clear_move_error()

    def TeachStartProject(self, request, context):
        return robot_pb2.ResponseI(data1=robot.start_project(request.arg1))

    def TeachStopProject(self, request, context):
        return robot_pb2.ResponseI(data1=robot.stop_project())

    def TeachMoveStart(self, request, context):
        global power_on
        power_on = True
        return robot_pb2.ResponseI(data1=robot.teach_move_start())

    def TeachMoveStop(self, request, context):
        global power_on
        power_on = False
        return robot_pb2.ResponseI(data1=robot.teach_move_stop())

    def TeachMoveHome(self, request, context):
        return robot_pb2.ResponseI(data1=robot.teach_move_home())

    def TeachMove(self, request, context):
        return robot_pb2.ResponseI(data1=robot.teach_move(request.arg1, request.arg2))

    def TeachStop(self, request, context):
        return robot_pb2.ResponseI(data1=robot.teach_stop())

    def TeachCalibrateAxis(self, request, context):
        return robot_pb2.ResponseI(data1=robot.teach_calibrate_axis(request.arg1))

    def TeachCalibrate(self, request, context):
        return robot_pb2.ResponseI(robot.teach_calibrate())


def run_rpc_server():
    """
    启动RPC Server
    :return:
    """
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    robot_pb2_grpc.add_RobotServiceServicer_to_server(RobotService(), server)
    server.add_insecure_port("0.0.0.0:50051")
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    kill_by_port(6666)
    kill_by_port(50051)
    robot = Robot()
    robot.system_initialize()
    run_rpc_server()
