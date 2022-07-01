import datetime
import time
from zoneinfo import ZoneInfo
from BotInstance import Bot
from CLIworker import CLI

class AntiAFK:
    afktype = 1
    afktext = 'Default anti AFK text'
    afkinterval = 899

    def worker():
        time.sleep(100)
        while True:
            if AntiAFK.afktype == 1:
                send = datetime.datetime.now(ZoneInfo("Asia/Tokyo"))
            elif AntiAFK.afktype == 2:
                send = AntiAFK.afktext
            else:
                send = datetime.datetime.now(ZoneInfo("Asia/Tokyo"))

            Bot.bot.roomSend(send)

            time.sleep(AntiAFK.afkinterval)