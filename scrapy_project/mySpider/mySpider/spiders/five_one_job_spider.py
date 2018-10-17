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
        node_list = response.xpath("//div[@id='resultList']/div[@class='el']")
        for node in node_list:
            item = MyspiderItem()
            # print(node.xpath("/p/span/a/text()"))
            item['positionName'] = node.xpath("./p/span/a/text()").extract_first(default="").strip()

            item['positionLink'] = node.xpath("./p/span/a/@href").extract_first(default="").strip()

            item['companyName'] = node.xpath("./span[1]/a/text()").extract_first(default="").strip()

            item['workLocation'] = node.xpath("./span[2]/text()").extract_first(default="").strip()

            item['salary'] = node.xpath("./span[3]/text()").extract_first(default="").strip()

            item['publishTime'] = node.xpath("./span[4]/text()").extract_first(default="").strip()

            yield item

            if self.offset < 20:
                self.offset += 1
                url = self.baseURL % (self.offset)
                yield scrapy.Request(url, callback=self.parse)

            # if len(response.xpath("//li[@class='bk'][2]/span/text()")) == 0:
            #     url = response.xpath("//li[@class='bk'][2]/a/@href").extract_first()
            #     yield scrapy.Request(url.split('?')[0], callback=self.parse)
