## @file test_driver.py
#  @author Yousam Asham
#  @brief Driver to test out date_adt.py and pos_adt.py classes
#  @date 11-01-2020
from date_adt import DateT
from pos_adt import GPosT
import math

#testing for DateT
testDate1 = DateT(11,1,2020)
testDate2 = DateT(28,2,2008)
testDate3 = DateT(1,3,2004)
testDate4 = DateT(1,3,2001)
testDate5 = DateT(1,1,2000)
testDate6 = DateT(31,12,2005)
#Flags (could also be bools)
dayMethod = 0
monthMethod = 0
yearMethod = 0
prevMethod = 0
nextMethod = 0
beforeMethod = 0
afterMethod = 0
equalMethod = 0
days_betweenMethod = 0
add_daysMethod = 0

#TESTING THE DAY() METHOD
print("Testing the day() method...")
if testDate1.day() == 11:
    if testDate2.day() == 28:
        if testDate3.day() == 1:
            if testDate4.day() == 1:
                if testDate5.day() == 1:
                    assert testDate6.day() == 31
                    dayMethod = 1
                    print("DONE")

#TESTING THE MONTH() METHOD
print("Testing the month() method...")
if testDate1.month() == 1:
    if testDate2.month() == 2:
        if testDate3.month() == 3:
            if testDate4.month() == 3:
                if testDate5.month() == 1:
                    assert testDate6.month() == 12
                    monthMethod = 1
                    print("DONE")

#TESTING THE YEAR() METHOD
print("Testing the year() method...")
if testDate1.year() == 2020:
    if testDate2.year() == 2008:
        if testDate3.year() == 2004:
            if testDate4.year() == 2001:
                if testDate5.year() == 2000:
                    assert testDate6.year() == 2005
                    yearMethod = 1
                    print("DONE")

#TESTING THE NEXT() METHOD
print("Testing the next() method...")
if testDate1.next().day() == 12 and testDate1.next().month() == 1 and testDate1.next().year() == 2020:
    if testDate2.next().day() == 29 and testDate2.next().month() == 2 and testDate2.next().year() == 2008:
        if testDate3.next().day() == 2 and testDate3.next().month() == 3 and testDate3.next().year() == 2004:
            if testDate4.next().day() == 2 and testDate4.next().month() == 3 and testDate4.next().year() == 2001:
                if testDate5.next().day() == 2 and testDate5.next().month() == 1 and testDate5.next().year() == 2000:
                    assert testDate6.next().day() == 1 and testDate6.next().month() == 1 and testDate6.next().year() == 2006
                    nextMethod = 1
                    print("DONE")

#TESTING THE PREV() METHOD
print("Testing the prev() method...")
if testDate1.prev().day() == 10 and testDate1.prev().month() == 1 and testDate1.prev().year() == 2020:
    if testDate2.prev().day() == 27 and testDate2.prev().month() == 2 and testDate2.prev().year() == 2008:
        if testDate3.prev().day() == 29 and testDate3.prev().month() == 2 and testDate3.prev().year() == 2004:
            if testDate4.prev().day() == 28 and testDate4.prev().month() == 2 and testDate4.prev().year() == 2001:
                if testDate5.prev().day() == 31 and testDate5.prev().month() == 12 and testDate5.prev().year() == 1999:
                    assert testDate6.prev().day() == 30 and testDate6.prev().month() == 12 and testDate6.prev().year() == 2005
                    prevMethod = 1
                    print("DONE")

#TESTING THE BEFORE() METHOD
print("Testing the before() method...")
if testDate1.before(testDate2) == False:
    if testDate2.before(testDate3) == False:
        if testDate3.before(testDate4) == False:
            if testDate3.before(testDate2) == True:
                if testDate5.before(testDate6) == True:
                    assert testDate6.before(testDate1) == True
                    beforeMethod = 1
                    print("DONE")

#TESTING THE AFTER() METHOD
print("Testing the after() method...")
if testDate2.after(testDate1) == False:
    if testDate3.after(testDate2) == False:
        if testDate4.after(testDate3) == False:
            if testDate2.after(testDate3) == True:
                if testDate6.after(testDate5) == True:
                    assert testDate1.after(testDate6) == True
                    afterMethod = 1
                    print("DONE")

