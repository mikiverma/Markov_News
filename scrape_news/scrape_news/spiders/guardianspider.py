import scrapy

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrape_news.items import SourceItem

class VoxSpider(CrawlSpider):
    name = 'guardian'
    start_urls = ['https://www.theguardian.com/us-news/us-politics',]

    allowed_domains = ['theguardian.com', 'www.theguardian.com']

    def process_url(self, response):
        src = SourceItem()
        src['sourceurl'] = response.url
        src['sourcename'] = self.name
        src['response_body'] = response.body
        yield src

    rules = (
        Rule(LinkExtractor(allow=('/us-news',), deny=None), callback='process_url', follow=True),
    )