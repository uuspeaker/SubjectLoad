import scrapy
import re
import pymongo

from SubjectLoad.SubjectItem import SubjectItem


class SubjectSpider(scrapy.Spider):
    name = "test"
    allowed_domains = ["xkw.com"]
    parentId = '5119'
    start_urls = [
        "http://zujuan.xkw.com/czsx/zsd5119/qt1102o2/"
    ]
    myclient = pymongo.MongoClient('mongodb://129.211.21.250:27017/')
    subjectData = myclient["SubjectData"]
    xkwSubject = subjectData['xkw_subject']

    def parse(self, response):
        for sel in response.css('div[class*="quesbox question"]'):
            # print(sel.extract())
            item = SubjectItem()
            item['id'] = sel.xpath('div[1]/@id').extract_first()[7:15]
            item['key'] = sel.xpath('div[1]/@key').extract_first()
            questionContents = sel.xpath('div[1]/div/div/text() | div[1]/div/div/img/@src | div[1]/div/div/i/text()').extract()
            item['questionContent'] = self.parseContent(questionContents)
            item['options'] = sel.xpath('div[1]//table[@name="optionsTable"]//td/text() | div[1]//table[@name="optionsTable"]//td/img/@src').extract()
            item['knowledgeId'] = self.parentId
            item['knowledgeType'] = sel.xpath('div[1]/div[2]/span[1]/a[2]/@cname').extract_first()
            item['questionResource'] = sel.xpath('div[2]/span[1]/a[1]/@title').extract_first()
            item['updateDate'] = sel.xpath('div[3]/div[1]/span[1]/text()').extract_first()[5:20]
            item['questionLevel'] = sel.xpath('div[3]/div[1]/span[2]/text()').extract_first()[5:20]
            item['questionType'] = sel.xpath('div[3]/div[1]/span[3]/text()').extract_first()[3:20]
            useTimeStr = sel.xpath('div[3]/div[1]/span[4]/text()').extract_first()
            item['useTime'] = int(re.findall(r"\d+", useTimeStr)[0])
            item['answer'] = 'http://im.zujuan.xkw.com/Answer/' + item['id'] + '/2/843/14/28/' + item['key']
            item['parse'] = 'http://im.zujuan.xkw.com/Parse/' + item['id'] + '/2/843/14/28/' + item['key']
            print(item)
            self.saveItem(item)

    def parseContent(self, contents):
        resultContent = []
        tmpContent = ''
        for content in contents:
            if(re.match('http://static.zujuan.xkw.com', content, flags=0)):
                resultContent.append(tmpContent)
                resultContent.append(content)
                tmpContent = ''
            else:
                tmpContent += content

        if tmpContent != '':
            resultContent.append(tmpContent)

        return resultContent

    def saveItem(self, item):
        self.xkwSubject.insert_one(item)
        print('mongo 保存成功')
