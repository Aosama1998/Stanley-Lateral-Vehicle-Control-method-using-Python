import math 
pi =3.14
#Basic stanley method for lateral Control maneavuring in autonomous car systems 
#Number of assumptions must be made in order for this module to run effectively

#Assume we know cross track error value, the Gain K is obtained through trial and error or assumptions
#and the velocity of the car is given to us or obtained through sensors 

def stanley_Controller(error,Gain,Velocity):
    cross_track_error = error
    Gain_K =Gain 
    velocity_of_car = Velocity
    if error <= 5: 
     steering_angle = math.atan((Gain_K * cross_track_error)/velocity_of_car)

# for large positive corss track error, we add π/2 to the equation to ease with the reaction speed of the controller
    elif cross_track_error > 5: 
     steering_angle = math.atan((Gain_K * cross_track_error)/velocity_of_car) + pi/2
    print(steering_angle) # prints steering angle in radians 
    print(math.degrees(steering_angle))  # prints steering angle in degrees 

stanley_Controller(5,2.5,5)

#We can keep on trying different values for our assumed parameters 

