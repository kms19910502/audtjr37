import time
import serial

import dbConn as dC

import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QWidget, QVBoxLayout
from PyQt5.QtGui import QFont


import RPi.GPIO as GPIO




import smbus			#import SMBus module of I2C
from time import sleep          #import



#some MPU6050 Registers and their Address
PWR_MGMT_1   = 0x6B
SMPLRT_DIV   = 0x19
CONFIG       = 0x1A
GYRO_CONFIG  = 0x1B
INT_ENABLE   = 0x38
ACCEL_XOUT_H = 0x3B
ACCEL_YOUT_H = 0x3D
ACCEL_ZOUT_H = 0x3F
GYRO_XOUT_H  = 0x43
GYRO_YOUT_H  = 0x45
GYRO_ZOUT_H  = 0x47


def MPU_Init():
	#write to sample rate register
	bus.write_byte_data(Device_Address, SMPLRT_DIV, 7)
	
	#Write to power management register
	bus.write_byte_data(Device_Address, PWR_MGMT_1, 1)
	
	#Write to Configuration register
	bus.write_byte_data(Device_Address, CONFIG, 0)
	
	#Write to Gyro configuration register
	bus.write_byte_data(Device_Address, GYRO_CONFIG, 24)
	
	#Write to interrupt enable register
	bus.write_byte_data(Device_Address, INT_ENABLE, 1)

def read_raw_data(addr):
	#Accelero and Gyro value are 16-bit
        high = bus.read_byte_data(Device_Address, addr)
        low = bus.read_byte_data(Device_Address, addr+1)
    
        #concatenate higher and lower value
        value = ((high << 8) | low)
        
        #to get signed value from mpu6050
        if(value > 32768):
                value = value - 65536
        return value


bus = smbus.SMBus(1) 	# or bus = smbus.SMBus(0) for older version boards
Device_Address = 0x68   # MPU6050 device address

MPU_Init()









# 센서 핀 설정

#자이로센서 SDA=2,SCL=3

#수위감지 센서
sensor_pin = 27



# 부저 
buzzer_pin = 18


#불꽃감지 센서
inputPin = 17


# GPIO 설정
GPIO.setmode(GPIO.BCM) #BCM이 아니라  BOARD명 피지컬핀
GPIO.setup(sensor_pin, GPIO.IN)
GPIO.setup(inputPin, GPIO.IN)
GPIO.setup(buzzer_pin, GPIO.OUT)


# 센서로부터 데이터 읽기
def read_sensor():
    return GPIO.input(sensor_pin)














ser = serial.Serial('/dev/ttyAMA0', 9600, timeout=1)

app = QApplication(sys.argv)

window = QMainWindow()
layout = QVBoxLayout()

temperature_label = QLabel("Temperature")
humidity_label = QLabel("Humidity")
light_label = QLabel("Light")
soil_label = QLabel("Soil moisture")
water_label = QLabel("물통의 물이 있는지 체크합니다.")
mpu_label = QLabel("수평을 체크합니다.")

font = QFont("Arial", 20)
temperature_label.setFont(font)
humidity_label.setFont(font)
light_label.setFont(font)
soil_label.setFont(font)
water_label.setFont(font)
mpu_label.setFont(font)



layout.addWidget(temperature_label)
layout.addWidget(humidity_label)
layout.addWidget(light_label)
layout.addWidget(soil_label)
layout.addWidget(water_label)
layout.addWidget(mpu_label)


widget = QWidget()
widget.setLayout(layout)

window.setCentralWidget(widget)
window.setWindowTitle("smartFarm")
window.setStyleSheet("background-color: white;")
window.show()







