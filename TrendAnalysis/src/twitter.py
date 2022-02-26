import tweepy
import requests
import numpy as np
import config
import pandas as pd


class TwitterAPI:


    def __init__(self):
        self.api_key             = config.API_KEY
        self.api_key_secret      = config.API_KEY_SECRET
        self.bearer_token        = config.BEARER_TOKEN
        self.access_token        = config.ACCESS_TOKEN
        self.access_token_secret = config.ACCESS_TOKEN_SECRET

    def __f_authentate_twitter_api(self):
        """Twitter API認証関数

        return:
            api:認証済のAPI情報(tweepy.api.API)
        """
        auth = tweepy.OAuthHandler(self.api_key, self.api_key_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        api = tweepy.API(auth)

        return api


class GetTrend(TwitterAPI):
    def __init__(self):
        super().__init__()
        df = self.__f_get_trend()

    def __f_get_trend(self):
        # 日本のWOEID
        woeid = 23424856
        # トレンド取得
        api = self.__f_authentate_twitter_api()
        trends = api.get_place_trends(woeid)
        df = pd.DataFrame(trends[0]['trends'])

        return df

g = GetTrend()
    