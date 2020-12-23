
#include "HYYRobotInterface.h"
int MainModule()
{
	//上电，使用move指令进行运动时必须使用该语句上电
	move_start();

	//获取数据
	robpose rpose;
	getrobpose("p20", &rpose);
	speed sp;
	getspeed("v1",&sp);
	zone ze;
        getzone("z1",&ze);
	tool to;
	gettool("tool0",&to);
	wobj wo;
	getwobj("wobj0",&wo);

	moveL(&rpose,&sp,&ze,&to,&wo);

	//下电，使用move指令进行运动时必须使用该语句下电
	move_stop();
    return 0;
}
