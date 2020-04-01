import boto3

aws_con = boto3.session.Session(profile_name="default")

iam = aws_con.client('iam')

response = iam.list_users()
for users in response['Users']:
    print(users['UserName'])