import scrapy
from bs4 import BeautifulSoup
from SpiderMeet.items import MeetItem
from datetime import date
from datetime import datetime
from SpiderMeet.KeyMeet import KeyMeet




class BeijingjiankangcujinSpider(scrapy.Spider):
    name = "beijingjiankangcujin"
    # allowed_domains = ["www.chinahpa.org"]
    start_urls = ["http://www.chinahpa.org/index.php/Index/yixuehuodong.html"]

    def parse(self, response):
        current_datetime = datetime.now()
        formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
        print(f'\033[32m{formatted_datetime} 北京健康促进协会\033[0m')
        page_text = response.text
        soup = BeautifulSoup(page_text, 'lxml')
        li_li = soup.find('div', class_='list-5block').find_all('li')
        item = MeetItem()
        for li in li_li:
            try:
                title = li.h3.a.string
                url = 'http://www.chinahpa.org' + li.h3.a['href']
                date_time = li.find('p', class_='data').string.replace('月', '-').replace('年', '-').replace('日',
                                                                                                           '').strip()
                # print(title, url, date_time)
                if KeyMeet(title)!=None:
                    item['title'] = title
                    item['url'] = url
                    item['date_time'] = date_time
                    item['source'] = '北京健康促进协会'
                    item['state'] = 0
                    item['claw_date'] = date.today().strftime("%Y-%m-%d")
                    yield item
            except Exception as e:
                print(f'\033[31m北京健康促进协会 数据采集异常: {e}\033[0m')

