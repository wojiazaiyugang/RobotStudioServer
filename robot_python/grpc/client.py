import sys
sys.path.append("/root/RobotPython")
import grpc

from robot_python.grpc import robot_pb2
from robot_python.grpc import robot_pb2_grpc

if __name__ == '__main__':
    channel = grpc.insecure_channel("localhost:50051")
    stub = robot_pb2_grpc.RobotServiceStub(channel)
    resp = stub.HelloWorld(robot_pb2.RequestI(arg1=1111))
    print(resp.data1)