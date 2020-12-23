
#include "HYYRobotInterface.h"
int MainModule()
{
	//启动egm功能
	move_start();
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


        EGMCreate_c("egmtest", 0, 0, 1, 4, &to, &wo);
	EGMRunJoint_c("egmtest", 1);
	printf("egm release\n");
	EGMRelease_c("egmtest");
printf("end\n");


	move_stop();
    return 0;
}
