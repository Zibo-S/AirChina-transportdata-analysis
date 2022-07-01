# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import os

class CaSpiderPipeline:
    def process_item(self, item, spider):
        df = item['df']
        path = r'CA_data.csv'
        file_exists = os.path.exists(path)
        df.to_csv(path,mode = 'a',encoding='utf-8')
        return item
