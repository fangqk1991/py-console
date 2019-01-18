# coding: utf-8
import traceback
from datetime import datetime
from termcolor import colored


class FCConsole:

    @staticmethod
    def d(*args):

        print('----------- %s -----------' % colored(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        print('----------- %s -----------' % colored(traceback.format_stack()[-2].strip(), 'white'))

        for obj in args:
            if isinstance(obj, list):
                print(colored('--- list start ---', 'magenta'))
                for item in obj:
                    print(colored(item, 'green'))
                print(colored('--- list end ---', 'magenta'))
            else:
                print(type(obj), end=' ')
                print(colored(obj, 'magenta'))

    @staticmethod
    def i(*args):

        for obj in args:
            if isinstance(obj, list):
                print(colored('--- list start ---', 'magenta'))
                for item in obj:
                    print(colored(item, 'green'))
                print(colored('--- list end ---', 'magenta'))
            else:
                print(colored(obj, 'magenta'), end=' ')

        print('')

    @staticmethod
    def special(*args, **kwargs):

        color = kwargs.get('color', 'magenta')
        on_color = kwargs.get('on_color', 'on_blue')

        for obj in args:
            if isinstance(obj, list):
                print(colored('--- length: %d ---' % len(obj), color))
                print(colored('--- list start ---', color))
                for item in obj:
                    print(colored(item, 'green'))
                print(colored('--- list end ---', color))
            else:
                print(colored(obj, color, on_color=on_color), end=' ')

        print('')

    @staticmethod
    def print(*args):
        FCConsole.i(*args)

