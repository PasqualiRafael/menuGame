from modules import colors


def ini(title):
    print(f'')
    print('{}'.format(colors.cores['bw']) + ('-=-' * 12) + '{}'.format(colors.cores['close']))
#   print('{:^36}'.format('{}-=-{}' * 12).format(colors.cores['bw'], colors.cores['close']))
    print('{:-^36}'.format(title))
#   print('{}'.format(colors.cores['green']) + title + '!{}'.format(colors.cores['close']))
    print('{}'.format(colors.cores['bw']) + ('-=-' * 12) + '{}'.format(colors.cores['close']))
#   print('{}   {}'.format(colors.back['purple'], colors.back['close']) * 12)
    print(f'')


def close():
    print(f'')
    print('{}'.format(colors.cores['bw']) + ('-=-' * 12) + '{}'.format(colors.cores['close']))
    input('{}Pressione qualquer tecla para fechar!{}'.format(colors.cores['green'], colors.cores['close']))



