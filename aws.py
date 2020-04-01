import boto3
import botocore
import json

aws_console = boto3.session.Session(profile_name="default")
ec2 = aws_console.client('ec2')

regions = ec2.describe_regions()['Regions']
for region in regions:
    print(region['RegionName'])
    ec2_instances = ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])

    for ec2_instance in ec2_instances:
        ec2_instance.stop()
        print('Stopped instances :', ec2_instance.id)




