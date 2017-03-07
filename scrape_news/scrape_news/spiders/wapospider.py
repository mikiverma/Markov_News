import scrapy

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrape_news.items import SourceItem

class VoxSpider(CrawlSpider):
    name = 'wapo'
    start_urls = ['https://www.washingtonpost.com/politics/',]

    allowed_domains = ['washingtonpost.com', 'www.washingtonpost.com']

    def process_url(self, response):
        src = SourceItem()
        src['sourceurl'] = response.url
        src['sourcename'] = self.name
        src['response_body'] = response.body
        yield src

    rules = (
        Rule(LinkExtractor(allow=('/post-politics', '/politics'), deny=('/video',)), callback='process_url', follow=True),
    )