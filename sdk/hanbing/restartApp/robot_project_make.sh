#!/bin/sh
robot_project_make_path=$(dirname $(readlink -f "$0"))
cd $robot_project_make_path

project_path=$1
project_name=$2
#echo "项目路径:"$project_path
#echo "项目名称:"$project_name
#lib="/usr/lib"
lib="/home/hanbing/work/program/robot/1RobotLib"
include="./include"

makeso="-lRobotLib -lRobotControlerAPI -lRobotInterface -lExternallyGuidedMotion -lRobotControlLib -lTorqueSensorLib -lBaseLib -lDynamicsLib -lGripLib -lEtherCATLib -lInterpolateLib -lAdditionAxisLib -lKinematicCalibrationLib -lKinematicLib -lKinematicLibCustom -lExtraLib -lExtraLib2 -lnlopt -lmodbus -lpthread -lrt -lm -ldl"

makefile=$project_path$project_name".c"
compilestatus=$project_name"_compile_status.txt"

rm -rf $project_path"libRobotProjectLib.so"
rm -rf $compilestatus

gcc -L $lib -I $include -Wall -fPIC $makefile -shared -o libRobotProjectLib.so $makeso 2>$compilestatus

cp libRobotProjectLib.so $project_path
cp $compilestatus $project_path

rm -rf libRobotProjectLib.so
rm -rf $compilestatus

flag=$(find $project_path"libRobotProjectLib.so")
if [ -n "$flag" ]; then
#echo "编译成功"
exit 0 
else
#echo "编译失败"
exit 1 
fi


