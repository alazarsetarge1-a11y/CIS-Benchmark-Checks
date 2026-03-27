from config import get_client

s3 = get_client('s3')

response = s3.list_buckets()

findings = []

for bucket in response['Buckets']:
    name = bucket["Name"]
    try:
        block = s3.get_public_access_block(Bucket=name)
        config = block['PublicAccessBlockConfiguration']

        if config['BlockPublicAcls'] == False:
            findings.append({
                'bucket' : name,
                'severity' : 'CRITICAL',
                'issue' : 'Public access not blocked'
            })

    except Exception: 
        findings.append({
            'bucket' : name,
            'severity' : 'CRITICAL',
            'issue' : 'NO Block Config'
        })

    
for f in findings:
    print(f"[{f['severity']}] {f['bucket']} -- {f['issue']}")

