# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from SpiderMeet.items import MeetItem
from SpiderMeet.MySQLConnector import Database
from scrapy.exceptions import DropItem

class SpidermeetPipeline:
    def process_item(self, item, spider):
        return item

class MeetPipeline:
    def __init__(self):
        self.db = Database(host='localhost', user='root', password='369369', database='meeting')

    def process_item(self, item, spider):
        if isinstance(item, MeetItem):
            source = item['source']
            date_time = item['date_time']
            title = item['title']
            url = item['url']
            state = item['state']
            claw_date = item['claw_date']
            query = "SELECT COUNT(*) FROM test_meet WHERE title='{}'".format(title)  # 检查是否存在相同标题的数据
            result = self.db.execute_query(query)
            if result[0][0] == 0:  # 如果不存在相同标题的数据
                columns = ['source', 'date_time', 'title', 'url', 'state', 'claw_date']
                values = (source, date_time, title, url, state, claw_date)
                placeholders = ', '.join(['%s'] * len(values))  # 使用占位符 %s
                query = "INSERT INTO test_meet ({}) VALUES ({})".format(', '.join(columns), placeholders)
                try:
                    self.db.execute_insert_query(query, values)
                    return item
                except Exception as e:
                    raise DropItem(f"Failed to process item: {e}")
            else:
                raise DropItem("Item already exists in the database")
        else:
            return item