#TESTING THE EQUAL() METHOD
print("Testing the equal() method...")
if testDate2.equal(testDate1) == False:
    if testDate3.equal(testDate2) == False:
        if testDate4.equal(testDate3) == False:
            if testDate2.equal(testDate2) == True:
                if testDate6.equal(testDate6) == True:
                    assert testDate5.equal(testDate5) == True
                    equalMethod = 1
                    print("DONE")

#TESTING THE ADD_DAYS() METHOD
print("Testing the add_days() method...")
if testDate2.add_days(1).day() == 29:
    if testDate3.add_days(2).day() == 3:
        if testDate4.add_days(3).day() == 4:
            if testDate2.add_days(4).year() == 2008:
                if testDate6.add_days(5).month() == 1:
                    assert testDate1.add_days(6).day() == 17
                    add_daysMethod = 1
                    print("DONE")
#TESTING THE days_between() METHOD
print("Testing the days_between() method...")
if testDate2.days_between(testDate1) == 4335:
    if testDate3.days_between(testDate4) == 1096:
        if testDate4.days_between(testDate1) == 6890:
            if testDate2.days_between(testDate4) == 2555:
                if testDate6.days_between(testDate5) == 2191:
                    assert testDate1.days_between(testDate6) == 5124
                    days_betweenMethod = 1
                    print("DONE")
total = dayMethod + monthMethod + yearMethod + prevMethod + nextMethod + beforeMethod + afterMethod + equalMethod + days_betweenMethod + add_daysMethod
print("DateT: " + str(total) + '/10 functions passed.')
#testing for GPosT

testPos1 = GPosT(10,56)
testPos2 = GPosT(47,-88)
testPos3 = GPosT(-54, -90)
testPos4 = GPosT(-22, 2)
bearing = 48
distance = 37.5
speed = 23664
#Flags (could also be bools)
latMethod = 0
longMethod = 0
west_ofMethod = 0
north_ofMethod = 0
equalMethodGPosT = 0
moveMethod = 0
distanceMethod = 0
arrival_dateMethod = 0

print("Testing the lat() method...")
assert testPos1.lat() == 10
assert testPos3.lat() == -54
latMethod = 1
print("DONE")

print("Testing the long() method...")
assert testPos2.long() == -88
assert testPos4.long() == 2
longMethod = 1
print("DONE")

print("Testing the west_of() method...")
assert testPos1.west_of(testPos2) == False
assert testPos3.west_of(testPos1) == True
west_ofMethod = 1
print("DONE")

print("Testing the north_of() method...")
assert testPos3.north_of(testPos1) == False
assert testPos4.north_of(testPos3) == True
north_ofMethod = 1
print("DONE")

print("Testing the equal() method...")
assert testPos3.equal(testPos1) == False
assert testPos4.equal(testPos4) == True
equalMethodGPosT = 1
print("DONE")

print("Testing the move() method...")
testPos2.move(bearing, distance)
assert round(testPos2.lat(),4) == 47.2251
assert round(testPos2.long(), 4) == -87.631
testPos4.move(bearing, distance)
assert round(testPos4.lat(),4) == -21.7741
assert round(testPos4.long(),4) == 2.2699
moveMethod = 1
print("DONE")

print("Testing the distance() method...")
assert round(testPos3.distance(testPos4),4) == 8209.5470
assert round(testPos2.distance(testPos1),4) == 12706.4544
distanceMethod = 1
print("DONE")

print("Testing the arrival_date() method...")
Cairo = GPosT(30.0626, 31.2497)
Toronto = GPosT(43.651070, -79.347015)
assert Cairo.arrival_date(Toronto, testDate2, speed).day() == 28
assert Toronto.arrival_date(Cairo, testDate3, speed).day() == 1
arrival_dateMethod = 1
print("DONE")
total2 = latMethod + longMethod + west_ofMethod + north_ofMethod + equalMethodGPosT + moveMethod + distanceMethod + arrival_dateMethod
print("GPosT: " + str(total2) + '/8 functions passed.')
