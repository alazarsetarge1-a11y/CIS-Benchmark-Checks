from config import get_client

s3 = get_client('s3')
iam = get_client('iam')
ec2 = get_client('ec2')

#S3 below is vulnerable because public access is NOT blocked
s3.create_bucket(Bucket = 'vulnerable-bucket')
s3.delete_public_access_block(Bucket = 'vulnerable-bucket')
print('Created vulnerable bucket')


#S3 below is safe because public access is blocked
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

#IAM below is vulnerable because it does not have MFA configured

iam.create_user(UserName = 'no-mfa-user')
print('Created IAM user with no MFA')