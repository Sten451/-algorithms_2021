"""
Задание 1.

Выполните профилирование памяти в скриптах.
Проанализируйте результат и определите программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 3-5 ваших РАЗНЫХ скриптов!
(хотя бы 3 разных для получения оценки отл).
На каждый скрипт вы должны сделать как минимум по две реализации.

Можно взять только домашние задания с курса Основ
или с текущего курса Алгоритмов

Результаты профилирования добавьте в виде комментариев к коду.
Обязательно сделайте аналитику (что с памятью в ваших скриптах, в чем ваша оптимизация и т.д.)

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""

import memory_profiler
import timeit
from pympler import asizeof
from collections import deque
from collections import Counter


""" 1. Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский
язык.
Например: >>> num_translate("one") "один" >>> num_translate("eight")
"восемь"
Если перевод сделать невозможно, вернуть None.
Подумайте: как и где лучше хранить информацию, необходимую для перевода:
какой тип данных выбрать, в теле функции или снаружи?
2. * (вместо задачи 1) Доработать предыдущую функцию num_translate_adv(): реализовать корректную работу
с числительными, начинающимися с заглавной буквы. Например: >>> num_translate_adv("One")
"Один" >>> num_translate_adv("two") "два" """


def memory_time(func):
    def wrapper(*args):
        m1 = memory_profiler.memory_usage()
        start_time = timeit.default_timer()
        result = func(*args)
        m2 = memory_profiler.memory_usage()
        return result, m2[0] - m1[0], timeit.default_timer() - start_time

    return wrapper


@memory_time
def num_translate_adv(word_translate):
    word_translate_temp = word_translate
    word_translate_temp = word_translate_temp.lower()
    word_translate_value = language.get(word_translate_temp)
    if word_translate_value is None:
        print("Перевод данного слова не найден")
    else:
        if word_translate[0].isupper():
            word_translate_value = word_translate_value.capitalize()
        print(word_translate_value)


@memory_time
def num_translate_adv2(dictionary, word):
    if word.lower() not in dictionary:
        print(f"Перевод слова {word.lower()} не найден")
        return None
    elif word[0].isupper():
        print(f"Перевод слова {word.capitalize()} --- {dictionary.get(word.lower()).capitalize()}")
    else:
        print(f"Перевод слова {word} --- {dictionary.get(word.lower())}")


language = {
    "zero": "ноль",
    "one": "один",
    "two": "два",
    "three": "три",
    "four": "четыре",
    "five": "пять",
    "six": "шесть",
    "seven": "семь",
    "eight": "восемь",
    "nine": "девять",
    "ten": "десять"
}

word = input("Введите слово для перевода от 0-10 на английском языке ")
while not word.isalpha():
    word = input("Ввести надо именно слово без цифр ")
value = num_translate_adv(word)
print(f"Выполнение функции ОРИГИНАЛЬНОЙ по памяти {value[1]} Mib и {value[2]} сек")

word = input("Введите слово для перевода от 0-10 на английском языке ")
while not word.isalpha():
    word = input("Ввести надо именно слово без цифр ")
value = num_translate_adv2(language, word)
print(f"Выполнение функции ИЗМЕНЕННОЙ по памяти {value[1]} Mib и {value[2]} сек")
"""
Результаты:
Введите слово для перевода от 0-10 на английском языке one
один
Выполнение функции ОРИГИНАЛЬНОЙ по памяти 0.00390625 Mib и 0.11173449999999896 сек
Введите слово для перевода от 0-10 на английском языке one
Перевод слова one --- один
Выполнение функции ИЗМЕНЕННОЙ по памяти 0.0 Mib и 0.10875190000000146 сек
Ну вроде стало чуть быстрее и памяти меньше. Использование меньшего количества переменных, плюс 
изначально словарь не передавался в функцию. Да и более лаконичнее стала функция.
"""
# ****************** Задание 2 ***************************
"""
2. Реализовать класс Road (дорога).
определить атрибуты: length (длина), width (ширина);
значения атрибутов должны передаваться при создании экземпляра класса;
атрибуты сделать защищёнными;
определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
использовать формулу: длина * ширина * масса асфальта для покрытия одного
кв. метра дороги асфальтом, толщиной в 1 см * число см толщины полотна;
проверить работу метода.
Например: 20 м*5000 м*25 кг*5 см = 12500 т.
"""


class Road:
    # Я так понял это известная величина
    weight_1 = 25

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def work(self, think):
        try:
            weight = self._length * self._width * Road.weight_1 * think
            print("Потребуется:", weight / 1000, "тонн")
        except TypeError:
            print("Переданные параметры не цифры")


# Создаем экземпляр класса и вызываем метод с которым передаем высоту полотна
a = Road(5000, 20)
a.work(5)
print('Использование объекта без __slots__:  ', asizeof.asizeof(a))


class Road2:
    # Я так понял это известная величина
    weight_1 = 25
    __slots__ = ["_length", "_width"]

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def work(self, think):
        try:
            weight = self._length * self._width * Road2.weight_1 * think
            print("Потребуется:", weight / 1000, "тонн")
        except TypeError:
            print("Переданные параметры не цифры")


# Создаем экземпляр класса и вызываем метод с которым передаем высоту полотна
a = Road2(5000, 20)
a.work(5)
print('Использование объекта со __slots__:  ', asizeof.asizeof(a))

"""
Результаты:
Потребуется: 12500.0 тонн
Использование объекта без __slots__:   328
Потребуется: 12500.0 тонн
Использование объекта со __slots__:   112
Использование Slots позволило уменьшить память в три раза со 328 до 112.
"""

# **************************** Задание 3 *****************************
"""
2. * (вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла логов
из предыдущего задания. Спамер — это клиент, отправивший больше всех запросов; код должен работать
даже с файлами, размер которых превышает объем ОЗУ компьютера.
Примечание:
- Уверены ли вы, что максимальное кол-во запросов - уникально? Т.е. найденный спамер - только один?
Или таких спамеров может быть несколько?
"""


# Логика будет следующая: создаем словарь, в котором IP будет ключ, а значение количество раз
# которое встретится этот IP в файле.
# Если IP не встречался, то присваем новому ключу 1, если встречалось, считываем значение,
# прибавляем единицу и записываем обратно.


@memory_time
def find_spammer():
    spam = {}
    file = open('nginx_logs.txt', 'r', encoding='utf-8')
    for line in file:
        line = line.split(" ")
        spamer = line[0]
        if spamer not in spam:
            spam[spamer] = 1
        else:
            value = spam.get(spamer)
            value += 1
            spam[spamer] = value

    file.close()
    # Често я не знаю как работает код ниже, он создает список кортежей, в котором первое
    # значение IP, а второе количество запросов.
    spam2 = sorted(spam.items(), key=lambda x: x[1], reverse=True)
    print(spam2[:3])


value = find_spammer()
print(f"Выполнение функции ОРИГИНАЛЬНОЙ по памяти {value[1]} Mib и {value[2]} сек")


@memory_time
def find_spammer2():
    file = open('nginx_logs.txt', 'r', encoding='utf-8')
    print(Counter([line.split(" ")[0] for line in file]).most_common(3))
    file.close()


value = find_spammer2()
print(f"Выполнение функции ИЗМЕНЁННОЙ по памяти {value[1]} Mib и {value[2]} сек")
"""
Результаты:
[('216.46.173.126', 2350), ('180.179.174.219', 1720), ('204.77.168.241', 1439)]
Выполнение функции ОРИГИНАЛЬНОЙ по памяти 0.484375 Mib и 0.1416255999999998 сек
[('216.46.173.126', 2350), ('180.179.174.219', 1720), ('204.77.168.241', 1439)]
Выполнение функции ИЗМЕНЁННОЙ по памяти 0.375 Mib и 0.13961950000000023 сек

Уход от словаря в сторону списка с помшью LC и применение Counter из Collection позволило 
существенно минимизировать код, снизить расход памяти и чуть ускорить выполнение программы. 
"""

# **************************** Задание 4 *****************************
"""
# 2.Дан список:
# ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками (добавить кавычку до и 
кавычку после элемента списка, являющегося числом) и дополнить нулём до двух целочисленных разрядов:
# ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
# Подумать, какое условие записать, чтобы выявить числа среди элементов списка? Как модифицировать это условие для чисел 
со знаком?

