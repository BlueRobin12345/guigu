function 右转 () {
    neZha.setMotorSpeed(neZha.MotorList.M1, 35)
    neZha.setMotorSpeed(neZha.MotorList.M2, -35)
    basic.pause(400)
    neZha.stopAllMotor()
}
function 左转 () {
    neZha.setMotorSpeed(neZha.MotorList.M1, -35)
    neZha.setMotorSpeed(neZha.MotorList.M2, 35)
    basic.pause(400)
    neZha.stopAllMotor()
}
input.onButtonPressed(Button.A, function () {
    basic.showString("1")
    到路口1()
    左转()
    neZha.setMotorSpeed(neZha.MotorList.M2, 50)
    neZha.setMotorSpeed(neZha.MotorList.M1, 50)
    basic.pause(200)
    neZha.stopAllMotor()
    识别颜色()
    basic.pause(500)
    neZha.setMotorSpeed(neZha.MotorList.M2, -50)
    neZha.setMotorSpeed(neZha.MotorList.M1, -50)
    basic.pause(200)
    neZha.stopAllMotor()
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
    neZha.setMotorSpeed(neZha.MotorList.M2, 50)
    neZha.setMotorSpeed(neZha.MotorList.M1, 50)
    basic.pause(700)
    neZha.stopAllMotor()
    左转()
    basic.pause(100)
    到路口1()
})
function 巡线 () {
    PlanetX_Basic.Trackbit_get_state_value()
    if (PlanetX_Basic.TrackbitState(PlanetX_Basic.TrackbitStateType.Tracking_State_1)) {
        neZha.setMotorSpeed(neZha.MotorList.M1, -40)
        neZha.setMotorSpeed(neZha.MotorList.M2, -40)
    }
    if (PlanetX_Basic.TrackbitState(PlanetX_Basic.TrackbitStateType.Tracking_State_3) || PlanetX_Basic.TrackbitState(PlanetX_Basic.TrackbitStateType.Tracking_State_11)) {
        neZha.setMotorSpeed(neZha.MotorList.M1, -80)
        neZha.setMotorSpeed(neZha.MotorList.M2, -9)
    }
    if (PlanetX_Basic.TrackbitState(PlanetX_Basic.TrackbitStateType.Tracking_State_2) || PlanetX_Basic.TrackbitState(PlanetX_Basic.TrackbitStateType.Tracking_State_14)) {
        neZha.setMotorSpeed(neZha.MotorList.M1, -9)
        neZha.setMotorSpeed(neZha.MotorList.M2, -80)
    }
    if (PlanetX_Basic.TrackbitState(PlanetX_Basic.TrackbitStateType.Tracking_State_8)) {
        neZha.setMotorSpeed(neZha.MotorList.M1, -80)
        neZha.setMotorSpeed(neZha.MotorList.M2, -4)
    }
    if (PlanetX_Basic.TrackbitState(PlanetX_Basic.TrackbitStateType.Tracking_State_12)) {
        neZha.setMotorSpeed(neZha.MotorList.M1, -4)
        neZha.setMotorSpeed(neZha.MotorList.M2, -80)
    }
    if (PlanetX_Basic.TrackbitState(PlanetX_Basic.TrackbitStateType.Tracking_State_0)) {
        neZha.setMotorSpeed(neZha.MotorList.M1, -40)
        neZha.setMotorSpeed(neZha.MotorList.M2, -40)
    }
}
function 舵机 () {
    neZha.setServoAngel(neZha.ServoTypeList._360, neZha.ServoList.S1, 120)
    basic.pause(300)
    neZha.setServoAngel(neZha.ServoTypeList._360, neZha.ServoList.S1, 225)
}
function 识别颜色 () {
    while (true) {
        if (PlanetX_Basic.checkColor(PlanetX_Basic.ColorList.red)) {
            PlanetX_Display.ledBrightness(PlanetX_Display.DigitalRJPin.J1, true)
            neZha.stopAllMotor()
            break;
        } else if (PlanetX_Basic.checkColor(PlanetX_Basic.ColorList.yellow)) {
            PlanetX_Display.ledBrightness(PlanetX_Display.DigitalRJPin.J2, true)
            neZha.stopAllMotor()
            break;
        } else if (PlanetX_Basic.checkColor(PlanetX_Basic.ColorList.green)) {
            PlanetX_Display.ledBrightness(PlanetX_Display.DigitalRJPin.J3, true)
            neZha.stopAllMotor()
            break;
        } else {
            neZha.setMotorSpeed(neZha.MotorList.M1, 50)
            neZha.setMotorSpeed(neZha.MotorList.M2, 50)
        }
    }
}
function 到路口1 () {
    while (!(PlanetX_Basic.TrackbitState(PlanetX_Basic.TrackbitStateType.Tracking_State_5))) {
        巡线()
    }
    neZha.setMotorSpeed(neZha.MotorList.M2, -50)
    neZha.setMotorSpeed(neZha.MotorList.M1, -50)
    basic.pause(200)
    neZha.stopAllMotor()
}
function 到路口2 () {
    while (!(PlanetX_Basic.TrackbitState(PlanetX_Basic.TrackbitStateType.Tracking_State_13))) {
        巡线()
    }
    neZha.setMotorSpeed(neZha.MotorList.M2, -50)
    neZha.setMotorSpeed(neZha.MotorList.M1, -50)
    basic.pause(200)
    neZha.stopAllMotor()
}
neZha.setServoAngel(neZha.ServoTypeList._360, neZha.ServoList.S1, 225)
