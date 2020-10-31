import requests
import json

url = "https://health.10086.cn/sfi/s/wechat/question/getQuestionTopic?manageId=2&questionId=6"

payload = {}
headers= {}

r = requests.request("POST", url, headers=headers, data = payload)
json_data = json.loads(r.text)
dic_data = json_data["dataList"]
for dic1 in dic_data: 
    print('问：' + dic1["topic"])
    options = dic1["options"]
    for option in options:
        print(option["option"])