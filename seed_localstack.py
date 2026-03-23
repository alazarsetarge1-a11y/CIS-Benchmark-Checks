from config import get_client

s3 = get_client('s3')
iam = get_client('iam')
ec2 = get_client('ec2')

