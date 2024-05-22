from _datetime import datetime, timedelta


def get_plan_days():
    """ Получает список планируемых дат """

    date_now = datetime.now().date()  # получаем текущую дату

    dates_list = [date_now]  # задаем список дат

    # добавляем в список планируемые даты на неделю вперед
    for day in range(1, 7):
        next_day = date_now + timedelta(days=day)
        dates_list.append(next_day)

    return dates_list
