import math
from math import sin, cos, pi, radians, sqrt, degrees
from numpy import array

def point(theta, r):
	x = r * cos(radians(theta))
	y = r * sin(radians(theta))
	return array([x, y])

def get_angle(vec):
	return math.atan2(vec[1], vec[0])

def get_len(vec):
	return math.sqrt(sum(i**2 for i in vec))

def get_angle_dif(a1, a2):
	return 180 - abs(abs(a1 - a2) - 180)
