import scrapy

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrape_news.items import SourceItem

class VoxSpider(CrawlSpider):
    name = 'vox'
    start_urls = ['http://www.vox.com/policy-and-politics',]

    allowed_domains = ['vox.com', 'www.vox.com']

    def process_url(self, response):
        src = SourceItem()
        src['sourceurl'] = response.url
        src['sourcename'] = self.name
        src['response_body'] = response.body
        yield src

    rules = (
        Rule(LinkExtractor(allow=('/policy-and-politics',), deny=None), callback='process_url', follow=True),
    )