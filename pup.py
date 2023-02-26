nick = input()
secret_list = ['Мавпродош', 'Лорнектиф', 'Древерол', 'Фиригарпиг',
               'Клодобродыч']

while nick not in secret_list:
    print('Тут ничего нет. Еще есть вопросы?')
    nick = input()
print(f'Ты – свой. Приветствую, любезный {nick}!')
