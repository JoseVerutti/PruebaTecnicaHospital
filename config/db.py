import boto3
from dotenv import load_dotenv
import os

load_dotenv()
KEY = os.getenv('KEY')
SECRET_KEY = os.getenv('SECRET_KEY')


session = boto3.Session(
    aws_access_key_id=KEY,
    aws_secret_access_key=SECRET_KEY,
    region_name='us-east-2'  # Cambia a tu región
)

# Conectar a DynamoDB
dynamodb = session.resource('dynamodb')
