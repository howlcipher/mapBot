from datetime import datetime

import pytz


# botTime class
class sTime:
    def __init__(self, ct: str):
        self.ct = ct


# botTime
def currentTime():
    tz_NY = pytz.timezone('America/New_York')
    datetime_NY = datetime.now(tz_NY)
    return datetime_NY.strftime("%H:%M:%S")
