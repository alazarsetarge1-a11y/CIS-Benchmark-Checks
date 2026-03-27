from config import get_client

s3 = get_client('s3')

response = s3.list_buckets()

for bucket in response['Buckets']:
    name = bucket["Name"]