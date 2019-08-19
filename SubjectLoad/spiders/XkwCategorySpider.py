import scrapy

from SubjectLoad.SubjectItem import SubjectItem


class SubjectSpider(scrapy.Spider):
    name = "xkw1"
    allowed_domains = ["xkw.com"]
    beginUrl = "http://zujuan.xkw.com/Web/Handler1.ashx?action=categorytree&iszsd=1&isinit=1&parentid="
    childId = "4677"
    categoryAll = [4677]
    categoryLast = []
    start_urls = [
        beginUrl + childId
    ]
    total = 1

    def parse(self, response):
        parentid = str(response.url).strip().split("parentid=")[-1]
        # print("===================", str(response.url), parentid)
        childs = response.xpath('//@id').extract()
        # print('childs', childs)

        self.categoryAll += childs

        if len(childs) == 0:
            # parentid = response.meta['parentid']
            self.categoryLast.append(parentid)
            return

        for child in childs:
            # print('parent', child)
            yield scrapy.Request(url=self.beginUrl + child, meta={'parentid': child}, callback=self.parse)

    def closed(self, reason) :
        print('categoryAll', self.categoryAll)
        print('categoryLast', self.categoryLast)
        return

