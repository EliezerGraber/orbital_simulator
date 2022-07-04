import turtle
from math import sin, cos, pi, radians, sqrt
import asyncio
import random
from numpy import array
import numpy
import keyboard
import time
import tkinter as tk
import datetime
from ui import UI
from body import Body

bodyList = []

def point(theta, r):
	x = r * cos(radians(theta))
	y = r * sin(radians(theta))
	return array([x, y])

ui = UI()

async def main():
	
	hr = 0
	activeBodyLastPos = array([0,0])
	date = datetime.datetime(2022, 1, 4, 0, 0)
	sun = Body("Sun", [0.0, 0.0], [0.0, 0.0], 132712000000.0, "yellow", 10)
	#earth = Body([0.0, 29.29], [152100000.0, 0.0], 0, "blue")
	earth = Body("Earth", point(102.9+90, 30.29), point(102.9, 147095000), 398600, "blue", 6)
	mars = Body("Mars", point(251.0+90, 26.5), point(251.0, 206650000), 42828, "red", 6)
	venus = Body("Venus", point(131.0+90, 35.26), point(131.0, 107480000), 324860, "#804020", 6)
	luna = Body("Luna", point(102.9+90, 30.29) + point(180, 1.082), point(102.9, 147095000) + point(90, 363300), 4902.8, "grey", 4)
	
	bodyList.append(sun)
	bodyList.append(earth)
	bodyList.append(mars)
	bodyList.append(venus)
	bodyList.append(luna)

	ui.add_body()
	ui.add_body()
	ui.add_body()
	ui.add_body()
	ui.add_body()

	ui.sc.bgcolor("black")
	
	while True:
		await asyncio.sleep(0.001)
		ui.t.clear()
		if not keyboard.is_pressed(" "):
			hr += 24
			date += datetime.timedelta(days=1)
			earth.update([sun, venus, mars, luna], round(hr/24), 366)
			mars.update([sun, earth, venus, luna], round(hr/24), 687)
			venus.update([sun, earth, mars, luna], round(hr/24), 230)
			sun.update([venus, earth, mars, luna], round(hr/24), 10000)
			luna.update([sun, venus, mars, earth], round(hr/24), 366)
		ui.draw_body(earth)
		ui.draw_body(mars)
		ui.draw_body(venus)
		ui.draw_body(sun)
		ui.draw_body(luna)
		ui.t.goto(-380, 360)
		ui.t.color("white")
		style = ('Arial', 14, 'normal')
		ui.t.write(f'Date: {date.strftime("%Y/%m/%d")}', font=style)
		ui.t.goto(-380, 330)
		ui.t.write(f'Scale: {round(ui.scale)} km/px', font=style)
		ui.t.goto(-380, 300)
		ui.t.write(f'Body: {bodyList[ui.activeBody].name}', font=style)
		ui.sc.update()
		
		ui.translation -= bodyList[ui.activeBody].pos - activeBodyLastPos
		activeBodyLastPos = bodyList[ui.activeBody].getPos()

		if keyboard.is_pressed("Esc"):
			break

asyncio.run(main())