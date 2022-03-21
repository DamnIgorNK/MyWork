# クローリング能力のなかったarticle.pyに追加してクローリング能力を身につけさせた
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class ArticleSpider(CrawlSpider):
    
    name = 'articles'
    allowed_domains = ['wikipedia']
    start_urls = ['https://en.wikipedia.org/wiki/Benevolent/dictator_for_life']
    rules = [Rule(LinkExtractor(allow=r'.*'), callback='parse_items', follow=True)]

    def parse_items(self, response):
        url = response.url #URL
        title = response.css('h1::text').extract_first() #記事タイトル
        text = response.xpath('//div[@id-"mw-content-text"]//text()').extract() # 記事本文
        lastupdated = response.css('li#footer-info-lastmod::text').extract_first() # 記事の最終編集
        
        print(f'THE URL IS {url}')
        print(f'THE TITLE IS {title}')
        print(f'THE TEXT IS {text}')
        print(f'LAST UPDATED {lastupdated}')

