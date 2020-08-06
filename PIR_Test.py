from gpiozero import MotionSensor
from signal import pause

pir = MotionSensor(12)
#led = LED(16)
def piron():
    print('led.on')
    
def piroff():
    print('led.off')
    
pir.when_motion = piron
pir.when_no_motion = piroff

pause()