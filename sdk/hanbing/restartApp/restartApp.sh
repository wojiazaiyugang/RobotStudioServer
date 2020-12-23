#!/bin/sh

/hanbing/restartApp/killpid.sh HYYRobotMain
/hanbing/restartApp/killpid.sh lua
sleep 30
/robot/HYYRobotMain &
