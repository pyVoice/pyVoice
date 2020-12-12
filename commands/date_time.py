import datetime

from utils.audio import speak


class DateTimeCommands:
    def __init__(self):
        self.command_list = ['date', 'time']
        self.date_keywords = ['data', 'qual a data', 'data de hoje']

    @staticmethod
    def speak_date():
        today_date = datetime.date.today()
        speak('A data de hoje é ' + str(today_date))
        return f'A data de hoje é {str(today_date)}'

    def get_date_keywords(self):
        return self.date_keywords
