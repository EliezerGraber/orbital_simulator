from Body import Body

class BodyManager(object):
	body_list = {}
	body_order = []

	def __init__(self, ui):
		self.ui = ui

	def add_body(self, name, vel, pos, grav_con, color, r, max_rendered_ticks):
		self.body_list[name] = Body(name, vel, pos, grav_con, color, r, max_rendered_ticks)
		self.ui.add_body()
		self.body_order.append(name)

	def update_bodies(self):
		for name, body in self.body_list.items():
			body.update([b for n, b in self.body_list.items() if n is not name])

	def draw_bodies(self):
		for name, body in self.body_list.items():
			self.ui.draw_body(body)

	def get_active_body(self):
		return self.body_list[self.body_order[self.ui.active_body]]