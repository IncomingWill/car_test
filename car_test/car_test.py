# Title: Car Test Program
# Program created by William Schaeffer
# CPS 313
# P. 579, Exercise 2, Car Test Program
# 03.15.22

# This program will showcase the car class and it's member functions

# imports for class

import Car

# Main Function

def main():
   
    my_car = Car.Car(2012, 'Nissan')

    # Display the car's data, blocked out for testing purposes

    #print('Model Year: ', my_car.get_year_model())
    #print('Make: ', my_car.get_make())
    #print('Speed: ', my_car.get_speed())

    print('Car is accelerating:')
    for i in range(5):
        my_car.accelerate()        
        print(my_car)

    print()

    print('Car is braking:')
    for i in range(5):
        my_car.decelerate()        
        print(my_car)



if __name__ == '__main__':
    main()                                                      # call main function

