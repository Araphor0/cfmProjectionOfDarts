import math
from matplotlib.pyplot import show
import pandas as pd

# Creating Phase I.
# assuming no air resistance, 
# asuming dart always hits wall,
# frame of reference: shot origin has same coordinates [z,y] aas the bullseye 
# 1.73m is from floor to bullseye (height)
# 2.37m is distance from throw to board (8ft)

class projectile:
    """
    A class for the projectile motion of the dart.
    """
    
    def range(swivel_angle):
        
        """
        this is the range of the projectile assuming it hits the board at d = 8m. 
        """
        d = 2.37 # distance  metres away from dartboard
        
        k = (math.pi / 180) ## degrees to radians converter since trig fucntions take radians
        
        
        return  d / (math.cos(swivel_angle * k))
    
    
    
    def height(tilt_angle, swivel_angle, initial_velocity):
        
        """
        this is the distance in the y-direction relative to the bullseye.
        """
        
        g = 9.81
        k = (math.pi / 180)
        
        global R_x
        R_x = projectile.range(swivel_angle)

        return (math.tan(k*tilt_angle)*R_x) - ((g * R_x**2) / (2 * (initial_velocity *  math.cos(k*tilt_angle))**2 ))   
    
    
    def shift(tilt_angle, swivel_angle, initial_velocity):                                          
        """
        this is the distance in the z-direction relative to the bullseye.
        """

        d=2.37
        k = (math.pi / 180)
       
        if swivel_angle > 0:
            return d * (math.tan(abs(swivel_angle*k)))
        if swivel_angle <0:
            return d * -(math.tan(abs(swivel_angle*k)))
        if swivel_angle == 0 or initial_velocity ==0:
            return 0

class coordinates: 
    
    def cartesian_coordinates(tilt_angle, swivel_angle, initial_velocity):

        z = projectile.shift(tilt_angle, swivel_angle, initial_velocity)
        y = projectile.height(tilt_angle, swivel_angle, initial_velocity)

        return [z,y]


    def theta(tilt_angle, swivel_angle, initial_velocity):

        """
        this gives us our theta value used to determine score
        """

        k = math.pi / 180 ## this is used to counteract the radians output of the functions math does. 

        z = projectile.shift(tilt_angle, swivel_angle, initial_velocity)
        y = projectile.height(tilt_angle, swivel_angle, initial_velocity)

        if z==0 and y>0:
            return 90
        if z==0 and y<0:
            return 270
        if y==0 and z>0:
            return 0
        if y==0 and z<0 :
            return 180
        if z>0 and y>0:
            return math.atan(y/z) * (k**-1)
        if z<0 and y>0:
            return 180 - math.atan(abs(y/z)) * (k**-1)
        if z<0 and y<0: 
            return  180 + math.atan(y/z) * (k**-1)
        if z>0 and y<0:
            return 360 - math.atan(abs(y/z)) * (k**-1)
    

    def r(tilt_angle, swivel_angle, initial_velocity):

        """
        this gives us our r value used to determine score
        """

        z = projectile.shift(tilt_angle, swivel_angle, initial_velocity)
        y = projectile.height(tilt_angle, swivel_angle, initial_velocity)

        r = math.sqrt((z)**2 + (y)**2)
    
        return r 
    
    def polar_coordinates(tilt_angle, swivel_angle, initial_velocity):
    
        """
        this function combines the projectiles and coordinates class to create the r and theta used in the scores class.
        """

        r = coordinates.r(tilt_angle, swivel_angle, initial_velocity)
        theta = coordinates.theta(tilt_angle, swivel_angle, initial_velocity)

        
        return [r, theta]

