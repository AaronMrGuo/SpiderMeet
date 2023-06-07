from datetime import date
import scrapy
from bs4 import BeautifulSoup
from SpiderMeet.items import MeetItem
from datetime import datetime
from SpiderMeet.KeyMeet import KeyMeet


class ZhonguoshengwuyixueSpider(scrapy.Spider):
    name = "zhonguoshengwuyixue"
    # allowed_domains = ["www.csbme.org"]
    start_urls = ["http://www.csbme.org/meeting/index.htm"]

    def parse(self, response):
        current_datetime = datetime.now()
        formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
        print(f'\033[32m{formatted_datetime} 中国生物医学工程学会\033[0m')
        soup = BeautifulSoup(response.text, 'lxml')
        li_li = soup.find('ul', class_='commcontent').find_all('li')
        item = MeetItem()
        for li in li_li:
            try:
                title = li.a['title']
                title_url = li.a['href']
                date_time = li.span.string
                title = KeyMeet(title)
                if title!= None:
                    item['title'] = title
                    item['url'] = title_url
                    item['date_time'] = date_time
                    item['source'] = '中国生物医学工程学会'
                    item['state'] = 0
                    item['claw_date'] = date.today().strftime("%Y-%m-%d")
                    yield item
            except Exception as e:
                print(f'\033[31m中国生物医学工程学会 解析异常\033[0m{e}')
