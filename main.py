import pandas as pd
import re

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

#
# a = clean_punc(test, punct, punct_mapping)
# clean_text(a)
#
import kss
#
# print(test)
# print(kss.split_sentences(test))

a = clean_text(test)

print(a)

b = clean_punc(test, punct, punct_mapping)
print(b)

print(kss.split_sentences(b))
