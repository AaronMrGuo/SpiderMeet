from bs4 import BeautifulSoup
import scrapy
from datetime import date
from ClawMeeting.items import MeetItem
from datetime import datetime

class XibaoshengwuxuexuehuiSpider(scrapy.Spider):
    name = "xibaoshengwuxuexuehui"
    # allowed_domains = ["www.cscb.org.cn"]
    start_urls = ["http://www.cscb.org.cn/conferencelist/35.html"]

    def KeyMeet(self, title):
        """
        验证是否为会议相关文章
        :param title: 文章标题
        :param date_time: 标题链接
        :return: 符合条件的文章标题和链接
        """
        meeting_key = ['研讨会', '培训班', '会议', '大会', '论坛', '交流会']
        # now = datetime.datetime.now().strftime('%Y-%m-%d')
        for key_word in meeting_key:
            if key_word in title:
                return title
            else:
                continue

    def parse(self, response):
        current_datetime = datetime.now()
        formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
        print(f'\033[32m{formatted_datetime} 中国细胞生物学学会\033[0m')
        page_text = response.text
        soup = BeautifulSoup(page_text, 'lxml')
        tr_li = soup.find('table',class_="table table-striped in_table").find_all('tr')[1:]
        item = MeetItem()
        for tr in tr_li:
            try:
                title = tr.a.string
                title_url = 'http://www.cscb.org.cn/' + tr.a['href']
                date_time = tr.find_all('td')[1].string.split('-')[0].replace('.', '-')
                title = self.KeyMeet(title)
                if title != None:
                    item['title'] = title
                    item['url'] = title_url
                    item['date_time'] = date_time
                    item['source'] = '中国细胞生物学学会'
                    item['state'] = 0
                    item['claw_date'] = date.today().strftime("%Y-%m-%d")
                    yield item
            except Exception as e:
                print(f'\033[31m中国细胞生物学学会 解析异常\033[0m{e}')

