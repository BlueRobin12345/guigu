def 右转():
    neZha.set_motor_speed(neZha.MotorList.M1, 33)
    neZha.set_motor_speed(neZha.MotorList.M2, -33)
    basic.pause(400)
    neZha.stop_all_motor()
def 左转():
    neZha.set_motor_speed(neZha.MotorList.M1, -33)
    neZha.set_motor_speed(neZha.MotorList.M2, 33)
    basic.pause(400)
    neZha.stop_all_motor()

def on_button_pressed_a():
    basic.show_string("1")
    到路口1()
    左转()
    neZha.set_motor_speed(neZha.MotorList.M2, 50)
    neZha.set_motor_speed(neZha.MotorList.M1, 50)
    basic.pause(200)
    neZha.stop_all_motor()
    识别颜色()
    basic.pause(500)
    neZha.set_motor_speed(neZha.MotorList.M2, -50)
    neZha.set_motor_speed(neZha.MotorList.M1, -50)
    basic.pause(200)
    neZha.stop_all_motor()
    右转()
    basic.pause(50)
    到路口2()
    basic.pause(50)
    右转()
    basic.pause(50)
    到路口1()
    basic.pause(50)
    舵机()
    basic.pause(300)
    舵机()
    neZha.set_motor_speed(neZha.MotorList.M2, 50)
    neZha.set_motor_speed(neZha.MotorList.M1, 50)
    basic.pause(700)
    neZha.stop_all_motor()
    左转()
    neZha.set_motor_speed(neZha.MotorList.M2, -50)
    neZha.set_motor_speed(neZha.MotorList.M1, -50)
    basic.pause(2000)
    neZha.stop_all_motor()
    到路口1()
    右转()
    neZha.set_motor_speed(neZha.MotorList.M2, -50)
    neZha.set_motor_speed(neZha.MotorList.M1, -50)
    basic.pause(300)
    neZha.stop_all_motor()
    basic.pause(50)
    neZha.set_motor_speed(neZha.MotorList.M2, 50)
    neZha.set_motor_speed(neZha.MotorList.M1, 50)
    basic.pause(300)
    neZha.stop_all_motor()
    
input.on_button_pressed(Button.A, on_button_pressed_a)

def 巡线():
    PlanetX_Basic.Trackbit_get_state_value()
    if PlanetX_Basic.trackbit_state(PlanetX_Basic.TrackbitStateType.TRACKING_STATE_1):
        neZha.set_motor_speed(neZha.MotorList.M1, -40)
        neZha.set_motor_speed(neZha.MotorList.M2, -40)
    if PlanetX_Basic.trackbit_state(PlanetX_Basic.TrackbitStateType.TRACKING_STATE_3) or PlanetX_Basic.trackbit_state(PlanetX_Basic.TrackbitStateType.TRACKING_STATE_11):
        neZha.set_motor_speed(neZha.MotorList.M1, -80)
        neZha.set_motor_speed(neZha.MotorList.M2, -9)
    if PlanetX_Basic.trackbit_state(PlanetX_Basic.TrackbitStateType.TRACKING_STATE_2) or PlanetX_Basic.trackbit_state(PlanetX_Basic.TrackbitStateType.TRACKING_STATE_14):
        neZha.set_motor_speed(neZha.MotorList.M1, -9)
        neZha.set_motor_speed(neZha.MotorList.M2, -80)
    if PlanetX_Basic.trackbit_state(PlanetX_Basic.TrackbitStateType.TRACKING_STATE_8):
        neZha.set_motor_speed(neZha.MotorList.M1, -80)
        neZha.set_motor_speed(neZha.MotorList.M2, -4)
    if PlanetX_Basic.trackbit_state(PlanetX_Basic.TrackbitStateType.TRACKING_STATE_12):
        neZha.set_motor_speed(neZha.MotorList.M1, -4)
        neZha.set_motor_speed(neZha.MotorList.M2, -80)
    if PlanetX_Basic.trackbit_state(PlanetX_Basic.TrackbitStateType.TRACKING_STATE_0):
        neZha.set_motor_speed(neZha.MotorList.M1, -40)
        neZha.set_motor_speed(neZha.MotorList.M2, -40)
def 舵机():
    neZha.set_servo_angel(neZha.ServoTypeList._360, neZha.ServoList.S1, 120)
    basic.pause(300)
    neZha.set_servo_angel(neZha.ServoTypeList._360, neZha.ServoList.S1, 225)
def 识别颜色():
    while True:
        if PlanetX_Basic.check_color(PlanetX_Basic.ColorList.RED):
            PlanetX_Display.led_brightness(PlanetX_Display.DigitalRJPin.J1, True)
            neZha.stop_all_motor()
            break
        elif PlanetX_Basic.check_color(PlanetX_Basic.ColorList.YELLOW):
            PlanetX_Display.led_brightness(PlanetX_Display.DigitalRJPin.J2, True)
            neZha.stop_all_motor()
            break
        elif PlanetX_Basic.check_color(PlanetX_Basic.ColorList.GREEN):
            PlanetX_Display.led_brightness(PlanetX_Display.DigitalRJPin.J3, True)
            neZha.stop_all_motor()
            break
        else:
            neZha.set_motor_speed(neZha.MotorList.M1, 50)
            neZha.set_motor_speed(neZha.MotorList.M2, 50)

def on_button_pressed_b():
    左转()
    basic.pause(1000)
    右转()
input.on_button_pressed(Button.B, on_button_pressed_b)

def 到路口1():
    while not (PlanetX_Basic.trackbit_state(PlanetX_Basic.TrackbitStateType.TRACKING_STATE_5)):
        巡线()
    neZha.set_motor_speed(neZha.MotorList.M2, -50)
    neZha.set_motor_speed(neZha.MotorList.M1, -50)
    basic.pause(200)
    neZha.stop_all_motor()
def 到路口2():
    while not (PlanetX_Basic.trackbit_state(PlanetX_Basic.TrackbitStateType.TRACKING_STATE_13)):
        巡线()
    neZha.set_motor_speed(neZha.MotorList.M2, -50)
    neZha.set_motor_speed(neZha.MotorList.M1, -50)
    basic.pause(200)
    neZha.stop_all_motor()
neZha.set_servo_angel(neZha.ServoTypeList._360, neZha.ServoList.S1, 225)