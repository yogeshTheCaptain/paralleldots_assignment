# paralleldots_assignment

### Instruction to run the program :

##### 1) install docker on local machine first:
#####    sudo apt install apt-transport-https ca-certificates curl gnupg-agent software-properties-common
#####    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
#####    sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
#####    sudo apt install docker-ce

##### 2) pull latest rabbitmq version from docker:
#####    docker pull rabbitmq

##### 3) create docker image:
#####    docker build -t celery_simple:latest .

##### 4) run rabbitmq container:
#####    docker-compose up
#####    Now , the api is live in local system to use the api use postman 

##### 5) Select GET method and then paste this in url box:
#####    http://localhost:8080/inputString?s1=people
#####    change string after '=' sign to test different inputs

### OUTPUT FORMAT:

##### 1) If the requested input key already processed then returns the value as correspoding key
######    Input  = http://localhost:8080/inputString?s1=people
######    Output = {"result": "people","statusMessage": "Already Processed"}

##### 2) If the requested input key is processed for the first time then 
######    Input  = http://localhost:8080/inputString?s1=people
######    Output = {"result": "people","statusMessage": "Successfully Completed"}

##### 3) If the requested input key is processed for the first time and at the same time another same key is requested then 
######    Input  = http://localhost:8080/inputString?s1=people
######    Output = {"result": "people","statusMessage": "Request In Progress"}


