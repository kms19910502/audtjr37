import requests
import json

with open(r"C:/Users/2/Desktop/KMS/KAKAO_API/kakao_code.json","r") as kakao:
# with open("token.json","r") as kakao:
    tokens = json.load(kakao)

url="https://kapi.kakao.com/v2/api/talk/memo/default/send"

# kapi.kakao.com/v2/api/talk/memo/default/send 

headers={
    "Authorization" : "Bearer " + tokens["access_token"]
}

data={
    "template_object": json.dumps({
       "object_type": "text",
        "text": "안녕? 나는 사람이야",
        "link": {
            "web_url" : "https://www.naver.com"
        }
    })
}

response = requests.post(url, headers=headers, data=data)
response.status_code

print(response.status_code)
if response.json().get('result_code') == 0:
   print('메시지를 성공적으로 보냈습니다.')
else:
   print('메시지를 성공적으로 보내지 못했습니다. 오류메시지 : ' + str(response.json()))