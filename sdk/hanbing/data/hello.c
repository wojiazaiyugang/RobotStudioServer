
#include "HYYRobotInterface.h"
int MainModule()
{
    	sleep(3);
	printf("BSplineSample start\n");

	robjoint rjoint0;
	getrobjoint("j10", &rjoint0);
	robjoint rjoint1;
	getrobjoint("j11", &rjoint1);
	robjoint rjoint2;
	getrobjoint("j12", &rjoint2);

	speed sp;
	getspeed("v1",&sp);

	moveA(&rjoint0,&sp,0,0,0);
moveA(&rjoint1,&sp,0,0,0);
moveA(&rjoint2,&sp,0,0,0);
	printf("BSplineSample end\n");
    return 0;
}
