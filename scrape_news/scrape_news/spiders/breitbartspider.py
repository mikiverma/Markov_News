import scrapy

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrape_news.items import SourceItem

class BreitbartSpider(CrawlSpider):
    name = 'breitbart'
    start_urls = ['http://www.breitbart.com/big-government/',]

    allowed_domains = ['breitbart.com', 'www.breitbart.com']

    def process_url(self, response):
        src = SourceItem()
        src['sourceurl'] = response.url
        src['sourcename'] = self.name
        src['response_body'] = response.body
        yield src

    rules = (
        Rule(LinkExtractor(allow=('/big-government',), deny=('/video',)), callback='process_url', follow=True),
    )