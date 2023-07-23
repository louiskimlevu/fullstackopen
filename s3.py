import boto3

from aws_lambda_typing import context as context_, events

def handler(event: events.S3Event, context: context_.Context) -> None:
    event["Records"][0][""]
    event_detail.
    # bucket = event_detail['bucket']['name']
    # file_key = event_detail['object']['key']
    bucket = event_detail['bucket']['name']

    s3 = boto3.client('s3')
    file_to_process = s3.get_object(Bucket=bucket, Key=file_key)