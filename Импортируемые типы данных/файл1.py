
import sys
import io

# Устанавливаем кодировку вывода
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
# Пропишите нужные импорты.
from datetime import datetime,timedelta

def get_weekday_name(weekday_number):
    # В зависимости от weekday_number функция должна вернуть название дня.
    if weekday_number == 0:
        return 'понедельник'
    elif weekday_number == 1:
        return 'вторник'
    elif weekday_number == 2:
        return 'среда'
    elif weekday_number == 3:
        return 'четверг'
    elif weekday_number == 4:
        return 'пятница'
    elif weekday_number == 5:
        return 'суббота'
    elif weekday_number == 6:
        return 'воскресенье'
        


def get_day_after_tomorrow(date_string):
    # С помощью шаблона преобразуйте date_string в значение типа datetime
    now = datetime.strptime(date_string,'%Y-%m-%d')
    
    # Получите день недели для now:
    now_weekday = get_weekday_name(now.weekday())
    # Вычислите послезавтрашнюю дату:
    day_after_tomorrow = now + timedelta(days = 2)
    # Получите день недели для day_after_tomorrow:
    day_after_tomorrow_weekday = get_weekday_name(day_after_tomorrow.weekday())
    return f'Сегодня {date_string}, {now_weekday}, а послезавтра - {day_after_tomorrow_weekday}.'


# Проверьте работу программы, можете подставить свои значения.
print(get_day_after_tomorrow('2024-01-01'))
print(get_day_after_tomorrow('2024-01-02'))
print(get_day_after_tomorrow('2024-01-03'))
print(get_day_after_tomorrow('2024-01-04'))
print(get_day_after_tomorrow('2024-01-05'))
print(get_day_after_tomorrow('2024-01-06'))