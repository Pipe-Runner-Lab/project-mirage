from ..franka_cabinet_drawer_top_open.config import TASK_CFG  # noqa

TASK_CFG["headless"] = True
TASK_CFG["task"]["env"]["numEnvs"] = 1024

TASK_CFG["task"]["env"]["openRewardScale"] = 12.0

JOINT_INDEX = 3
