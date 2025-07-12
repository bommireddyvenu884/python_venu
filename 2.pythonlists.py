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

    # learning list functions
    aws_region.append(venu)
    aws_region.pop()
    aws_region.sort()
    aws_region.delete(venu)
    aws_region_1 = aws_region.copy()
    id(aws_region)

    # combination of two list 
    x = [1,2,3,4,5,6]
    y = [1,2,3,4,5,6]
    x.extend(y)

    aws_region.index("venu")
    aws_region.reverse()
    print(aws_region)


    # working with tuples
    def tuple_check(*args):
        print(args)
        print(type(args))
        