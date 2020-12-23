
#include "HYYRobotInterface.h"
int MainModule()
{
	SetDo(0,0);
	Rsleep(1000);
	SetDo(0,1);
	Rsleep(1000);
	SetDo(0,0);
	return 0;
}
