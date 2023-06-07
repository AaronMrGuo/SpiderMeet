import scrapy
from SpiderMeet.items import MeetItem
from datetime import datetime
import json
from fake_useragent import UserAgent


class HenanyixuewangSpider(scrapy.Spider):
    name = "henanyixuewang"
    start_urls = ["http://meeting.henanyixue.com/meet/api/meet/home"]

    def parse(self, response):
        ua = UserAgent()
        current_datetime = datetime.now()
        formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
        print(f'\033[32m{formatted_datetime} 河南医学网\033[0m')
        data = {
            "genre": "",
            "index": "1",
            "mold": "0,1",
            "month": "",
            "pageSize": "40",
            "subject": "",
            "title": "",
            "year": ""
        }
        headers = {
            "User-Agent": ua.random,
            "X-Requested-With": "XMLHttpRequest",
            "Content-Type": 'application/json'
        }
        yield scrapy.Request(
            url=r'http://meeting.henanyixue.com/meet/api/meet/home',
            method='POST',
            headers=headers,
            body=json.dumps(data),
            callback=self.parse_page
        )

    def parse_page(self, response):
        if response.status == 200:
            result_data = json.loads(response.text)
            yield from self.process_data(result_data['data'])
        else:
            self.logger.error(f"\033[31m请求失败，状态码: {response.status}\033[0m")

    def process_data(self, data):
        item = MeetItem()
        for item_data in data:
            title = item_data['title']
            title_url = 'https://meeting.henanyixue.com/web.html#/schedule?meet={}&mold=0'.format(item_data['meet'])
            date_time = item_data['start'][:10]
            item['title'] = title
            item['url'] = title_url
            item['date_time'] = date_time
            item['source'] = '河南医学网'
            item['state'] = 0
            item['claw_date'] = datetime.now().strftime("%Y-%m-%d")
            yield item
