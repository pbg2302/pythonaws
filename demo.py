import boto3
aws_conso = boto3.session.Session(profile_name="default")
iam = aws_conso.client('s3')
print(iam)