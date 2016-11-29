__auth__ = 'NguyenTTin'

class Clock(object):
    def __doc__(self):
        return(''' The init method to check the value of input which are following the right format or not?''')

    def __init__(self, hour, minute, second):
        self.set_clock(hour, minute,second)

    def set_clock(self, hour, minute, second):
        if type(hour) == int and hour >= 0 and hour < 24:
            self._hour = hour
        else:
            raise TypeError("You have entered wrong hour format")
        if type(minute) == int and minute >= 0 and minute < 60:
            self.__minute = minute
        else:
            raise TYpeError("You have entered wrong minute format")
        if type(second) == int and second >= 0 and second < 60:
            self.__second = second
        else:
            raise TypeError("You have entered wrong second format")

    def tick(self):
        if self.__second == 59:
            self.__second = 0
            if self.__minute == 59:
                self.__minute = 0
                if self._hour == 23:
                    self._hour = 0
                else:
                    self._hour += 1
            else:
                self.__minute += 1
        else:
            self.__second += 1

    def __str__(self):
        return (" The time is {0:2d}:{1:2d}:{2:2d}".format(self._hour,self.__minute,self.__second))



class Calendar(object):

    months = (31,28,31,30,31,30,31,31,30,31,30,31)
    date_style = "British"

    @staticmethod
    def leapyear(year):
        """
        The method leapyear returns True if the parameter year
        is a leap year, False otherwise
        """

        if year % 4 == 0:
            if year % 100 == 0:
                # divisible by 4 and by 100
                if year % 400 == 0:
                    leapyear = True
                else:
                    leapyear = False
            else:
                # divisible by 4 but not by 100
                leapyear = True
        else:
            # not divisible by 4
            leapyear = False

        return leapyear


    def __init__(self, d, m, y):
        """
        d, m, y have to be integer values and year has to be
        a four digit year number
        """

        self.set_Calendar(d,m,y)


    def set_Calendar(self, d, m, y):
        """
        d, m, y have to be integer values and year has to be
        a four digit year number
        """

        if type(d) == int and type(m) == int and type(y) == int:
            self.__days = d
            self.__months = m
            self.__years = y
        else:
            raise TypeError("d, m, y have to be integers!")


    def __str__(self):
        if Calendar.date_style == "British":
            return "{0:02d}/{1:02d}/{2:4d}".format(self.__days,
                                                   self.__months,
                                                   self.__years)
        else:
            # assuming American style
            return "{0:02d}/{1:02d}/{2:4d}".format(self.__months,
                                                   self.__days,
                                                   self.__years)



    def advance(self):
        """
        This method advances to the next date.
        """

        max_days = Calendar.months[self.__months-1]
        if self.__months == 2 and Calendar.leapyear(self.__years):
            max_days += 1
        if self.__days == max_days:
            self.__days= 1
            if self.__months == 12:
                self.__months = 1
                self.__years += 1
            else:
                self.__months += 1
        else:
            self.__days += 1


class CalendarClock(Clock, Calendar):
    """
        The class CalendarClock implements a clock with integrated
        calendar. It's a case of multiple inheritance, as it inherits
        both from Clock and Calendar
    """

    def __init__(self,day, month, year, hour, minute, second):
        Clock.__init__(self,hour, minute, second)
        Calendar.__init__(self,day, month, year)


    def tick(self):
        """
        advance the clock by one second
        """
        previous_hour = self._hours
        Clock.tick(self)
        if (self._hours < previous_hour):
            self.advance()

    def __str__(self):
        return Calendar.__str__(self) + ", " + Clock.__str__(self)


c = CalendarClock(28,11,2016,16,30,30)
print(c.__str__())