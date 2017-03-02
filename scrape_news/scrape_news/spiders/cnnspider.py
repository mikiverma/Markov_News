import scrapy

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrape_news.items import SourceItem

class CNNSpider(CrawlSpider):
    name = 'cnn'
    start_urls = ['http://edition.cnn.com/politics',]

    allowed_domains = ['edition.cnn.com', 'cnn.com', 'www.cnn.com']

    def process_url(self, response):
        src = SourceItem()
        src['sourceurl'] = response.url
        src['sourcename'] = self.name
        src['response_body'] = response.body
        yield src

    rules = (
        Rule(LinkExtractor(allow=('/politics',), deny=('interactive','/videos',)), callback='process_url', follow=True),
    )

