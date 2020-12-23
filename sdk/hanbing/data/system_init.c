
#include "HYYRobotInterface.h"
int MainModule()
{
	
	//设置初始化参数
	 command_arg arg;
	 if (0!=commandLineParser1("--iscopy true", &arg))//MATLAB以副本方式启动，要求控制内RobotMain是运行状态
	 {
	    return -1;
	 }
	//系统初始化
	 if (0!=system_initialize(&arg))
	 {
	    return -2;
	 }
    return 0;
}
