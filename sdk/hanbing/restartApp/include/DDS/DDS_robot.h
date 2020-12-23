/**
 * @file DDS_robot.h
 *
 * @brief  dds 机器人数据收发接口
 * @author hanbing
 * @version 1.0
 * @date 2020-05-18
 *
 */

#ifndef __DDS_ROBOT__
#define __DDS_ROBOT__



#ifdef __cplusplus
namespace HYYRobotBase
{
extern "C" {
#endif

/*-------------------------------------------------------------------------*/
/**
  @brief	DDS机器人关节数据结构 

	@detail 描述机器人关节状态
 */
/*-------------------------------------------------------------------------*/
typedef struct {
	double angle1;///< 机器人关节数据
	double angle2;///< 机器人关节数据
	double angle3;///< 机器人关节数据
	double angle4;///< 机器人关节数据
	double angle5;///< 机器人关节数据
	double angle6;///< 机器人关节数据
	int flag;///< 数据更新标识
	long long test1;
	float test2;
}RotationAngle;

/**
 * @brief 创建DDS发布服务
 *
 * @param domain_id id号
 * @return 程序执行成功与否
 * @retval int 0:成功； other:失败
 */
extern int create_participant_pub(int domain_id);

/**
 * @brief   DDS发布机器人关节状态
 *
 * @param RotAngle 机器人关节数据
 * @return 发布是否成功  
 *	@retval 0:成功；
 *	@retval other:失败
 */
extern int start_publisher(RotationAngle RotAngle);

/**
 * @brief 关闭DDS发布服务
 *
 * @return int 0:成功； other:失败
 */
extern int participant_shutdown_pub();

/**
 * @brief 创建DDS订阅服务
 *
 * @param domain_id id号
 * @return int 0:成功； other:失败
 */
extern int create_participant_sub(int domain_id);

/**
 * @brief DDS订阅机器人关节状态
 *
 * @return RotationAngle 机器人关节数据
 */
extern RotationAngle start_subscriber();

/**
 * @brief 关闭DDS订阅服务
 *
 * @return int 0:成功； other:失败
 */
extern int participant_shutdown_sub();

#ifdef __cplusplus
}
}
#endif


#endif 


