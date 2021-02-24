import scrapy
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from cumpa.items import CumpaItem
from scrapy.exceptions import CloseSpider

class cumpaMusica(scrapy.spiders.CrawlSpider):
    name = 'DamasGratis'
    item_count= 0
    allowed_domain = ['https://www.musica.com']
    start_urls = ['https://www.musica.com/letras.asp?letras=17059&orden=alf']

    rules = {
        Rule(LinkExtractor(allow=(), restrict_xpaths=('//ul[@class="listado-letras"]//li')), callback= 'parse_item', follow= False)
    }

    def parse_item(self,response):
        items = CumpaItem()
        items['letra'] = response.xpath('//div[@id = "letra"]//p').extract()
        items['nombre'] = response.xpath('//div[@id = "letra"]//h3//text()').extract()
        #self.item_count += 1
        #if self.item_count >30:
        #    raise (CloseSpider('cantidad alcanzada'))
        yield items
