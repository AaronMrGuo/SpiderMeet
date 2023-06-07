import scrapy
from bs4 import BeautifulSoup
from datetime import date
from SpiderMeet.items import MeetItem
from datetime import datetime
from SpiderMeet.KeyMeet import KeyMeet


class ZhongguokangfuyixuehuiSpider(scrapy.Spider):
    name = "zhongguokangfuyixuehui"
    # allowed_domains = ["www.carm.org.cn"]
    start_urls = ["http://www.carm.org.cn/col/col6705/index.html"]

    def parse(self, response):
        current_datetime = datetime.now()
        formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
        print(f'\033[32m{formatted_datetime} 中国康复医学会\033[0m')
        page_text = response.text
        soup = BeautifulSoup(page_text, 'lxml')
        cdata = soup.find('div', id='24942').script.string
        cdata_soup = BeautifulSoup(cdata, 'html.parser')
        c_data = cdata_soup.find_all('record')
        item = MeetItem()
        for record in c_data:
            try:
                li = record.get_text(strip=True)
                title = BeautifulSoup(li, features="lxml").a.string
                title_url = 'http://www.carm.org.cn' + BeautifulSoup(li, features="lxml").a['href']
                div_date = BeautifulSoup(li, features="lxml").find('div', class_='fl data').find_all('span')
                date_time = div_date[2].string + '-' + div_date[0].string
                title = KeyMeet(title)
                if title != None:
                    item['title'] = title
                    item['url'] = title_url
                    item['date_time'] = date_time
                    item['source'] = '中国康复医学会'
                    item['state'] = 0
                    item['claw_date'] = date.today().strftime("%Y-%m-%d")
                    yield item
            except Exception as e:
                print(f'\033[31中国康复医学会 解析异常\033[0m{e}')
