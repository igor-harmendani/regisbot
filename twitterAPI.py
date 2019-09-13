#!/usr/bin/env python
# -*- coding: utf-8 -*-

from twitter import *
from random import randrange
import tokens

t = Twitter(auth=OAuth(tokens.twitter_token,
                       tokens.twitter_token_secret,
                       tokens.twitter_api_key,
                       tokens.twitter_api_secret,
                       ))

# A API do twitter aqui só lê os 20 tweets mais recentes da conta selecionada,
# portanto foi incluído uma seleção aleatória de números entre 0 e 19,
# correspondentes aos tweets mais recentes e os mais antigos, respectivamente.
def registweets():
    tweets = t.statuses.user_timeline(screen_name="RegissTadeu", include_rts = False, tweet_mode='extended')
    num = randrange(20)
    return tweets[num]['full_text']

