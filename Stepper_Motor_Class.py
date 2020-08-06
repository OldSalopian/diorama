#!/usr/bin/env python  
from gpiozero import OutputDevice as stepper 
import time  


class Motor(object):
    def __init__(self, pins):
        """Initialise the motor object.

        pins -- a list of 4 integers referring to the GPIO pins that the IN1, IN2
                IN3 and IN4 pins of the ULN2003 board are wired to
        mode -- the stepping mode to use:
                1: wave drive (not yet implemented)
                2: full step drive
                3: half step drive (default)

        """
        self.IN1 = stepper(pins[0])    # pin11  
        self.IN2 = stepper(pins[1])  
        self.IN3 = stepper(pins[2])  
        self.IN4 = stepper(pins[3])
#        self.P1 = pins[0]
#        self.P2 = pins[1]
#        self.P3 = pins[2]
#        self.P4 = pins[3]
##        self.mode = mode
##        self.deg_per_step = 5.625 / 64  # for half-step drive (mode 3)
##        self.steps_per_rev = int(360 / self.deg_per_step)  # 4096
##        self.step_angle = 0  # Assume the way it is pointing is zero degrees
        
        #GPIO.setwarnings(False)
        #GPIO.setmode(GPIO.BCM)
        
        #for p in pins:
            #GPIO.setup(p, GPIO.OUT)
            #GPIO.output(p, 0)


    def setStep(self, w1, w2, w3, w4):  
        if w1==1:
            self.IN1.on()
        else:
            self.IN1.off()
        if w2==1:
            self.IN2.on()
        else:
            self.IN2.off()
        if w3==1:
            self.IN3.on()
        else:
            self.IN3.off()
        if w4==1:
            self.IN4.on()
        else:
            self.IN4.off()
#        GPIO.output(self.IN1, w1)
#        GPIO.output(self.IN2, w2)
#        GPIO.output(self.IN3, w3)
#        GPIO.output(self.IN4, w4)

    def stop(self):  
        self.setStep(0, 0, 0, 0)  

    def forward(self, delay, steps):    
        for i in range(0, steps):  
            self.setStep(1, 0, 0, 0)  
            time.sleep(delay)  
            self.setStep(0, 1, 0, 0)  
            time.sleep(delay)  
            self.setStep(0, 0, 1, 0)  
            time.sleep(delay)  
            self.setStep(0, 0, 0, 1)  
            time.sleep(delay)  

    def backward(self, delay, steps):    
        for i in range(0, steps):  
            self.setStep(0, 0, 0, 1)  
            time.sleep(delay)  
            self.setStep(0, 0, 1, 0)  
            time.sleep(delay)  
            self.setStep(0, 1, 0, 0)  
            time.sleep(delay)  
            self.setStep(1, 0, 0, 0)  
            time.sleep(delay)  



    def close_ports(self):
      
        self.IN1.close()
        print("Close port 1")
        self.IN2.close()
        print("Close port 2")
        self.IN3.close()
        print("Close port 3")
        self.IN4.close()
        print("Close port 4")
    
if __name__ == '__main__':     # Program start from here  
    #setup()  
    try:
        #fishman = Motor([17,27,22,23])
        #e_dive = Motor([24,25,16,20])
        #e_swim = Motor([5,6,13,19])
        m1 = Motor([5,6,13,19])
        m1.forward(0.003, 374)  

        print ("stop...")  
        m1.stop()
        #m1.setStep(0, 0, 0, 0) 
        time.sleep(3)
        m1.forward(0.003, 138)
        time.sleep(3)
        #m1.loop()  

    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child function destroy() will be  executed.  
            print("Exception ... Keyboard Exception CTRL-C")
            m1.close_ports()

    except:  
    # this catches ALL other exceptions including errors.  
    # You won't get any error messages for debugging  
    # so only use it once your code is working  
            print ("Other error or exception occurred!")
            m1.close_ports()
  
    finally:  
            print ("Finally ....!")
            m1.close_ports()