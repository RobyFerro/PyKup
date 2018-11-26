import os


class Logger:

    def __init__(self):
        if os.path.exists('./log/history.log'):
            print('File exist')
        else:
            print('File does not exists')
            exit(255)

    @staticmethod
    def make_log_file():
        open('./log/history.log')

