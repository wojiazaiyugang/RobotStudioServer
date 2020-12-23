
#include "HYYRobotInterface.h"
int MainModule()
{
	move_start();//上电，使用move指令进行运动时必须使用该语句上电

	//获取数据

	//获取笛卡尔位置
	robpose rpose5;
	getrobpose("p5", &rpose5);

	robpose rpose6;
	getrobpose("p6", &rpose6);

	//获取关节位置
	robjoint joint5;
	getrobjoint("j5",&joint5);
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

	moveA(&joint5,&sp,&ze,&to,&wo);
	moveHP(&rpose6, 5, 1, &sp, &ze, &to, &wo);

	move_stop();
    return 0;
}
