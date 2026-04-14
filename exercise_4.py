from config import get_client

ec2 = get_client('ec2')

DANGEROUS_PORTS = {
    22:    'SSH',
    3389:  'RDP',
    3306:  'MySQL',
    5432:  'PostgreSQL',
    27017: 'MongoDB'
}

def check_open_ports():
    findings = []
    response = ec2.describe_security_groups()

    for sg in response['SecurityGroups']:
        sg_id   = sg['GroupId']
        sg_name = sg['GroupName']

        # YOUR TASK:
        # Loop through sg['IpPermissions']
        # Each rule has FromPort and IpRanges
        # Check if any IpRanges entry has CidrIp == '0.0.0.0/0'
        # AND FromPort is in DANGEROUS_PORTS
        #
        # Append to findings:
        
        for rule in sg['IpPermissions']:
            port = rule.get('FromPort')
            for ip_range in rule['IpRanges']:
                if port in DANGEROUS_PORTS and ip_range ['CidrIp'] == '0.0.0.0/0':
                    findings.append({
                    'sg_id': sg_id,
                    'sg_name': sg_name,
                    'port': port,
                    'service': DANGEROUS_PORTS[port],
                    'severity': 'CRITICAL',
                    'issue': f'Port {port} open to 0.0.0.0/0'})
        
        



    return findings

results = check_open_ports()
for r in results:
    print(f"[{r['severity']}] {r['sg_id']} -- {r['issue']}")
