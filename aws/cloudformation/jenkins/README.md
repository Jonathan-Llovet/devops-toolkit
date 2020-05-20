# Jenkins

This cloudformation template will create a [Jenkins](https://www.jenkins.io/) server, along with appropriate security groups.

## What is Jenkins?

From [the docs](https://www.jenkins.io/doc/):

Jenkins is a self-contained, open source automation server which can be used to automate all sorts of tasks related to building, testing, and delivering or deploying software.

Jenkins can be installed through native system packages, Docker, or even run standalone by any machine with a Java Runtime Environment (JRE) installed.

### Creating the Jenkins Stack

```SHELL
aws cloudformation create-stack \
--stack-name jenkins \
--template-body file://jenkins-server.yml \
--parameters file://jenkins-server-parameters.json \
--region=us-east-1
```

### Getting the Initial Admin Password

When you navigate to your Jenkins server for the first time, you will need to enter a password that is generated during installation in order to verify that you are an administrator.

To get the initial administrator password:
- SSH into the Jenkins server that you want to get the password for using the key specified in the `jenkins-server-parameters.yml`.

- Run the following command on the server with a direct installation of Jenkins:
```SHELL
sudo cat /var/lib/jenkins/secrets/initialAdminPassword
```

- Alternatively, if you are connecting to the dockerized Jenkins server, run the following:
```SHELL
docker exec -it jenkins-blueocean cat /var/jenkins_home/secrets/initialAdminPassword
```

### Deleting the Jenkins Stack

When you are finished with the stack and want to delete it, you can use the following command.

```SHELL
aws cloudformation delete-stack \
--stack-name jenkins
```