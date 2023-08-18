# DailyTaskNotifier

```
Written by Minbo Chung in 18-Aug-2023
```

```
This project is purposed for knowledge sharing from my understanding to following topics: 
* Gmail API for Python
* Jenkins
* Docker
```

## Project objectives
```
1. Understand how to send an email via python scripts
2. Understand fundamentals in a use of docker as well as jenkins
3. Be able to implement a Jenkins pipeline to upload changes in github repo perodically (manaully-set)
4. Any engineering-enthusiasts can install and follow the instruction
```

## Software used
```
Python: 3.11.4
pip: 23.2.1
Docker: 24.0.5 build ced0996
Jenkins (LTS): 2.401.3
OS: Windows 10

... To be updated ...

```

## How to install necessities
### Prerequisites for Windows-ers
```
It would be best to use Unix-based OS for Docker-usage. Please install WSL.
Please follow this link to install WSL2: https://www.omgubuntu.co.uk/how-to-install-wsl2-on-windows-10
and to setup WSL2 in your VS Code: https://minbolife.wordpress.com/2022/12/27/how-to-set-up-wsl2-in-vs-code-windows-10/
```

### Docker
```
Follow this link: https://docs.docker.com/desktop/install/windows-install/
Install docker first on your computer and once you have installed your docker, 
Check if the docker is successfully installed by commanding "docker" in your prompt.

When running python scripts later from your linux container, you have to install software necessaries mentioned above for python and python packages.

If error found, ask gpt :P.
```
#### Docker terminologies
```
Image: a blueprint for docker to run the virtual machine.
container: An instance that is running on docker image. (E.g. a process running on an executable file.)
```

### Jenkins

```
Personally preference to install jenkins in the docker container.

To install jenkins and execute it, command this on your prompt.
1. docker pull jenkins/jenkins:lts
    - It returns newly created image's id
    - To check if your docker image is installed, command "docker images" 
2. docker run -d -p 8080:8080 -p 50000:50000 --name <your_desired_container_name> jenkins/jenkins:lts
    - It will create a container that will be hosted in port 8080 and your agent on port 50000.
    - To check if your container is running, execute docker image "docker ps -a" 
4. Go to https://localhost:8080 and proceed to your container configuration then you are done with basic installation.
```

### Python3 and pip
#### Python3 for Windows
```
Installation link: https://www.python.org/downloads/windows/

Once your python is installed, command the following string to install pip:
python3 m ensurepip --upgrade

```


### Gmail API for Pythoneers
```
Follow this link for now: https://github.com/googleworkspace/python-samples/blob/main/gmail/snippet/send%20mail/create_draft.py

It will be updated soon.
```
## Useful Docker commands
```
To list images of the docker
* docker images
To list containers of the docker image
* docker ps -a
To (create if container name not exist) / run the container
- first run
    * docker run -d -p hostportnum:hostportnum -p agentportnum:agentportnum --name <name> <imagename>
- else
    * docker run <container_name or id>
To stop the container
* docker stop <container_id or name>
To remove the container
* docker rm <container_id or name>
To remove the image
* docker rmi <image>
To execute your Dockerfile script
* docker build ... 
* docker pull (from somewhere)

To clean your docker
1. Stop the docker containers and remove them
    - docker stop $(docker ps -aq) && docker rm $(docker ps -aq)
2. Remove the images 
    - docker rmi $(docker images -aq)
```
