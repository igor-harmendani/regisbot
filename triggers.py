import re

# Lista com as palavras que ativam o bot
trigger_words = ['regis',
                 'régis',
                 'tadeu',
                 'música',
                 'funk',
                 'regisbot',
                 'anitta',
                 'anita',
                 'carreira',
                 'internacional',
                 'fix that gub',
                 'pablo',
                 'vitar',
                 'vittar',
                 'kpop',
                 'k-pop',
                 'vinil',
                 'mpb',
                 'caetano',
                 'samba',
                 'rock',
                 'metal',
                 'prog',
                 'progressivo',
                 'progressive',
                 'reggae',
                 'regendo',
                 'reger',
                 'rádio',
                 'radio',
                 'som',
                 'fã',
                 'fa',
                 'fan',
                 'ost',
                 'trilha',
                 'debate',
                 'grenal',
                 'unibot',
                 'palhaço',
                 'otario',
                 'bobo',
                 'feio',
                 'vsf',
                 'tnc',
                 'FUCK',
                 'YEAH']

# Concatenação da lista para formato aceitável pelo regex e desconsideração de case
regex_list = re.compile('|'.join(trigger_words), re.IGNORECASE)
