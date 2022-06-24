from drrrbot import Drrrbot, DrrrbotDataParse
import sys
import threading
import datetime
import time
from zoneinfo import ZoneInfo

#0fde5ac9683bfab65e7e26b0ec1554cf

def Cli():
    CommandList = {
        'help':CliCommand_Help,
        'send':CliCommand_Send,
        'login':CliCommand_Login,
        'logout':CliCommand_Logout,
        'newhost':CliCommand_newhost,
        'kick':CliCommand_kick,
        'newname':CliCommand_newroomname,
        'getmember':CliCommand_getmember
    }

    while True:
        commandinput = input('\x1b[32mDrrrKariBot\033[0m> ')
        splitCommand = commandinput.split(' ')

        if(splitCommand[0] in CommandList):
            CommandList[splitCommand[0]](splitCommand)
        else:
            CommandList['help'](splitCommand)

#CLI commands
def CliCommand_Help(arg):
    print('Help')

def CliCommand_Send(arg):
    if len(arg) > 1:
        bot.roomSend(arg[1])
        print('sended! >>'+str(arg[1]))
    else:
        print('Enter the message you want to send!')

def CliCommand_Login(arg):
    if len(arg) > 1:
        bot.roomLogin(arg[1])
        print('logged in!')
    else:
        print('Please enter roomid!!!!')

def CliCommand_Logout(arg):
    yorno = 0
    
    while True:
        confirmation = input('Do you really want to log out?[Y/n]')

        if confirmation == 'y' or confirmation == 'Y':
            yorno = 1
            break
        if confirmation == 'n' or confirmation == 'N':
            yorno = 0
            break

    if yorno == 1:
        bot.roomLogout()
        print('Logged out!')

def CliCommand_kick(arg):
    if len(arg) > 1:
        bot.roomKick(arg[1])
        print('Kicked! >>'+str(arg[1]))
    else:
        print('Please enter userid!!!!')

def CliCommand_newhost(arg):
    if len(arg) > 1:
        bot.roomNewhost(arg[1])
        print('Newhost >>'+str(arg[1]))
    else:
        print('Please enter userid!!!!')

def CliCommand_newroomname(arg):
    if len(arg) > 1:
        bot.roomNewname(arg[1])
        print('Newname >>'+str(arg[1]))
    else:
        print('Please enter new room name!!!!')

def CliCommand_getmember(arg):
    print(DrrrbotDataParse.users(bot.getAllRoomData()))

def cliappend(text):
    sys.stdout.write("\033[2K\033[G")
    sys.stdout.flush()
    print(str(text)+'\n\x1b[32mDrrrKariBot\033[0m>', end="")



def TimeReport():
    time.sleep(899)
    while True:
        bot.roomSend(datetime.datetime.now(ZoneInfo("Asia/Tokyo")))
        time.sleep(899)



def ChatWorker():
    users_tmp = 0
    while True:
        if(bot.roomLoginStatus):
            users = DrrrbotDataParse.users(bot.getAllRoomData())
            
            if len(users) != users_tmp:
                cliappend(users)
            
            users_tmp = len(users)

        time.sleep(5)



if __name__ == "__main__":
    try:
        bot = Drrrbot(
            'うんぶり',
            'usa',
            'Mozilla/5.0 (iphone; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/102.0.5005.87 Mobile/15E148 Safari/604.1'
        )

        cliThread = threading.Thread(target=Cli)
        TimeReportThread = threading.Thread(target=TimeReport)
        ChatWorkerThread = threading.Thread(target=ChatWorker)

        cliThread.start()
        TimeReportThread.start()
        ChatWorkerThread.start()

    except ZeroDivisionError as e:
        bot.roomLogout()
        bot.exit()
        print(e)

    finally:
        bot.roomLogout()

