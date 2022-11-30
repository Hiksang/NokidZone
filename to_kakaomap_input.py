import openpyxl
import time
import sys
import pandas as pd

## 카카오 지도 API를 활용하기 위한 딕셔너리 형식을 만드는 코드

## 엑셀파일 열기
filename = "nokids.xlsx"
exelFile = openpyxl.load_workbook(filename)

## 시트 설정
sheet = exelFile.worksheets[0]
df = pd.DataFrame()
adr = []
rowCount = 1

for row in sheet.rows:
    try:
        a = row[0].value
        b = row[2].value
        c = row[3].value
        print(row[0].value)
        print(row[1].value)
        print(row[2].value)
        k = dict()
        k['title'] = a
        k['lat'] = b
        k['lng'] = c
        adr.append(k)
    except:
        print("error")


##  식당명, X, Y 로 구성된 데이터를 웹을 구현하는데 필요한 형식인
## {'title': '식당명', 'lat': 37.5654272, 'lng': 126.9816208} 으로 변경
new_adr = [i for i in adr if i['lat'] != None]
f = open('kakao_map_input.txt', 'w')
print(new_adr, file=f)
f.close()