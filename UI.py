import tkinter as tk
import turtle
from numpy import array

class UI():
	start = [0, 0]
	dragging = False
	active_body = 0
	wheel_count = 0.0
	scale = 800000.0
	translation = [0, 0]
	body_num = 0
	activeBodyLastPos = array([0,0])
	style = ('Arial', 14, 'normal')

	def __init__(self):
		self.root = tk.Tk()
		self.root.title("Orbital Simulator")
		self.canvas = turtle.ScrolledCanvas(self.root, 800, 800)
		self.root.resizable(False, False)
		self.canvas.pack()
		self.sc = turtle.TurtleScreen(self.canvas)
		self.t = turtle.RawTurtle(self.sc)
		self.t.speed(0)
		self.sc.tracer(False)
		self.canvas.bind('<MouseWheel>', self.mouse_wheel)
		self.canvas.bind('<B2-Motion>', self.drag)
		self.canvas.bind('<ButtonPress-2>', self.startMove)
		self.canvas.bind('<ButtonRelease-2>', self.stopMove)
		self.root.bind('<Up>', lambda event, up=True: self.switch_focus(event, up))
		self.root.bind('<Down>', lambda event, up=False: self.switch_focus(event, up))
		self.t.ht()
		self.t.penup()

	def mouse_wheel(self, event):
		# respond to Linux or Windows wheel event
		if event.num == 5 or event.delta == -120:
			self.wheel_count += 0.08
		if event.num == 4 or event.delta == 120:
			self.wheel_count -= 0.08

		self.scale = 800000.0 * 10 ** self.wheel_count

	def startMove(self, event):
		self.dragging = True
		self.start[0] = event.x_root
		self.start[1] = event.y_root

	def stopMove(self, event):
		self.dragging = False

	def drag(self, event):
		if self.dragging:
			self.translation[0] += (event.x_root - self.start[0]) * self.scale
			self.translation[1] -= (event.y_root - self.start[1]) * self.scale
			self.start[0] = event.x_root
			self.start[1] = event.y_root
		else:
			self.dragging = True
			self.start[0] = event.x_root
			self.start[1] = event.y_root

	def switch_focus(self, event, up):
		if up:
			self.active_body += 1
			self.active_body %= self.body_num
		else:
			self.active_body -= 1
			self.active_body %= self.body_num

	def add_body(self):
		self.body_num += 1

	def draw_body(self, body):
		self.t.color(body.color)
		if len(body.stored_pos) > 0:
			self.t.goto(round((body.stored_pos[0][0]*10000 + self.translation[0])/self.scale), round((body.stored_pos[0][1]*10000 + self.translation[1])/self.scale))
		self.t.pendown()
		#on_screen = [p for p in body.stored_pos if abs((p[0]+ self.translation[0])/self.scale) < 1000 and abs((p[1]+ self.translation[0])/self.scale) < 1000]
		for p in body.stored_pos:
			self.t.goto(round((p[0]*10000 + self.translation[0])/self.scale), round((p[1]*10000 + self.translation[1])/self.scale))
		self.t.penup()
		self.t.goto((body.pos[0] + self.translation[0])/self.scale, (body.pos[1] + self.translation[1])/self.scale-body.r)
		self.t.pendown()
		self.t.color(body.color)
		self.t.begin_fill()
		self.t.circle(body.r)
		self.t.end_fill()
		self.t.penup()

	def update(self, active_body, date):
		self.translation -= active_body.get_pos() - self.activeBodyLastPos
		self.activeBodyLastPos = active_body.get_pos()

		self.t.goto(-380, 360)
		self.t.color("white")
		self.t.write(f'Date: {date.strftime("%Y/%m/%d")}', font=self.style)
		self.t.goto(-380, 330)
		self.t.write(f'Scale: {round(self.scale)} km/px', font=self.style)
		self.t.goto(-380, 300)
		self.t.write(f'Body: {active_body.name}', font=self.style)

		self.sc.update()