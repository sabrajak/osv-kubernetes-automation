import logging
import pods_manager

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def trigger(action, target_pods, pod_count, namespace):
    if "All" in target_pods and action == "Scale":
        pods_manager.scale_all(pod_count, namespace)
    elif "All" in target_pods and action == "Restart":
        pods_manager.restart_all(namespace)
    elif action == "Scale":
        pods_manager.scale(target_pods, pod_count, namespace)
    elif action == "Restart":
        pods_manager.restart(target_pods, namespace)
    else:
        logger.error("Invalid action. Action: %s", action, " TargetPod's: %s", target_pods)
