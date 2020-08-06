from gpiozero import MotionSensor
from signal import pause
import sys
from time import sleep
import LED_module
import Figure_Movements

pir = MotionSensor(12)
def piron():
    LED_module.light_LED() #call light_LED function when button is pressed
    Figure_Movements.move_figures_in_sequence()
    sleep(6)
    LED_module.dowse_LED()
    
def piroff():
    print('led.off')
    
if __name__ == '__main__':
    while True:
        
        try:
            #green_led.on()
            #button.wait_for_press()
            pir.when_motion=piron

        #pause()
        except KeyboardInterrupt:
            print("Exception ...")
            LED_module.dowse_LED()
            #kb_exception_actions()

        #except:  
        # this catches ALL other exceptions including errors.  
        # You won't get any error messages for debugging  
        # so only use it once your code is working  
                #print ("Other error or exception occurred!")
      
        #finally:  
                #print ("Finally ....!")
