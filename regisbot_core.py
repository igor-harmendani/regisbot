## -*- coding: utf-8 -*-
#!/usr/bin/env python3

# RÉGIS TADEU BOT FOR TELEGRAM v2.2
# by Igor Harmendani
# https://github.com/igor-harmendani/regisbot


from twitter import *
import tokens
import re
import logging
from random import randrange
import random
from telegram.ext import Updater, MessageHandler, Filters

# Twitter API start
t = Twitter(auth=OAuth(tokens.twitter_token,
                       tokens.twitter_token_secret,
                       tokens.twitter_api_key,
                       tokens.twitter_api_secret,
                       ))


# This function generates a random number and gets the full text of the tweet corresponded to it.
# It seems that the Twitter API limits the number of tweets to be fetched to 20, but I could be wrong on that.
def registweets():
    tweets = t.statuses.user_timeline(screen_name="RegissTadeu", include_rts=False, tweet_mode='extended')
    try:
        num = randrange(20)
        return tweets[num]['full_text']
    except IndexError:
        num = randrange(5)
        return tweets[num]['full_text']


# This function gets a random word from the tweet returned by the responses function above
# and writes it to a plain text file that will be used as a list of filters for regex later.
# It verifies the length of the word, to avoid adding too common words like 'an', 'and', 'the', etc.,
# and also simulates some kind of dice throw, so it won't write words to the file every single time
# a tweet message is sent, as that would make the bot pretty annoying. In this case, for every tweet,
# it has a 30% chance of adding a word to the file.
def append():
    word_txt = open('trigger_words.txt', 'a+')
    tweet = registweets()
    turn_to_list = re.sub(r'[^\w]', ' ', tweet).split()
    rand_word = str(random.choice(turn_to_list))
    throw_dice = randrange(100)
    ignore_words = ['https', 'http', ]
    if len(rand_word) > 4 and throw_dice > 70:
        if rand_word not in (ignore_words or word_txt):
            return word_txt.write(str('\n' + rand_word))


# Telegram API Start

# Telegram logs for debugging purposes
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Load Telegram API tokens
bot_token = tokens.telegram_token
updater = Updater(token = bot_token, use_context=True)
dispatche = updater.dispatcher


# This function will send the tweet text as a message to the user or chat group, using regex to filter out URLs.
# As the append function needs to run everytime a response is sent, it will run everytime the response function
# is called.
def response(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text = re.sub(r'https://\S+', '', registweets()))
    append()


# This function will concatenate the words in the text file to be used as filters for the bot,
# using proper regex operators and ignoring the line breaks.
# And of course the name needed to be that one, couldn't let that pun pass :)
def regextadeu():
    data = open('trigger_words.txt', 'r').read().splitlines()
    regex_list = re.compile('|' .join(data), re.IGNORECASE)
    return regex_list


# Finally, this class will use those words to filter out messages sent by users,
# so that it only sends the tweet when the user sends a keyword
echo_handler = MessageHandler(Filters.regex(regextadeu()), response)
dispatche.add_handler(echo_handler)

# Starts the bot processes and keeps it on standby for messages
updater.start_polling()













