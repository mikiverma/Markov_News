import scrapy

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrape_news.items import SourceItem

class FoxSpider(CrawlSpider):
    name = 'fox'
    start_urls = ['http://www.foxnews.com/politics.html',]

    allowed_domains = ['foxnews.com', 'www.foxnews.com']

    def process_url(self, response):
        src = SourceItem()
        src['sourceurl'] = response.url
        src['sourcename'] = self.name
        src['response_body'] = response.body
        yield src

    rules = (
        Rule(LinkExtractor(allow=('/politics',), deny=('/elections', '/interactive', '/playlist')), callback='process_url', follow=True),
    )