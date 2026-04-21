import boto3

try:
    session = boto3.Session(profile_name='default')
    sts = session.client('sts')
    identity = sts.get_caller_identity()
    print(f"Success!")
    print(f"Account ID: {identity['Account']}")
    print(f"User ARN: {identity['Arn']}")
except Exception as e:
    print(f"Connection failed")
    print(f"Error: {e}")
