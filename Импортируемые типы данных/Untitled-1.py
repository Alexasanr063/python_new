import sys
import io

# Устанавливаем кодировку вывода
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Пропишите нужные импорты.
from datetime import datetime,timedelta

# Допишите код функции.
def get_results(leader_time, your_time):
    # Сохраните формат времени как строку в переменную time_format:
    time_format = "%H:%M:%S"
    # Преобразуйте полученные в аргументах строки в объекты datetime:
    leader_time_object = datetime.strptime(leader_time,time_format)
    your_time_object =  datetime.strptime(your_time,time_format)

    # Если два объекта datetime равны, то получатель сообщения – лидер.
    # Составьте и верните строку c сообщением для лидера.
    if leader_time_object == your_time_object:
        return f'Вы пробежали за {leader_time} и победили!'
    else:
        # В противном случае вычислите разницу
        # между временем лидера и временем участника.
        # Результатом будет значение типа timedelta.
        difference = your_time_object - leader_time_object

        # Верните сообщение с указанием времени участника
        # и его отставания от лидера:
        return f'Вы пробежали за {your_time} с отставанием от лидера на {difference}.'


# Проверьте работу программы. Здесь вы можете подставить свои значения.
print(get_results('02:02:02', '02:02:02'))
print(get_results('02:02:02', '03:04:05'))