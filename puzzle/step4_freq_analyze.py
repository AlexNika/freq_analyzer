"""Частотный анализ слов"""


def analize(words):
    """
    Частотный анализ слов
    :param words: входной список слов
    :return: самое частое слово кортеж (слово, кол-во)
    """
    # сохдаем словарь для анализа
    analyze = {}
    for word in words:
        # если слово уже есть в словаре
        if word in analyze:
            # увеличиваем кол-во этих слов на 1
            analyze[word] += 1
        else:
            # добавляем слово в словарь с количеством 1
            analyze[word] = 1
    # сортируем словарь и получаем кортеж слово и самое большое кол-во
    result = sorted(analyze.items(), key=lambda item: item[1], reverse=True)
    #print(result)
    # берем 1-ый элемент и слово - это будет тема
    theme = result[0]
    # возвращаем результат
    return theme


if __name__ == '__main__':
    words = ['красивый', 'хороший', 'уродливый', 'явный', 'хороший', 'неявный', 'простой', 'хороший', 'сложный',
             'сложный',
             'хороший', 'запутанный', 'плоский', 'хороший', 'вложить', 'разредить', 'хороший', 'плотный', 'читаемость',
             'иметь', 'значение', 'особый', 'случай', 'настолько', 'особый', 'нарушать', 'правило', 'это',
             'практичность',
             'важный', 'безупречность', 'ошибка', 'должный', 'замалчиваться', 'замалчиваться', 'явно', 'встретить',
             'двусмысленность', 'отбросить', 'искушение', 'угадать', 'должный', 'существовать', 'желательно',
             'очевидный',
             'способ', 'сделать', 'это', 'хотя', 'поначалу', 'мочь', 'очевидный', 'голландец', '12', 'хороший', 'хотя',
             'зачастую', 'хороший', 'прямо', 'реализация', 'сложно', 'объяснить', 'идея', 'плохой', 'реализация',
             'легко',
             'объяснить', 'идея', 'возможно', 'хороший', 'пространство', 'имя', 'отличный', 'штука', 'делать',
             'большой']
    theme = analize(words)
    print(theme)
