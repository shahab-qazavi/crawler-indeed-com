# indeed

from pymongo import MongoClient
import requests
from bs4 import BeautifulSoup

con = MongoClient()
db = con['crawling_indeed']
col_crawl = db['crawling']


def crawling_indeed(what, where):
    x = 0
    y = 0

    next_page = "Next »"

    while next_page == "Next »":
        a = 0
        result = requests.get('https://www.indeed.com/jobs?q='+what+'&l='+where+'&start='+str(x))
        x += 10
        print(next_page)
        print(x)
        html = result.text
        parsed_html = BeautifulSoup(html, "html.parser")
        paragraph = parsed_html.select('.jobsearch-SerpJobCard')
        # print(paragraph)

        try:
            if len(parsed_html.select('div.pagination span.np'))>1:
                next_page = parsed_html.select('div.pagination span.np')[1].text
            else:
                next_page = parsed_html.select('div.pagination span.np')[0].text
        except IndexError:
            next_page = ""

        print(next_page)
        y += 1
        print('page '+str(y))
        for item in paragraph:
            url = 'https://www.indeed.com/'+item.select("div.title a")[0]['href']
            # print(url)

            title = item.select("div.title a")[0].text.strip()

            # print(title)
            company_name = ""
            if item.select('span.company a'):
                company_name = item.select('span.company a')[0].text.strip()

            salary = ""
            if item.select('div.salarySnippet'):
                salary = item.select('div.salarySnippet span.salary')[0].text.translate({ord("\n"): None}).strip()
                # print(salary)

            result = requests.get(url)
            html = result.text
            parsed_html = BeautifulSoup(html, "html.parser")
            a += 1
            contain_list = ""
            for items in parsed_html.select("div.jobsearch-JobComponent-description"):
                contain_list += "(" + (items.text.translate({ord("\n"): None})) + ") , "
            contain_dict = {
                'title': title,
                'url': url,
                'contain': contain_list,
                'salary': salary,
                'company name': company_name,
                'job title': what,
                'job location': where,
            }
            col_crawl.insert_one(contain_dict)
            print(a)


crawling_indeed('Python', 'manhattan')


