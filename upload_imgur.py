import requests
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.models import *

handler = WebhookHandler('2031248e7178c55005e9ec4e38ad6c6b')
line_bot_api = LineBotApi('qViXP87MAqgvClsq69dXG+hlPmYWTetH2H5/8Jw5ediVmOJMekaS5V0ThOPbW15sClK7OIvc+woNClpEIbtuIq6hc5ztNsS9KRqchcPN8e5NkC+oWh9Y+4HK4fc6vcn0dan0D+aV2XxroKBBothevwdB04t89/1O/w1cDnyilFU=')

client_id='自己的imgur id' 
'''    訊息得先被讀取 : message_content = line_bot_api.get_message_content(event.message.id)
        取得圖檔訊息 : image_data = message_content.content    '''
def upload_ptoto(image_data):
    link =str
    headers = {'Authorization': f'Client-ID {client_id}'}
    files = {'image': image_data}
    response = requests.post('https://api.imgur.com/3/image', headers=headers, files=files)
    if  response.status_code == 200:
        data = response.json()
        link = data['data']['link']
    return link
