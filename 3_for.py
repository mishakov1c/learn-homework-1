"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    phones_list = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
    ]
    
    total_sold = 0
    total_sold = 0

    for item in phones_list:
        item_sold = 0
        total_average = 0

        for sale in  item['items_sold']:
            item_sold += sale
        
        product = item['product']
        print(f'Всего продано {product} {item_sold} шт. ')
        item_average = int(item_sold / 12)
        print(f'Среднее количество продаж {product} {item_average} шт. ')

        total_sold += item_sold
        total_average = int(total_sold / 12)
      
    print(f'Суммарное количество продаж всех товаров: {total_sold} шт.')
    print(f'Среднее количество продаж всех товаров: {total_average} шт.')

    
if __name__ == "__main__":
    main()
