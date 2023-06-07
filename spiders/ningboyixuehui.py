import scrapy
from datetime import date
from SpiderMeet.items import MeetItem
from datetime import datetime
from bs4 import BeautifulSoup
from SpiderMeet.KeyMeet import KeyMeet


class NingboyixuehuiSpider(scrapy.Spider):
    name = "ningboyixuehui"
    # allowed_domains = ["www.nbygzx.org.cn"]
    start_urls = ["http://www.nbygzx.org.cn/col/col8277/index.html"]

    def parse(self, response):
        current_datetime = datetime.now()
        formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
        print(f'\033[32m{formatted_datetime} 宁波医学会\033[0m')
        page_text = response.text
        soup = BeautifulSoup(page_text, 'lxml')
        div_data = soup.find('div', id='15017')
        cdata = div_data.script.string
        cdata_soup = BeautifulSoup(cdata, 'html.parser')
        # 提取所有的<record>元素
        records = cdata_soup.find_all('record')
        item = MeetItem()
        for record in records:
            try:
                li = record.get_text(strip=True)
                title = BeautifulSoup(li, features="lxml").a['title']
                title_url = 'http://www.nbygzx.org.cn' + BeautifulSoup(li, features="lxml").a['href']
                date_time = BeautifulSoup(li, features="lxml").span.string
                title = KeyMeet(title)
                if title != None:
                    item['title'] = title
                    item['url'] = title_url
                    item['date_time'] = date_time
                    item['source'] = '宁波医学会'
                    item['state'] = 0
                    item['claw_date'] = date.today().strftime("%Y-%m-%d")
                    yield item
            except Exception as e:
                print(f'\033[31m宁波医学会 解析异常\033[0m{e}')
