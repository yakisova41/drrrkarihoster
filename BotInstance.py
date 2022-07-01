from config import config
from drrrbot import Drrrbot, DrrrbotDataParse

class Bot:
    bot = object
    def login():
        try:
            Bot.bot = Drrrbot(
                config['name'],
                config['icon'],
                config['useragent']
            )
            
        except ZeroDivisionError as e:
            Bot.bot.roomLogout()
            Bot.bot.exit()
            print(e)
        finally:
            Bot.bot.roomLogout()