import boto3
from botocore.exceptions import ClientError
import json
import sys
import argparse

#TODO: Change default behavior with no args to describe rather than create
#TODO: Add Create flag

def parse_cli():
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument(
            "-n",
            "--name",
            default="cf-stack",
            help="path to file containing parameters for cloudformation template",
        )
        parser.add_argument(
            "-t",
            "--template",
            default="./template.yml",
            help="path to file containing cloudformation template",
        )
        parser.add_argument(
            "-p",
            "--params",
            help="path to file containing parameters for cloudformation template",
        )
        parser.add_argument(
            "-del",
            "--delete",
            action="store_true",
            help="optional flag indicating whether to delete the cloudformation stack",
        )
        describe_group = parser.add_mutually_exclusive_group()
        describe_group.add_argument(
            "-desc",
            "--describe",
            action="store_true",
            help="optional flag to describe cloudformation stacks",
        )
        describe_group.add_argument(
            "-da",
            "--describe_all",
            action="store_true",
            help="optional flag to describe all cloudformation stacks",
        )
        describe_group.add_argument(
            "-l",
            "--list",
            action="store_true",
            help="optional flag to list all cloudformation stack names",
        )
        return parser.parse_args()
    except argparse.ArgumentError as err:
        print(str(err))
        sys.exit(2)

def stack_exists(name, required_status='CREATE_COMPLETE'):
    # See: https://stackoverflow.com/questions/23019166/boto-what-is-the-best-way-to-check-if-a-cloudformation-stack-is-exists
    try:
        data = client.describe_stacks(StackName=name)
    except ClientError:
        return False
    return data['Stacks'][0]['StackName'] == name
    # TODO: Add flag for using status
    # return data['Stacks'][0]['StackStatus'] == required_status

def get_stack_name_list(data):
    stack_ids = []
    for stack in data['Stacks']:
        stack_ids.append(stack['StackName'])
    return stack_ids

if __name__ == "__main__":

    client = boto3.client('cloudformation')
    cli_args = parse_cli()
    stack_name = cli_args.name

    if cli_args.list:
       cli_args.describe_all = True

    if cli_args.describe_all:
       cli_args.describe = True
       describe_function = client.describe_stacks()

    if cli_args.describe:
        if not cli_args.describe_all:
            describe_function = client.describe_stacks(StackName=stack_name)
        try:
            data = describe_function
            if cli_args.list:
                stack_names = get_stack_name_list(data)
                result = stack_names
            else:
                result = data
            print(result)
        except ClientError:
            print(f"Stack with id {stack_name} does not exist")
        sys.exit()

    if cli_args.delete:
        result = client.delete_stack(
            StackName=stack_name
        )
        print(result)
        sys.exit()

    with open(cli_args.params, 'r') as f:
        parameters = json.load(f)

    with open(cli_args.template, 'r') as f:
        template = f.read()

    if stack_exists(stack_name):
        result = client.update_stack(
            StackName=stack_name,
            TemplateBody=template,
            Parameters=parameters
        )
        print(result)
    else:
        result = client.create_stack(
            StackName=stack_name,
            TemplateBody=template,
            Parameters=parameters
        )
        print(result)
