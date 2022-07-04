import turtle
from math import sin, cos, pi, radians, sqrt
import asyncio
import random
from numpy import array
import numpy
import keyboard
import time
import tkinter as tk

#sc = turtle.Screen()
#t = turtle.Turtle()
count = 0.0
scale = 800000.0
translation = [0, 0]

start = [0, 0]
dragging = False

def mouse_wheel(event):
	global count
	global scale
	# respond to Linux or Windows wheel event
	if event.num == 5 or event.delta == -120:
		count -= 0.08
	if event.num == 4 or event.delta == 120:
		count += 0.08

	scale = 800000.0 * 10 ** count

def startMove(event):
	global dragging
	dragging = True
	start[0] = event.x_root
	start[1] = event.y_root

def stopMove(event):
	global dragging
	dragging = False

def drag(event):
	global dragging
	if dragging:
		translation[0] += (event.x_root - start[0]) * scale
		translation[1] -= (event.y_root - start[1]) * scale
		start[0] = event.x_root
		start[1] = event.y_root
	else:
		dragging = True
		start[0] = event.x_root
		start[1] = event.y_root

root = tk.Tk()
canvas = turtle.ScrolledCanvas(root, 800, 800)
canvas.pack()
sc = turtle.TurtleScreen(canvas)
t = turtle.RawTurtle(sc)
t.speed(0)
sc.tracer(False)
canvas.bind("<MouseWheel>", mouse_wheel)
canvas.bind("<B2-Motion>", drag)
canvas.bind('<ButtonPress-2>', startMove)
canvas.bind('<ButtonRelease-2>', stopMove)
t.ht()
t.penup()

def point(theta, r):
	x = r * cos(radians(theta))
	y = r * sin(radians(theta))
	return [x, y]

class Body:
	#pos = km
	#vel = km/s
	#gravCon = G*m = km^3/s^2
	def __init__(self, vel, pos, gravCon, color):
		self.vel = array(vel)
		self.pos = array(pos)
		self.gravCon = gravCon
		self.color = color
		self.storePos = []
		self.storeIdx = 0

	#deltaT = s
	def update(self, bodyList, day, max_list_len):
		self.pos += self.vel * 60 * 60 * 24
		for body in bodyList:
			direction = (body.pos - self.pos)/numpy.linalg.norm(self.pos - body.pos)
			self.vel += 60 * 60 * 24 * direction * body.gravCon/((numpy.linalg.norm(self.pos - body.pos))*(numpy.linalg.norm(self.pos - body.pos)))
		self.storeDay = day
		if(len(self.storePos) < max_list_len):
			self.storePos.append(self.pos/10000)

		self.draw(6)

	def redraw(self):
		t.color(self.color)
		for pos in self.storePos:
			t.goto( round((pos[0]*10000 + translation[0])/scale), round((pos[1]*10000 + translation[1])/scale))
			t.pendown()
		t.penup()
		#turtle.update()

	def draw(self, r):
		t.goto((self.pos[0] + translation[0])/scale, (self.pos[1] + translation[1])/scale-r)
		t.pendown()
		t.color(self.color)
		t.begin_fill()
		t.circle(r)
		t.end_fill()
		t.penup()
		#turtle.update()

async def main():
	
	hr = 0
	bodyList = []
	#for theta in range(0, 360):
	#	graph.update(theta, 0.5)
	#x = 0
	#draw_task = asyncio.create_task(graph.draw())
	#while True:
	#	graph.update(x, random.randint(0, 50)/100.0 + 0.5)
	#	await asyncio.sleep(0.01)
	#	print(x)
	#	x += 1
	#	x %= 360
	sun = Body([0.0, 0.0], [0.0, 0.0], 132712000000.0, "yellow")
	bodyList.append(sun)
	#earth = Body([0.0, 29.29], [152100000.0, 0.0], 0, "blue")
	earth = Body(point(102.9+90, 30.29), point(102.9, 147095000), 398600, "blue")
	mars = Body(point(251.0+90, 26.5), point(251.0, 206650000), 42828, "red")
	venus = Body(point(131.0+90, 35.26), point(131.0, 107480000), 324860, "#804020")
	
	sc.bgcolor("black")
	
	while True:
		#time.sleep(0.002)
		hr += 24
		#if(hr%48 == 0):
		#	print("Dis:", round(numpy.linalg.norm(earth.pos)/(1000000), 2), "Vel:", round(numpy.linalg.norm(earth.vel), 2), "Day:", hr/24)
		
		await asyncio.sleep(0.001)
		t.clear()
		earth.update([sun, venus, mars], round(hr/24), 366)
		earth.redraw()
		mars.update([sun, earth, venus], round(hr/24), 687)
		mars.redraw()
		venus.update([sun, earth, mars], round(hr/24), 230)
		venus.redraw()
		sun.update([venus, earth, mars], round(hr/24), 10000)
		sun.redraw()
		t.goto(-380, 360)
		t.color("white")
		style = ('Arial', 14, 'normal')
		t.write(f'Day: {round(hr/24,2)}', font=style)
		t.goto(-380, 330)
		t.write(f'Scale: {round(scale)} km/px', font=style)
		sc.update()
		
		if keyboard.is_pressed("Esc"):
			break

asyncio.run(main())