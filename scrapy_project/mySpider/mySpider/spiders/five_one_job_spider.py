import scrapy

from mySpider.items import MyspiderItem


class fiveOneJobSpider(scrapy.Spider):
    name = '51job'
    allowed_domains = ['51job.com']

    # just search Beijing python jobs
    baseURL = "https://search.51job.com/list/010000,000000,0000,00,9,99,python,2,%s.html"
    offset = 1
    start_urls = [baseURL % (offset)]

    def parse(self, response):
        node_list = response.xpath("//div[@class='el']")
        for node in node_list:
            item = MyspiderItem()
            item['positionName'] = node.xpath("./p/span/a/text()").extract()[0].encode("utf-8")
            item['postionLink'] = node.xpath("./p/span/a/@href").extract()[0].encode("utf-8")
            item['companyName'] = node.xpath("./span[class='t2']/a/text()").extract()[0].encode("utf-8")
            item['workLocation'] = node.xpath("./span[class='t3']/text()").extract()[0].encode("utf-8")
            if len(node.xpath("./span[class='t4']/text()")):
                item['salary'] = node.xpath("./span[class='t4']/text()").extract()[0].encode("utf-8")
            else:
                item['salary'] = ""

            item['publishTime'] = node.xpath("./span[class='t5']/text()").extract()[0].encode("utf-8")
            yield item

            if self.offset<126:
                self.offset+=1
                url=self.baseURL%(self.offset)
                yield scrapy.Request(url,callback=self.parse)

            if len(response.xpath("//li[@class='bk'][2]/span/text()"))==0:
                url=response.xpath("//li[@class='bk'][2]/a/@href").extract()[0]
                yield scrapy.Request(url.split('?')[0],self.parse)
