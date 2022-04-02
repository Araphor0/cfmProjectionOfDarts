import math

##This is a whole rewrite of the code
#Due to the fact that there are multiple instances where the code does note work.

#The projectile class does work.

#The scores class doesn't work that well in comparison.
'''
A lot of the code regarding the the z, y angles are always repeated in the code.

Therefore the strucutre will follow this type of format.

class:
    Projectile

functions:

'''

class Projectile:
    
    """
    A class for the projectile motion of the dart.
    """

    ##using constructors instantiate the object which initializes
    ##The data values to the class
    def __init__(self,tilt_angle, swivel_angle, initial_velocity):
        self.tiltAngle = tilt_angle
        self.swivelAngle = swivel_angle
        self.initialVelocity = initial_velocity
    
    def range(self):
        """
        this is the range of the projectile assuming it hits the board at d = 8m. 
        """
        d = 2.37 # distance  metres away from dartboard
        
        k = (math.pi / 180) ## degrees to radians converter since trig fucntions take radians
        
        return  d / (math.cos(self.swivelAngle * k))
    
    
    
    def height(self):
        """
        this is the distance in the y-direction relative to the bullseye.
        """
        
        g = 9.81
        k = (math.pi / 180)
        
        global R_x
        R_x = Projectile.range(self.swivelAngle, self.initialVelocity)
        
     
        return (math.tan(k*self.tiltAngle)*R_x) - ((g * R_x**2) / (2 * (self.initialVelocity *  math.cos(k*self.tiltAngle))**2 ))   
    
    def shift(self):
                                                 
        """
        this is the distance in the z-direction relative to the bullseye.
        """

        d=2.37
        k = (math.pi / 180)
       
        if self.swivelAngle > 0:
            return d * (math.tan(abs(self.swivelAngle*k)))
        if self.swivelAngle <0:
            return d * -(math.tan(abs(self.swivelAngle*k)))
        if self.swivelAngle == 0 or self.initialVelocity ==0:
            return 0

    def cartesian_coordinates(self):
        """
        Returns the cartesian coordinates in relation to the given tilt angle,
        swivel angle and initial velocity.
        """

        z = Projectile.shift(self.tiltAngle, self.swivelAngle, self.initialVelocity)
        y = Projectile.height(self.tiltAngle, self.swivelAngle, self.initialVelocity)

        return [z,y]

class coordinates: 
    ##using constructors instantiate the object which initializes
    ##The data values to the class
    def __init__(self,tilt_angle, swivel_angle, initial_velocity):
        self.tiltAngle = tilt_angle
        self.swivelAngle = swivel_angle
        self.initialVelocity = initial_velocity
    
    def cartesian_coordinates(self):
        """
        Returns the cartesian coordinates in relation to the given tilt angle,
        swivel angle and initial velocity.
        """

        z = Projectile.shift(self.tiltAngle, self.swivelAngle, self.initialVelocity)
        y = Projectile.height(self.tiltAngle, self.swivelAngle, self.initialVelocity)

        return [z,y]


    def theta(self):
        """
        this gives us our theta value used to determine score
        """

        k = math.pi / 180 ## this is used to counteract the radians output of the functions math does. 

        z = Projectile.shift(self.tiltAngle, self.swivelAngle, self.initialVelocity)
        y = Projectile.height(self.tiltAngle, self.swivelAngle, self.initialVelocity)

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
    

    def r(self):
        """
        this gives us our r value used to determine score
        """

        z = Projectile.shift(self.tiltAngle, self.swivelAngle, self.initialVelocity)
        y = Projectile.height(self.tiltAngle, self.swivelAngle, self.initialVelocity)

        r = math.sqrt((z)**2 + (y)**2)
    
        return r

    def polar_coordinates(self):
        """
        this function combines the projectiles and coordinates class to create the r and theta used in the scores class.
        """

        r = coordinates.r(self.tiltAngle, self.swivelAngle, self.initialVelocity)
        theta = coordinates.theta(self.tiltAngle, self.swivelAngle, self.initialVelocity)

        
        return [r, theta]

class scores:

    def __init__(self, theta, r):
        self.theta = theta
        self.r = r

    def initial_score(self):

        '''
        this function takes the value of 
        theta and outputs the INITIAL
        score that is obtained from that value.
        '''
        ## 
    
        if self.theta >= 0 and self.theta < 9:
            return 6
        elif self.theta >= 9 and self.theta < 27:
            return 13
        elif self.theta >= 27 and self.theta < 45:
            return 4
        elif self.theta >= 45 and self.theta < 63:
            return 18
        elif self.theta >= 63 and self.theta < 81:
            return 1
        elif self.theta >= 81 and self.theta < 99:
            return 20
        elif self.theta >= 99 and self.theta < 117:
            return 5
        elif self.theta >= 117 and self.theta < 135:
            return 12 
        elif self.theta >= 135 and self.theta < 153:
            return 9
        elif self.theta >= 153 and self.theta < 171:
            return 14 
        elif self.theta >= 171 and self.theta < 189:
            return 11
        elif self.theta >= 207 and self.theta < 225:
            return 8
        elif self.theta >= 225 and self.theta < 243:
            return 7
        elif self.theta >= 243 and self.theta < 261:
            return 19
        elif self.theta >= 261 and self.theta < 279:
            return 3
        elif self.theta >= 279 and self.theta < 297:
            return 17
        elif self.theta >= 297 and self.theta < 315:
            return 2
        elif self.theta >= 315 and self.theta < 333 :
            return 15
        elif self.theta >= 333 and self.theta < 351:
            return 10
        elif self.theta >= 351 and self.theta < 360:
            return 6
        elif self.theta < 0 or self.theta >= 360:
            return "error"
        

    def final_score(self):
    
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
            score_i = scores.initial_score() 

            if self.r < r_1:
                return 50
            elif  r_1 <= self.r and self.r < r_2:
                return 25
            elif r_2 <= self.r and self.r < r_3:
                return score_i
            elif r_3 <= self.r and self.r < r_4: 
                return score_i * 3
            elif r_4 <= self.r and self.r < r_5: 
                return score_i
            elif r_5 <= self.r and self.r < r_6:
                return score_i * 2 
            elif self.r >= r_6: 
                return  0

class dart_simulation:
    def __init__(self,tilt_angle, swivel_angle, initial_velocity):
        self.tiltAngle = tilt_angle
        self.swivelAngle = swivel_angle
        self.initialVelocity = initial_velocity

    def simulation(self):
        '''
        This is a new dart_simulation function with classes instead of usual parameters
        '''
        r = coordinates.r(self.tiltAngle, self.swivelAngle, self.initialVelocity)
        theta = coordinates.theta(self.tiltAngle, self.swivelAngle, self.initialVelocity)

        if self.tiltAngle >= 90 or self.tiltAngle <= -90:
            return "null shot, please ensure the tilt and swivel angles are both between -90 and 90, and that the velocity is positive"
        elif self.swivelAngle >= 90 or self.swivelAngle <= -90:
            return "null shot, please ensure the tilt and swivel angles are both between -90 and 90, and that the velocity is positive"
        elif self.initialVelocity == 0:
            return "null shot, please ensure the tilt and swivel angles are both between -90 and 90, and that the velocity is positive"
        else:
            return scores.final_score(r, theta)

    



#matthew = Projectile(0, 0, 25)

#william = dart_simulation(0, 0, 25)
#print(william.simulation())

matthew = dart_simulation(0, 0, 25)
print(matthew.simulation())
