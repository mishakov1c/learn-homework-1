"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
import settings
import datetime
import ephem
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)

def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)

def get_ephem_planet(planet_name):
    now = datetime.datetime.now()

    if planet_name == 'Mars':
        ephem_planet = ephem.Mars(now)
    elif planet_name == 'Mercury':
         ephem_planet = ephem.Mercury(now)
    elif planet_name == 'Venus':
        ephem_planet = ephem.Venus(now)
    elif planet_name == 'Earth':
        ephem_planet = ephem.Earth(now)
    elif planet_name == 'Jupiter':
        ephem_planet = ephem.Jupiter(now)
    elif planet_name == 'Uranus':
        ephem_planet = ephem.Uranus(now)
    elif planet_name == 'Neptune':
        ephem_planet = ephem.Neptune(now)

    return ephem_planet

def planet_info(update, context):
    user_text = update.message.text
    print(user_text) 
    splitted_text = user_text.split()
    
    try:
        planet_name = splitted_text[1]
        print(planet_name)
        ephem_planet = get_ephem_planet(planet_name)
        const = ephem.constellation(ephem_planet)
        constellation = const[1]
        update.message.reply_text(f'Планета "{planet_name}" находится в созвездии "{constellation}"')   
    except IndexError:
        error_text = "Имя планеты не введено" 
        print(error_text)
        update.message.reply_text(error_text)


    

def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet_info))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
