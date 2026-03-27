from config import get_client

s3 = get_client('s3')
response = s3.list_buckets()