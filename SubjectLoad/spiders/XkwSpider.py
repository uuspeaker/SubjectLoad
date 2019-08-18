import scrapy

from SubjectLoad.SubjectItem import SubjectItem


class SubjectSpider(scrapy.Spider):
    name = "xkw"
    allowed_domains = ["xkw.com"]
    start_urls = [
        "http://zujuan.xkw.com/czsx/zsd4677/"
    ]

    def parse(self, response):
        for sel in response.css('div[class*="quesbox question"]'):
            # print(sel.extract())
            item = SubjectItem()
            item['id'] = sel.xpath('div[1]/@id').extract_first()
            item['key'] = sel.xpath('div[1]/@key').extract_first()
            item['questionText'] = sel.xpath('div[2]/span').extract()
            # item['questionLevel'] = sel.xpath('div/[class*="info left fl"]/span[2]').extract_first()
            # item['questionLevel'] = sel.xpath('div/[class*="info left fl"]/span[3]').extract_first()
            # #item.key = sel.css('attr(key)').extract()
            print(item)
            # #yield item
