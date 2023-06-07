import scrapy
from datetime import date
from SpiderMeet.items import MeetItem
from datetime import datetime



class RentijiankangkejicujinhuiSpider(scrapy.Spider):
    name = "rentijiankangkejicujinhui"
    # allowed_domains = ["www.chstpa.cn"]
    start_urls = ["http://www.chstpa.cn/chstpa/article/getArticleListsByF?navigateId=17&pageNo=1&pageNum=60"]

    def parse(self, response):
        current_datetime = datetime.now()
        formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
        print(f'\033[32m{formatted_datetime} 人体健康科技促进会\033[0m')
        result_data = response.json()['data']['data']
        item = MeetItem()
        for data in result_data:
            if '招商函' not in data['title'] and '邀请函' not in data['title']:
                title = data['title']
                title_url = 'http://www.chstpa.com.cn/partyConstruction/list/detail?id={}'.format(data['id'])
                date_time = datetime.fromtimestamp(data['createTime']/1000).strftime('%Y-%m-%d')
                item['title'] = title
                item['url'] = title_url
                item['date_time'] = date_time
                item['source'] = '人体健康科技促进会'
                item['state'] = 0
                item['claw_date'] = date.today().strftime("%Y-%m-%d")
                yield item

