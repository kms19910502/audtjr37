import requests

url = 'https://kauth.kakao.com/oauth/token'
rest_api_key = 'a83f56f0b66eac1a24fb6c7dc05b9f7a'
redirect_uri = 'https://www.naver.com'
authorize_code = 'q6IQ21vilCbdh8vv1g9YSviiI-RLrRO2Q_4vI1D3LR7BFxZu4FbL55iJ8gTBMj8p4DJ-Mgopb1UAAAGEiKibPA'

data = {
    'grant_type':'authorization_code',
    'client_id':rest_api_key,
    'redirect_uri':redirect_uri,
    'code': authorize_code,
    }

response = requests.post(url, data=data)
tokens = response.json()
print(tokens)

# json 저장
import json
#1.
# with open(r"C:\Users\user\Desktop\PythonWorkspace\kakao_test\kakao_code.json","w") as fp:
#     json.dump(tokens, fp)

#2.
with open("kakao_code.json","w") as fp:
    json.dump(tokens, fp)