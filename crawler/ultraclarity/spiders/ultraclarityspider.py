# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider
from scrapy.selector    import Selector 
from ultraclarity.items import UltraclarityItem
from scrapy.http    import Request
from datetime import datetime

# Function that returns the number of pages that the spider must crawl
# based on the form results of yperdiavgeia.gr
def pages(number):
    if number % 10 > 0:
        return number / 10 + 1;
    else:
        return number / 10;

# Current year to download files when no arguments are used
current_year = datetime.now().year

# We create our Spider (by overriding CrawlSpider)
class UltraclaritySpider(CrawlSpider):
    # Crawler name
    name = "ultraclarity"

    # List of strings containing domains that spider is allowed to crawl
    allowed_domains = ["yperdiavgeia.gr", "et.gr"]

    # Spider constructor
    # Start_urls : List of urls that the spider should start to crawl from
    # If no arguments are given current year will be used
    def __init__(self, year=str(current_year)+','+str(current_year), *args, **kwargs):
        super(UltraclaritySpider, self).__init__(*args, **kwargs)
        self.start_urls = []
        # If user has given only one argument
        if len(year.split(',')) < 2 :
            for year in range(int(year.split(',')[0]), int(year.split(',')[0])+1):
                self.start_urls.append("http://yperdiavgeia.gr/laws/search/year_from:" + str(year) + "/year_to:" + str(year) + "/teuxos:A")
        else:
            for year in range(int(year.split(',')[0]), int(year.split(',')[1])+1):
                self.start_urls.append("http://yperdiavgeia.gr/laws/search/year_from:" + str(year) + "/year_to:" + str(year) + "/teuxos:A")	

    def parse(self, response):
        sel = Selector(response)
        # XPATHs return list of strings (str -> int)
        num_pages = pages(int(sel.xpath('//span[@id="total-results"]/text()').extract()[0]))
        for n in range(1, num_pages + 1): 
            request = Request(response.url + "/page:" + str(n), callback = self.parse_objects)
            yield request

    def parse_objects(self, response):
        sel = Selector(response)
        # We follow all divs with either id "law" or "law alt" according to the DOM of each page
        paths = sel.xpath('//div[@class="law clearfix"]')
        for paths in paths:
            item = UltraclarityItem()
            title = paths.xpath('a[@class="subject"]/text()').extract()
            # Construction of items title based on number, name and year of publication (e.g. 1_A_2015)
            item['title'] = title[0].split()[2].replace("/","_").replace(",","")+'_'+title[0].split()[3]      
            item['url'] = paths.xpath('a[@class="subject"]/@href').extract()
            request = Request(item['url'][0], callback = self.parse_urls)
            # Pass the item as metadata in our request
            request.meta['item'] = item
            yield request

    def parse_urls(self,response):
        item = response.meta['item']
        # Store response.body in item['desc']
        item['desc'] = response.body
        yield item
