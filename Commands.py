from BotInstance import Bot
from CLIworker import CLI
from Chatworker import Chatworker
from config import config
from AntiAFK import AntiAFK 
def send(cmd):
    sendmesstage = cmd.setarg(1,'Send messtage','Enter the message you want to send!')
    cmd.setDescription('Send message')

    def send():
        if Bot.bot.roomLoginStatus:
            Bot.bot.roomSend(sendmesstage)
            cmd.print('Message sent! >>'+str(sendmesstage))
        else:
            cmd.print('Could not send because you are not logged in to the room')

    cmd.run(send)
    return cmd

def login(cmd):
    roomid = cmd.setarg(1,'Roomid','Please enter roomid!')
    cmd.setDescription('Login to Room')

    def login():
        if not Bot.bot.roomLoginStatus:
            Bot.bot.roomLogin(roomid)
            cmd.print('logged in!')
        else:
            cmd.print('You are already logged in to the room')

    cmd.run(login)
    return cmd

def logout(cmd):
    cmd.setDescription('Logout of the Room')

    def logout():
        if Bot.bot.roomLoginStatus:
            Bot.bot.roomLogout()
            cmd.print('logged out!')
        else:
            cmd.print('You have not entered the room')

    cmd.run(logout)
    return cmd

def newhost(cmd):
    userid = cmd.setarg(1,'Newhost userid','Please enter newhost userid!')
    cmd.setDescription('Specify new host')

    def newhost():
        if Bot.bot.roomLoginStatus:
            Bot.bot.roomNewhost(userid)
            
            cmd.print('newhost >> %s' %(userid))
    cmd.run(newhost)
    
    return cmd

def kick(cmd):
    userid = cmd.setarg(1,'Kick userid','Please enter kick userid!')
    cmd.setDescription('Kick user')

    def kick():
        if Bot.bot.roomLoginStatus:
            Bot.bot.roomKick(userid)

            cmd.print('kick >> %s' %(userid))

    cmd.run(kick)
    
    return cmd

def newroomname(cmd):
    roomname = cmd.setarg(1,'new roomname','Please enter new roomname!')
    def newname():
        if Bot.bot.roomLoginStatus:
            Bot.bot.roomNewname(roomname)

            cmd.print('newRoomname >> %s'%(roomname))
    
    cmd.run(newname)

def ban(cmd):
    userid = cmd.setarg(1,'ban userid','Please enter ban userid!')

    cmd.setDescription('Ban user')

    def ban():
        Chatworker.banusers['idban'].append(userid)
        Bot.bot.roomKick(userid)

        cmd.print('BANNED >> %s' %(userid))

    cmd.run(ban)
    return cmd

def unban(cmd):
    userid = cmd.setarg(1,'unban userid','Please enter unban userid!')

    cmd.setDescription('Ban user')

    def unban():
        Chatworker.banusers['idban'].remove(userid)
        cmd.print('Unbanned >> %s' %(userid))

    cmd.run(unban)
    return cmd

def changeAFKmode(cmd):
    mode = cmd.setarg(1,'afkmode','Please enter afkmode')
    cmd.setDescription('set AFKmode 1:timereport 2:text')

    def change():
        AntiAFK.afktype = int(mode)
        cmd.print('Changed afk mode >> %s' %(mode))

    cmd.run(change)
    return cmd  

def changeAFKtext(cmd):
    text = cmd.setarg(1,'afktext','Please enter afktext')
    cmd.setDescription('set anti afk text')

    def change():
        AntiAFK.afktext = text
        cmd.print('Changed afk text >> %s' %(text))

    cmd.run(change)
    return cmd  

def changeAFKinterval(cmd):
    interval = cmd.setarg(1,'afk interval','Please enter afk interval')
    cmd.setDescription('set anti afk interval')

    def change():
        AntiAFK.afkinterval = int(interval)
        cmd.print('Changed afk interval >> %s' %(interval))

    cmd.run(change)
    return cmd  