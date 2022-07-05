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

	def update_bodies(self, iterations, min_per_tick):
		for tick in range(0, iterations):
			names = [body.update([b for n, b in self.body_list.items() if n is not name and b.grav_con > 0], min_per_tick) for name, body in self.body_list.items()]

		for name, body in self.body_list.items():
			body.store_update()

	def draw_bodies(self):
		temp = [self.ui.draw_body(body) for name, body in self.body_list.items()]

	def get_active_body(self):
		return self.body_list[self.body_order[self.ui.active_body]]