1.pulling the git repository and installation is in docker file

2. build the docker images using the following command `docker build -t wisecow .`

3. command to run the docker image `docker run -p 4499:4499 wisecow`

4. now will deploy the docker image into docker-hub
    1. To tag the docker image
        `docker tag wisecow:latest <your-username>/wisecow:latest`
       example: `docker tag front_end:latest 9440866803/front_end:latest`
    2. pusing the docker image into docker hub
       `docker push <your-username>/wisecow:latest`
       example:`docker push 9440866803/frontend_0001:tagname`

5. instruction related to k8s <br>
    please do check the [Deploy.yaml](Deploy.yaml) to view the k8s configuration 
    1. In `deploy.yaml` file contains both service and deployment configuration which has 4 replicas at a time
    2. To run the pods in k8s is `kubectl apply -f Deploy.yaml`

6. Use JenkinsFile to perform CI/CD 


7. [monitor.py](monitor.py)please do check the `monitor.py` for System Health Monitoring Script.

8. [backup.py](backup.py) will take backup of the file in regular intervel of a time.

9. [log_analyzer.py](log_analyzer.py) to analyze the log

10. [application_health_checker.py](application_health_checker.py) to check the health of the application


**Note:In python file i've used dummy date <br> and i've used black python libary to organize thge python code**

