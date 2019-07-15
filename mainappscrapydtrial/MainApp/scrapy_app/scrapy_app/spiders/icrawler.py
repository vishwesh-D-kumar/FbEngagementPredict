from scrapy.selector import HtmlXPathSelector
from scrapy.spiders import CrawlSpider
from scrapy.http import Request
 
# DOMAIN = 'xml-sitemaps.com'
# URL = 'http://%s' % DOMAIN
 
class MySpider(CrawlSpider):
    name='icrawler'
    # name = DOMAIN
    # allowed_domains = [DOMAIN]
    # start_urls = [
    #     URL
    # ]
    def __init__(self, *args, **kwargs):
    #       # We are going to pass these args from our django view.
    #       # To make everything dynamic, we need to override them inside __init__ method
        self.url = kwargs.get('url')
        self.domain = kwargs.get('domain')
        self.start_urls = [self.url]
        self.allowed_domains = [self.domain]
        self.subsites=[]
        print(str(self.start_urls)+"wassup")
    def parse(self, response):
        print(response.url)
        hxs = HtmlXPathSelector(response)
        URL=self.url
        # print(response)
        for url in hxs.select('//a/@href').extract():
            
            if not ( url.startswith('http://') or url.startswith('https://') ):
                url= URL + url
            # print (url)
            self.subsites.append(url)
            if len(self.subsites)>500:
                break
            yield Request(url, callback=self.parse)
        if len(self.subsites)>500:
            # print(self.subsites)
            final={}
            final['url']=self.subsites
            # return {'url':self.subsites}
            yield final
            # return(url)
        final={}
        final['url']=self.subsites
        # return {'url':self.subsites}
        # print("****************************************************")
        # print(final)
        yield final
        # for item in self.parse2(response):
        #     yield item


    def parse2(self,response):
        hxs = HtmlXPathSelector(response)
        items={}
        items['url']=list(set(hxs.select('//a/@href').extract()))
        return items




        
