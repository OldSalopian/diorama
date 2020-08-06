from Stepper_Motor_Class import Motor
import time

#if __name__ == "__main__":

#def setup_figures():    
fishman = Motor([17,27,22,23])
e_dive = Motor([24,25,16,20])
e_swim = Motor([5,6,13,19])

def move_figures_in_sequence():
    e_dive.backward(0.003, 138)    # 512 steps --- 360 angle ( 1 deg = 1.42222 steps)
    time.sleep(2)
    fishman.backward(0.003, 40)
    time.sleep(1)
    #e_dive.rpm(30)
    e_dive.backward(0.003, 274)
    #Motor.rpm(30)
    fishman.backward(0.003, 230)
    #Motor.rpm(20)
    e_dive.backward(0.003, 100)
    time.sleep(3)
    
    
    
    e_swim.backward(0.003, 128)
    time.sleep(3)
    fishman.backward(0.003, 142)
    time.sleep(3)
    
    
    e_swim.forward(0.003, 128)
    time.sleep(6)
    fishman.backward(0.003, 100)
    
def close_ports():    
    #release the GPIO ports for all 3 motors. Otherwise power stays on
    # and creates resistance to manually adjusting the positions of the figures.
    fishman.close_ports()
    e_dive.close_ports()
    e_swim.close_ports()
    
if __name__ == "__main__":
    #setup_figures()
    move_figures_in_sequence()
    close_ports()