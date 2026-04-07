from config import get_client

iam = get_client('iam')

def check_mfa():
    findings =[]

    #Paginator handles fetching all pages automatically

    paginator = iam.get_paginator('list_users')

    for page in paginator.paginate():
        for user in page['Users']:
            username = user['Username']

