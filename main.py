import turtle
from math import sin, cos, pi, radians, sqrt
import asyncio
from numpy import array
import numpy
import keyboard
import tkinter as tk
import datetime
from UI import UI
from Body import Body
from BodyManager import BodyManager

def point(theta, r):
	x = r * cos(radians(theta))
	y = r * sin(radians(theta))
	return array([x, y])

async def main():
	ui = UI()
	body_manager = BodyManager(ui)
	ui.sc.bgcolor("black")

	date = datetime.datetime(2022, 1, 4, 0, 0)

	body_manager.add_body(
		name = "Sun",
		vel = [0.0, 0.0],
		pos = [0.0, 0.0],
		grav_con = 132712000000.0,
		color = "yellow",
		r = 10,
		max_rendered_ticks = 1000)

	body_manager.add_body(
		name = "Earth",
		vel = point(102.9+90, 30.29),
		pos = point(102.9, 147095000),
		grav_con = 398600,
		color = "blue",
		r = 6,
		max_rendered_ticks = 366)

	body_manager.add_body(
		name = "Mars",
		vel = point(251.0+90, 26.5),
		pos = point(251.0, 206650000),
		grav_con = 42828,
		color = "red",
		r = 6,
		max_rendered_ticks = 687)

	body_manager.add_body(
		name = "Venus",
		vel = point(131.0+90, 35.26),
		pos = point(131.0, 107480000),
		grav_con = 324860,
		color = "#804020",
		r = 6,
		max_rendered_ticks = 230)

	body_manager.add_body(
		name = "Luna",
		vel = point(102.9+90, 30.29) + point(180, 1.082),
		pos = point(102.9, 147095000) + point(90, 363300),
		grav_con = 4902.8,
		color = "grey",
		r = 4,
		max_rendered_ticks = 366)

	while True:
		await asyncio.sleep(0.001)
		ui.t.clear()

		if not keyboard.is_pressed(" "):
			date += datetime.timedelta(days=1)
			body_manager.update_bodies()
		
		body_manager.draw_bodies()

		ui.update(body_manager.get_active_body(), date)

		if keyboard.is_pressed("Esc"):
			break

asyncio.run(main())