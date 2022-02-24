## install docker in AWS EC2 instance

```bash
$ sudo yum update -y
```
* Amazon Linux 2
```bash
$ sudo amazon-linux-extras install docker
```
* Amazon Linux
```bash
$ sudo yum install docker
```
* Start the Docker service
```bash
$ sudo service docker start
```
* (Optional) On Amazon Linux 2, to ensure that the Docker daemon starts after each system reboot, run the following command:
```bash
$ sudo systemctl enable docker
```
* Add the ec2-user to the docker group so you can execute Docker commands without using sudo.
```bash
$ sudo usermod -a -G docker ec2-user
```
```
* Log out and log back in again to pick up the new docker group permissions.
* You can accomplish this by closing your current SSH terminal window and reconnecting to your instance in a new one.
* Your new SSH session will have the appropriate docker group permissions.
```
## pull the synapse cortex docker image into AWS EC2 instance & launch it
```bash
$ docker pull vertexproject/synapse-cortex:v2.x.x
```
```bash
$ docker ps -a    
CONTAINER ID   IMAGE                                 COMMAND                  CREATED        STATUS                    PORTS     NAMES
f54a5e0393ec   vertexproject/synapse-cortex:v2.x.x   "tini -- /vertex/syn…"   14 hours ago   Exited (0) 14 hours ago             recursing_euclid

```
```bash
$ docker run vertexproject/synapse-cortex:v2.x.x

```
* in other tab
```bash
$ docker ps                  
CONTAINER ID   IMAGE                                 COMMAND                  CREATED          STATUS                            PORTS                 NAMES
34231df2da37   vertexproject/synapse-cortex:v2.x.x   "tini -- /vertex/syn…"   10 seconds ago   Up 9 seconds (health: starting)   4443/tcp, 27492/tcp   nifty_hodgkin
```

```bash
$ docker exec -it f54a5e0393ec /bin/bash
root@f54a5e0393ec:/# whoami
root
```

####  Spin up Storm shell 
```bash
root@f54a5e0393ec:/# python -m synapse.tools.storm cell:///vertex/storage

Welcome to the Storm interpreter!

Local interpreter (non-storm) commands may be executed with a ! prefix:
    Use !quit to exit.
    Use !help to see local interpreter commands.

storm>

```

