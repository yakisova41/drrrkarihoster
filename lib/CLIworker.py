import sys
import os

class CLIworker:
    def __init__(self):
        self.clearConsole()
        self.commands = {'help':self.help}
        self.nameToAsk = 'CLI'
        self.notfoundFunction = self.commandnotfound

    def addCommand(self, commandName, commandFunction):
        self.commands[commandName] = commandFunction

    def setAskname(self, name):
        self.nameToAsk = name

    def clearConsole(self):
        command = 'clear'
        if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
            command = 'cls'
        os.system(command)

    def worker(self):
        while True:
            inputtext = input('%s> ' %(self.nameToAsk))
            splitedtext = inputtext.split(' ')
            commandsArray = list(filter(None, splitedtext))

            if(commandsArray[0] in self.commands):
                commandFunction = self.commands[commandsArray[0]]
                commandFunction(CLICommand(commandsArray, True))
            else:
                self.notfoundFunction(CLICommand(commandsArray, True))

    def append(self, output):
        sys.stdout.write("\033[2K\033[G")
        sys.stdout.flush()
        print(str(output), end="")
        print('\n%s> ' %(self.nameToAsk), end="")

    def commandnotfound(self, cmd):
        commandname = cmd.setarg(0, 'commandName')
        cmd.print('Command "%s" was not found' %(commandname))
        cmd.print('Type "help" to display help for a command')

    def help(self,cmd):
        def help():
            for commandname in self.commands:
                command = self.commands[commandname]
                commandobj = command(CLICommand([commandname], False))

                cmd.print('%s '%(commandname),end="")
                
                for arg in commandobj.args:
                    cmd.print(" [%s] "%(arg['name']),end="")

                cmd.print(": %s"%(commandobj.description))
        cmd.run(help)
        return cmd


class CLICommand:
    def __init__(self, args, Runmode):
        self.inputargs = args
        self.Runmode = Runmode
        self.args = []
        self.description = "%s command"%(self.inputargs[0])

    def setarg(self, number, name, missingArgErrorText = "Missing argument"):
        self.args.insert(number, {
            'name':name
        })

        if self.Runmode:
            if number < len(self.inputargs):
                return self.inputargs[number]
            else:
                self.Runmode = False
                print(missingArgErrorText,end="\n\n")

    def setDescription(self, description):
        self.description = description

    def print(self, output, end = "\n"):
        if self.Runmode:
            print(output, end=end)

    def run(self, function, args = []):
        if self.Runmode:
            function(*args)
    