# Cloudformation

Cloudformation is an Infrastructure as Code (IAC) service from AWS that allows you to automate provisioning, updating, and destroying resources in an AWS environment. In Cloudformation, groups of resources are referred to as `stacks`. These stacks are defined inside of `Cloudformation Templates` that are defined in either `.yml` or `.json` files, with parameters passed in through `.json` files.

## Usage

Cloudformation stacks can be created either in the [AWS Management Console](https://aws.amazon.com/console/) or through the [AWS CLI](https://aws.amazon.com/cli/).
### General and Management Console
- [About AWS Cloudformation](https://aws.amazon.com/cloudformation/)
- [Documentation](https://docs.aws.amazon.com/cloudformation/)

### Cloudformation CLI
- [Installing the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html)
- [CLI Documentation](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/index.html)

#### Frequently Used CLI Commands

List existing stacks
```SHELL
aws cloudformation list-stacks
```

In the examples below, I will use an nginx cloudformation stack as an example:

Create a stack
```SHELL
aws cloudformation create-stack \
--stack-name nginx \
--template-body file://nginx-server.yml \
--parameters file://nginx-server-parameters.json \
--region=us-east-1
```

Update a stack
```SHELL
aws cloudformation update-stack \
--stack-name nginx \
--template-body file://nginx-server.yml \
--parameters file://nginx-server-parameters.json \
--region=us-east-1
```

Delete a stack
```SHELL
aws cloudformation delete-stack \
--stack-name nginx
```

## Resources
### Online Courses and Talks on Cloudformation
- [AWS CloudFormation Master Class](https://www.udemy.com/course/aws-cloudformation-master-class/)
- [Introduction to AWS CloudFormation](https://acloud.guru/learn/intro-aws-cloudformation?_ga=2.21875451.1908753196.1591491545-1748460874.1586184576)
- [Advanced AWS CloudFormation](https://acloud.guru/learn/aws-advanced-cloudformation?_ga=2.21875451.1908753196.1591491545-1748460874.1586184576)
- [Create and Manage Stacks with AWS CloudFormation Using the Command Line Interface](https://app.pluralsight.com/library/courses/create-manage-stacks-aws-cloudformation-command-line-interface/table-of-contents)
- [CloudFormation example using EC2, SecurityGroup and S3 | Amazon Web Services | Tech Primers](https://www.youtube.com/watch?v=Zz5xljI1gn8)
- [AWS re:Invent 2019: [REPEAT 1] Best practices for authoring AWS CloudFormation (DOP302-R1)](https://www.youtube.com/watch?v=bJHHQM7GGro)

### Books on Cloudformation and AWS
- [Amazon Web Services in Action](https://www.amazon.com/Amazon-Services-Action-Andreas-Wittig/dp/1617295116/)
