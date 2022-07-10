from numpy import array
from math import sqrt
import numpy as np
from Util import *

class Body:
	__slots__ = ("name", "vel", "pos", "grav_con", "color", "stored_pos", "r", "max_rendered_ticks")

	#pos = km
	#vel = km/s
	#grav_con = G*m = km^3/s^2
	def __init__(self, name, vel, pos, grav_con, color, r, max_rendered_ticks):
		self.name = name
		self.vel = array(vel)
		self.pos = array(pos)
		self.grav_con = grav_con
		self.color = color
		self.stored_pos = []
		self.r = r
		self.max_rendered_ticks = max_rendered_ticks

	#deltaT = s
	def update(self, bodyList, sec_per_tick):
		self.pos += self.vel * sec_per_tick
		px = self.pos[0]
		py = self.pos[1]
		dvx = 0
		dvy = 0
		for body in bodyList:
			if body.grav_con and body is not self:
				vecx = body.pos[0] - px
				vecy = body.pos[1] - py
				dist = sqrt(vecx * vecx + vecy* vecy)
				k = sec_per_tick * body.grav_con/(dist * dist * dist)
				dvx += k * vecx
				dvy += k * vecy
		self.vel += [dvx, dvy]

	def store_update(self):
		if(len(self.stored_pos) < self.max_rendered_ticks):
			self.stored_pos.append(self.pos/10000)

	def get_pos(self):
		return array(self.pos)

	def get_vel(self):
		return array(self.vel)

	def add_vel(self, vel, date):
		self.vel += vel
		print(f'Thrusted for deltaV of {get_len(vel)} km/s heading {get_angle(vel)} degrees at {date.strftime("%Y/%m/%d %H:%M")}')