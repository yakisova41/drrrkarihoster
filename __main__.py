import threading
from BotInstance import Bot
from CLIworker import CLI
import Commands
from Chatworker import Chatworker
from AntiAFK import AntiAFK

def cliworker():
    CLI.start()

    CLI.cli.addCommand('send',Commands.send)
    CLI.cli.addCommand('login',Commands.login)
    CLI.cli.addCommand('logout',Commands.logout)
    CLI.cli.addCommand('newhost',Commands.newhost)
    CLI.cli.addCommand('kick',Commands.kick)
    CLI.cli.addCommand('ban',Commands.ban)
    CLI.cli.addCommand('unban',Commands.unban)
    CLI.cli.addCommand('newroomname',Commands.newroomname)
    CLI.cli.addCommand('change-afk-mode',Commands.changeAFKmode)
    CLI.cli.addCommand('change-afk-text',Commands.changeAFKtext)
    CLI.cli.addCommand('change-afk-interval',Commands.changeAFKinterval)
    CLI.listen()


if __name__ == "__main__":
    Bot.login()

    cliworker = threading.Thread(target=cliworker)
    chatworker = threading.Thread(target=Chatworker.worker)
    antiafk = threading.Thread(target=AntiAFK.worker)
    cliworker.start()
    chatworker.start()
    antiafk.start()