while True:
    data = ser.readline().decode()

    if "temperature:" in data:
        temperature = int(data.split(":")[1])
        temperatureValue = temperature
        dC.insertSensor1(temperatureValue)
        temperature_label.setText("Temperature(°C) : " + str(temperatureValue))
        app.processEvents()
        temperature_label.setStyleSheet("color: blue;"
                       "background-color: #87CEFA;"
                       "border-style: dashed;"
                       "border-width: 3px;"
                       "border-color: #1E90FF")
        

    if "humidity:" in data:
        humidity = int(data.split(":")[1])
        humidityValue = humidity
        dC.insertSensor2(humidityValue)
        humidity_label.setText("Humidity(%) : " + str(humidityValue))
        app.processEvents()
        humidity_label.setStyleSheet("color: blue;"
                       "background-color: #87CEFA;"
                       "border-style: dashed;"
                       "border-width: 3px;"
                       "border-color: #1E90FF")
     

    if "light :" in data:
        adc1 = int(data.split(":")[1])
        adc1Value = adc1
        dC.insertSensor3(adc1Value)
        light_label.setText("Light : " + str(adc1Value))
        app.processEvents()
        light_label.setStyleSheet("color: blue;"
                       "background-color: #87CEFA;"
                       "border-style: dashed;"
                       "border-width: 3px;"
                       "border-color: #1E90FF")
        

    if "soil :" in data:
        adc2 = int(data.split(":")[1])
        adc2Value = adc2
        dC.insertSensor4(adc2Value)
        soil_label.setText("Soil moisture : " + str(adc2Value))
        soil_label.setStyleSheet("color: blue;"
                       "background-color: #87CEFA;"
                       "border-style: dashed;"
                       "border-width: 3px;"
                       "border-color: #1E90FF")
        app.processEvents()




    #불꽃감지 센서 관련 동작
    val = GPIO.input(inputPin)
    #print(val)

    if val == 0:
        
        GPIO.output(buzzer_pin, True)
        time.sleep(1)
    else:
        
        GPIO.output(buzzer_pin, False)

# 수위센서 관련 동작
   

    if (read_sensor() == 0):
        water_label.setText("물통에 물이 충분합니다.")
        water_label.setStyleSheet("color: green;"
                      "border-style: dashed;"
                      "border-width: 3px;"
                      "border-color: #7FFFD4;;"
                      "background-color: white;"
                      "border-radius: 3px")
    else:
        water_label.setText("경고 : 물통에 물이 부족합니다!!")
        water_label.setStyleSheet("color: red;"
                      "border-style: dashed;"
                      "border-width: 3px;"
                      "border-color: #FA8072;"
                      "background-color: white;"
                      "border-radius: 3px")






    #자이로센서 관련동작

    #Read Accelerometer raw value
    acc_x = read_raw_data(ACCEL_XOUT_H)
    acc_y = read_raw_data(ACCEL_YOUT_H)
    acc_z = read_raw_data(ACCEL_ZOUT_H)

    #Read Gyroscope raw value
    gyro_x = read_raw_data(GYRO_XOUT_H)
    gyro_y = read_raw_data(GYRO_YOUT_H)
    gyro_z = read_raw_data(GYRO_ZOUT_H)

    #Full scale range +/- 250 degree/C as per sensitivity scale factor
    Ax = acc_x/16384.0
    Ay = acc_y/16384.0
    Az = acc_z/16384.0

    Gx = gyro_x/131.0
    Gy = gyro_y/131.0
    Gz = gyro_z/131.0


    print ("Gx=%.2f" %Gx, u'\u00b0'+ "/s", "\tGy=%.2f" %Gy, u'\u00b0'+ "/s", "\tGz=%.2f" %Gz, u'\u00b0'+ "/s", "\tAx=%.2f g" %Ax, "\tAy=%.2f g" %Ay, "\tAz=%.2f g" %Az) 	
    sleep(1)

    if Ax>0.35 or Ax<-0.35:
        mpu_label.setText("경고!! 수평이 맞지 않습니다!!")
        mpu_label.setStyleSheet("color: red;"
                      "border-style: dashed;"
                      "border-width: 3px;"
                      "border-color: #FA8072;"
                      "background-color: white;"
                      "border-radius: 3px")

    elif Ay>0.2 or Ay<-0.2:
        mpu_label.setText("경고!! 수평이 맞지 않습니다!!")
        mpu_label.setStyleSheet("color: red;"
                      "border-style: dashed;"
                      "border-width: 3px;"
                      "border-color: #FA8072;"
                      "background-color: white;"
                      "border-radius: 3px")
        

    elif Az>1.05:
        mpu_label.setText("경고!! 수평이 맞지 않습니다!!")
        mpu_label.setStyleSheet("color: red;"
                      "border-style: dashed;"
                      "border-width: 3px;"
                      "border-color: #FA8072;"
                      "background-color: white;"
                      "border-radius: 3px")
    

    else:
        mpu_label.setText("수평 이상 없습니다.")
        mpu_label.setStyleSheet("color: green;"
                      "border-style: dashed;"
                      "border-width: 3px;"
                      "border-color:#7FFFD4;"
                      "background-color: white;"
                      "border-radius: 3px")


# GPIO 정리
GPIO.cleanup()
