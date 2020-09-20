# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 03:07:04 2020

@author: pinra
"""

import serial
import time
import numpy  as np 
import matplotlib.pyplot as plt

tempF= []
hum=[]
tempP = []
humP = []
cntan = []
cnt = 0

arduinoData = serial.Serial('com6', 9600) 
 
while True: 
    while (arduinoData.inWaiting()==0): #Wait until data
        pass 
   # time.sleep(2)
    arduinoString = arduinoData.readline() 
    decoded_values = str(arduinoString[0:len(arduinoString)].decode("utf-8"))
    dataArray = decoded_values.split('x')   
    temp = float( dataArray[0])          
    H = float( dataArray[1])
    
    mintemp = 25 
    rangetemp = 20
    difftemp = temp - mintemp
    increment = 1/rangetemp
    scaledtemp = difftemp * increment
    
    minhum = 25
    rangehum = 75
    diffhum = H - minhum
    incrementH = 1/rangehum
    scaledhum = diffhum * incrementH
    
    tempP.append(scaledtemp)
    humP.append(scaledhum)
    
    temparr = np.array(tempP)
    humarr = np.array(humP)
    
    cnteff = np.deg2rad(cnt*6)
    cntan.append(cnteff)
    cntarr = np.array(cntan)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='polar')
    ax = plt.subplot(111, polar=True)
    ax.set_theta_direction(-1)       
    ax.set_ylim(0,1)
    ax.set_theta_offset(np.pi/2.0)   

    plt.polar(cntarr,temparr,'x-', color ="orange")
    plt.polar(cntarr,humarr,'.-', color="purple")                          

    plt.pause(.000001)
    cnt=cnt+1
