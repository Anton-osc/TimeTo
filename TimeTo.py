import datetime
from datetime import datetime as dt
import json

class TimeTo():
    def __init__(self, year, month, day, hour, min_):
        '''Values we get from user'''
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour 
        self.min = min_ 
        self.sec = 0
        '''Const'''
        self.daysInYear = 365
        self.hoursInDay = 24
        self.minInHour = 60
        self.secInHour = 60
        '''Amount days in Months'''
        self.daysInJanuary = 31                         #1
        self.daysInFebruary = self.check_leapYear() #2
        self.daysInMarch = 31                           #3
        self.daysInApril = 30                           #4
        self.daysInMay = 31                             #5
        self.daysInJune = 30                            #6
        self.daysInJuly = 31                            #7
        self.daysInAugust = 31                          #8
        self.daysInSeptember = 30                       #9
        self.daysInOctober = 31                         #10
        self.daysInNovember = 30                        #11
        self.daysInDecember = 31                        #12
        self.month_numb = {
            1     :   self.daysInJanuary,
            2     :   self.daysInFebruary,
            3     :   self.daysInMarch,
            4     :   self.daysInApril,
            5     :   self.daysInMay,
            6     :   self.daysInJune,
            7     :   self.daysInJuly,
            8     :   self.daysInAugust,
            9     :   self.daysInSeptember,
            10    :   self.daysInOctober,
            11    :   self.daysInNovember,
            12    :   self.daysInDecember
            }

    def count(self):
        time_to = [{
        'days'      : self.count_days(),
        'hours'     : self.count_hours(),
        'minutes'   : self.count_mins(),
        'seconds'   : self.count_seconds()
        }]
        to_json = json.dumps(time_to)
        print(to_json)

    def count_days(self):
        now = dt.now()
        nowTupple = now.timetuple()
        now_year = nowTupple[0]
        now_month = nowTupple[1]
        now_day = nowTupple[2]
        #Days to event#
        daysToEvent = 0 
        if now_month < self.month: 
            range_month = []
            for i in range(now_month, self.month):
                range_month.append(i)
            n = 0
            for i in range_month:
                if n == 0:
                    daysToEvent = self.month_numb[now_month] - now_day
                else:    
                    daysToEvent += self.month_numb[i]
                n += 1
            daysToEvent += self.day
            
        elif now_month > self.month: 
            range_month = []
            for i in range(now_month, 13):
                range_month.append(i)
            n = 0
            for i in range_month:
                if n == 0:
                    daysToEvent = self.month_numb[now_month] - now_day
                else:
                    daysToEvent += self.month_numb[i]
                n += 1
            range_month.clear()
            for i in range(1, self.month): 
                range_month.append(i)
            n = 0
            for i in range_month:
                daysToEvent += self.month_numb[i]
            daysToEvent += self.day
            
            if self.daysInFebruary == 29 and now_year != self.year:
                daysToEvent = daysToEvent - self.daysInYear - 1
            elif self.daysInFebruary == 28 and now_year != self.year:
                daysToEvent -= self.daysInYear
            else:
                raise TypeError   

        elif now_month == self.month and self.year == now_year:
            daysToEvent = self.day - now_day
        elif now_month == self.month and self.year != now_year:
            daysToEvent = self.day - now_day
            
        daysToEvent = daysToEvent + self.count_years()

        return daysToEvent

    def check_leapYear(self):
        leap_years = []
        n = dt.now().timetuple()[0]
        for i in range(200):
                n += 4
                if n / 100 == int(n / 100):
                    if n / 400 == int(n / 400):
                        leap_years.append(n)
                    else:
                        pass
                else:
                    leap_years.append(n)

        for i in leap_years:
            if self.year == i:
                daysInFebruary = 29
                break
            else: 
                daysInFebruary = 28
        return daysInFebruary

    def count_years(self):
        daysToEvent = 0
        now = dt.now()
        nowTupple = now.timetuple()
        now_year = nowTupple[0]
        now_month = nowTupple[1]
        now_day = nowTupple[2]
        years = []
        years.append(now_year)
        while now_year != self.year:
            now_year += 1
            years.append(now_year)
        n = 0
        now_year = nowTupple[0]
        for i in range(self.year - now_year):
            n += 1
            if years[n] / 4 == int(years[n] / 4):
                if years[n] / 100 == int(years[n] / 100):
                    if years[n] / 400 == int(years[n] / 400):
                        daysToEvent += self.daysInYear + 1
                    else:
                        daysToEvent += self.daysInYear
                else:
                    daysToEvent += self.daysInYear + 1
            else:
                daysToEvent += self.daysInYear
            if n == 1:
                if years[0] / 4 == int(years[0] / 4):
                    print(years[0])
                    if years[0] / 100 == int(years[0] / 100):
                        if years[0] / 400 == int(years[0] / 400):
                            daysToEvent += self.daysInYear + 1
                        else:
                            daysToEvent += self.daysInYear
                    else:
                        daysToEvent += self.daysInYear + 1
        return daysToEvent
    def count_hours(self):
        #HOURS#
        now = dt.now()
        nowTupple = now.timetuple()
        now_year = nowTupple[0]
        now_month = nowTupple[1]
        now_day = nowTupple[2]
        now_hour = str(nowTupple[3])

        hoursToEvent = 0
        if str(now_hour) == '00' or str(now_hour) == '0':
            now_hour = 0
        elif str(now_hour)[0] == '0' and len(str(now_hour)) > 1:
            now_hour = str(now_hour).replace('0', '')

        hoursToEvent = self.hoursInDay - int(now_hour) + self.hour 
        if hoursToEvent < 24:
            pass
        else:
            hoursToEvent = self.hour - int(now_hour)
        if self.count_days() == 1:
            hoursToEvent -= 1
            if hoursToEvent < 0:
                hoursToEvent += 24
        return hoursToEvent

    def count_mins(self):
        #MINUTES#
        now = dt.now()
        nowTupple = now.timetuple()
        now_min = str(nowTupple[4])
        minsToEvent = 0
        if str(now_min) == '00' or str(now_min) == '0':
            now_min = 0
        elif str(now_min)[0] == '0' and len(str(now_min)) > 1:
            now_min = str(now_min).replace('0', '')

        minsToEvent = self.minInHour - int(now_min) + self.min 
  
        if minsToEvent < 59:
            minsToEvent -= 1
        else:
            minsToEvent -= 60
            if str(minsToEvent)[0] == '-':
                minsToEvent += 60

        if len(str(minsToEvent)) == 1:
            minsToEvent = '0' + str(minsToEvent)

        return minsToEvent 

    def count_seconds(self):
        now = dt.now()
        nowTupple = now.timetuple()
        now_sec = str(nowTupple[5])
        secToEvent = 0
        #SECONDS#
        if str(now_sec) == '0':
            now_sec = 0
        elif str(now_sec)[0] == '0':
            now_sec = str(now_sec).replace('0', '')

        secToEvent = self.secInHour - int(now_sec) + self.sec
     
        if secToEvent < 59:
            secToEvent -= 1
        else:
            secToEvent -= 60
            if str(secToEvent)[0] == '-':
                secToEvent += 60

        if len(str(secToEvent)) == 1:
            secToEvent = '0' + str(secToEvent)
        return(secToEvent)
