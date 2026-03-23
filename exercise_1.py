from config import get_client

s3 = get_client('s3')

# Ask for all buckets
response = s3.list_buckets()

total = 0


for bucket in response['Buckets']:
    print(bucket)
    total+=1

name = bucket["Name"]
date = bucket["CreationDate"]

print (f"Bucket:  {name} | Created:  {date}")
print(f"Total: {total}")