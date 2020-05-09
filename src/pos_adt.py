## @file pos_adt.py
#  @author Yousam Asham
#  @brief A Global position module that implements many functions
#  @date 11-01-2020
import math
from date_adt import DateT
global earthRadius
earthRadius = 6371
## @brief An ADT for the class GPosT
class GPosT:
    ## @brief A constructor for the GPosT class
    #  @details Initializes the attributes of the GPosT objects. Some assumptions made include that the latitude is between -90 and 90 degrees while the longitude is between -180 to 180.
    #  @param phi represents the latitude
    #  @param lam represents the longitude
    def __init__(self, phi, lam):
        self.phi = phi
        self.lam = lam
    ## @brief A getter method for the latitude
    #  @details Assumptions: None
    #  @return The latitude
    def lat(self):
        return self.phi
    ## @brief A getter method for the longitude
    #  @details Assumptions: None
    #  @return The longitude
    def long(self):
        return self.lam
    ## @brief Compares if a position is west of the current position
    #  @details Assumptions: A position is west of another location if the it has a smaller (or more negative) longitude.
    #  @param p represents position to be compared to
    #  @return True if it is west of, False if not west of
    def west_of(self, p):
        if (self.lam < p.lam):
            return True
        else:
            return False
    ## @brief Compares if a position is north of the current position
    #  @details Assumptions: A position is north of another position if it has a greater (or more positive) latitude.
    #  @param p represents position to be compared to
    #  @return True if it is north of, False is not north of
    def north_of(self, p):
        if (self.phi > p.phi):
            return True
        else:
            return False
    ## @brief Checks if two positions are equal
    #  @details Assumptions: None
    #  @param p represents position to be compared to
    #  @return True if they are equal (or within 1 km away from each other), False if they are not equal
    def equal(self, p):
        if (p.lam == self.lam) and (p.phi == self.phi):
            return True
        if (self.distance(p) < 1):
            return True
        else:
            return False
    ## @brief Moves the current GPosT object to a new position
    #  @details Assumptions: None
    #  @param b represents bearing to be moved towards
    #  @param d represents distance to be moved
    def move(self, b, d):
        phi = math.radians(self.phi)
        angularDistance = (d/earthRadius)
        b = math.radians(b)
        lam = math.radians(self.lam)
        self.phi = math.asin((math.sin(phi)*(math.cos(angularDistance)))+((math.cos(phi))*(math.sin(angularDistance))*(math.cos(b))))
        self.lam = lam + (math.atan2((math.sin(b) * math.sin(angularDistance) * (math.cos(phi))),((math.cos(angularDistance))-((math.sin(phi))*(math.sin(self.phi))))))
        self.phi = math.degrees(self.phi)
        self.lam = math.degrees(self.lam)
    ## @brief Calculates distance between the current object and point p
    #  @details Assumptions: Distance to be returned is in kilometers
    #  @param p represents the point to calculate the distance to
    #  @return The distance between the two positions
    def distance(self, p):
        deltaPhi = math.radians(abs(p.phi - self.phi))
        deltaLam = math.radians(abs(p.lam - self.lam))
        phi = math.radians(self.phi)
        phi2 = math.radians(p.phi)
        a = ((math.sin(deltaPhi/2))**2) + (math.cos(phi))*(math.cos(phi2))*((math.sin(deltaLam/2))**2)
        c = 2*(math.atan2((math.sqrt(a)),(math.sqrt(1 - a))))
        d = earthRadius * c
        return d
    ## @brief Calculates the date of arrival for someone starting at the current position on date d and moving to position p at speed s
    #  @details Assumptions: The starting day always starts at 00:00:00
    #  @param p represents the end position
    #  @param d represents the date the travel starts
    #  @param s represents the speed of travel
    #  @return The date of arrival (a DateT object)
    def arrival_date(self, p, d, s):
        distance = self.distance(p)
        days_taken = distance/s
        date_arrival = d.add_days(int(days_taken))
        return date_arrival
