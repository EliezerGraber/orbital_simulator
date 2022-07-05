from numpy import array
import numpy

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
	def update(self, bodyList):
		self.pos += self.vel * 60 * 60 * 24
		for body in bodyList:
			direction = (body.pos - self.pos)/numpy.linalg.norm(self.pos - body.pos)
			self.vel += 60 * 60 * 24 * direction * body.grav_con/((numpy.linalg.norm(self.pos - body.pos))*(numpy.linalg.norm(self.pos - body.pos)))

		if(len(self.stored_pos) < self.max_rendered_ticks):
			self.stored_pos.append(self.pos/10000)

	def get_pos(self):
		return array(self.pos)

	def get_vel(self):
		return array(self.vel)