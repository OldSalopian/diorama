from gpiozero import Button
from signal import pause
import sys
from time import sleep
import LED_module
import Figure_Movements

button = Button(12)

if __name__ == '__main__':
    while True:
        
        try:
            #green_led.on()
            button.wait_for_press()
            LED_module.light_LED() #call light_LED function when button is pressed
            #pause()
            #BasicStepperTest.run_stepper(0.004, 0)
            Figure_Movements.move_figures_in_sequence()
            sleep(6)
            LED_module.dowse_LED()
    #button.when_released = green_led.off # turn LED off when button is released
            #LED_module.green_led.source=button      #toggles true/false on/off press/release    #light_LED()

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
