# osv-kubernetes-service

## Why do we need automation?
Now a days, micro-service numbers are growing up and during the integration testing or performance benchmarking testing in dev environment, there are numerous scenarios for scaling up, scaling down, shutting down, and restarting the pods.

In light of the large number of microservices, it may be difficult to perform the mentioned operations within a short period of time.


## What is automated?
In order to simplify the process and reduce time and effort as well, here scale-up, scale-down, shut-down, and restart operations are automated in Python. 


## Prerequisites
> 1. Install python `brew install python` or` brew install python@3.10.12`
> 2. Verify the installation `python3 --version`
> 3. Clone [repo](https://github.com/sabrajak/osv-kubernetes-service.git)
> 4. Right-click on the project -> open module settings -> choose python module sdk (if not configured)
> 5. Install required modules

## How to run?
> 1. Login duo-sso
> 2. Navigate to the repository path `cd <repo-path>/osv-kubernetes-service/service`
> 3. Run: `python  kubernetes_service.py`
> 4. Follow the instructions in the console and choose appropriate options


#### Example:
```
sabrajak@SABRAJAK-M-L8P1 service % python3  kubernetes_service.py
✔ Choose an account:  dev01
INFO:root:Cluster: cluster01_usw2_cx-nprd-dev, Region: us-west-2, Namespace: osv, profile: dev01
✔ Choose a request type:  Scale
Enter the desired pod count: 1
✔ Select the pod's:  [osv-data-preparation-service]
INFO:root:Target Pod's: ['osv-data-preparation-service']
Please type 'confirm' to perform the actions described above: confirm
Updated context arn:aws:eks:us-west-2:071545084450:cluster/cluster01_usw2_cx-nprd-dev in /Users/sabrajak/.kube/config
INFO:root:Context updated for cluster: cluster01_usw2_cx-nprd-dev
deployment.apps/osv-data-preparation-service scaled
INFO:root:Scale osv-data-preparation-service request initiated. PodCount: 1
INFO:root:Scale request completed. PodCount: 1, TargetPod's: ['osv-data-preparation-service']
```
