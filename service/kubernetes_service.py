import logging
import sys

from PyInquirer import prompt

import config_reader
import request_handler
import pods_manager


def get_target_account():
    account_list = [
        {
            'type': 'list',
            'qmark': '✔',
            'name': 'selected_account',
            'message': 'Choose an account:',
            'choices': ['dev01', 'test']
        }
    ]
    account = prompt(account_list)
    return account


def get_request_type():
    request_types = [
        {
            'type': 'list',
            'qmark': '✔',
            'name': 'request_types',
            'message': 'Choose a request type:',
            'choices': ['Scale', 'Restart']
        }
    ]
    request_type = prompt(request_types)
    return request_type


def get_pod_count():
    count = 0
    if request_type == "Scale":
        count = int(input("Enter the desired pod count: "))
        if count < 0:
            raise ValueError("Pod count must be non-negative")
    return count


def get_target_pods():
    pod_list = [
        {
            'type': 'checkbox',
            'qmark': '✔',
            'name': 'pod_list',
            'message': "Select the pod's:",
            'choices': [
                {
                    'name': 'All'
                },
                {
                    'name': 'osv-api-service'
                },
                {
                    'name': 'osv-audit-tracking'
                },
                {
                    'name': 'osv-data-preparation-service'
                },
                {
                    'name': 'osv-inventory-processor-service'
                },
                {
                    'name': 'osv-pfm-service'
                },
                {
                    'name': 'osv-software-release-refresh-service'
                },
                {
                    'name': 'osv-psirt-fn-refresh-service'
                },
                {
                    'name': 'osv-recommendation-engine-service'
                },
                {
                    'name': 'osv-campusnetwork-views-etl-service'
                },
                {
                    'name': 'osv-cloudnetwork-views-etl-service'
                },
                {
                    'name': 'osv-cloudnetwork-api-service'
                },
                {
                    'name': 'osv-gatekeeper-service'
                },
                {
                    'name': 'osv-recommendation-reinitiate-service'
                },
                {
                    'name': 'osv-schema-mapping'
                },
                {
                    'name': 'osv-schema-migration'
                },
                {
                    'name': 'osv-test-mock-data'
                },
                {
                    'name': 'osv-customer-data-refresh-service'
                }
            ]
        }
    ]
    pods = prompt(pod_list)

    if not pods:
        raise ValueError("Target pod's should not be empty")

    return pods


def confirm_request():
    response = input("Please type 'confirm' to perform the actions described above: ")
    if response == "confirm":
        return bool(True)
    print("Request aborted.")
    sys.exit()


logger = logging.getLogger()
logger.setLevel(logging.INFO)

try:
    # Get a target account
    target_account = get_target_account()['selected_account']

    # Fetching inputs from config file
    config = config_reader.read('config.ini')
    cluster = config.get(target_account, "cluster")
    region = config.get(target_account, "region")
    namespace = config.get(target_account, "namespace")
    profile = config.get(target_account, "profile")
    logging.info("Cluster: %s, Region: %s, Namespace: %s, profile: %s", cluster, region, namespace, profile)

    # Get an operation to perform
    request_type = get_request_type()['request_types']

    # Get the pod count
    pod_count = get_pod_count()

    # Get the target pods
    target_pods = get_target_pods()['pod_list']
    logging.info("Target Pod's: %s", target_pods)

    # Confirmation to apply changes
    confirm_request()

    # update_context
    pods_manager.update_context(cluster, region, profile)

    # Trigger service based on the request
    request_handler.trigger(request_type, target_pods, pod_count, namespace)
    logging.info("%s request completed. PodCount: %s, TargetPod's: %s", request_type, pod_count, target_pods)

except Exception as err:
    logging.error('Could not complete %s request. %s', request_type, err)
    raise err
