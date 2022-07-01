import time
from drrrbot import DrrrbotDataParse
from lib.dictCompare import dictCompare
from BotInstance import Bot
from CLIworker import CLI
from config import config

class Chatworker:
    usersTmp = {}
    talksTmp = {'id':'','talks':{}}
    banusers = {'idban':[]}

    
    def useractionLog(usersCompare, text):
        for userkey in usersCompare:
            user = usersCompare[userkey]
            CLI.cli.append('\n\x1b[46m[userAction]\033[0m "'+user['name']+'" '+text+'\n>>ID:'+user['id']+'\n>>Encip:'+user['encip']+'\n')

    def talksAppend(talkcompare):
        talk = talkcompare[len(talkcompare)]
        
        if not 'type' in talk:
            CLI.cli.append('\x1b[32m[message]\033[0m "'+talk['name']+'" >> "'+talk['message']+'", Time:'+str(talk['time']))

    def userEnterAction(usersCompare):
        Chatworker.useractionLog(usersCompare,'has entered the room.')

        for userkey in usersCompare:
            enteruser = usersCompare[userkey]

            if enteruser['id'] in Chatworker.banusers['idban']:
                Bot.bot.roomKick(enteruser['id'])

    def userLeftAction(usersCompare):
        Chatworker.useractionLog(usersCompare,'has left the room')

    def talkAction(talksCompare):
        Chatworker.talksAppend(talksCompare)


    def worker():
        while True:
            if Bot.bot.roomLoginStatus :
                allRoomData = Bot.bot.getAllRoomData()

                usersdata = DrrrbotDataParse.users(allRoomData)
                talksdata = allRoomData['talks']

                #////USER WORK/////////////////////////////
                recentTalkID = talksdata[0]['id']

                usersCompare = dictCompare(Chatworker.usersTmp, usersdata)

                if len(usersCompare['added']) > 0:
                    Chatworker.userEnterAction(usersCompare['added'])

                elif len(usersCompare['removed']) > 0:
                    Chatworker.userLeftAction(usersCompare['removed'])
                #////////////////////////////////////////////



                #///////////TALKWORK/////////////////////////
                if recentTalkID != Chatworker.talksTmp['id']:
                    talks_dict = {(i + 1): talksdata[i] for i in range(0, len(talksdata))}
                    talksCompare = dictCompare(Chatworker.talksTmp['talks'],talks_dict)



                    if len(talksCompare['added']) > 1:
                        Chatworker.talkAction(talksCompare['added'])

                    if len(talksCompare['updated']) > 1:
                        Chatworker.talkAction(talksCompare['updated'])

                    Chatworker.talksTmp['id'] = recentTalkID
                    Chatworker.talksTmp['talks'] = talks_dict
                #////////////////////////////////////////////
                
                Chatworker.usersTmp = usersdata

            time.sleep(1)