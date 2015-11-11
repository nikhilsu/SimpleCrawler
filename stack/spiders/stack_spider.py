from scrapy import Spider
from scrapy.selector import Selector

class StackSpider(Spider):
	name = "stack"
	allowed_domains = ["coursebook.utdallas.edu"]
	start_urls = ["http://coursebook.utdallas.edu/now/ce/term_16s",]
	def parse(self, response):
		course_status = Selector(response).xpath('//tbody/tr/td[2]/a[contains(text(),"CE 1202.002")]/../../td[1]/span/text()').extract()		
		
		for c in course_status:
			if c == "Open":
				print "Send email now"
