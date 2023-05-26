import json

def p1():
    with open('10lab.json', encoding="utf-8") as f:
        s = json.load(f)
    for i in range(len(s.get('products'))):
        k = s.get('products')[i]
        print('Название: ' + str(k.get('name')))
        print('Цена: ' + str(k.get('price')))
        print('Вес: ' + str(k.get('weight')))
        if str(k.get('available: true')):
            print('В наличии')
        else:
            print('Нет в наличии!''\n')

def p2():
    with open('10lab.json', 'r', encoding='utf8') as f:
        s = json.load(f)

    for i in range(len(s.get('products'))):
        k = s.get('products')[i]
        print('Название: ' + str(k.get('name')))
        print('Цена: ' + str(k.get('price')))
        print('Вес: ' + str(k.get('weight')))
        if str(k.get('name')):
            print('В наличии')
        else:
            print('Нет в наличии!''\n')
        print('')

    dop = {}
    dop['name'] = input('Название: ')
    dop['price'] = input('Цена: ')
    dop['available'] = input('В наличии?: ')
    dop['weight'] = input('Вес: ')

    s['products'].append(dop)

    with open('10lab.json', 'w', encoding='utf8') as f:
        json.dump(s, f, indent=4, ensure_ascii=False)
        print(s)


def p3():
    en_ru = open('en-ru.txt ', encoding="utf-8").read().split('\n')
    s = {}
    for i in range(len(en_ru)):
        en_ru[i] = en_ru[i].split(' - ')
        s[en_ru[i][0]] = en_ru[i][1:]
    print(s)

    s1 = {}
    for i in s:
        for k in s[i]:
            k = k.split(', ')
            for j in k:
                if j not in s1:
                    s1[j] = i
                else:
                    s1[j] = s1[j] + ', ' + i
    s1 = dict(sorted(s1.items()))
    print(s1)
    f = open('ru-en.txt','wt')
    f.write(str(s1))
    f.close

p1(), p2(), p3()


