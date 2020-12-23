
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
	robjoint joint9;
	getrobjoint("j9",&joint9);
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

	moveA(&joint9,&sp,NULL,NULL,NULL);

	//初始化力控制
	int ret=SFCInit("SFCtest", 1, 0, &to, &wo, 0);
	Rdebug("SFCInit,ret=%d\n",ret);
	
	//设置目标力
	double target_force[6]={0,0,0,0,0,5};
	ret=SFCSetHybridForceMotionTargetForce("SFCtest", target_force);
	Rdebug("SFCSetHybridForceMotionTargetForce,ret=%d\n",ret);
	double P[6]={0.01,0.01,0.01,0.01,0.01,0.01};
	double I[6]={0.001,0.001,0.001,0.001,0.001,0.001};
	double D[6]={0,0,0,0,0,0};
	ret=SFCSetHybridForceMotionCtrlParam("SFCtest", P, I, D);
	//开启力控制
	ret=SFCStart("SFCtest");
	Rdebug("SFCStart,ret=%d\n",ret);
	Rsleep(1000000);
	//moveL(&rpose2,&sp,&ze,&to,&wo);
	printf("1111111111\n");
	ret=SFCEnd("SFCtest");
	Rdebug("SFCEnd,ret=%d\n",ret);


	move_stop();
    return 0;
}
