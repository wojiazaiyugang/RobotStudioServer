
#include "HYYRobotInterface.h"
int MainModule()
{
	move_start();//上电，使用move指令进行运动时必须使用该语句上电

	//获取数据

	//获取笛卡尔位置
	robpose rpose1;
	getrobpose("p1", &rpose1);

	robpose rpose2;
	getrobpose("p2", &rpose2);

	robpose rpose3;
	getrobpose("p3", &rpose3);

	robpose rpose4;
	getrobpose("p4", &rpose4);
	//获取关节位置
	robjoint joint1;
	getrobjoint("j1",&joint1);
	//获取速度
	speed sp;
	getspeed("v1",&sp);
	//转弯区
	zone ze;
        getzone("z0",&ze);
	//获取工具
	tool to;
	gettool("tool0",&to);
	//获取工件
	wobj wo;
	getwobj("wobj0",&wo);

	//循环执行运动指令
	
	/*
	1、moveA等运动指令默认以阻塞方式运行，如以线程方式运行，使用setMoveThread(1)设置所以指令为线程方式运行。可利用get_robot_move_state(int robot_index)获取机器人运动状态。
	2、多机器人操作使用multi_moveA代替moveA，其他指令类似。
	3、双臂运动使用dual_moveA等指令。

	*/

	while(robot_ok())//当发送停止命令时或系统状态错误时退出循环
	{
		Rdebug("设置指令为线程运行方式\n");
		//设置指令为线程运行方式
		setMoveThread(1);
		Rdebug("关节空间运动（关节目标）\n");
		//关节空间运动（关节目标）
		moveA(&joint1,&sp,&ze,&to,&wo);
		
		Rdebug("等待moveA运动完成\n");
		//等待moveA运动完成
		wait_move_finish(0);

		Rdebug("设置指令为阻塞运行方式\n");
		//设置指令为阻塞运行方式
		setMoveThread(0);

		Rdebug("关节空间运动（笛卡尔目标）\n");
		//关节空间运动（笛卡尔目标）
		moveJ(&rpose2,&sp,&ze,&to,&wo);

		Rdebug("笛卡尔空间直线运动\n");
		//笛卡尔空间直线运动
		moveL(&rpose1,&sp,&ze,&to,&wo);

		Rdebug("笛卡尔空间圆弧运动\n");
		//笛卡尔空间圆弧运动
		moveC(&rpose2,&rpose3,&sp,&ze,&to,&wo);

		Rdebug("笛卡尔空间螺旋线运动\n");
		//笛卡尔空间螺旋线运动
		moveH(&rpose2,&rpose3,&rpose4,20.0,&sp,&ze,&to,&wo);

		Rdebug("笛卡尔空间B样条运动\n");
		//笛卡尔空间B样条运动
		moveS("test_data.txt",&sp,&to,&wo);

		Rdebug("关节空间运动（关节目标）\n");
		//关节空间运动（关节目标）
		moveA(&joint1,&sp,&ze,&to,&wo);

		Rdebug("笛卡尔空间相对rpose1沿着工件坐标系的z轴移动100mm\n");
		//笛卡尔空间相对rpose1沿着工件坐标系的z轴移动100mm
		robpose op=Offs(&rpose1,0,0,100,0,0,0);
		moveL(&op,&sp,&ze,&to,&wo);

		Rdebug("关节空间运动（关节目标）\n");
		//关节空间运动（关节目标）
		moveA(&joint1,&sp,&ze,&to,&wo);

		Rdebug("笛卡尔空间相对rpose1沿着工具坐标系的z轴移动100mm并绕z轴选择1rad\n");
		//笛卡尔空间相对rpose1沿着工具坐标系的z轴移动100mm并绕z轴选择1rad
		robpose orp=OffsRel(&rpose1,0,0,0,0,1,0);
		moveL(&orp,&sp,&ze,&to,&wo);

	}

	move_stop();
    return 0;
}