# Примечание: - Задача обычной сложности: создайте новый список и заполните его нужными значениями,
# включая элементы-кавычки,например: ['в', '"', '05', '"', 'часов',...] или измените существующий список,
# но не добавляйте новые элементы-кавычки, кавычки сразу внесите в элемент-число, например: ['в', '"05"', 'часов',
# ...]
"""


@memory_time
def my_temperature(temp):
    temperature2 = []
    for i in temp:
        if not i.isdigit() and "+" not in i:
            temperature2.append(i)
        else:
            if i.isdigit() and len(i) == 1:
                i = "0" + i
            elif "+" in i:
                i = "+" + "0" + i[1:]
            temperature2.extend(['"', i, '"'])
    print(temperature2)


temperature = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
value = my_temperature(temperature)
print(f"Выполнение функции ОРИГИНАЛЬНОЙ по памяти {value[1]} Mib и {value[2]} сек")


@memory_time
def my_temperature2(temp):
    dec = deque()
    for line in temp:
        if not line.isdigit() and line[0] != "+":
            dec.append(line)
        else:
            if line.isdigit() and len(line) == 1:
                line = "0" + line
            elif line[0] == "+":
                line = "+" + "0" + line[1:]
            dec.extend(['"', line, '"'])
    print(list(dec))


value = my_temperature2(temperature)
print(f"Выполнение функции ИЗМЕНЕННОЙ по памяти {value[1]} Mib и {value[2]} сек")
"""
['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
Выполнение функции ОРИГИНАЛЬНОЙ по памяти 0.00390625 Mib и 0.1116697000000002 сек
['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
Выполнение функции ИЗМЕНЕННОЙ по памяти 0.00390625 Mib и 0.10963650000000058 сек

По сути код такой же. Даже сейчас не знаю как его переписать. Замена списка деком по сути сэкономила 
доли секунды не более. Загруженность памяти такая же осталась. 
"""