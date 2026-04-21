import boto3

session = boto3.Session(profile_name='default')
s3 = session.client('s3')
total_bytes = 0

try:
    # get a list of buckets from S3
    response = s3.list_buckets()
    print(f"{'BUCKET NAME':<40} | {'STATUS':<10}")
    print(f"-" * 55)

    for bucket in response['Buckets']:
        name = bucket['Name']
    
        # list all the objects in each bucket to see if it's empty
        objs = s3.list_objects_v2(Bucket=name, MaxKeys=1)
        if 'Contents' in objs:
            status = "Contains Data"
        else:
            status = "Empty"

except Exception as e:
    print(f"Error during audit: {e}")

print(f"Total bytes: {total_bytes}")
