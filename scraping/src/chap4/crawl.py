
import requests
from bs4 import BeautifulSoup


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

    def __init__(self, name, url, search_url, result_listing, result_url, absolute_url,title_tag, body_tag):
        self.name = name # サイト名
        self.url = url #サイトURL
        self.search_url = search_url #対象のトピックを追加するときにどこで結果を探し始めるか
        self.result_listing = result_listing #結果情報を格納する箱
        self.result_url = result_url #結果を含むURL
        self.absolute_url = absolute_url # 絶対パス
        self.title_tag = title_tag # タイトルタグ，h1など
        self.body_tag = body_tag # 本文タグ，サイトによって異なる

    
class Crawler:
    """クローリングするクラス"""

    def get_page(self,url:str):
        try:
            req = requests.get(url)
        except requests.exceptions.RequestException: #urlがなかったとき
            return None
        return BeautifulSoup(req.text, 'html.parser')

    def safe_get(self, page_obj:BeautifulSoup, selector:str):
        child_obj = page_obj.select(selector)
        if child_obj is not None and len(child_obj)>0:
            return child_obj[0].get_text()
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

            

def main():
    crawler = Crawler()

    site_data = {'name':'Reuters',
                 'url':'http://reuters.com',
                 'search_url':'http://www.reuters.com/search/news?blob=',
                 'result_listing':'div.search-result-content',
                 'result_url':'h3.search-result-title a',
                 'absolute_url':False,
                 'title_tag':'h1',
                 'body_tag':'div.StandardArticleBody_body_1gnLA'} #bodyタグが間違っている可能性

    
    sites = []

    sites.append(Website(site_data['name'],
                         site_data['url'],
                         site_data['search_url'],
                         site_data['result_listing'],
                         site_data['result_url'],
                         site_data['absolute_url'],
                         site_data['title_tag'],
                         site_data['body_tag']))

    topics = ['python', 'data science']
    for topic in topics:
        print('GETTING INFO ABOUT ' + topic)
        for target_site in sites:
            crawler.search(topic, target_site)


if __name__ == '__main__':
    main()


    


