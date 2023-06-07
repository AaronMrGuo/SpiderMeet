import scrapy
from datetime import date
from SpiderMeet.items import MeetItem
from datetime import datetime
from bs4 import BeautifulSoup


class ZhongguoyaoxuehuiSpider(scrapy.Spider):
    name = "zhongguoyaoxuehui"
    start_urls = ["http://www.cpa.org.cn/?do=infolist&classid=270"]

    def start_requests(self):
        # 发起第一页的请求
        current_datetime = datetime.now()
        formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
        print(f'\033[32m{formatted_datetime} 中国药学会\033[0m')
        yield scrapy.Request(url=self.start_urls[0], callback=self.parse)

    def parse(self, response):
        # 处理第一页的数据
        yield self.parse_page(response)

        # 获取总页数
        total_pages = 3

        # 生成分页请求
        for page in range(1, total_pages + 1):
            page_url = f"http://www.cpa.org.cn/?do=infolist&classid=270&page={page}"
            yield scrapy.Request(url=page_url, callback=self.parse_page)

    def parse_page(self, response):
        page_text = response.text
        soup = BeautifulSoup(page_text, 'lxml')
        li_li = soup.find('div', id='clist').find_all('li')[:-9]
        item = MeetItem()
        for li in li_li:
            try:
                title = li.a['title']
                title_url = 'http://www.cpa.org.cn/' + li.a['href']
                date_time = li.span.string.replace('/', '-')
                item['title'] = title
                item['url'] = title_url
                item['date_time'] = date_time
                item['source'] = '中国药学会'
                item['state'] = 0
                item['claw_date'] = date.today().strftime("%Y-%m-%d")
                yield item
            except Exception as e:
                print(f'\033[31m中国药学会 解析异常\033[0m{e}')
