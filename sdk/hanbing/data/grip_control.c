
#include "HYYRobotInterface.h"
int MainModule()
{
	int ret=0;
	//创建夹抓，系统会启动默认创建索引为0的夹抓，如果使用系统创建的夹抓，无需使用该接口。
	//ret=CreateGrip2("mygrip", "grip_config.ini");
	//Rdebug("CreateGrip2,ret=%d\n",ret);
	//获取系统内置夹爪的名字
	const char* system_grip_name=GetGripName(0,NULL);

	//获取自己创建的传感器名字
	//const char* my_grip_name=GetGripName(1,NULL);//="mygrip"
	//if (NULL==my_grip_name)
	//{
	//	Rdebug("can't find grip\n");
	//}
	Rsleep(10000);
	Rdebug("close grip\n");
	//闭合夹爪
	ret=ControlGrip(system_grip_name, 1);
	Rdebug("controlGrip,ret=%d\n",ret);
	Rsleep(5000);
	//打开夹爪
	ret=ControlGrip(system_grip_name, 0);
	Rdebug("controlGrip,ret=%d\n",ret);

    return 0;
}
