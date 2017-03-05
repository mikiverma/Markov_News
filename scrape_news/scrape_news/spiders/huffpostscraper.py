import scrapy

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrape_news.items import SourceItem

class BloombergSpider(CrawlSpider):
    name = 'huffpost'
    start_urls = ['http://www.huffingtonpost.com/section/politics',]

    allowed_domains = ['huffingtonpost.com', 'www.huffingtonpost.com']

    def process_url(self, response):
        src = SourceItem()
        src['sourceurl'] = response.url
        src['sourcename'] = self.name
        src['response_body'] = response.body
        yield src

    rules = (
        Rule(LinkExtractor(allow=('/entry', '/topic')), callback='process_url', follow=True),
    )