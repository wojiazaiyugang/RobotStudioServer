
#include "HYYRobotInterface.h"
extern void clear_robot_move_error(int robot_index);
int MainModule()
{
	//启动egm功能
//	if (0!=ClientCreate("192.168.0.x", 8888, "pc"))
//	{
//		Rdebug("client connect failure!\n");
//		return -1;
//	}
	robjoint egmjoint;
	getrobjoint("jegm", &egmjoint);
	speed sp;
	getspeed("v1",&sp);
	tool to;
	gettool("tool0",&to);
	wobj wo;
	getwobj("wobj0",&wo);

	RESTART:
	move_start();
//	SocketSendString("i", "pc");
	moveA(&egmjoint,&sp,NULL,NULL,NULL);
//	SocketSendString("s", "pc");
	EGMCreate_c("egmapp", 0, 0, 1, 4, &to, &wo);	
	EGMRunJoint_c("egmapp", 1);
	EGMRelease_c("egmapp");
	if (!robot_move_ok())
	{
//		SocketSendString("e", "pc");
		clear_robot_move_error(0);
		Rsleep(2000);
		goto RESTART;
	}

	move_stop();
    return 0;
}