class scores:

    def initial_score(theta):

        '''
        this function takes the value of 
        theta and outputs the INITIAL
        score that is obtained from that value.
        '''
        ## 
    
        if theta >= 0 and theta < 9:
            return 6
        elif theta >= 9 and theta < 27:
            return 13
        elif theta >= 27 and theta < 45:
            return 4
        elif theta >= 45 and theta < 63:
            return 18
        elif theta >= 63 and theta < 81:
            return 1
        elif theta >= 81 and theta < 99:
            return 20
        elif theta >= 99 and theta < 117:
            return 5
        elif theta >= 117 and theta < 135:
            return 12 
        elif theta >= 135 and theta < 153:
            return 9
        elif theta >= 153 and theta < 171:
            return 14 
        elif theta >= 171 and theta < 189:
            return 11
        elif theta >= 207 and theta < 225:
            return 8
        elif theta >= 225 and theta < 243:
            return 7
        elif theta >= 243 and theta < 261:
            return 19
        elif theta >= 261 and theta < 279:
            return 3
        elif theta >= 279 and theta < 297:
            return 17
        elif theta >= 297 and theta < 315:
            return 2
        elif theta >= 315 and theta < 333 :
            return 15
        elif theta >= 333 and theta < 351:
            return 10
        elif theta >= 351 and theta < 360:
            return 6
        elif theta < 0 or theta >= 360:
            return "error"


    def final_score(r, theta):
    
            """
            this function will take the initial_score value and depending solely 
            on our r value  (in accordance to the points system of darts) will output 
            the following:


              0 <= r < r_1   ---   bullseye, gives 50

            r_1 <= r < r_2   ---   25 ring, gives 25

            r_2 <= r < r_3   ---   blank, gives initial score as is  

            r_3 <= r < r_4   ---   triple ring, multiplies initial score by 3

            r_4 <= r < r_5   ---   blank, gives initial score as is 

            r_5 <= r < r_6   ---   double ring, multiplies initial score by 2

                  r >= r_6   ---   missed shot, null score (0)

            """

            ## defining dartboard r_n values in meters [m]
            ## https://dartsavvy.com/dart-board-dimensions-and-sizes/

            r_1 = 0.0127 / 2
            r_2 = 0.0318 / 2
            r_3 = 0.107
            r_4 = 0.107 + 0.008
            r_5 =  0.170 - 0.008
            r_6 = 0.170

            ## defining intial_score

            global score_i 
            score_i = scores.initial_score(theta) 

            if r < r_1:
                return 50
            elif  r_1 <= r and r < r_2:
                return 25
            elif r_2 <= r and r < r_3:
                return score_i
            elif r_3 <= r and r < r_4: 
                return score_i * 3
            elif r_4 <= r and r < r_5: 
                return score_i
            elif r_5 <= r and r < r_6:
                return score_i * 2 
            elif r >= r_6: 
                return  0

def dart_simulation(tilt_angle, swivel_angle, initial_velocity):
    
    """
    this function will combine phase I and II's functions in order to calculate the final score. 
    """
    
    r = coordinates.r(tilt_angle, swivel_angle, initial_velocity)
    theta = coordinates.theta(tilt_angle, swivel_angle, initial_velocity)
    
    if tilt_angle >= 90 or tilt_angle <= -90 or swivel_angle >= 90 or swivel_angle <= -90 or initial_velocity ==0:
        return "null shot, please ensure the tilt and swivel angles are both between -90 and 90, and that the velocity is positive"
    else:
        return scores.final_score(r, theta)

'''
##Simulation examples
A = [0,0,25]
B = [1, 2, 26]
C = [6,7, 420]

COLUMNS = ['Tilt Angle', 'Swivel Angle', 'Inital Velocity']
simulation_writer = pd.DataFrame([A, B, C], columns=COLUMNS)
simulation_writer.to_csv('simulation.csv', index=False)
pd.read_csv('simulation.csv', names=COLUMNS,skiprows=[0])
print(simulation_writer.head())
'''



def simulation_writer(tilt_angle, swivel_angle, initial_velocity, csv_file):

    
    #This function creates a csv file and writes the variables on a single table.
    
    Simulation1 = [tilt_angle, swivel_angle, initial_velocity, dart_simulation(tilt_angle, swivel_angle, initial_velocity)]

    #Column headers
    COLUMNS = ['Tilt Angle', 'Swivel Angle', 'Inital Velocity', 'Score']

    #Places data in column headers
    simulation_writer = pd.DataFrame([Simulation1], columns=COLUMNS)
    simulation_writer.to_csv(csv_file, index=False)
    pd.read_csv(csv_file, names=COLUMNS,skiprows=[0])
    print(simulation_writer.head())



#simulation_writer(0,0,25,'simulation.csv')


class simulation_writer:

    def write(tilt_angle, swivel_angle, initial_velocity, csv_file):

        #This function creates a csv file and writes the variables on a single table.
        Simulation1 = [tilt_angle, swivel_angle, initial_velocity, dart_simulation(tilt_angle, swivel_angle, initial_velocity)]
        #Column headers
        COLUMNS = ['Tilt Angle', 'Swivel Angle', 'Inital Velocity', 'Score']

        #Places data in column headers
        simulation_writer = pd.DataFrame([Simulation1], columns=COLUMNS)
        simulation_writer.to_csv(csv_file, index=False)
        pd.read_csv(csv_file, names=COLUMNS,skiprows=[0])
        print(simulation_writer.head())

    def add(tilt_angle, swivel_angle, initial_velocity):
        #This function adds a new row to the csv file
        Simulation2 = [tilt_angle, swivel_angle, initial_velocity, dart_simulation(tilt_angle, swivel_angle, initial_velocity)]
        #Column headers
        #Places data in column headers
        simulation_writer = simulation_writer.append(Simulation2, ignore_index=True)

    def show_data():
        #This function prints out the data added so far in the terminal
        print(simulation_writer.head())



#simulation_writer(0,0,25,'simulation.csv')

#task1 = simulation_writer
task1 = simulation_writer
task1.write(0,0,40,'simulation.csv')
task1.add(0,0,25)
