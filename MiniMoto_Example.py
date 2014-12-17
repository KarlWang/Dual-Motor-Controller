#!/usr/bin/python
# Copyright 2014 Herman Liu , Geekroo Technologies
#
#Example code demonstrating the use of the python Library for the MiniMoto Copper
#from Geekroo, which uses the DRV8830 IC for I2C low-voltage DC motor control.

#MOTO1 I2C Address
#SJ1=0(L)
#SJ1=0(L)
#WRITE=0xC0h
#READ=0xC1h

#MOTO2 I2C Address
#SJ3=0(L)
#SJ4=Open
#WRITE=0xC2h
#READ=0xC3h

from Raspi_MiniMoto_Driver import MOTO
import time

# ===========================================================================
# Example Code
# ===========================================================================

# Initialise the MiniMoto
motor1 = MOTO(0x60)
motor2 = MOTO(0x65)

while (1):
  print "Forward Speed=40!"
  motor1.drive(40)
  motor2.drive(40)
  time.sleep(3)
  print "Stop!"
  motor1.stop()
  motor2.stop()
  time.sleep(2)
  print "Reverse Speed=-40!"
  motor1.drive(-40)
  motor2.drive(-40)
  time.sleep(3)
  print "Brake!"
  motor1.brake()
  motor2.brake()
  time.sleep(2)

