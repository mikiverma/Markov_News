import scrapy

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrape_news.items import SourceItem

class BloombergSpider(CrawlSpider):
    name = 'bloomberg'
    start_urls = ['https://www.bloomberg.com/politics',]

    allowed_domains = ['bloomberg.com', 'www.bloomberg.com']

    def process_url(self, response):
        src = SourceItem()
        src['sourceurl'] = response.url
        src['sourcename'] = self.name
        src['response_body'] = response.body
        yield src

    rules = (
        Rule(LinkExtractor(allow=('/politics/articles', '/news/articles')), callback='process_url', follow=True),
    )