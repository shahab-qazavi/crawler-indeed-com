from pymongo import MongoClient
from collections import Counter, OrderedDict
from openpyxl import Workbook

skill = Workbook()
skill_sheet = skill.active


con = MongoClient()
db = con['crawling_indeed']
col_crawl = db['crawling']
sep_dict = {}
sep_list = []
separate_list = []
counter = 0
for record in col_crawl.find():
    s = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', ',', '/', '\\', '-', '=', '"', '+', '*','–', '?', '!', '@',
         '#', '$', '%', '$', '^', '&', '*', '(', ')', '>', '<', ':', ';', '|', '{', '}', '[', ']', '•', '”', '“',
         '"I', '~', '…', '®', '©', '™', "'", '—', '"']
    for rem in s:
        record['contain'] = record['contain'].replace(rem, ' ')

    sep_list = record['contain'].split()
    for value in sep_list:
        if value.islower() is False:
            separate_list.append(value)
        else:
            pass

print(len(separate_list))

final = OrderedDict(sorted(Counter(separate_list).items(), key=lambda x: x[-1], reverse=True))

print(final)

