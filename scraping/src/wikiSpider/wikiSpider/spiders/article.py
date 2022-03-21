# scrapyを用いてスクレイピングするときはターミナルで
# scrapy startproject <プロジェクト名>と打ち込んで作成する．

import scrapy

class ArticleSpider(scrapy.Spider):
    """クローラ'wikiSpider'記事担当クラス
    
    ブログ，プレスリリース，記事など種類ごとに別々のScrapyを用意して
    各Scrapyが自分の担当のサイトをスクレイピングする

    """

    name = 'article'

    def start_requests(self):
        """
        各サイトについて，Scrapy内のRequestオブジェクトを生成する
        """
        urls = [
            'http://en.wikipedia.org/wiki/Python_'
            '%28programming_language%29',
            'https://en.wikipedia.org/wiki/Functional_programming',
            'https://en.wikipedia.org/wiki/Monty_Python'
        ]
        return [scrapy.Request(url=url,callback=self.parse) for url in urls]

    def parse(self, response):
        """
        ユーザー定義のコールバック関数
        callback=self.parseとしてRequestオブジェクトに渡す
        """
        url = response.url 
        title = response.css('h1::text').extract_first()
        print(f'THE URL IS {url}')
        print(f'THE TITLE IS {title}')

    