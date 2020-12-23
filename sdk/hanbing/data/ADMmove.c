
#include "HYYRobotInterface.h"
int MainModule()
{

	//--------------------------自定义部分-----------------------------------
	move_start();//上电，使用move指令进行运动时必须使用该语句上电
	//获取数据

	//获取笛卡尔位置
	robpose rpose1;
	getrobpose("p1", &rpose1);
	robpose rpose2;
	getrobpose("p2", &rpose2);
	robpose rpose3;
	getrobpose("p3", &rpose3);
	//获取关节位置
	robjoint joint1;
	getrobjoint("j1",&joint1);
	robjoint joint2;
	getrobjoint("j2",&joint2);
	//获取速度
	speed sp;
	getspeed("v1",&sp);
	//转弯区
	zone ze;
        getzone("z0",&ze);
	//获取工具
	tool to;
	gettool("tool11",&to);
	//获取工件
	wobj wo;
	getwobj("wobj0",&wo);

	moveA(&joint1,&sp,NULL,NULL,NULL);

	//Rsleep(3000);
	//初始化力控制
	int ret=SFCInit("SFCtest", 0, 1, &to, &wo, 0);
	Rdebug("SFCInit,ret=%d\n",ret);
	

	double M[6]={1,1,1,1,1,1};
	double B[6]={80,80,2,80,80,80};
	double K[6]={1000,1000,5,1000,1000,1000};
	ret=SFCSetAdmittanceCtrlParam("SFCtest", M, B, K);
	Rdebug("SFCSetAdmittanceCtrlParam,ret=%d\n",ret);
	//开启力控制
	ret=SFCStart("SFCtest");
	Rdebug("SFCStart,ret=%d\n",ret);
	//Rsleep(100000);
	moveL(&rpose2,&sp,&ze,&to,&wo);
	Rsleep(2000);
	moveL(&rpose3,&sp,&ze,&to,&wo);
	Rsleep(100000);
	//moveL(&rpose1,&sp,&ze,&to,&wo);
	ret=SFCEnd("SFCtest");
	Rdebug("SFCEnd,ret=%d\n",ret);


	move_stop();
    return 0;
}
