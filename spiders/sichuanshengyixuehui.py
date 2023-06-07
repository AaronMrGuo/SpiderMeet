from bs4 import BeautifulSoup
import scrapy
from datetime import date
from SpiderMeet.items import MeetItem
from datetime import datetime


class SichuanshengyixuehuiSpider(scrapy.Spider):
    name = "sichuanshengyixuehui"
    # allowed_domains = ["ent2006615ent2006615ent2006615www.sma.org.cn"]
    start_urls = ["http://ent2006615ent2006615ent2006615www.sma.org.cn/main/xshd.asp"]

    def parse(self, response):
        current_datetime = datetime.now()
        formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
        print(f'\033[32m{formatted_datetime} 四川省医学会\033[0m')
        page_text = response.text
        soup = BeautifulSoup(page_text, 'lxml')
        tr_li = soup.find_all('tr')[4:23]
        item = MeetItem()
        for tr in tr_li:
            try:
                title = tr.find_all('font')[0].a['title']
                title_url = 'http://ent2006615ent2006615ent2006615www.sma.org.cn/main/' + tr.find_all('font')[0].a[
                    'href']
                date_time = tr.find_all('font')[1].string
                item['title'] = title
                item['url'] = title_url
                item['date_time'] = date_time
                item['source'] = '四川省医学会'
                item['state'] = 0
                item['claw_date'] = date.today().strftime("%Y-%m-%d")
                yield item
            except Exception as e:
                print(f'\033[31m四川省医学会 解析异常\033[0m{e}')
