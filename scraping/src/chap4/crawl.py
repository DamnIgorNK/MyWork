
import requests
from bs4 import BeautifulSoup
import re


class Content:
    """全ページ/サイトの共通基底クラス"""
    def __init__(self, topic, url, title, body):
        self.topic = topic
        self.url = url
        self.title = title
        self.body = body

    def printing(self):
        """Flexible output func controls output"""
        print(f'New article found for topic:{self.topic}')
        print(f'URL: {self.url}')
        print(f'TITLE: {self.title}')
        print(f'BODY: {self.body}')        


class Website:
    """Webサイトの構造についての情報

    個別にページで情報を取得するのではなく，タイトルのありかを示すタグを返す．
    ex) 「ガジェマガ」ではなく，返すのは「h1」

    """

    def __init__(self, name, url, target_pattern, absolute_url, title_tag, body_tag):
        self.name = name # サイト名
        self.url = url #サイトURL
        self.target_pattern = target_pattern
        self.absolute_url = absolute_url # 絶対パス
        self.title_tag = title_tag # タイトルタグ，h1など
        self.body_tag = body_tag # 本文タグ，サイトによって異なる

    
class Crawler:
    """クローリングするクラス"""

    def __init__(self, site):
        self.site = site
        self.visited = []


    def get_page(self,url:str):
        try:
            req = requests.get(url)
        except requests.exceptions.RequestException: #urlがなかったとき
            return None
        return BeautifulSoup(req.text, 'html.parser')

    def safe_get(self, page_obj:BeautifulSoup, selector:str):
        selected_elems = page_obj.select(selector)
        if selected_elems is not None and len(selected_elems)>0:
            return selected_elems[0].get_text()
        return ""

    def search(self, topic, site):
        """Webサイトでトピックを検索して見つけたページを全部記録する"""
        bs = self.get_page(site.search_url + topic)
        search_results = bs.select(site.result_listing)

        for result in search_results:
            url = result.select(site.result_url)[0].attrs['href']

            # 絶対か相対URLかのチェック
            if (site.absolute_url):
                bs = self.get_page(url)
            else:
                bs = self.get_page(site.url + url)

            if bs is None:
                print("Something is wrong with that page or URL. Skipping!")
                return
            
            title = self.safe_get(bs, site.title_tag)
            body = self.safe_get(bs, site.body_tag)
            
            if title!='' and body!='':        
                content = Content(topic=topic, title=title, body=body, url=url)
                content.printing()

            

    def parse(self,url):
        bs = self.get_page(url)
        if bs is not None:
            title = self.safe_get(bs, self.site.title_tag)
            body = self.safe_get(bs, self.site.body_tag)
            if title!='' and body!='':
                content = Content(url, title, body)
                content.printing()

    
    def crawl(self):
        """Webサイトからホームページ取得"""
        bs = self.get_page(self.site.url)
        target_pages = bs.findAll('a', href=re.compile(self.site.target_pattern))

        for target_page in target_pages:
            target_page = target_page.attrs['href']
            if target_page not in self.visited: # 既出かどうか
                self.visited.append(target_page)
                if not self.site.absolute_url:
                    target_page = '{}{}'.format(self.site.url, target_page)
                
                #target_pageの解析
                self.parse(target_page)


def main():
    reuters = Website(
        name='Reuters',
        url='https://www.reuters.com',
        target_pattern='^(/article/)',
        absolute_url=False,
        title_tag='h1',
        body_tag='div.StandardArticleBody_body_1gnLA'
    )

    crawler = Crawler(reuters)
    crawler.crawl()


if __name__ == '__main__':
    main()


    


