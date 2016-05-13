from scrapy.spiders import Spider
from scrapy.selector import Selector

from dirbot.items import Website


class crawl(Spider):
    name = "crawl"
    allowed_domains = ["msbase.org"]
    start_urls = ['https://www.msbase.org/cms/benchmarking.json']

    def parse(self, response):
        sel = Selector(response)
        labels = sel.xpath('//tr[not(@*)]')
        items = []

        open('crawl_data.json', 'w').close()

        for data in labels:
            item = Website()
            item['description'] = data.xpath("td[1]/text()").extract()
            item['count'] = data.xpath('td[2]/text()').extract()
            item['percentage'] = data.xpath('td[3]/text()').extract()
            items.append(item)
        return items


