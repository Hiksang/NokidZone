import pandas as pd
nk = []
j = 1
l = 0
df = pd.read_excel('1_pre.xlsx', usecols = ['content']) #사용할 열 지정
sf = pd.read_excel('1_pre.xlsx', usecols = ['place'])
#print(df['content'][l]) #파일명['열이름']['행이름']
#print(sf['place'][l])
k=df['content'][0].split()
#print(k[1])
nokids = 'false'
for l in range(len(df)) :
     for i in range(len(k)) :
          if k[i] == '노키즈존' :
               nokids = 'true'
               i = i+1
          elif k[i] == '노키즈' :
               nokids = 'true'
               i = i+1
          elif k[i] == 'nokid':
               nokids = 'true'
               i = i+1
          elif k[i] == 'nokids':
               nokids = 'true'
               i = i+1
          elif k[i] == 'Nokid':
               nokids = 'true'
          elif k[i] == 'Nokid':
               nokids = 'true'
          elif k[i] == '예스키즈존':
               nokids = 'false'
               i = i+1
          elif k[i] == '예스키즈':
               nokids = 'false'
          elif k[i] == 'yeskids':
               nokids = 'false'
          elif k[i] == 'Yeskids':
               nokids = 'false'
               i = i+1
          else :
               i = i+1

     if nokids == 'true' :
          if sf['place'][l] != '' :
                         nk.append(sf['place'][l])
          l = l+1
     else :
          l = l+1
n=0
for m in range(len(df)):
     nk[m] = str(nk[m])
     if nk[m] != 'nan' :
          nk[n] = nk[m]
          n = n+1
     m = m+1

nk = set(nk)
nk = list(nk)

nn = pd.DataFrame(nk)
print(nn)
nn.to_excel("nokids.xlsx")
