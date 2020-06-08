# indeed
from pymongo import MongoClient
from .write_excel import write_excel

con = MongoClient()
db = con['crawling_indeed']
col_crawl = db['crawling']
col_tags = db['tags']


def update_count():
    col_tags.update_many({}, {"$set": {"cont": 0}})
    for contain in col_crawl.find():
        for tag in col_tags.find():
            s = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', ',', '/', '\\', '-', '=', '+', '*',  '?', '!', '@',
                 '#', '$', '%', '$', '^', '&', '*', '(', ')', '>', '<', ':', ';', '|', '{', '}', '[', ']']
            for item in s:
                contain['contain'] = contain['contain'].replace(item, ' ')

            if tag['name'].lower() in contain['contain'].lower():
                print(tag['name'].lower())
                counter = tag['cont']
                counter += 1
                print(counter)
                print(col_tags.update_one({'_id': tag['_id']}, {"$inc": {'cont': 1}}).raw_result)


update_count()

write_excel('tag_name', col_tags)
