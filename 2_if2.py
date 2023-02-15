"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def analyze_strings(string_1, string_2):
    
    if type(string_1) != str or type(string_2) != str:
        result = 0
    elif string_1 == string_2:
        result = 1
    elif len(string_1) > len(string_2):
        result = 2
    elif (string_1 != string_2) and string_2 == 'learn':
        result = 3
    
    return result

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    print(analyze_strings(4, '4'))
    print(analyze_strings('4', '4'))
    print(analyze_strings('40', '4'))
    print(analyze_strings('4', 'learn'))
    
if __name__ == "__main__":
    main()
