import pandas as pd
import emoji
from emoji import core
import re
import kss
import openpyxl

data = pd.read_excel('Data.xlsx')
content = data['content']

test = content[3]

punct = "/-'?!.,#$%\'()*+-/:;<=>@[\\]^_`{|}~" + '""“”’' + '∞θ÷α•à−β∅³π‘₹´°£€\×™√²—–&'
punct_mapping = {"‘": "'", "₹": "e", "´": "'", "°": "", "€": "e", "™": "tm", "√": " sqrt ", "×": "x", "²": "2",
                 "—": "-", "–": "-", "’": "'", "_": "-", "`": "'", '“': '"', '”': '"', '“': '"', "£": "e",
                 '∞': 'infinity', 'θ': 'theta', '÷': '/', 'α': 'alpha', '•': '.', 'à': 'a', '−': '-', 'β': 'beta',
                 '∅': '', '³': '3', 'π': 'pi', }


def clean_punc(text, punct, mapping):
    for p in mapping:
        text = text.replace(p, mapping[p])

    for p in punct:
        text = text.replace(p, f' {p} ')

    specials = {'\u200b': ' ', '…': ' ... ', '\ufeff': '', 'करना': '', 'है': ''}
    for s in specials:
        text = text.replace(s, specials[s])

    return text.strip()


def clean_text(texts):
    corpus = []
    for i in range(0, len(texts)):
        review = re.sub(r'[@%\\*=()/~#&\+á?\xc3\xa1\-\|\.\:\;\!\-\,\_\~\$\'\"]', '',
                        str(texts[i]))  # remove punctuation
        review = re.sub(r'\d+', '', str(texts[i]))  # remove number
        review = review.lower()  # lower case
        review = re.sub(r'\s+', ' ', review)  # remove extra space
        review = re.sub(r'<[^>]+>', '', review)  # remove Html tags
        review = re.sub(r'\s+', ' ', review)  # remove spaces
        review = re.sub(r"^\s+", '', review)  # remove space from start
        review = re.sub(r'\s+$', '', review)  # remove space from the end
        corpus.append(review)
    return corpus

def clean_str(text):
    pattern = '([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)' # E-mail제거
    text = re.sub(pattern=pattern, repl='', string=text)
    pattern = '(http|ftp|https)://(?:[-\w.]|(?:%[\da-fA-F]{2}))+' # URL제거
    text = re.sub(pattern=pattern, repl='', string=text)
    pattern = '([ㄱ-ㅎㅏ-ㅣ]+)'  # 한글 자음, 모음 제거
    text = re.sub(pattern=pattern, repl='', string=text)
    pattern = '<[^>]*>'         # HTML 태그 제거
    text = re.sub(pattern=pattern, repl='', string=text)
    pattern = '[^\w\s\n]'         # 특수기호제거
    text = re.sub(pattern=pattern, repl='', string=text)
    text = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]','', string=text)
    text = re.sub('\n', '.', string=text)
    return text


a  = clean_punc(test,punct, punct_mapping)
b = clean_str(a)

print("a" ,a)
print("*"*10)
print("b",b)
print("*"*10)
print(kss.split_sentences(b)[0])
print(kss.split_sentences(b)[1])
print(kss.split_sentences(b)[0], kss.split_sentences(b)[1])
c = kss.split_sentences(b)[0] + " " +  kss.split_sentences(b)[1]
# print(kss.split_sentences(a_test))
# from hanspell
print(c)

print(" ".join(kss.split_sentences(b)))

from soynlp.normalizer import *
# print(repeat_normalize("안녕하세요 ㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎ 아 진자 배고파 ㅎㅋㅋㅋㅋㅋㅋ", num_repeats=2))

# from hanspell import spell_checker
# result = spell_checker.check(b)
# c = result.as_dict()
# print(c['checked'])
# from konlpy.tag import Okt
# okt = Okt()
# print(okt.nouns(b))
# db = pd.DataFrame({'content' :1 ,
#                    'date' : 2,
#                    'place' :3 })

db = pd.DataFrame(columns=["content", "data", "place"])
for i in range(len(data)):
    try:
        bb = data['date'][i]
        cc = data['place'][i]
        a = clean_punc(data['content'][i], punct, punct_mapping)
        b = clean_str(a)
        aa = " ".join(kss.split_sentences(b))
        db = db.append({'content': aa,
                        "data": bb,
                        'place': cc}, ignore_index=True)
    except:
        print("empty")
print(db)
db3 = db.drop_duplicates()
db3.to_excel("preprocess1.xlsx")




