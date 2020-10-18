from __future__ import print_function # use python 3 syntax but make it compatible with python 2
from __future__ import division       #                           ''

import time     # import the time library for the sleep function
import brickpi3 # import the BrickPi3 drivers


class Brick:
    def __init__(self):
        self._brickPi = brickpi3.BrickPi3()
        self._brickPi.reset_all()
        # init sensors
        BP = self._brickPi
        BP.set_sensor_type(BP.PORT_1, BP.SENSOR_TYPE.EV3_COLOR_REFLECTED)
        BP.set_sensor_type(BP.PORT_4, BP.SENSOR_TYPE.EV3_COLOR_REFLECTED)
        self.wait_sensors_ready([BP.PORT_1, BP.PORT_4])
        self._speed = 180

    def wait_sensors_ready(self, sensors):
        while True:
            try:
                for s in sensors:
                    self._brickPi.get_sensor(s)
                break
            except brickpi3.SensorError as error:
                print(error)


    def move_follow_line(self, stop, degrees=9999):
        
        # Forward only
        assert degrees >= 0
        
        BP = self._brickPi
        k = 1.2
        
        # обнуляем энкодеры моторов
        BP.reset_motor_encoder(BP.PORT_A | BP.PORT_D)
                
        ports = [BP.PORT_A, BP.PORT_D]
        while self.get_motor_encoder_avg(ports) < degrees:
            try:
                value1 = BP.get_sensor(BP.PORT_1)
                value2 = BP.get_sensor(BP.PORT_4)
                BP.set_motor_dps(BP.PORT_A, self._speed+(value1-value2)*k)
                BP.set_motor_dps(BP.PORT_D, self._speed-(value1-value2)*k)
                print("move", value1, " --- ", value2)
                if stop():
                    break
            except brickpi3.SensorError as error:
                print(error)
            
            time.sleep(0.02)
        # Stopping
        BP.set_motor_dps(BP.PORT_A | BP.PORT_D, 0)
        time.sleep(0.3)
    
    def move_for_degrees(self, degrees):
        import math
        
        BP = self._brickPi
        speed = self._speed
        
        # обнуляем энкодеры моторов
        BP.reset_motor_encoder(BP.PORT_A | BP.PORT_D)
        
        # устанавливаем скорость вращения моторов
        BP.set_motor_dps(BP.PORT_A | BP.PORT_D, math.copysign(speed, degrees))
        
        # ждем пока энкодеры не достинут целевого значения
        ports = [BP.PORT_A, BP.PORT_D]
        while abs(self.get_motor_encoder_avg(ports)) < abs(degrees):
            time.sleep(0.03)
            
        # тормозим!
        self.stop_motors()
        
    def stop_motors(self):
        BP = self._brickPi
        # понижаем скорость плавно за 10 итераций
        for i in range(10, 0, -1):
            speed = int((i / 10) * BP.get_motor_status(BP.PORT_A)[-1])
            BP.set_motor_dps(BP.PORT_A | BP.PORT_D, speed)
            time.sleep(0.02)
            
        # оконательно тормозим
        BP.set_motor_dps(BP.PORT_A | BP.PORT_D, 0)
        time.sleep(0.1)
        
    def get_motor_encoder_avg(self, ports):
        return sum([self._brickPi.get_motor_encoder(p) for p in ports]) / len(ports)
    
    def black_or_white(self):
        BP = self._brickPi
        value1 = self._brickPi.get_sensor(BP.PORT_1)
        value2 = self._brickPi.get_sensor(BP.PORT_4)
        if (value1 + value2)/2 >= 25:
            return 0
        else:
            return 1
    def stop_if_line(self):
        BP = self._brickPi
        
        value1 = self._brickPi.get_sensor(BP.PORT_1)
        value2 = self._brickPi.get_sensor(BP.PORT_4)
        return (value1 + value2)/2 <= 10
    
    def reset_all(self):
        self._brickPi.reset_all()
    
    def rotate(self, degrees):
        #degrees = -degrees
        
        BP = self._brickPi
        
        BP.reset_motor_encoder(BP.PORT_A | BP.PORT_D)
        
        if degrees >= 0:
            port = BP.PORT_D
            BP.set_motor_dps(BP.PORT_D, self._speed)
            BP.set_motor_dps(BP.PORT_A, -self._speed)
        else:
            port = BP.PORT_A
            BP.set_motor_dps(BP.PORT_D, -self._speed)
            BP.set_motor_dps(BP.PORT_A, self._speed)
        
        
        target_degrees = BP.get_motor_encoder(port) + abs(degrees)
        
        while BP.get_motor_encoder(port) < target_degrees:
            time.sleep(0.03)
        
        BP.set_motor_dps(BP.PORT_A | BP.PORT_D, 0)
        time.sleep(0.3)
    
if __name__ == '__main__':
    b = Brick()
    try:
        b.rotate(135)
        #b.move_follow_line(b.stop_if_line)
        #b.move_for_degrees(140)
    finally: # except the program gets interrupted by Ctrl+C on the keyboard.
        b.reset_all()    
