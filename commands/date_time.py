import datetime

from utils.audio import speak


# date and time commands
def date():
    today_date = datetime.date.today()
    speak('A data de hoje é ' + str(today_date))
