## -*- coding: utf-8 -*-
#!/usr/bin/env python3

##      
##          |  __ \ _/_/_ / ____|_   _|/ ____| |__   __|/\   |  __ \|  ____| |  | | |  _ \ / __ \__   __|
##          | |__) | ____| |  __  | | | (___      | |  /  \  | |  | | |__  | |  | | | |_) | |  | | | |   
##          |  _  /|  _| | | |_ | | |  \___ \     | | / /\ \ | |  | |  __| | |  | | |  _ <| |  | | | |   
##          | | \ \| |___| |__| |_| |_ ____) |    | |/ ____ \| |__| | |____| |__| | | |_) | |__| | | |   
##          |_|  \_\_____|\_____|_____|_____/     |_/_/    \_\_____/|______|\____/  |____/ \____/  |_|                                                                                                 
##      
## by Igor Harmendani

import telegram_token
import logging
import random
import keywords
import re
from telegram.ext import Updater, BaseFilter, MessageHandler, Filters

bot_token = telegram_token.token
updater = Updater(token = bot_token, use_context=True)
dispatche = updater.dispatcher

def response(update, context): # Respostas que o bot envia
    context.bot.send_message(chat_id=update.message.chat_id, text = random.choice(keywords.responses)) 

echo_handler = MessageHandler(Filters.regex(keywords.trigger_words), response) # Filtra as palavras chave
dispatche.add_handler(echo_handler)

updater.start_polling()













