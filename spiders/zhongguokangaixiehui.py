import scrapy
from bs4 import BeautifulSoup
from SpiderMeet.items import MeetItem
from datetime import date
from datetime import datetime

class ZhongguokangaixiehuiSpider(scrapy.Spider):
    name = "zhongguokangaixiehui"
    # allowed_domains = ["www.caca.org.cn"]
    start_urls = ["http://www.caca.org.cn/xshy/hytz/"]

    def parse(self, response):
        current_datetime = datetime.now()
        formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
        print(f'\033[32m{formatted_datetime} 中国抗癌协会\033[0m')
        page_text = response.text
        soup = BeautifulSoup(page_text, 'lxml')
        table_li = soup.find('table', width='98%').find('table', width='100%').find_all('table', width='95%')
        item = MeetItem()
        for tr in table_li:
            try:
                title = tr.a.string
                url = tr.a['href']
                date_time = '20' + tr.find('td', width='8%').string.strip()
                item['title'] = title
                item['url'] = url
                item['date_time'] = date_time
                item['source'] = '中国抗癌协会'
                item['state'] = 0
                item['claw_date'] = date.today().strftime("%Y-%m-%d")
                yield item
            except Exception as e:
                print(f'\033[31m中国抗癌协会 数据采集异常: {e}\033[0m')
