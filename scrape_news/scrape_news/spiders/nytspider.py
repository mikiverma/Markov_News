import scrapy

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrape_news.items import SourceItem

class NYTSpider(CrawlSpider):
    name = 'nyt'
    start_urls = ['https://www.nytimes.com/pages/politics/index.html',]

    allowed_domains = ['nytimes.com', 'www.nytimes.com']

    def process_url(self, response):
        src = SourceItem()
        src['sourceurl'] = response.url
        src['sourcename'] = self.name
        src['response_body'] = response.body
        yield src

    rules = (
        Rule(LinkExtractor(allow=('/us/politics', '\?ref=politics$'), deny=('/video', '/interactive')), callback='process_url', follow=True),
    )