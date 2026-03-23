from config import get_client

s3 = get_client('s3')

# Ask for all buckets
response = s3.list_buckets()

total = 0


for bucket in response['Buckets']:
    name = bucket["Name"]
    date = bucket["CreationDate"]
    total+=1
    print (f"\nBucket: {name} | Created: {date}")




print(f"\nTotal: {total}")