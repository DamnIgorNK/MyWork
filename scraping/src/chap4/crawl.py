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

