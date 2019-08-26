import scrapy
import pymongo
from SubjectLoad.SubjectItem import SubjectItem


class SubjectSpider2(scrapy.Spider):
    name = "xkw-tree"
    allowed_domains = ["xkw.com"]
    beginUrl = "http://zujuan.xkw.com/Web/Handler1.ashx?action=categorytree&iszsd=1&isinit=1&parentid="
    childId = "4677"
    categoryAll = [4677]
    categoryLast = []
    start_urls = [
        beginUrl + childId
    ]
    total = 1
    myclient = pymongo.MongoClient('mongodb://129.211.21.250:27017/')
    subjectDB = myclient["SubjectData"]
    categoryTree = subjectDB["CategoryTree"]
    categoryTree.delete_many({})
    categoryTree.insert_one({'id': 4677, 'lable': '初中数学'})

    def parse(self, response):
        parentId = str(response.url).strip().split("parentid=")[-1]
        print("===================", str(response.url), parentId)
        childIds = response.xpath('//@id').extract()
        childTitles = response.xpath('//a/@title').extract()
        # print('childs', childIds, childTitles)
        self.fillTree(parentId, childIds, childTitles)
        #self.categoryAll += childs

        if len(childIds) == 0:
            myquery = {"id": parentId}
            newvalues = {"$set": {"isLeaf": 'leaf'}}
            self.categoryTree.update_one(myquery, newvalues)
        else:
            myquery = {"id": parentId}
            newvalues = {"$set": {"isLeaf": 'node'}}
            self.categoryTree.update_one(myquery, newvalues)

        for child in childIds:
            # print('parent', child)
            yield scrapy.Request(url=self.beginUrl + child, meta={'parentId': child}, callback=self.parse)

    def closed(self, reason):
        #print('categoryAll', self.categoryAll)
        #print('categoryLast', self.categoryLast)
        return

    def fillTree(self, parentId, childIds, childTitles):
        index = 0
        for child in childIds:
            children = {'id': childIds[index], 'lable': childTitles[index], 'parentId': parentId}
            print('children',children)
            self.categoryTree.insert_one(children)
            index = index + 1


