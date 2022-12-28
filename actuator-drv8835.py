from gpiozero import CamJamKitRobot
import time

#Speed ajusted
MAX_SPEED = 70

robot = CamJamKitRobot()
move_state = 0

def set_speed(intSpeed):
    global cur_speed
    global move_state
    cur_speed = intSpeed/100
    if move_state == -1:
        rew()
    elif move_state == 1:
        ffw()
    #speed = int(MAX_SPEED * intSpeed / 100)
    #print(speed)
    #cur_speed = min(MAX_SPEED, speed)
    #print(cur_speed)

def get_speed():
    return int(cur_speed * 100 / MAX_SPEED)

def ffw():
    global move_state
    motorspeed = (-cur_speed, 0)
    robot.value = motorspeed
    # motors.motor2.setSpeed(cur_speed)
    move_state = 1
    time.sleep(1)

def rew():
    global move_state
    motorspeed = (cur_speed, 0)
    robot.value = motorspeed
    # motors.motor2.setSpeed(-cur_speed)
    move_state = -1
    time.sleep(1)

def left(speed=-1):
    # motors.motor1.setSpeed(int(speed * MAX_SPEED))
    motorspeed = (0, cur_speed * speed)
    robot.value = motorspeed
    time.sleep(3)


def right(speed=1):
    # motors.motor1.setSpeed(int(speed * MAX_SPEED))
    motorspeed = (0, cur_speed * speed)
    robot.value = motorspeed
    time.sleep(3)

def center():
    motorspeed = (0, 0)

def turn_off():
    center()
    robot.stop()

def init(default_speed=0.10416666666):
    motorspeed = (0, 0)
    set_speed(default_speed)


# set_speed(50)
# print(get_speed())
#
# for x in range(11):
#     set_speed(x/10)
#     ffw()