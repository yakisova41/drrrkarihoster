from lib.CLIworker import CLIworker

class CLI:
    cli = CLIworker()

    def start():
        print('DrrrKari Hoster v1.0 (https://github.com/yakisova41/drrrkarihoster)')
        print('Made by Yakisova41\n')

        CLI.cli.setAskname('\x1b[32mDrrrKariHoster\033[0m')  

    def listen():
        CLI.cli.worker()