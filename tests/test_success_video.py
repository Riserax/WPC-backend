import boto3
import json
import os

sqs = boto3.client('sqs')
NOTIFICATIONS_QUEUE_URL = os.getenv("NOTIFICATIONS_QUEUE_URL")

video_ready_request = {
    "video_url": 'example/video',
    "email": "kamilcala05@gmail.com"
}

resp = sqs.send_message(
    QueueUrl=NOTIFICATIONS_QUEUE_URL,
    MessageBody=json.dumps(video_ready_request)
)