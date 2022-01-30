#TASK7
#7.	Написать функцию make_readable() принимающая количество секунд и возвращающая количество времени которое прошло HH:MM:SS.
# Секунды запрашивать у пользователя. Максимально возможное время в 359999 секундах  «99:99:99».
# Обработать условие сверх времени, если ввели 360000 или более то вывести «99:99:99», «00:00:00» и так для каждого круга сверх времени.

def make_readable(time_sec):
    h, m, s = int(), int(),int()
    h = time_sec // 3600
    m = (time_sec - h*3600) // 60
    s = time_sec % 60
    if time_sec>=360000:
        return print("99:99:99")
    else:
        return print(round(h),':',round(m), ':',round(s))

sec = int(input())
make_readable(sec)