USE_LOCALSTACK = True

LOCALSTACK_CONFIG = {
    'endpoint_url' : 'http://localhost:4566',
    'region_name' : 'us-east-1',
    'aws_access_key_id' : 'test',
    'aws_secret_access_key' : 'test'
}


REAL_AWS_CONFIG = {
    'region_name' : 'us-east-1'
}

def get_client(service):
    import boto3
    config = LOCALSTACK_CONFIG if USE_LOCALSTACK else REAL_AWS_CONFIG # if/else statement meant to choose between the localstack env or real AWS
    return boto3.client(service, **config) # ** Is a dict unpack element meant to read key value pairs as one 