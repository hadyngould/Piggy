#!/usr/bin python3
from teacher import PiggyParent
import sys
import time

class Piggy(PiggyParent):

    '''
    *************
    SYSTEM SETUP
    *************
    '''

    def __init__(self, addr=8, detect=True):
        PiggyParent.__init__(self) # run the parent constructor

        ''' 
        MAGIC NUMBERS <-- where we hard-code our settings
        '''
        self.LEFT_DEFAULT = 80
        self.RIGHT_DEFAULT = 80
        self.MIDPOINT = 1500  # what servo command (1000-2000) is straight forward for your bot?
        self.set_motor_power(self.MOTOR_LEFT + self.MOTOR_RIGHT, 0)
        self.load_defaults()
        
    def load_defaults(self):
        """Implements the magic numbers defined in constructor"""
        self.set_motor_limits(self.MOTOR_LEFT, self.LEFT_DEFAULT)
        self.set_motor_limits(self.MOTOR_RIGHT, self.RIGHT_DEFAULT)
        self.set_servo(self.SERVO_1, self.MIDPOINT)
        
    def menu(self):
        """Displays menu dictionary, takes key-input and calls method"""
        ## This is a DICTIONARY, it's a list with custom index values. Python is cool.
        # Please feel free to change the menu and add options.
        print("\n *** MENU ***") 
        menu = {"n": ("Navigate", self.nav),
                "d": ("Dance", self.dance),
                "o": ("Obstacle count", self.obstacle_count),
                "s": ("Shy", self.shy),
                "f": ("Follow", self.follow),
                "c": ("Calibrate", self.calibrate),
                "q": ("Quit", self.quit)
                }
        # loop and print the menu...
        for key in sorted(menu.keys()):
            print(key + ":" + menu[key][0])
        # store the user's answer
        ans = str.lower(input("Your selection: "))
        # activate the item selected
        menu.get(ans, [None, self.quit])[1]()

    '''
    ****************
    STUDENT PROJECTS
    ****************
    '''

    def dance(self):
        """A higher-ordered algorithm to make your robot dance"""
        
        if not self.safe_to_dance():
            return false # SHUT THE DANCE DOWN
        
        for x in range(3):
            self.strut()
            self.right_twist()
            self.strut()
            self.left_twist()
            self.backward_shimmey()
            self.spinarama()
            self.foward_shimmey()

    def right_twist(self):
        """The robot turns in a right circle once"""
        self.turn_by_deg(180)
        #time.sleep(.1)
        self.stop()
        self.turn_by_deg(180)
        #time.sleep(.1)
        self.stop()

    def left_twist(self):
        """Robot turns in a circle once to the left"""
        self.turn_by_deg(-179)
        #time.sleep(.1)
        self.stop()
        self.turn_by_deg(-179)
        #time.sleep(.1)
        self.stop()

    def strut(self):
        """Robot is moving foward while looking right to left """
        self.fwd(left=50, right=50)
        for x in range(2):
            self.servo(1000)
            time.sleep(.1) 
            self.servo(1500) # Look Straight
            time.sleep(1)
            self.servo(2000)
            time.sleep(.1)
            self.servo(1500)

    def backward_shimmey(self):
        """Robot is moving backwards while moving his body left and right"""
        for x in range(6):
            self.right(primary=-70, counter=-30)
            time.sleep(.5)
            self.left(primary=-70, counter=-30)
            time.sleep(.5)
        self.stop()

    def spinarama(self):
        """Robot moves in a circle to turn around and move forward"""
        for x in range(6):
            self.right(primary=-100, counter=-500)
            time.sleep(3.5)
            self.fwd()
            time.sleep(1)
            self.stop()

    def foward_shimmey(self):
        """Robot moves forward while moving his body left and right"""
        for x in range(6):
            self.right(primary=60, counter=30)
            time.sleep(.5)
            self.left(primary=70, counter=30)
            time.sleep(.5)
        self.back()
        time.sleep(2)        
        self.stop()


       
        
      

    def safe_to_dance(self):
        """ Does a 360 distance check and returns true if safe """
        # check for all fail/early-termination conditions
        for _ in range(4):
            if self.read_distance() < 300:
                print("NOT SAFE TO DANCE!")
                return False
            else: 
                self.turn_by_deg(90)        

        #after all checks have been done. We deduce it's safe
        print("SAFE TO DANCE!")
        return True

        for x in range(3):  
            self.shake()

    def shake(self):
        self. deg_fwd(720)
        slef.stop()

    def example_move(self):
        """this is an example dance move that should be replaced by student-created content"""
        self.right() # start rotating right
        time.sleep(1) # turn for a second
        self.stop() # stop
        self.servo(1000) # look right
        time.sleep(.25) # give your head time to move
        self.servo(2000) # look left

    def scan(self):
        """Sweep the servo and populate the scan_data dictionary"""
        for angle in range(self.MIDPOINT-350, self.MIDPOINT+350, 3):
            self.servo(angle)
            self.scan_data[angle] = self.read_distance()

    def obstacle_count(self):
        """Does a 360 scan and returns the number of obstacles it sees"""
        pass

    def nav(self):
        print("-----------! NAVIGATION ACTIVATED !------------\n")
        print("-------- [ Press CTRL + C to stop me ] --------\n")
        print("-----------! NAVIGATION ACTIVATED !------------\n")
        
        # TODO: build self.quick_check() that does a fast, 3-part check instead of read_distance
        while self.read_distance() > 250:  # TODO: fix this magic number
            self.fwd()
            time.sleep(.01)
        self.stop()
        # TODO: scan so we can decide left or right
        # TODO: average the right side of the scan dict
        # TODO: average the left side of the scan dict
        


###########
## MAIN APP
if __name__ == "__main__":  # only run this loop if this is the main file

    p = Piggy()

    if sys.version_info < (3, 0):
        sys.stdout.write("Sorry, requires Python 3.x\n")
        p.quit()

    try:
        while True:  # app loop
            p.menu()

    except KeyboardInterrupt: # except the program gets interrupted by Ctrl+C on the keyboard.
        p.quit()  
