import scrapy

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrape_news.items import SourceItem

class VoxSpider(CrawlSpider):
    name = 'natreview'
    start_urls = ['http://www.nationalreview.com/',]

    allowed_domains = ['nationalreview.com', 'www.nationalreview.com']

    def process_url(self, response):
        src = SourceItem()
        src['sourceurl'] = response.url
        src['sourcename'] = self.name
        src['response_body'] = response.body
        yield src

    rules = (
        Rule(LinkExtractor(allow=('/article',), deny=None), callback='process_url', follow=True),
    )