import boto3
 def sample_function():
    ec2 = boto3.client('ec2',region_name='us-east-1')
    all_vpcs = ec2.describe_vpcs().get('Vpcs',[])
    for vpc in all_vpcs:
        print(vpc['vpcId'])




         import boto3
   ...:
   ...: def sample_function():
   ...:     ec2 = boto3.client('ec2', region_name='us-east-1')
   ...:
   ...:     # Typo fixed: "describe_vpcs" instead of "descibe_vpcs"
   ...:     all_vpcs = ec2.describe_vpcs().get('Vpcs', [])
   ...:
   ...:     for vpc in all_vpcs:
   ...:         print(vpc['VpcId'])
   ...:
   ...: sample_function()
 def sample_function(region):
   ...:     ec2 = boto3.client('ec2', region_name=region)
   ...:
   ...:     # Typo fixed: "describe_vpcs" instead of "descibe_vpcs"
   ...:     all_vpcs = ec2.describe_vpcs().get('Vpcs', [])
   ...:
   ...:     for vpc in all_vpcs:
   ...:         print(vpc['VpcId'])
   ...:
   ...: sample_function('us-west-1')

## for s3
s3 = boto3.client('s3')
response = s3.list_buckets()  # ✅ Correct: call the method
print(response)

## for iam
 iam = boto3.client('iam',region_name='us-east-1')
 all_vpcs=iam.describe_vpcs().get('Vpcs', [])

##ACM
import boto3

acm = boto3.client('acm', region_name='us-east-1')

response = acm.request_certificate(
    DomainName='example.com',
    ValidationMethod='DNS'
)

print("Certificate ARN:", response['CertificateArn'])

