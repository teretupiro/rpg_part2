hello=input('Press \'Enter\' to start ')

feelings=input('\"Как ты себя чувствуешь?\" ')

help = ''

while help != 'да':

    if feelings =='плохо':
        print ('Я тебе сочувствую ')

    elif feelings == 'хорошо':
        print ('Это хорошо')
    else:
        print('Почему ты молчишь?')


    help = input('Ты поможешь мне? ')

    dead = ('Вы умерли')
    life = ('Вы выжили')

    if help == 'нет':
        print('\"Ты предатель\"')
        print('Хозяин убивает Вас.')
        print(dead)

    elif  help=='да':
        print('Идем')

    print('О!Монстр! ')
    monsters=input('Ваше действие: атака, защита' )
    if monsters== 'атака':
        print('Вы убили монстра ' )
    elif monsters== 'зашита':
        print('Вы зашитились' )
    else:
        print(dead)