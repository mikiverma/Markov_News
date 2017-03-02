# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


from newspaper import Article as ArticleParse
from scrapy.exceptions import DropItem

# ContentExtractor.get_publishing_date.PUBLISH_DATE_TAGS.append({'attribute': 'name', 'value': 'article.published', 'content': 'content'})
class ExtractArticlePipeline(object):
    def __init__(self):
        self.aparse = ArticleParse

    def process_item(self, item, spider):
        try:
            a = self.aparse(item['sourceurl'], language='en')
            a.download(html=item['response_body']) #None if not explicitly set in Spider
            a.parse()
            item['response_body'] = a.text
            item['date'] = a.publish_date
            item['title'] = a.title
        except ValueError:
            raise DropItem('Unable to extract article from: ' + item['sourceurl'])

        return item
