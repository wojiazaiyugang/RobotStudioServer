
#include "HYYRobotInterface.h"
int camera_work(double data[][6]);
int robot_work(double data[][6], int data_num, double force, double radius, double screw, const char* cspeed, const char* czone, const char* ctool, const char* cwobj);
int MainModule()
{
	double data[100][6];
	int data_num=camera_work(data);//4dica的视觉模块
	if (data_num<0)
	{
		Rdebug("camera_work failure\n");
		return -1;
	}
	int ret=robot_work(data, data_num, 5, 50, 10, "v1", "z0", "tool0", "wobj0");//4dica的机器人模块
	return ret;
}

/*相机
data  返回机器人加工数据

return 加工数据点数目
*/
int camera_work(double data[][6])
{
	int data_num=0;
	//连接相机
	int ret=ClientCreate("192.168.1.100", 8888, "camera");
	if (0!=ret)
	{
		Rdebug("camera_work:ClientCreate failure, err=%d\n",ret);
		return ret;
	}
	while (0==data_num)//直到获取数据方可推出
	{
		//命令相机获取运动数据
		SocketSendString("S", "camera");

		//获取运动数据
		data_num=SocketRecvDoubleArray(&(data[0][0]), "camera");//数据格式：x1,y1,z1,rx1,ry1,rz1,x2,y2,z2,rx2,ry2,rz2,......(单位：mm,rad，姿态为固定角度描述)
		
		//计算数据点数据		
		data_num=data_num/6;
	}
	
	//断开相机连接
	SocketClose("camera");

	return data_num;
}

/*机器人
data 机器人加工数据
data_num 加工数据点数目
force 加工力
radius 半径
screw 螺距离
cspeed 运行速度
czone 转弯去
ctool 使用工具名称
cwobj 加工工件名称
return 0:执行成功，其他：执行失败
*/
int robot_work(double data[][6], int data_num, double force, double radius, double screw, const char* cspeed, const char* czone, const char* ctool, const char* cwobj)
{
	int ret=0;
	if (data_num<2)
	{
		Rdebug("robot_work: 加工数据不足\n");
		ret=-1;
		goto ROBOTWORKEND;
	}

	//获取运行数据
	speed sp;
	zone zo;
	tool to;
	wobj wo;
	getspeed(cspeed, &sp);
	getzone(czone, &zo);
	gettool(ctool, &to);
	getwobj(cwobj, &wo);
	robpose P[100];
	int i=0;
	for (i=0;i<data_num;i++)
	{
		init_robpose(&(P[i]), data[i], &(data[i][3]));
	}
	robpose pstart=Offs(&(P[0]), 0, 0, 50, 0, 0, 0);
	robpose pend=Offs(&(P[data_num-1]), 0, 0, 50, 0, 0, 0);
	
	move_start();//上电	
	
	//初始化力控制数据
	ret=SFCInit("robotOsPolish", 1, 1, &to, &wo, 0);
	if (0!=ret)
	{
		Rdebug("robot_work: SFCInit failure\n");
		goto ROBOTWORKEND;
	}

	double target_force[6]={0,0,force,0,0,0};
	ret=SFCSetHybridForceMotionTargetForce("robotOsPolish", target_force);
	if (0!=ret)
	{
		Rdebug("robot_work: SFCSetHybridForceMotionTargetForce failure\n");
		goto ROBOTWORKEND;
	}
	double M[6]={0,0,0.1,0,0,0};
	double B[6]={0,0,1,0,0,0};
	double coeff[6]={0,0,0,0,0,0};
	ret=SFCSetHybridForceMotionCtrlParam("robotOsPolish", M, B, coeff);
	if (0!=ret)
	{
		Rdebug("robot_work: SFCSetHybridForceMotionCtrlParam failure\n");
		goto ROBOTWORKEND;
	}

	//运动
	moveJ(&pstart, &sp, &zo, &to, &wo);//运动到其实点正上方
	moveL(&(P[0]), &sp, &zo, &to, &wo);//开始运动

	//开启力控制
	ret=SFCStart("robotOsPolish");
	if (0!=ret)
	{
		Rdebug("robot_work: SFCStart failure\n");
		goto ROBOTWORKEND;
	}
	//加工运动
	for (i=1;i<data_num;i++)
	{
		moveHP(&(P[i]), radius, screw, &sp, &zo, &to, &wo);
	}
	ret=SFCEnd("robotOsPolish");
	if (0!=ret)
	{
		Rdebug("robot_work: SFCEnd failure\n");
		goto ROBOTWORKEND;
	}
	moveL(&pend, &sp, &zo, &to, &wo);//结束运动
	ROBOTWORKEND:
	move_stop();//下电
	return ret;
}




