import os 
import requests
from dotenv import load_dotenv

load_dotenv()

url = os.getenv('URL_SLACK')
msg = 'this message was sendend of vs code'
result = requests.post(url,json={'text':msg})

if result.text =='ok':
    print('/// message was recibed successfully')
else:
    print('algo anda mal',result.text)
    
    