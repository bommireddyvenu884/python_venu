import boto3
ec2_conn = boto3.client('ec2',region_name='us-east-1')
#dir(ec2_conn)
all_vpcs = ec2_conn.describe_vpcs().get('Vpcs','KeyNotFound')
all_vpc_id = [  vpc['VpcId'] for vpc in all_vpcs ]
all_cidr = [  vpc['CidrBlock'] for vpc in all_vpcs ]
print(all_vpc_id)
print(all_cidr)
vpc_dict = dict(zip(all_vpc_id, all_cidr))
print(vpc_dict)


import boto3
iam = boto3.client('iam',region_name='us-east-1')
all_roles = iam.list_roles().get('Roles')
role_names = [  role['RoleName'] for role in all_roles ]
role_arns  = [  role['Arn'] for role in all_roles ]
role_dict = dict(zip(role_names,role_arns))
print(role_dict)