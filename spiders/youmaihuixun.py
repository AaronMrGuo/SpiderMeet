import scrapy
from bs4 import BeautifulSoup
from datetime import date
from SpiderMeet.items import MeetItem
from datetime import datetime


class youmaihuixunSpider(scrapy.Spider):
    name = 'youmaihuixun'
    start_urls = ['http://wechat.umer.com.cn/meeting/main/index']

    def parse(self, response):
        current_datetime = datetime.now()
        formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
        print(f'\033[32m{formatted_datetime} 优麦会讯\033[0m')
        soup = BeautifulSoup(response.text, 'lxml')
        li_li = soup.find('ul').find_all('li')
        for li in li_li:
            try:
                data_id = li.find('div')['data-id']
                month_url = 'http://wechat.umer.com.cn/meeting/meeting/meetingList?id={}&sn='.format(data_id) + \
                            li.find('div')['data-sn']
                yield scrapy.Request(url=month_url, callback=self.parse_details)
            except Exception as e:
                print(e)

    def parse_details(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        art_li = soup.find_all('article')
        item = MeetItem()
        for art in art_li:
            try:
                title = art.h2.string.strip()
                title_url = art['ng-click'].replace("link('", '').replace("')", '')
                date_time = art['id']
                item['title'] = title
                item['url'] = title_url
                item['date_time'] = date_time
                item['source'] = '优麦会讯'
                item['state'] = 0
                item['claw_date'] = date.today().strftime("%Y-%m-%d")
                yield item
            except Exception as e:
                print(f'\033[31m优麦会讯 数据采集异常: {e}\033[0m')
