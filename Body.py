from numpy import array
import numpy

class Body:
	#pos = km
	#vel = km/s
	#grav_con = G*m = km^3/s^2
	def __init__(self, name, vel, pos, grav_con, color, r):
		self.name = name
		self.vel = array(vel)
		self.pos = array(pos)
		self.grav_con = grav_con
		self.color = color
		self.stored_pos = []
		self.r = r

	#deltaT = s
	def update(self, bodyList, max_list_len):
		self.pos += self.vel * 60 * 60 * 24
		for body in bodyList:
			direction = (body.pos - self.pos)/numpy.linalg.norm(self.pos - body.pos)
			self.vel += 60 * 60 * 24 * direction * body.grav_con/((numpy.linalg.norm(self.pos - body.pos))*(numpy.linalg.norm(self.pos - body.pos)))

		if(len(self.stored_pos) < max_list_len):
			self.stored_pos.append(self.pos/10000)

	def getPos(self):
		return array(self.pos)