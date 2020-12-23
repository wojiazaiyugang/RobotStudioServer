
#include "HYYRobotInterface.h"
int MainModule()
{
	int ret=0;
	//创建传感器，系统会启动默认创建索引为0的传感器，如果使用系统创建的传感器，无需使用该接口。
	ret=CreateTorqueSensor2("mysensor", "force_sensor.ini");
	Rdebug("CreateTorqueSensor2,ret=%d\n",ret);
	//获取系统内置传感器的名字
	const char* system_sensor_name=GetTorqueSensorName(0,NULL);

	//获取自己创建的传感器名字
	const char* my_sensor_name=GetTorqueSensorName(1,NULL);//="mysensor"
	if (NULL==my_sensor_name)
	{
		Rdebug("can't find sensor\n");
	}


	int robot_index=0;
	//获取索引robot_index的机器人名称
	const char* robot_name=get_name_robot_device(get_deviceName(0,NULL), robot_index);
	//获取使用的工具
	tool to;
	gettool("tool0",&to);
	//获取使用的工件
	wobj wo;
	getwobj("wobj0",&wo);
	//设置传感器转换数据
	ret=SetSensorTorqueTransformData(system_sensor_name, robot_name, &to, &wo);
	Rdebug("setSensorTorqueTransformData,ret=%d\n",ret);


	//标定传感器,一次执行永久生效，触发式执行
	//ret=TorqueSensorCalibration(system_sensor_name);
	Rdebug("TorqueSensorCalibration,ret=%d\n",ret);
	
	//创建定时器
	RTimer mytimer;
	ret=initUserTimer(&mytimer, 0, 1);
	Rdebug("initUserTimer,ret=%d\n",ret);

	while(robot_ok())
	{
		//定时
		userTimer(&mytimer);

		//获取传感器的原始数据
		double tor[6];
		ret=GetSensorTorque(system_sensor_name, tor);
		if (0!=ret)
		{
			Rdebug("TorqueSensorCalibration,ret=%d\n",ret);
		}
		
		
		//记录运行采集传感器数据。快速返回，不阻塞时钟
		RSaveDataFast1("original_data_record",1, 100, 6, tor );


		double angle[10];
		//获取机器人当前关节角度
		ret=GetGroupPosition(robot_name, angle);
		if (0!=ret)
		{
			Rdebug("GetGroupPosition,ret=%d\n",ret);
		}

		//对传感器数据进行转换(转换到工具坐标系下)
		ret=SensorTorqueTransformToTool(system_sensor_name, angle, tor);
		if (0!=ret)
		{
			Rdebug("SensorTorqueTransformToTool,ret=%d\n",ret);
		}
		//记录运行采集传感器转换数据。快速返回，不阻塞时钟
		RSaveDataFast1("transform_data_record",1, 100, 6, tor );

	}

    return 0;
}
