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
## https://github.com/igor-harmendani/regisbot


import tokens
import twitterAPI
import triggers
import re
from telegram.ext import Updater, MessageHandler, Filters

bot_token = tokens.telegram_token
updater = Updater(token = bot_token, use_context=True)
dispatche = updater.dispatcher

# Respostas que o bot envia, retiradas de algum tweet da conta @regisstadeu
def response(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text = re.sub(r'https://\S+', '', twitterAPI.registweets()))


# Filtro para que o bot seja ativado apenas quando receber uma mensagem contendo uma palavra da lista
echo_handler = MessageHandler(Filters.regex(triggers.regex_list), response)
dispatche.add_handler(echo_handler)

updater.start_polling()













