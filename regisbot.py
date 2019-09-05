# -*- coding: utf-8 -*-

# RÉGIS TADEU BOT
# by igorharmendani

# ANITTA NÃO TEM CARREIRA INTERNACIONAL
# KPOP É COISA DE RETARDADO
# AHHHHH MAS A POLÍTICA TÁ ESSE GRENAL N SEI O Q LA
# regis tadeu chorando baixinho após ser chamado de "régis tadando" (256.689 views)


import telebot
import time
import random
import telegram_token

bot_token = telegram_token.token
bot = telebot.TeleBot(token=bot_token)


# O código abaixo define as palavras-chave que irão acionar o bot e as respostas que ele dará.
# Tentei importar de outro arquivo, fazer uma variável, mas o regexp só funciona se as strings estiverem "coladas" nele
# Talvez depois eu conserte


@bot.message_handler(regexp='''regis|régis|tadeu|anitta|anita|album|álbum|disco|cd|fita|vinil|carreira|internacional|MC|kpop|guitarra|violão|bateria|metal|dream theater|fix that gub|manowar|funk|musica|pablo|fã|vittar|grenal''')
def handle_message(message):
    bot.reply_to(message, random.choice(['Envie um email para registadeu@yahoo.com.br',
                                        'ANITA NÃO TEM CARREIRA INTERNACIONAL!!',
                                        'A sociedade está muito infantilizada',
                                        'SÓ ANALFABETO FUNCIONAL OUVE K-POP',
                                        'K-POP É COISA DE DÉBIL MENTAL',
                                        'The Voice é programa pra enganar otário',
                                        'Eu conheço Manowar',
                                        'Olha aqui, a carreira internacional da Anitta é uma FARSA!',
                                        'O sucesso internacional da Anitta é uma MENTIRA!',
                                        'Aposto que você não sabe: Fix That Gub',
                                        'Roberto Carlos nunca foi rei de nada, ok?',
                                        'Letra de Kpop é tudo parachoque de caminhão',
                                        'O Raul Gil tem uma voz boa',
                                        'É "YOUTCHUBER" que fala, tá, né "youtuber" não',
                                        '"O Pablo Vittar", ok, tem nada de "A Pablo" não, vsf',
                                        'Ah mas a política ultimamente tá um verdadeiro GRENAL',
                                        'TODO FÃ É IMBECIL',
                                        'Olha, isso aí pouca gente sabe, viu'
                                        ]))


# Isso é pra impedir um erro que dá no server do Telegram
# Aparentemente depois de 1 hora rodando o script dá algum pau lá e isso conserta
# Nem sei direito o que é kkkkkk

while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(15)