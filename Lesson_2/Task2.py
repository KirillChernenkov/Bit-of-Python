#TASK2
#2.	Выполнить функцию, которая принимает несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Осуществить вывод данных о пользователе одной строкой.

def info(name,surname,birthday,city,email,tel):
    return print(f'Здравствуйте,{name} {surname}, дата рождения {birthday}, проживающий в городе {city}, email {email}, телефон {tel}')

name_input,surname_input,birthday_input,city_input,email_input,tel_input = [input() for _ in range(6)]
info(name=name_input,surname=surname_input,birthday=birthday_input,city=city_input,email=email_input,tel=tel_input)
