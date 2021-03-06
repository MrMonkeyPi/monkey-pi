
import RPi.GPIO as GPIO
import time
import threading
import random

ServoLeftRightPos = 90
ServoUpDownPos = 90
g_frontServoPos = 90
g_nowfrontPos = 0

# engines of wheels
IN1 = 20
IN2 = 21
IN3 = 19
IN4 = 26
ENA = 16
ENB = 13

# supersonic wave
EchoPin = 0
TrigPin = 1

# RGB light
LED_R = 22
LED_G = 27
LED_B = 24

FrontServoPin = 23
ServoUpDownPin = 9
ServoLeftRightPin = 11

AvoidSensorLeft = 12
AvoidSensorRight = 17

buzzer = 8

# fin engine
OutfirePin = 2

# TrackSensorLeftPin1 TrackSensorLeftPin2 TrackSensorRightPin1 TrackSensorRightPin2
#      3                 5                  4                   18
TrackSensorLeftPin1 = 3
TrackSensorLeftPin2 = 5
TrackSensorRightPin1 = 4
TrackSensorRightPin2 = 18


LdrSensorLeft = 7
LdrSensorRight = 6


WalkSpeed = 60
is_Auto_Pilot = False

infrared_track_value = ''
infrared_avoid_value = ''
LDR_value = ''
g_lednum = 0


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


