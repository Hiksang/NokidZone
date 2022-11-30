import urllib3
import json
import pandas as pd


# 공공 인공지능 OPEN API 사용
openApiURL = "http://aiopen.etri.re.kr:8000/MRCServlet"
accessKey = "f6387a7b-9790-4866-84f5-a7b4c7b63e8c"
question = "노키즈존인 곳이 어디야?"

# 전처리된 파일을 Load
data = pd.read_excel('1_pre.xlsx')
content = data['content']

test = content[3]

db = pd.DataFrame(columns=["place", "confidence"])

# AI를 활용한 언어처리
for i in range(len(data)):
    try:
        passage =   data['content'][i]
        requestJson = {"argument": {"question": question, "passage": passage}}
        http = urllib3.PoolManager()
        response = http.request("POST", openApiURL, headers={"Content-Type": "application/json; charset=UTF-8","Authorization": accessKey}, body=json.dumps(requestJson))
        a = json.loads(response.data.decode('utf-8'))['return_object']['MRCInfo']['answer']
        b = json.loads(response.data.decode('utf-8'))['return_object']['MRCInfo']['confidence']
        db = db.append({'place': a,
                        "confidence": b,
                       }, ignore_index = True)
        print(a,b)

    except:
        print("Missing Data")

db3 = db.drop_duplicates()

# mlplace.xlsx 파일 생성
db3.to_excel("mlplace.xlsx")


