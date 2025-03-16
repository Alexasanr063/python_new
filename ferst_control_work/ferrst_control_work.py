import datetime as dt
from decimal import Decimal
from datetime import datetime, timedelta

import datetime

DATE_FORMAT = '%Y-%m-%d'
goods = {'Яйца Фабрики №1': [{'amount': Decimal('1'),
                      'expiration_date': datetime.date(2025, 3, 15)}],
 'Фабрика №2: яйца': [{'amount': Decimal('2'),
                       'expiration_date': datetime.date(2025, 3, 11)},
                      {'amount': Decimal('3'),
                       'expiration_date': datetime.date(2025, 3, 13)}],
 'макароны': [{'amount': Decimal('100'), 'expiration_date': None}]}

def add(items, title, amount, expiration_date=None):
    if title not in items:
        items[title] = []
    expiration_date = dt.datetime.strptime(
        expiration_date,
        DATE_FORMAT
    ).date() if expiration_date else expiration_date
    list.append(
        items[title],
        {'amount':amount,'expiration_date':expiration_date}
    )





def add_by_note(items, note):
    parts = str.split(note,' ')
    #print(parts)
    if len(str.split(parts[-1],'-'))==3:
        expiration_date = parts[-1]
        good_amount = Decimal(parts[-2])
        title = str.join(' ',parts[0:-2])
        add(items,title,good_amount,expiration_date)
    else:
        #print(items)
        good_amount = Decimal(parts[1])
        title = parts[0]
        add(items, title, good_amount)


def find(items, needle):
    spisok = []
    for item in items:
        #print(item)
        if  needle.lower() in item.lower():
            spisok.append(item)
    return spisok



def get_amount(items, needle):
    spisok = find(items,needle)
    sum = Decimal('0')
    for key,value in items.items():
        for val in value:
            if key in spisok:
                sum += val['amount']
    return sum

def get_expired(items, in_advance_days=0):
    now = dt.datetime.now().strftime(DATE_FORMAT)
    now = dt.datetime.strptime(now, DATE_FORMAT).date()
    lists = []
    slovar = {}
    for key,value in items.items():
        for val in value:
            if val['expiration_date'] is not None:
                if val['expiration_date'] <= now + timedelta(days=in_advance_days):
                    lists.append((key,val['amount']))
                    #print(f'название {key} количество {get_amount(items,key)}')
    for key,value in lists:
        if key in slovar:
            slovar[key] += value
        else: slovar[key] = value
    finish = [(i,y)for i,y in slovar.items()]
    #print(finish)
    #print(slovar)
    return finish



#print(get_expired(goods),None)
#[('Фабрика №2: яйца', Decimal('5'))]
# Вывод: [('Хлеб', Decimal('1'))]
#print(get_expired(goods, 1))
# Вывод: [('Хлеб', Decimal('1')), ('Яйца', Decimal('3'))]
print(get_expired(goods, 2))
# Вывод: [('Хлеб', Decimal('1')), ('Яйца', Decimal('5'))]
