from gpiozero import LED


green_led = LED(21,0)



def light_LED():
    print("turn led on")
    green_led.on()
    return
    
def dowse_LED():
    print("turn led off")
    green_led.off()
    return



