from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
# from pariity.models import Website, Credentials
from scrapy import FormRequest, Request
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrape_news.items import SourceItem

# from pariity.parscrapy.items import SourceItem

class WSJScraper(CrawlSpider):
    name = 'wallstreet'
    # website = Website.objects.get(websitename=name)
    # credentials = Credentials.objects.get(credentialsid=website.credentialsid.credentialsid)
    username = '' #empty for commit
    password = '' #empty for commit
    allowed_domains = ['wsj.com', 'www.wsj.com']
    login_page = 'https://id.wsj.com/access/pages/wsj/us/signin.html'
    start_urls = [
        'https://www.wsj.com/news/politics',
    ]

    rules = (
        Rule(LinkExtractor(allow=('/articles',), deny=('/video',)), callback='process_url', follow=True),
    )

    def get_cookies(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(12)
        driver.get(self.login_page)
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys(str(self.username))
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys(str(self.password))
        driver.find_element_by_id("submitButton").click()
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME,'logged-in')))
        cookies = driver.get_cookies()
        print(cookies)
        return cookies

    def process_url(self, response):
        src = SourceItem()
        src['sourceurl'] = response.url
        src['sourcename'] = self.name
        src['response_body'] = response.body

        yield src

    def start_requests(self):
        self.cookies = self.get_cookies()
        # yield Request(
        #     url=self.start_urls[0],
        #     cookies = self.cookies
        # )
        return [Request(url=url, cookies=self.cookies) for url in self.start_urls]