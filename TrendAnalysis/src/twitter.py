import tweepy
import requests
import numpy as np
import config
import pandas as pd
from datetime import datetime
import openpyxl

class TwitterAPI:
    """API認証を行う親クラス
    """
    def __init__(self):
        self.api_key             = config.API_KEY
        self.api_key_secret      = config.API_KEY_SECRET
        self.bearer_token        = config.BEARER_TOKEN
        self.access_token        = config.ACCESS_TOKEN
        self.access_token_secret = config.ACCESS_TOKEN_SECRET

    def authentate_twitter_api(self):
        """Twitter API認証関数

        return:
            api:認証済のAPI情報(tweepy.api.API)
        """
        auth = tweepy.OAuthHandler(self.api_key, self.api_key_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        api = tweepy.API(auth)

        return api


class GetTrend(TwitterAPI):
    """Twitter APIの中でもトレンド関連に特化したクラス
    """
    def __init__(self):
        super().__init__()


    def get_trend(self):
        # 日本のWOEID
        woeid = 23424856
        # API獲得
        api = self.authentate_twitter_api()
        # トレンド取得
        trends = api.get_place_trends(woeid)
        df = pd.DataFrame(trends[0]['trends'])
        df.to_excel(f'{datetime.now()}_trend.xlsx')
        return df


    def get_tweet(self, word: str):
        q = f'{word}'
        item_num = 20

        api = self.authentate_twitter_api()
        # 取得するツイートは以下のようにJSON形式でまとめておく．中身はtweet.textで確認できるS
        tweets = tweepy.Cursor(
            api.search_tweets,
            q=q,
            lang='ja',
        ).items(item_num)
        for tweet in tweets:
            print(tweet.text)
        return tweets


def test():
    t = GetTrend()
    df = t.get_trend()
    for word in df['name'].tolist():
        print(word)
        tweets = t.get_tweet(word)


if __name__=='__main__':
    test()