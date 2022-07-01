import random
import time
import scrapy
import pandas as pd
from ..items import CaSpiderItem

class AcSpider(scrapy.Spider):
    name = 'AC'
    allowed_domains = ['www.airchina.com.cn']
    start_urls = ['http://www.airchina.com.cn/www/jsp/airlines_operating_data/exlshow_en.jsp']

    def start_requests(self):
        for year in [2019,2020,2021,2022]:
            for i in range(1,13):
                if i < 10:
                    m = '0' + str(i)
                else:
                    m = str(i)
                url = r'http://www.airchina.com.cn/www/jsp/airlines_operating_data/exldateshow_en.jsp'
                headers = {
                    # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'Accept-Encoding': 'gzip, deflate',
                    'Accept-Language': 'zh,en;q=0.9,zh-CN;q=0.8',
                    # 'Cache-Control': 'max-age=0',
                    # 'Connection': 'keep-alive',
                    # 'Content-Length': '39',
                    'Content-Type': 'application/json',
                    'Host': 'www.airchina.com.cn',
                    'Cookie': 'JSESSIONID=D3CB5A67AA7B9DEA04CF1A13EA99A05F; acw_tc=700d411816566274682834240eef7fc37dabb68195afc0644f007e8529; BIGipServerWeb_http=1292508844.20480.0000; _gcl_au=1.1.614058500.1656627469; _ga=GA1.3.931239149.1656627469; _gid=GA1.3.894965958.1656627469; mbox=session#1656627468555-910499#1656630713|check#true#1656628913; _gat_UA-183091710-1=1; s_pers=%20s_fid%3D0BE50D41DEA1A0A9-031F19FD46AE50B1%7C1814395261655%3B; s_sess=%20s_cc%3Dtrue%3B%20s_sq%3Dacna-dom2-sc-prd%253D%252526c.%252526a.%252526activitymap.%252526page%25253Dcn%2525253Ainvestment%25252520relationship%2525253Aairlines%25252520business%25252520data%252526link%25253DSearch%252526region%25253DBODY%252526pageIDType%25253D1%252526.activitymap%252526.a%252526.c%252526pid%25253Dcn%2525253Ainvestment%25252520relationship%2525253Aairlines%25252520business%25252520data%252526pidt%25253D1%252526oid%25253DSearch%25252520%252526oidt%25253D3%252526ot%25253DSUBMIT%3B',
                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
                }
                data = {
                    'year1': str(year),
                    'month1': m,
                    'year': str(year),
                    'month': m
                }
                time.sleep(random.randint(1,5))
                yield  scrapy.FormRequest(url,formdata =data,callback=self.parse,dont_filter=True)

    def parse(self, response):
        item = CaSpiderItem()
        df = pd.read_html(response.text,header=0)[0]
        item['df'] = df
        yield item
