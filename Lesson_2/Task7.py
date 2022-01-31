#TASK7
#7.	Написать функцию make_readable() принимающая количество секунд и возвращающая количество времени которое прошло HH:MM:SS.
# Секунды запрашивать у пользователя. Максимально возможное время в 359999 секундах  «99:59:59».
# Обработать условие сверх времени, если ввели 360000 или более то вывести «99:59:59», «00:00:00» и так для каждого круга сверх времени.

def make_readable(time_sec):
    h, m, s = int(), int(),int()
    for i in range(time_sec//360000+1):
        if time_sec>=360000:
            print("99:59:59")
            time_sec = time_sec - 360000
        else:
            h = time_sec // 3600
            m = (time_sec - h * 3600) // 60
            if time_sec == 0:
                s = 1
            else:
                s = time_sec % 60
            if h<10:
                h='0'+str(h)
            if m<10:
                m='0'+str(m)
            if s<10:
                s='0'+str(s)            print(h+':'+m+':'+s)


sec = int(input())
make_readable(sec)