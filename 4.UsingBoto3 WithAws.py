import boto3

# Create EC2 client for us-east-1 region
ec2_conn = boto3.client('ec2', region_name='us-east-1')

# Describe VPCs
all_vpcs = ec2_conn.describe_vpcs().get('Vpcs', 'keynotfound')  # Correct key is 'Vpcs' (capital V)

# Extract VPC IDs
all_vpc_ids = [vpc['VpcId'] for vpc in all_vpcs]

# Extract CIDR blocks
all_cidrs = [vpc['CidrBlock'] for vpc in all_vpcs]

# Print results
print("VPC IDs:", all_vpc_ids)
print("CIDR Blocks:", all_cidrs)
