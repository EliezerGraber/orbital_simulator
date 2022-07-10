import turtle
from math import sin, cos, pi, radians, sqrt, degrees
import asyncio
from numpy import array
import numpy as np
import keyboard
import tkinter as tk
import datetime
from UI import UI
from Body import Body
from BodyManager import BodyManager
import time
import math
from Util import *

async def main():
	ui = UI()
	bm = BodyManager(ui)
	ui.sc.bgcolor("black")

	date = datetime.datetime(2022, 1, 4, 0, 0)

	bm.add_body(
		name = "Sun",
		vel = [0.0, 0.0],
		pos = [0.0, 0.0],
		grav_con = 132712000000.0,
		color = "yellow",
		r = 10,
		max_rendered_ticks = 0)

	bm.add_body(
		name = "Earth",
		vel = point(102.9+90, 30.29),
		pos = point(102.9, 147095000),
		grav_con = 398600.0,
		color = "blue",
		r = 6,
		max_rendered_ticks = 367)

	while(date < datetime.datetime(2022, 1, 23, 0, 0)):
		date += datetime.timedelta(hours=24)
		bm.update_bodies(720, 120)
		
	bm.add_body(
		name = "Venus",
		vel = point(131.0+90, 35.26),
		pos = point(131.0, 107480000),
		grav_con = 324860.0,
		color = "#804020",
		r = 6,
		max_rendered_ticks = 230)

	while(date < datetime.datetime(2022, 2, 3, 0, 0)):
		date += datetime.timedelta(hours=24)
		bm.update_bodies(720, 120)

	bm.add_body(
		name = "Luna",
		vel = bm.get("Earth").get_vel() + point(207, 1.082),
		pos = bm.get("Earth").get_pos() + point(117, 363300+6378),
		grav_con = 4902.8,
		color = "grey",
		r = 4,
		max_rendered_ticks = 0)

	bm.add_body(
		name = "Hermes",
		vel = bm.get("Earth").get_vel() + point(257, 7.695),
		pos = bm.get("Earth").get_pos() + point(167, 6735),
		grav_con = 0,
		color = "white",
		r = 3,
		max_rendered_ticks = 10000)

	while(date < datetime.datetime(2022, 6, 21, 0, 0)):
		date += datetime.timedelta(hours=24)
		bm.update_bodies(720, 120)

	bm.add_body(
		name = "Mars",
		vel = point(336.0+90, 26.5),
		pos = point(336.0, 206650000),
		grav_con = 42828.0,
		color = "red",
		r = 6,
		max_rendered_ticks = 687)

	#bm.add_body(
	#	name = "Hermes2",
	#	vel = bm.get("Mars").get_vel() + point(257, 2ZZ),
	#	pos = bm.get("Mars").get_pos() + point(167, 50000),
	#	grav_con = 0,
	#	color = "pink",
	#	r = 3,
	#	max_rendered_ticks = 10000)

	#while True:
	#	ui.t.clear()
	#	if keyboard.is_pressed(" "):
	#		start = time.time()
	#		date += datetime.timedelta(hours=24)
	#		bm.update_bodies(720, 120)
	#		end = time.time()
	#		print(f"Time to complete a: {round(end - start, 5)}")
	#	bm.draw_bodies()
	#	ui.update(bm.get_active_body(), date)
	#	if keyboard.is_pressed("Esc"):
	#		break			

	#while(abs(math.degrees(get_angle(bm.body_list["Mars"].get_pos())) - math.degrees(get_angle(bm.body_list["Earth"].get_pos())) - 45) > 0.1):
		#date += datetime.timedelta(hours=12)
		#bm.update_bodies(72, 600)
	while(date < datetime.datetime(2022, 7, 31, 0, 0)):
		date += datetime.timedelta(hours=24)
		bm.update_bodies(720, 120)

	while(date < datetime.datetime(2022, 7, 31, 5, 15)):
		date += datetime.timedelta(minutes=1)
		bm.update_bodies(1, 60, False)

	#while(date < datetime.datetime(2022, 8, 30, 6, 0)):
	#	date += datetime.timedelta(minutes = 1)
	#	bm.update_bodies(1, 60, False)

	#while not keyboard.is_pressed("b"):
	#	ui.t.clear()
	#	bm.draw_bodies()
	#	ui.update(bm.get_active_body(), date)

	#while(abs(get_angle(bm.body_list["Hermes"].get_pos()) - get_angle(bm.body_list["Earth"].get_pos())) > 0.000000001 or abs(degrees(get_angle(bm.body_list["Hermes"].get_pos() - bm.body_list["Earth"].get_pos()) - get_angle(bm.body_list["Earth"].get_pos()))) > 90):
	#	date += datetime.timedelta(seconds = 1)
	#	bm.update_bodies(1, 1, False)

	while(abs((degrees(get_angle(bm.get("Hermes").get_vel() - bm.get("Earth").get_vel()) - get_angle(bm.get("Earth").get_pos())) + 360)%360 - 89.9886) > 0.0001):
		date += datetime.timedelta(seconds = 0.001)
		bm.update_bodies(1, 0.001, False)
		if(abs((degrees(get_angle(bm.get("Hermes").get_vel() - bm.get("Earth").get_vel()) - get_angle(bm.get("Earth").get_pos())) + 360)%360 - 90) < 0.1):
		#if(date < datetime.datetime(2022, 7, 31, 0, 41)):
			print(date.strftime("%Y/%m/%d %H:%M"), round((degrees(get_angle(bm.get("Hermes").get_vel() - bm.get("Earth").get_vel()) - get_angle(bm.get("Earth").get_pos())) + 360)%360, 4))
		#print(degrees(get_angle(bm.get("Hermes").get_vel() - bm.get("Earth").get_vel()) - get_angle(bm.get("Earth").get_pos())))
		#print(abs(get_angle_dif(degrees(get_angle(bm.get("Hermes").get_vel() - bm.get("Earth").get_vel())), degrees(get_angle(bm.get("Earth").get_pos()))) - 90))


	#print(degrees(get_angle(bm.get("Hermes").get_vel())))
	#print(get_len(bm.get("Hermes").get_vel() - bm.get("Earth").get_vel()))

	#while not keyboard.is_pressed("a"):
	#	ui.t.clear()
	#	bm.draw_bodies()
	#	ui.update(bm.get_active_body(), date)

	bm.get("Hermes").add_vel(point(degrees(get_angle(bm.get("Hermes").get_vel())), 4.25465), date)

	while not keyboard.is_pressed(" "):
		ui.t.clear()
		bm.draw_bodies()
		ui.update(bm.get_active_body(), date)

	while(get_len(bm.get("Hermes").get_pos() - bm.get("Earth").get_pos()) < 100000):
		ui.t.clear()
		date += datetime.timedelta(hours=24)
		bm.update_bodies(2880, 30)
		bm.draw_bodies()
		ui.update(bm.get_active_body(), date)

	while(get_len(bm.get("Hermes").get_pos() - bm.get("Mars").get_pos()) > 2000000):
		if(get_len(bm.get("Hermes").get_pos() - bm.get("Mars").get_pos()) < ui.closest):
			ui.closest = get_len(bm.get("Hermes").get_pos() - bm.get("Mars").get_pos())
		ui.t.clear()
		date += datetime.timedelta(hours=24)
		bm.update_bodies(720, 120)
		bm.draw_bodies()
		ui.update(bm.get_active_body(), date)

	while(get_len(bm.get("Hermes").get_pos() - bm.get("Mars").get_pos()) < ui.closest):
		ui.closest = get_len(bm.get("Hermes").get_pos() - bm.get("Mars").get_pos())
		ui.t.clear()
		date += datetime.timedelta(minutes=60)
		bm.update_bodies(720, 5)
		bm.draw_bodies()
		ui.update(bm.get_active_body(), date)

	while not keyboard.is_pressed(" "):
		ui.t.clear()
		bm.draw_bodies()
		ui.update(bm.get_active_body(), date)

	bm.get("Hermes").add_vel(point(degrees(get_angle(bm.get("Hermes").get_vel())), 4.6), date)

	while(get_len(bm.get("Hermes").get_pos() - bm.get("Mars").get_pos()) > 16000):
		ui.closest = get_len(bm.get("Hermes").get_pos() - bm.get("Mars").get_pos())
		ui.t.clear()
		date += datetime.timedelta(minutes=60)
		bm.update_bodies(720, 5)
		bm.draw_bodies()
		ui.update(bm.get_active_body(), date)

	while(get_len(bm.get("Hermes").get_pos() - bm.get("Mars").get_pos()) > 15200):
		ui.closest = get_len(bm.get("Hermes").get_pos() - bm.get("Mars").get_pos())
		ui.t.clear()
		date += datetime.timedelta(minutes=6)
		bm.update_bodies(72, 5)
		bm.draw_bodies()
		ui.update(bm.get_active_body(), date)

	u = bm.get("Hermes").get_pos()/get_len(bm.get("Hermes").get_pos())
	r = bm.get("Hermes").get_vel()
	t = array([-u[1], u[0]])
	a = get_len(r) * t - r
	#bm.body_list["Hermes"].add_vel(a)
	bm.get("Hermes").add_vel(a + point(degrees(get_angle(bm.get("Hermes").get_pos())) + 90, get_len(bm.get("Mars").get_vel()) - get_len(bm.get("Hermes").get_vel())) + point(degrees(get_angle(bm.get("Hermes").get_pos() - bm.get("Mars").get_pos())) + 90, 1.675), date)
	#bm.get("Hermes").vel = 	bm.get("Mars").get_vel()

	while True:
		#await asyncio.sleep(0.001)
		ui.t.clear()
		ui.closest = get_len(bm.get("Hermes").get_pos() - bm.get("Mars").get_pos())

		if keyboard.is_pressed(" "):
			#start = time.time()
			date += datetime.timedelta(minutes = 6)
			bm.update_bodies(36, 10)
			#end = time.time()
			#print(f"Time to complete a: {round(end - start, 4)}")

		bm.draw_bodies()
		ui.update(bm.get_active_body(), date)

		if keyboard.is_pressed("Esc"):
			break

if __name__ == "__main__":
	asyncio.run(main())