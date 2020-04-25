import boto3
import json

# TODO: Add command line parser
# TODO: Add default values

parameters_path = './infrastructure-parameters.json'

with open(parameters_path, 'r') as f:
    parameters = json.load(f)

template_path = './cloudformation-template.yml'

with open(template_path, 'r') as f:
    template = f.read()

stack_name = "mystack"

client = boto3.client('cloudformation')

client.describe_stacks()

# The following lines can be used to delete a cloudformation stack
# client.delete_stack(StackName=stack_name)

client.create_stack(
    StackName=stack_name,
    TemplateBody=template,
    Parameters=parameters
)
