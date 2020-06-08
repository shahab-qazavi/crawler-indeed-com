# crawler-indeed-com
Crawler function with Python looking for a job in www.indeed.com using BeautifulSoup.

Requirement libraries :

pymongo , requests , bs4 , openpyxl , collections.

This function in crawling_web_page.py file given tow arguments, one for a job title(Like Python) and one for the location(Manhattan, for example),
 and crawling in www.indeed.com and saves all the results found in the MongoDB on a regular basis.
 
Which has useful fields such as : Title , Url , Contain , Salary , Company Name , Job Title and Job Location.

And other scripts in create_report_in_excel folder creating some useful report in excel.
