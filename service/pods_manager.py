import logging
import subprocess
import time

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def update_context(cluster, region, profile):
    subprocess.run(f'aws eks --region {region} update-kubeconfig --name {cluster} --profile {profile}',
                   shell=True)
    time.sleep(3)
    logger.info("Context updated for cluster: %s", cluster)


def scale_all(pod_count, namespace):
    subprocess.run(f'kubectl scale deployment --all --replicas={pod_count} -n {namespace}', shell=True)
    logger.info("Scale all pods request initiated. PodCount: %s", pod_count)


def scale(pod_names, pod_count, namespace):
    for service in pod_names:
        subprocess.run(f'kubectl scale deployment {service} --replicas={pod_count} -n {namespace}', shell=True)
        logger.info("Scale %s request initiated. PodCount: %s", service, pod_count)


def restart_all(namespace):
    subprocess.run(f'kubectl delete pods --all -n {namespace}', shell=True)
    logger.info("Restart all pods request initiated.")


def restart(pod_names, namespace):
    for service in pod_names:
        subprocess.run(f'kubectl delete pods -l app={service} -n {namespace}', shell=True)
        logger.info("Restart %s request initiated.", service)
