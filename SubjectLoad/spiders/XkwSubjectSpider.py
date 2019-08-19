import scrapy

from SubjectLoad.SubjectItem import SubjectItem


class SubjectSpider(scrapy.Spider):
    name = "xkw2"
    allowed_domains = ["xkw.com"]
    start_urls = [
        "http://zujuan.xkw.com/czsx/zsd4677/"
    ]

    def parse(self, response):
        for sel in response.css('div[class*="quesbox question"]'):
            # print(sel.extract())
            item = SubjectItem()
            item['id'] = sel.xpath('div[1]/@id').extract_first()[7:15]
            item['key'] = sel.xpath('div[1]/@key').extract_first()
            item['questionText'] = sel.xpath('div[1]/div/div/text() | div[1]/div/div/img/@src').extract()
            item['knowledgeType'] = sel.xpath('div[1]/div[2]/span[1]/a[2]/@cname').extract()
            item['questionResource'] = sel.xpath('div[2]/span[1]/a[1]/@title').extract()
            item['questionLevel'] = sel.xpath('div[3]/div[1]/span[2]/text()').extract()
            item['answer'] = 'http://im.zujuan.xkw.com/Answer/' + item['id'] + '/2/843/14/28/' + item['key']
            item['parse'] = 'http://im.zujuan.xkw.com/Parse/' + item['id'] + '/2/843/14/28/' + item['key']
            # item['questionLevel'] = sel.xpath('div/[class*="info left fl"]/span[3]').extract_first()
            # #item.key = sel.css('attr(key)').extract()
            print(item)
            # #yield item

    def getText(self, textArry):
        texts = []
        for text in  textArry:
            texts.append(text.nodeValue)
        return texts