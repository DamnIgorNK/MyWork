import tweepy
import requests
import numpy as np
import config


api_key             = config.API_KEY
api_key_secret      = config.API_KEY_SECRET
bearer_token        = config.BEARER_TOKEN
access_token        = config.ACCESS_TOKEN
access_token_secret = config.ACCESS_TOKEN_SECRET


class TwitterAPI:
    api_key             = config.API_KEY
    api_key_secret      = config.API_KEY_SECRET
    bearer_token        = config.BEARER_TOKEN
    access_token        = config.ACCESS_TOKEN
    access_token_secret = config.ACCESS_TOKEN_SECRET

    def __init__(self):
        pass

    def f_authentate_twitter_api(self):
        """Twitter API認証関数

        return:
            api:認証済のAPI情報(tweepy.api.API)
        """
        auth = tweepy.OAuthHandler(self.api_key, self.api_key_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        api = tweepy.API(auth)

        return api


    