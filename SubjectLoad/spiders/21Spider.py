import scrapy

from SubjectLoad.SubjectItem import SubjectItem


class SubjectSpider(scrapy.Spider):
    name = "21cn"
    allowed_domains = ["21cnjy.com"]
    start_urls = [
        "https://zujuan.21cnjy.com/question?tree_type=category&xd=2&chid=3"
    ]

    def parse(self, response):
        for sel in response.xpath('//div[@class="QuestionView"]'):
            # print(sel.extract())
            item = SubjectItem()
            item['questionText'] = sel.xpath('//div[@class="q-tit"]/text()').extract_first()
            # item['questionLevel'] = sel.xpath('div/[class*="info left fl"]/span[2]').extract_first()
            # item['questionLevel'] = sel.xpath('div/[class*="info left fl"]/span[3]').extract_first()
            # #item.key = sel.css('attr(key)').extract()
            print(item)
            # #yield item
