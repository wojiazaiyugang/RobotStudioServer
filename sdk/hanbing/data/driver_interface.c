
#include "HYYRobotInterface.h"
int MainModule()
{
	int err=0;
	int robot_index=0;
	//获取索引robot_index的机器人名称
	const char* robot_name=get_name_robot_device(get_deviceName(0,NULL), robot_index);
	if (NULL==robot_name)
	{
		return -1;
	}

	//得到机器人自由度
	int dof=get_group_dof(robot_name);
	//数据会保存到日志文件，Rdebug用于保存操作过程中的关系信息。
	Rdebug("dof=%d\n",dof);

	//获取一轴关节力矩
	double torque=0;
	int axis_ID=1;
	torque=GetAxisTorque(robot_name, axis_ID);

	//设置一轴关节力矩
	err=SetAxisTorque(robot_name, torque, axis_ID);
	if (0!=err)
	{
		Rdebug("1\n");
	}

	//一轴上电
	err=axis_power_on(robot_name,axis_ID);
	if (0!=err)
	{
		Rdebug("2\n");
	}
	//一轴下电
	err = axis_power_off(robot_name,axis_ID);
	if (0!=err)
	{
		Rdebug("3\n");
	}
	//得到机器人当前关节角度（rad）
	double position[10];
	err=GetGroupPosition(robot_name, position);
	if (0!=err)
	{
		Rdebug("4\n");
	}


	Rdebug("angle=%f,%f,%f,%f,%f,%f\n",position[0],position[1],position[2],position[3],position[4],position[5]);

	//设置期望关节角度（rad）
	err=SetGroupPosition(robot_name, position);
	if (0!=err)
	{
		Rdebug("5\n");
	}

	//机器人上电
	err = group_power_on(robot_name);
	if (0!=err)
	{
		Rdebug("6\n");
	}

	//机器人下电
	err = group_power_off(robot_name);
	if (0!=err)
	{
		Rdebug("7\n");
	}

	//获取第一数字输入
	int id_index=0;
	int flag=1;
	flag=get_di(robot_name, id_index);
	//设置第一路数字输出
	err=set_do(robot_name, id_index,flag);
	if (0!=err)
	{
		Rdebug("8\n");
	}

	//获取第一模拟输入
	short ai=1;
	ai=get_ai(robot_name, id_index);
	//设置第一路模拟输出
	err=set_ao(robot_name, id_index, ai);
	if (0!=err)
	{
		Rdebug("9\n");
	}
	Rdebug("over\n");
    return 0;
}
