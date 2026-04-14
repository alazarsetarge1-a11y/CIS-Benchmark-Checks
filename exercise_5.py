from config import get_client
import json

s3 = get_client('s3')
iam = get_client('iam')
e2 = get_client('ec2')




scanner = SecurityScanner()
findings = scanner.run()
print(json.dumps(findings, indent=2, default=str))