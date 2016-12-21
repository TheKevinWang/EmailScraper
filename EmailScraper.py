'''
A simple email scraper that will spider every webpage and extract emails using regex
Usage Example:
scrapy runspider EmailScraper.py -a url=http://example.com/ -o emails.json -L INFO
'''
import re
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class EmailSpider(CrawlSpider):
    name = 'EmailScraper'
    #keep track of previously seen emails to prevent duplication
    emailHistory = {}
    custom_settings = {
        'ROBOTSTXT_OBEY' : False
    #  ,'DEPTH_LIMIT' : 6
    }

    emailRegex = re.compile(("([a-zA-Z0-9_{|}~-]+(?:\.[a-zA-Z0-9_"
                         "{|}~-]+)*(@)(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9]){2,}?(\."
                        "))+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?)"))

    def __init__(self, url=None, *args, **kwargs):
        super(EmailSpider, self).__init__(*args, **kwargs)
        self.start_urls = [url]
        self.allowed_domains = [url.replace("http://","").replace("www.", "").replace("/","")]
    rules = (Rule (LinkExtractor(),callback="parse_item",follow=True),)
    def parse_item(self, response):
        item = {}
        emails = re.findall(EmailSpider.emailRegex, response._body);
        for email in emails:
            if email[0] in EmailSpider.emailHistory:
                    continue
            else:
                    EmailSpider.emailHistory[email[0]] = True;
                    yield {
                            'site':response.url,
                            'email':email[0]
                         }
