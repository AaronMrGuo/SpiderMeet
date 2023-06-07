from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
# from scrapy.cmdline import execute


# 定义要执行的爬虫名列表
spiders = ['beijingjiankangcujin',
           'henanyixuewang',
           'ningboyixuehui',
           'rentijiankangkejicujinhui',
           'sichuanshengyixuehui',
           'youmaihuixun',
           'zhongguokangaixiehui',
           'zhongguokangfuyixuehui',
           'zhongguoyaoxuehui',
           'zhonguoshengwuyixue',
           'xibaoshengwuxuexuehui']

def run_spiders():
    settings = get_project_settings()
    settings['LOG_ENABLED'] = False

    crawler_process = CrawlerProcess(settings)

    for spider in spiders:
        crawler_process.crawl(spider)

    crawler_process.start()
    print('-' * 200)

# 定义定时任务
# schedule.every().day.at("02:28").do(run_spiders)
#
# while True:
#     schedule.run_pending()
#     time.sleep(1)

if __name__ == '__main__':
    run_spiders()






