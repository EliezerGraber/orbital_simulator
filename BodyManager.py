from Body import Body

class BodyManager(object):
	body_list = []
	body_names = {}

	def __init__(self, ui):
		self.ui = ui

	def add_body(self, name, vel, pos, grav_con, color, r, max_rendered_ticks):
		self.body_names[name] = len(self.body_list)
		self.body_list.append(Body(name, vel, pos, grav_con, color, r, max_rendered_ticks))
		self.ui.add_body()

	def update_bodies(self, iterations, sec_per_tick, update_store = True):
		#for tick in range(iterations):
		#	names = [body.update([b for n, b in self.body_list.items() if n is not name and b.grav_con > 0], sec_per_tick) for name, body in self.body_list.items()]
		
		for tick in range(iterations):
			for body in self.body_list:
				body.update(self.body_list, sec_per_tick)
				#body.update([b for b in self.body_list if b is not body and b.grav_con > 0], sec_per_tick)

		#for tick in range(iterations):
		#	self.body_list = list(map(lambda body: body.update([b for b in self.body_list if b.name is not body.name and b.grav_con > 0], sec_per_tick), self.body_list))

		if update_store:
			for body in self.body_list:
				body.store_update()
			#map(lambda body: body.store_update(), self.body_list)

	def draw_bodies(self):
		for body in self.body_list:
			self.ui.draw_body(body)
		#map(lambda body: self.ui.draw_body(body), self.body_list)

	def get_active_body(self):
		return self.body_list[self.ui.active_body]

	def get(self, name):
		return self.body_list[self.body_names[name]]