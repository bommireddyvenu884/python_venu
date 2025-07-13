import boto3
ec2_conn = boto3.client('ec2',region_name='us-east-1')
all_vpcs = ec2_conn.describe_vpcs().get('Vpcs','KeyNotFound')
all_vpc_id = [  vpc['VpcId'] for vpc in all_vpcs ]
all_cidr = [  vpc['CidrBlock'] for vpc in all_vpcs ]
vpc_dict = dict(zip(all_vpc_id, all_cidr))

def find_vpc_cidr(vpcid):
    for key,value in vpc_dict.items():
        if key == vpcid:
            print(f'The CIDR Block Of VPC {vpcid} Is {value}')
        else:
            #print(f'The VPC With ID {vpcid} Not Found...')
            pass