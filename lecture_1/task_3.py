color = input('твой любимый цвет: ')
match color:
    case 'красный' | 'оранжевый':
        print('любитель яркого')
    case 'зеленый':
        print('Ты не охотник')
    case 'синий' | 'голубой':
        print('Ха, классика')
    case _:
        print('тебя не понять')