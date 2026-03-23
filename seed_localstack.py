from config import get_client

s3 = get_client('s3')
iam = get_client('iam')
ec2 = get_client('ec2')

#S3 below is vulnerable because public access is NOT blocked
try:
    s3.create_bucket(Bucket = 'vulnerable-bucket')
    s3.delete_public_access_block(Bucket = 'vulnerable-bucket')
    print('Created vulnerable bucket')
except Exception:
    print('Bucket already exists, skipping')

#S3 below is safe because public access is blocked
try:
    s3.create_bucket(Bucket = 'safe-bucket')
    s3.put_public_access_block(
        Bucket = 'safe-bucket',
        PublicAccessBlockConfiguration = {
            'BlockPublicAcls' : True,
            'BlockPublicPolicy' : True,
            'IgnorePublicAcls' : True,
            'RestrictPublicBuckets' : True
        }
    )
    print('Created safe bucket')

except Exception:
    print('Bucket already exists, skipping')

#IAM below is vulnerable because it does not have MFA configured
try:
    iam.create_user(UserName='no-mfa-user')
    print('Created IAM user with no MFA')
except Exception:
    print('IAM user already exists, skipping')

#EC2 has security group with port 22 open to the entire world nooooooo!
try:
    vpc = ec2.describe_vpcs() ['Vpcs'][0]['VpcId']
    sg = ec2.create_security_group(
        GroupName = 'vulnerable-sg',
        Description = 'Intentionally misconfigured',
        VpcId = vpc
    )['GroupId']
    ec2.authorize_security_group_ingress(
        GroupId = sg,
        IpPermissions = [{
            'IpProtocol' : 'tcp',
            'FromPort' : 22,
            'ToPort' : 22,
            'IpRanges' : [{'CidrIp' : '0.0.0.0/0'}]
        }]
)
    print(f'Created vulnerable security group {sg}')
    
except Exception:
    print('Security Group already exists, skipping')


    

print('\nLocalStack seeded. Ready for exercises.\n')