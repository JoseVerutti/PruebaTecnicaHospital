import boto3

session = boto3.Session(
    aws_access_key_id='AKIAQKGGXMNWN2RQH46B',
    aws_secret_access_key='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',
    region_name='us-east-2'  # Cambia a tu región
)

# Conectar a DynamoDB
dynamodb = session.resource('dynamodb')
