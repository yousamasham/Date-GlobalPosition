## @file date_adt.py
#  @author Yousam Asham
#  @brief This module creates date related calculations using several methods. This includes getting the next and previous day and calculation differences between two given days.
#  @date 09-01-2020
import datetime
## @brief An ADT for the class DateT
#  @details Some assumptions made include that the user will be inputting correct dates in order for the module to return some correct dates.
class DateT:
  ## @brief A constructor for the DateT class
  #  @details Initializes the attributes of the DateT objects, assuming that the user inputs correct/valid AD dates.
  #  @param d represents the day number eg: 0-31
  #  @param m represents the month number eg: 1-12
  #  @param y represents the yea number eg: 2020
  def __init__(self, d, m, y):
      self.d = d
      self.m = m
      self.y = y
  ## @brief A getter method for the day number.
  #  @details Assumptions: None
  #  @return The day number
  def day(self):
      return self.d
  ## @brief A getter method for the month number.
  #  @details Assumptions: None
  #  @return The month number
  def month(self):
      return self.m
  ## @brief A getter method for the year number.
  #  @details Assumptions: None
  #  @return The year
  def year(self):
      return self.y
  ## @brief A method to provide the next day.
  #  @details Assumptions: Leap years occur every 4 years.
  #  @return The day after the current object
  def next(self):
      if (self.m == 2) and (self.d == 28) and (self.y % 4 != 0):
          nextDate = DateT(1, self.m+1, self.y)
      elif ((self.m == 1) or (self.m == 3) or (self.m == 5) or (self.m == 7) or (self.m == 8) or (self.m == 10) or (self.m == 12)) and (self.d == 31):
          nextDate = DateT(1, self.m+1, self.y)
          if (nextDate.m == 13):
              nextDate.m = 1
              nextDate.y += 1
      elif ((self.m == 4) or (self.m == 6) or (self.m == 9) or (self.m == 11)) and (self.d == 30):
          nextDate = DateT(1, self.m+1, self.y)
      else:
          nextDate = DateT(self.d+1, self.m, self.y)
      return nextDate
  ## @brief A method to provide the previous day
  #  @details Assumptions: Leap years occur every 4 years
  #  @return The day before the current object
  def prev(self):
      if (self.d == 1):
          prevDate = DateT(self.d, self.m-1, self.y)
          if prevDate.m == 0:
              prevDate.m = 12
              prevDate.y -= 1
              prevDate.d = 31
          elif (prevDate.m == 1) or (prevDate.m == 3) or (prevDate.m == 5) or (prevDate.m == 7) or (prevDate.m == 8) or (prevDate.m == 10) or (prevDate.m == 12):
              prevDate.d = 31
          elif (prevDate.m == 2):
              if (prevDate.y % 4 == 0):
                  prevDate.d = 29
              else:
                  prevDate.d = 28
          else:
              prevDate.d = 30
      else:
          prevDate = DateT(self.d-1, self.m, self.y)
      return prevDate
  ## @brief A method to provide whether the day provided is before the current day
  #  @details Assumptions: None
  #  @param d represents the day to be compared
  #  @return True if the day is before the current day, false if the day is not before the current day
  def before(self, d):
      if (self.y < d.y):
          return True
      elif (self.m < d.m) and (self.y == d.y):
          return True
      elif (self.d < d.d) and (self.m == d.m):
          return True
      return False
  ## @brief A method to provide whether the day provided is after the current day
  #  @details Assumptions: None
  #  @param d represents the day to be compared
  #  @return True if the day is after the current day, false if the day is not after the current day
  def after(self, d):
      if (self.y > d.y):
          return True
      elif (self.m > d.m) and (self.y == d.y):
          return True
      elif (self.d > d.d) and (self.m == d.m):
          return True
      else:
          return False
  ## @brief A method to provide whether the day provided is equal to the current day
  #  @details Assumptions: A day is equal to another day if and only if they are the same day.
  #  @param d represents the day to be compared
  #  @return True if the day is equal to the current day, false if the day is not equal to the current day
  def equal(self, d):
      if (self.y == d.y) and (self.m == d.m) and (self.d == d.d):
          return True
      else:
          return False
  ## @brief Adds a specific number of days to a DateT objects
  #  @details Assumptions: None
  #  @param n represents the number of days to be added
  #  @return The date after n days have been added to the DateT object
  def add_days(self, n):
      date = datetime.date(self.y, self.m, self.d)
      newDate = date + datetime.timedelta(days = n)
      newerDate = DateT(newDate.day, newDate.month, newDate.year)
      return newerDate
  ## @brief Calculates the difference in days between two dates
  #  @details Assumptions: There are no things such as negative days, and so the value returned is always the absolute value.
  #  @param d represents a date
  #  @return The difference betweent the date object and d in days
  def days_between(self, d):
      currentDate = datetime.date(self.y, self.m, self.d)
      dDate = datetime.date(d.y, d.m, d.d)
      diff = currentDate - dDate
      return abs(diff.days)
  ## @citations https://www.programiz.com/python-programming/datetime
