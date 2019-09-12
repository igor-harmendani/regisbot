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


def registweets():
    tweets = t.statuses.user_timeline(screen_name="RegissTadeu", include_rts = False, tweet_mode='extended')
    num = randrange(20)
    return tweets[num]['full_text']

