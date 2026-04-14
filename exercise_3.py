from config import get_client

iam = get_client('iam')

def check_mfa():
    findings =[]

    #Paginator handles fetching all pages automatically

    paginator = iam.get_paginator('list_users')

    for page in paginator.paginate():
        for user in page['Users']:
            username = user['UserName']
            # YOUR TASK:
            # Call iam.list_mfa_devices(UserName=username)
            mfa = iam.list_mfa_devices(UserName=username)            # Check if the returned 'MFADevices' list is empty
            # Empty list = no MFA set up = finding
            # Append to findings:
            
            if len(mfa['MFADevices']) == 0:
                findings.append({
                'user': username,
                'severity': 'HIGH',
                'issue': 'No MFA device configured'
            })
            #
            


            

    return findings

results = check_mfa()
for r in results:
    print(f"[{r['severity']}] {r['user']} -- {r['issue']}")
     

