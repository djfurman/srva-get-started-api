from database import db
from uuid import uuid4
from models import Message
import json

def lambda_handler(event, context):
    request = event['body']
    uuid = str(uuid4())
    payload = {
        'name': ' '.join([request['first_name'], request['last_name']]),
        'email_address': request['email_address'],
        'message': request['message'],
        'uuid': uuid,
        'phone_number': request['phone_number'],
    }
    my_message = Message.create(payload)

    response = {
        'isBase64Encoded': False,
        'statusCode': 201,
        'body': {'id': uuid},
        'headers': {'location': '/'.join(['http://example.com', my_message.serialize()['uuid']])},
    }
    print(json.dumps(response))  # log this
    return response  # respond to the gateway


def fetch_all(event, context):
    content = Message.all().serialize()
    response = {
        'isBase64Encoded': False,
        'statusCode': 200,
        'body': content,
    }
    print(json.dumps(response))
    return response