def init():
    global pwm_ENA
    global pwm_ENB
    global pwm_FrontServo
    global pwm_UpDownServo
    global pwm_LeftRightServo
    global pwm_rled
    global pwm_gled
    global pwm_bled
    GPIO.setup(ENA, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(IN1, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(IN2, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(ENB, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(IN3, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(IN4, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(buzzer, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(OutfirePin, GPIO.OUT)
    GPIO.setup(EchoPin, GPIO.IN)
    GPIO.setup(TrigPin, GPIO.OUT)
    GPIO.setup(LED_R, GPIO.OUT)
    GPIO.setup(LED_G, GPIO.OUT)
    GPIO.setup(LED_B, GPIO.OUT)
    GPIO.setup(FrontServoPin, GPIO.OUT)
    GPIO.setup(ServoUpDownPin, GPIO.OUT)
    GPIO.setup(ServoLeftRightPin, GPIO.OUT)
    GPIO.setup(AvoidSensorLeft, GPIO.IN)
    GPIO.setup(AvoidSensorRight, GPIO.IN)
    GPIO.setup(LdrSensorLeft, GPIO.IN)
    GPIO.setup(LdrSensorRight, GPIO.IN)
    GPIO.setup(TrackSensorLeftPin1, GPIO.IN)
    GPIO.setup(TrackSensorLeftPin2, GPIO.IN)
    GPIO.setup(TrackSensorRightPin1, GPIO.IN)
    GPIO.setup(TrackSensorRightPin2, GPIO.IN)

    pwm_ENA = GPIO.PWM(ENA, 2000)
    pwm_ENB = GPIO.PWM(ENB, 2000)
    pwm_ENA.start(0)
    pwm_ENB.start(0)

    pwm_FrontServo = GPIO.PWM(FrontServoPin, 50)
    pwm_UpDownServo = GPIO.PWM(ServoUpDownPin, 50)
    pwm_LeftRightServo = GPIO.PWM(ServoLeftRightPin, 50)
    pwm_FrontServo.start(0)
    pwm_UpDownServo.start(0)
    pwm_LeftRightServo.start(0)
    pwm_rled = GPIO.PWM(LED_R, 1000)
    pwm_gled = GPIO.PWM(LED_G, 1000)
    pwm_bled = GPIO.PWM(LED_B, 1000)
    pwm_rled.start(0)
    pwm_gled.start(0)
    pwm_bled.start(0)


def forward():
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(WalkSpeed)
    pwm_ENB.ChangeDutyCycle(WalkSpeed)


def back():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    pwm_ENA.ChangeDutyCycle(WalkSpeed)
    pwm_ENB.ChangeDutyCycle(WalkSpeed)


def left():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(WalkSpeed)
    pwm_ENB.ChangeDutyCycle(WalkSpeed)


def right():
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(WalkSpeed)
    pwm_ENB.ChangeDutyCycle(WalkSpeed)


def spin_left():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(WalkSpeed)
    pwm_ENB.ChangeDutyCycle(WalkSpeed)


def spin_right():
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    pwm_ENA.ChangeDutyCycle(WalkSpeed)
    pwm_ENB.ChangeDutyCycle(WalkSpeed)


def stop():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)
    all_servo_stop()


def set_walk_speed(i):
    global WalkSpeed
    WalkSpeed = max(min(i*20, 100), 20)


def walk_speed_up():
    global WalkSpeed
    WalkSpeed = min(WalkSpeed + 20, 100)


def walk_speed_down():
    global WalkSpeed
    WalkSpeed = max(WalkSpeed - 20, 20)


def get_Distance():
    GPIO.output(TrigPin, GPIO.HIGH)
    time.sleep(0.000015)
    GPIO.output(TrigPin, GPIO.LOW)
    while not GPIO.input(EchoPin):
        pass
    t1 = time.time()
    while GPIO.input(EchoPin):
        pass
    t2 = time.time()
    time.sleep(0.01)
    return ((t2 - t1) * 340 / 2) * 100


def set_front_servo_detection(pos):
    for i in range(18):
        pwm_FrontServo.ChangeDutyCycle(2.5 + 10 * pos/180)
        time.sleep(0.02)
        # pwm_FrontServo.ChangeDutyCycle(0)


def set_camera_servo_LR_detection(pos):
    for i in range(1):
        pwm_LeftRightServo.ChangeDutyCycle(2.5 + 10 * pos/180)
        time.sleep(0.02)
        # pwm_LeftRightServo.ChangeDutyCycle(0)


def set_camera_servo_UD_detection(pos):
    for i in range(1):
        pwm_UpDownServo.ChangeDutyCycle(2.5 + 10 * pos/180)
        time.sleep(0.02)
        # pwm_UpDownServo.ChangeDutyCycle(0)


def infrared_avoid_test():
    global infrared_avoid_value
    LeftSensorValue = GPIO.input(AvoidSensorLeft)
    RightSensorValue = GPIO.input(AvoidSensorRight)
    infrared_avoid_value_list = ['0', '0']
    infrared_avoid_value_list[0] = str(1 ^ LeftSensorValue)
    infrared_avoid_value_list[1] = str(1 ^ RightSensorValue)
    infrared_avoid_value = ''.join(infrared_avoid_value_list)


def follow_light_test():
    global LDR_value
    LdrSersorLeftValue = GPIO.input(LdrSensorLeft)
    LdrSersorRightValue = GPIO.input(LdrSensorRight)
    LDR_value_list = ['0', '0']
    LDR_value_list[0] = str(LdrSersorLeftValue)
    LDR_value_list[1] = str(LdrSersorRightValue)
    LDR_value = ''.join(LDR_value_list)


def fan():
    GPIO.output(OutfirePin, not GPIO.input(OutfirePin))
    time.sleep(0.5)


def beep():
    GPIO.output(buzzer, GPIO.LOW)
    time.sleep(0.1)
    GPIO.output(buzzer, GPIO.HIGH)
    time.sleep(0.001)


def set_led_rgb(iRed, iGreen, iBlue):
    v_red = (100*iRed)/255
    v_green = (100*iGreen)/255
    v_blue = (100*iBlue)/255
    pwm_rled.ChangeDutyCycle(v_red)
    pwm_gled.ChangeDutyCycle(v_green)
    pwm_bled.ChangeDutyCycle(v_blue)
    time.sleep(0.02)


def camera_up():
    global ServoUpDownPos
    pos = ServoUpDownPos
    set_camera_servo_UD_detection(pos)
    time.sleep(0.1)
    pos += 3
    ServoUpDownPos = min(pos, 180)


def camera_down():
    global ServoUpDownPos
    pos = ServoUpDownPos
    set_camera_servo_UD_detection(pos)
    time.sleep(0.1)
    pos -= 3
    ServoUpDownPos = max(pos, 45)


def camera_left():
    global ServoLeftRightPos
    pos = ServoLeftRightPos
    set_camera_servo_LR_detection(pos)
    time.sleep(0.1)
    pos += 3
    ServoLeftRightPos = min(pos, 180)


def camera_right():
    global ServoLeftRightPos
    pos = ServoLeftRightPos
    set_camera_servo_LR_detection(pos)
    time.sleep(0.1)
    pos -= 3
    ServoLeftRightPos = max(pos, 0)


def front_servo_left():
    set_front_servo_detection(180)


def front_servo_right():
    set_front_servo_detection(0)


def all_servo_init():
    servoinitpos = 90
    set_front_servo_detection(servoinitpos)
    set_camera_servo_UD_detection(servoinitpos)
    set_camera_servo_LR_detection(servoinitpos)
    time.sleep(0.5)
    all_servo_stop()


def all_servo_stop():
    pwm_LeftRightServo.ChangeDutyCycle(0)
    pwm_UpDownServo.ChangeDutyCycle(0)
    pwm_FrontServo.ChangeDutyCycle(0)


def stop_auto_pilot():
    global is_Auto_Pilot
    is_Auto_Pilot = False
    time.sleep(0.5)
    stop()


def auto_pilot():
    global is_Auto_Pilot
    if is_Auto_Pilot:
        return

    is_Auto_Pilot = True
    threading.Thread(target=_run_avoid_obstacle).start()


def _detect_obstacle():
    global WalkSpeed

    set_led_rgb(255, 0, 0)
    WalkSpeed = 25
    back()
    time.sleep(0.5)
    stop()

    set_front_servo_detection(0)
    time.sleep(0.8)
    right_dist = get_Distance()

    set_front_servo_detection(180)
    time.sleep(0.8)
    left_dist = get_Distance()

    set_front_servo_detection(90)
    time.sleep(0.8)
    front_dist = get_Distance()

    WalkSpeed = 10
    if left_dist < 30 and right_dist < 30 and front_dist < 30:
        set_led_rgb(255, 0, 0)
        spin_right()
        time.sleep(1.6)
    elif left_dist > right_dist:
        spin_left()
        time.sleep(0.8)
    else:
        spin_right()
        time.sleep(0.8)


def _run_avoid_obstacle():
    global is_Auto_Pilot
    global WalkSpeed

    while is_Auto_Pilot:
        dist = get_Distance()
        if dist > 30:
            leftFree = GPIO.input(AvoidSensorLeft)
            rightFree = GPIO.input(AvoidSensorRight)

            WalkSpeed = 20
            if leftFree == True and rightFree == False:
                set_led_rgb(255, 255, 0)
                left()
            elif leftFree == False and rightFree == True:
                set_led_rgb(255, 255, 0)
                right()
            elif leftFree == False and rightFree == False:
                set_led_rgb(255, 255, 0)
                if random.random() > 0.5:
                    right()
                else:
                    left()

            time.sleep(0.3)
            WalkSpeed = 20
            forward()
            set_led_rgb(0, 255, 0)
        else:
            _detect_obstacle()


#     init()
#     all_servo_init()

def get_infrared_sensor_status():
    leftStatus = GPIO.input(AvoidSensorLeft)
    rightRight = GPIO.input(AvoidSensorRight)
    return [leftStatus, rightRight]

def clean():
    pwm_ENA.stop()
    pwm_ENB.stop()
    pwm_rled.stop()
    pwm_gled.stop()
    pwm_bled.stop()
    pwm_FrontServo.stop()
    pwm_LeftRightServo.stop()
    pwm_UpDownServo.stop()
    GPIO.cleanup()
