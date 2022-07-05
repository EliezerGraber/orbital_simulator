from numpy import array
import math
import numpy as np

class Body:
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
		for body in bodyList:
			vec = body.pos - self.pos
			dist = math.sqrt(vec[0] * vec[0] + vec[1] * vec[1])
			self.vel += sec_per_tick * vec * body.grav_con/(dist * dist * dist)
		return self.name

	def store_update(self):
		if(len(self.stored_pos) < self.max_rendered_ticks):
			self.stored_pos.append(self.pos/10000)

	def get_pos(self):
		return array(self.pos)

	def get_vel(self):
		return array(self.vel)