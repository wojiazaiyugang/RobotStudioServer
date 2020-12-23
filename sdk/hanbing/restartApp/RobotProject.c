#include "HYYRobotInterface.h"
extern int MainModule();

int main(int argc, char *argv[])
{
	//------------------------initialize----------------------------------
	command_arg arg;
	if (0!=commandLineParser(argc, argv,&arg))
	{
		return -100;
	}

	if (0!=system_initialize(&arg))
	{
		return -101;
	}
	//-------------------------RobotProject-------------------------------
	return MainModule();
}
