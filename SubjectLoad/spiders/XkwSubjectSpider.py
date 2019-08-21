import scrapy
import re
import pymongo
import time
import random

from SubjectLoad.SubjectItem import SubjectItem


class SubjectSpider(scrapy.Spider):
    name = "xkw2"
    allowed_domains = ["xkw.com"]
    index = 1
    # parentIds = ['4685', '6041']
    firtPart = "http://zujuan.xkw.com/czsx/zsd"
    thirdPart = "/o2p"
    parentId = '6042'
    parentIndex = -1
    currentPage = 1
    pageIndex = 1
    proxy = ''
    start_urls = [
        'https://www.21cnjy.com'
    ]
    # file = open('subject.json', mode='wb')
    downLoadCount = 0
    myclient = pymongo.MongoClient('mongodb://129.211.21.250:27017/')
    subjectDB = myclient["SubjectData"]
    xkwSubject = subjectDB['XkwSubject']
    downloadResult = subjectDB['DownloadResult']
    downloadLog = subjectDB['DownloadLog']

    parentIds = ['6042', '6041', '5119', '5118', '5117', '4685', '5093', '5088', '5087', '5249', '5080', '5004', '5002', '5003','5001', '5092', '5094', '4962', '5101', '5100', '5098', '5199', '5162', '4982', '4980', '5102', '4979', '5099', '5194', '5193', '5192', '5190', '5189', '5188', '4972', '4984', '4983', '4971', '4970', '4969', '4976', '4975', '4974', '4978', '5195', '4968', '4964', '5116', '5115', '4967', '4966', '5157', '5191', '5105', '5174', '5173', '5172', '5171', '5164', '4977', '5170', '5185', '5184', '5246', '5228', '5207', '5206', '5163', '5245', '5244', '5238', '5237', '5226', '5222', '5217', '5216', '5210', '5186', '5235', '5168', '5167', '5166', '5165', '5234', '5224', '5223', '5233', '5232', '5243', '6038', '6037', '5230', '5208', '5214', '5209', '5213', '5231', '5212', '5221', '5220', '5219', '5218', '5225', '5236', '5211', '5215', '5241', '5240', '5183', '5169', '5179', '5178', '5177', '5187', '5175', '5242', '5239', '5104', '5103', '5248', '5176', '5017', '6039', '5016', '5014', '5013', '5012', '5011',
     '5010', '5009', '5008', '5006', '5015', '5078', '5077', '5076', '5075', '5007', '5073', '5005', '5079', '5074','5255', '6035',
     '4906', '4905', '5270', '5994', '5993', '5992', '5962', '5072', '4724', '4716', '5071', '4709', '4708', '4707','4787', '4715', '5989', '4712', '4711', '4799', '4798', '6040', '4722', '4796', '4710', '5988', '5874', '5873','4794',
     '4793', '5902', '5900', '5891', '4797', '4745', '5887', '5901', '4763', '4738', '5889', '4764', '5921', '4736',
     '4761', '5917', '4760', '4759', '4795', '5894', '4767', '5919', '4728', '4766', '4741', '4739', '5869', '5912',
     '5910', '5254', '5909', '5897', '5896', '5895', '4740', '4753', '4735', '4734', '4758', '4751', '4757', '5914', '5913', '4765', '4752', '4714', '4713', '4754', '4732', '4731', '5915', '5886', '5885', '5884', '4720', '5883', '5877', '5876', '5881', '4719', '4717', '4723', '4721', '5960', '5970', '5880', '5878', '4792', '5965', '5906', '5984', '5983', '5982', '5987', '4718', '5980', '5978', '4733', '5961', '5790', '5843', '5788', '5791', '5850', '5822', '5825', '5808', '5807', '5801', '5800', '5794', '5804', '5797', '5819', '5818', '5817', '5799', '5806', '5805', '5849', '5853', '5847', '5795', '5796', '5826', '5821', '4755', '5846', '5809', '5985', '5827', '5986', '5816', '5814', '5845', '5844', '5815', '5963', '4789', '5858', '5857', '5856', '4790', '5774', '5759', '4788', '5836', '5835', '5834', '5908', '5833', '5832', '5831', '5757', '5754', '4791', '5773', '5772', '5838', '5767', '5755', '5855', '5854', '5839', '5761', '5760', '5785', '5782', '5860', '5859', '5781', '5841', '6031', '6029', '5861', '5998', '5780', '5777', '5776', '5999', '5784', '5997', '5269', '5775', '5964', '4904', '4903', '4705', '4701', '5976', '4702', '4830', '4829', '4703', '5765', '5763', '5762', '4862', '5764', '4851', '4850', '4849', '4848', '4860', '4825', '4824', '4886', '4890',
     '5995', '4885', '4897', '4896', '4856', '4878', '4877', '5771', '4884', '5977', '4883', '4882', '4863', '4881',
     '4880', '4879',
     '4871', '4823', '5996', '4828', '4844', '4843', '4870', '4869', '4872', '4874', '4873', '4868', '4866', '4875',
     '4818', '4839', '4838', '4837', '4836', '4835', '4822', '4821', '4876', '4817', '4846', '4867', '5975', '5974',
     '4842',
     '4820', '4700', '4895', '4847', '4893', '4819', '4900', '4892', '4891', '4831', '4899', '4778', '4775', '4894',
     '4912', '4911', '4864', '4909', '4779', '4785', '4784', '4783', '4782', '4865', '4774', '4944', '4832', '5939',
     '6026', '6025', '6023', '4958', '6022', '6021', '4781', '6020', '5940', '4910', '4957', '5931', '5930', '5928', '4923', '4922', '5937', '4921', '5956', '5955', '5933', '5950', '5947', '5945', '5941', '4902', '5944', '5948', '5949', '5954', '5946', '5952', '4920', '4780', '4943', '5957', '5943', '4942', '4941', '4940', '4939', '5953', '4907', '4931', '4930', '4924', '4928', '4927', '4950', '4949', '4948', '4947', '4946', '5263', '4908', '5951', '5261', '5267', '4956', '4955', '5268', '4929', '4954', '4951', '5265', '5264', '4917', '4953', '4952', '6005', '5106', '5262', '6019', '6018', '6016', '6015', '6010', '5114', '5936', '4936', '4935', '5095', '4934', '4933', '4932', '5260', '5113', '5258', '5744', '5740', '5257', '5256', '5706', '5705', '6007', '6014', '5704', '5725', '5724', '5266', '5112', '5110', '5109', '5669', '5668', '5666', '5710', '5709', '5111', '5741', '5730', '5728', '5707', '5655', '5708', '5737', '5729', '5736', '5651', '5697', '5696', '5650', '5654', '5700', '5652', '5533', '5632', '5699', '5630', '5648', '5538', '5646', '5633', '5572', '5564', '5559', '5624', '5731', '5623', '5622', '5620', '5567', '5547', '5546', '5545', '5733', '5566'
        , '5653', '5641', '5551', '5558', '5701', '5548', '5560', '5571', '5702', '5570', '5569', '5640', '5639',
     '5638', '5637', '5644', '5552', '5643', '5647', '5645', '5259', '5557', '5540', '5539', '5619', '5612', '5605',
     '5604', '5596',
     '5544', '5593', '5592', '5591', '5590', '5695', '5694', '5693', '5692', '5588', '5550', '5690', '5602', '5600',
     '5598', '5691', '5601', '5587', '5586', '5611', '5584', '5543', '5595', '5574', '5603', '5597', '5585', '5608',
     '5607',
     '5594', '5615', '5614', '5599', '5613', '5618', '5609', '5616', '5663', '5662', '5659', '5642', '5606', '5020',
     '5679', '5610', '5671', '5670', '4998', '5689', '5686', '5683', '5682', '5681', '5024', '5054', '5023', '5677',
     '5052', '5051', '5676', '5049', '5050', '5346', '5342', '5617', '5374', '5371', '5369', '5389', '5382', '5381', '5375', '5027', '5026', '5387', '5385', '5384', '5383', '5386', '5367', '5370', '5373', '5372', '5388', '5028', '5368', '5356', '5561', '5353', '5350', '5345', '5344', '5343', '5035', '5034', '5363', '5362', '5033', '5360', '5477', '5352', '5380', '5359', '5048', '5047', '5420', '5419', '5474', '5528', '5431', '5444', '5341', '5403', '5470', '5469', '5468', '5467', '5432', '5496', '5495', '5435', '5494', '5458', '5397', '5415', '5414', '5463', '5462', '5523', '5519', '5413', '5406', '5433', '5481', '5480', '5412', '5456', '5482', '5410', '5405', '5404', '5408', '5411', '5046', '5409', '5492', '5491', '5454', '5489', '5518', '5488', '5490', '5455', '5457', '5484', '5483', '5487', '5486', '5416', '5514', '5493', '5516', '5439', '5417', '5512', '5511', '5510', '5509', '5508', '5506', '5505', '5504', '5503', '5502', '5501', '5513', '5449', '5517', '5445', '5485', '5451', '5527', '5526', '5524', '5473', '5472', '5450', '5448', '5357', '5471', '5045', '5044', '5358', '5041', '5453', '5459', '5040', '5321', '5031', '5324', '5340', '5339', '5338', '5337'
        , '5030', '5336', '5424', '5332', '5042', '5330', '5329', '5029', '5043', '5423', '5422', '5328', '5421',
     '5053', '4996', '5039', '5038', '5333', '5675', '5335', '4997', '5082', '5081', '5425', '5674', '5309', '5283',
     '5060', '5059',
     '5058', '5147', '5447', '5308', '5067', '5086', '5299', '5298', '5295', '5294', '5289', '5288', '5287', '5068',
     '5141', '5140', '5139', '5286', '5085', '5300', '5292', '5290', '5293', '5065', '5291', '5063', '5062', '5061',
     '5066',
     '5143', '5142', '5307', '5305', '5070', '5144', '5069', '5303', '5153', '5152', '5151', '5150', '5132', '5319',
     '5318', '5285', '5131', '5304', '5149', '5148', '5130', '5137', '5135', '5316', '5133', '5314', '5313', '5136',
     '5311', '5310', '5000', '5315', '5138', '4999', '5673', '5334']


    def parse(self, response):
        self.proxy = self.get_random_proxy()
        print('获取代理服务器',self.proxy)
        subjects = response.css('div[class*="quesbox question"]')
        print('题目长度为', len(subjects))
        #如果页面没有找到题目,则跳到下一个节点开始解析
        if len(subjects) == 0:
            print('未找到任何题目', subjects)
            # self.gotoNextParentId()
            print('进入下一个节点')
            self.parentIndex += 1
            self.parentId = self.parentIds[self.parentIndex]
            nextPage = 1
            url = self.firtPart + self.parentId + self.thirdPart + str(nextPage)
            yield scrapy.Request(url=url, callback=self.parse, meta={'dont_redirect': True,'handle_httpstatus_list': [301, 302]})
        else:
            #若有找到题目,则抽取题目并保存
            self.parseData(response)

            maxPage = self.getMaxPage(response)
            #若已经是最后一页,且已经是最后一个节点,则结束
            if maxPage <= self.currentPage and self.parentIndex + 1 >= len(self.parentIds):
                print('处理完所有节点')
                return
            # 若还不是最后一页,则继续下载
            if maxPage > self.currentPage:
                nextPage = self.currentPage + 1
                url = self.firtPart + self.parentId + self.thirdPart + str(nextPage)
                yield scrapy.Request(url=url, callback=self.parse, meta={'dont_redirect': True,'handle_httpstatus_list': [301, 302]})
            #若是最后一页但还不是最后节点, 则开始解析下一个节点
            if maxPage <= self.currentPage and self.parentIndex + 1 < len(self.parentIds):
                # self.gotoNextParentId()
                print('进入下一个节点')
                self.parentIndex += 1
                self.parentId = self.parentIds[self.parentIndex]
                nextPage = 1
                url = self.firtPart + self.parentId + self.thirdPart + str(nextPage)
                yield scrapy.Request(url=url, callback=self.parse, meta={'dont_redirect': True, 'handle_httpstatus_list': [301, 302]})

    def gotoNextParentId(self):
        print('进入下一个节点')
        self.parentIndex += 1
        self.parentId = self.parentIds[self.parentIndex]
        nextPage = 1
        url = self.firtPart + self.parentId + self.thirdPart + str(nextPage)
        yield scrapy.Request(url=url, callback=self.parse)

    def getCurrentPage(self, response):
        currentPage = int(response.xpath('//input[@id="iptGotoNum"]/@value').extract_first())
        return currentPage

    def getMaxPage(self, response):
        maxPageNode = response.xpath('//div[@class="page"]/span/text()').extract_first()
        maxPage = int(re.findall(r"\d+", maxPageNode)[0])
        return maxPage

    def parseData(self, response):
        currentPage = self.getCurrentPage(response)
        maxPage = self.getMaxPage(response)
        print(response.url, maxPage, currentPage)

        downloadParentData = self.downloadResult.find_one({'parentId': self.parentId})
        print('历史下载记录为', downloadParentData)
        # 若查询的页面已经下载过,则不保存且直接跳到已经下载的页码
        if downloadParentData is not None:
            if currentPage <= downloadParentData['currentPage']:
                print('跳过已下载页面', currentPage)
                self.currentPage = downloadParentData['currentPage']
                return
            else:
                self.currentPage = currentPage
                self.saveData(response)
        else:
            self.currentPage = currentPage
            self.saveData(response)

        # 保存下载记录
        # 若不存在下载记录则新增
        if downloadParentData is not None:
            # 若已经有下载记录则更新
            print('更新下载结果', self.currentPage)
            self.downloadResult.update({'parentId': self.parentId}, {"$set": {'currentPage': self.currentPage}})
        else:
            print('新增下载结果', self.currentPage)
            self.downloadResult.insert_one({
                'parentId': self.parentId,
                'maxPage': maxPage,
                'currentPage': currentPage
            })

    def saveData(self, response):
        print('开始保存数据',self.currentPage)
        self.downLoadCount += 1
        for sel in response.css('div[class*="quesbox question"]'):
            # print(sel.extract())
            item = SubjectItem()
            item['id'] = sel.xpath('div[1]/@id').extract_first()[7:15]
            item['key'] = sel.xpath('div[1]/@key').extract_first()
            question_contents = sel.xpath('div[1]/div/div/text() | div[1]/div/div/img/@src | div[1]/div/div/i/text()').extract()
            item['questionContent'] = self.parseContent(question_contents)
            item['options'] = sel.xpath(
                'div[1]//table[@name="optionsTable"]//td/text() | div[1]//table[@name="optionsTable"]//td/img/@src').extract()
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
            # print(item)
            self.xkwSubject.insert_one(item)

    def parseContent(self, contents):
        resultContent = []
        tmpContent = ''
        for content in contents:
            if (re.match('http://static.zujuan.xkw.com', content, flags=0)):
                resultContent.append(tmpContent)
                resultContent.append(content)
                tmpContent = ''
            else:
                tmpContent += content

        if tmpContent != '':
            resultContent.append(tmpContent)

        return resultContent

    def closed(self, reason):
        print('本次下载', self.downLoadCount, '页')
        self.downloadLog.insert_one({
            'date': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
            'info': '本次下载' + str(self.downLoadCount) + '页'
        })
        self.myclient.close()
        self.myclient = ''
        return

    def get_random_proxy(self):
        while 1:
            # with open('D:/program/vue/SubjectLoad/SubjectLoad\spiders/proxies.txt', 'r') as f:
            with open('SubjectLoad/util/proxies.txt', 'r') as f:
                proxies = f.readlines()
            if proxies:
                break
            else:
                time.sleep(1)
        proxy = random.choice(proxies).strip()
        return proxy




