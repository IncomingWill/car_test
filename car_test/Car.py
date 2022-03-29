# Title: Car Class
# Program created by William Schaeffer
# CPS 313
# P. 579, Exercise 2, Car Test Program
# 03.15.22

# This Class will hold data for a car, such as year model, make, and current speed
    # This class will have methods to accelerate and decelerate the Car object

# imports for functions

# Car Class

class Car:

# method for initializing data attributes
    # This initializing function accepts the car's year model and make as arguments. 
    # Speed is initialized as 0

    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0
    
# mutator methods

    def set_year_model(self, year_model):
        self.__year_model = year_model

    def set_make(self, make):
        self.__make = make

    def set_speed(self, speed):
        self.__speed = speed

# accessor methods

    def get_year_model(self):
        return self.__year_model

    def get_make(self):
        return self.__make

    def get_speed(self):
        return self.__speed

# additional methods

    # acceleration function to +5 to speed
    def accelerate(self):
        self.__speed += 5    

    # deceleration function to -5 from speed
        # because break is a keyword
    def decelerate(self):
        self.__speed -= 5
    
    def __str__(self):
        return f'Current speed: {self.__speed}'