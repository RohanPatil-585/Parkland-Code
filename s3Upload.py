from __future__ import print_function
import json
import boto3
# boto3 S3 initialization
# third lambda function
# test s3Upload
# test1
s3_client = boto3.client("s3")
def lambda_handler(event, context):
    for record in event['Records']:
        print("test")
        payload = record["body"]
        record_dict = json.loads(payload)
        s3_client.copy_object(CopySource=record_dict['CopySource'], Bucket=record_dict['dest_bucket'], Key=record_dict['file_name'])
    return {
       'statusCode': 200,
       'body': json.dumps('File copied to bucket'+dest_bucket)
    }