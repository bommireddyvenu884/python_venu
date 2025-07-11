aws_region = ['us-east-1','us-east-2', 'ap-south-1','us-east3']

#To access certain Elements
aws_regions[0]
aws_regions[1]
aws_regions[3]
aws_regions[4]

# to iterate though elements of a list
for venu in aws_regions:
    print(venu)
    print(f"the region name is:{venu}")


for index, value in enumerate(aws_region):
    print(f"Index: {index}, Value: {value}")