from korean_geocoding.geocoding import KoreanGeocoding as Kg
import openpyxl
import time

## NAVER API를 활용하여 주소를 위도 경도로 변환
kg = Kg()
kg.set_naver_api("hdfa8f31bk", "3uD3bopOrcTwYjeC6TnLOQxGDqIkwNPPYlhYo4JI")

## place와 주소로 이루어진 last.xlxs load
filename = "last.xlsx"
exelFile = openpyxl.load_workbook(filename)

## 주소를 위도와 경도로 변경해주는 코드
sheet = exelFile.worksheets[0]
rowCount = 1
for row in sheet.rows:
    try:
        print(row[1].value)
        g = kg.get_coordinates_by_api(row[1].value)
        lat_cell = sheet.cell(row=rowCount, column=3)
        lng_cell = sheet.cell(row=rowCount, column=4)

        lat_cell.value = g[0]
        lng_cell.value = g[1]
        rowCount = rowCount + 1
    except:
        rowCount = rowCount + 1
        print("error")

## nokids.xlsx로 저장
exelFile.save("nokids.xlsx")