#!/usr/bin/env python

from manimlib.imports import *

class Control(Scene):
	def construct(self):
		circle = Circle()
		circle.set_fill(PINK, opacity=0.5)

		square = Square()
		square.set_color(BLUE)
		square.set_fill("#19ffef", opacity=0.5)
		square.flip(RIGHT)
		square.rotate(-3 * TAU / 8)

		triangle = Triangle()
		triangle.scale(1.5)
		triangle.set_color(YELLOW)
		triangle.set_fill("#eaff0b", opacity=0.5)

		self.wait()
		self.play(FadeInFromDown(circle))
		self.wait()
		self.play(ReplacementTransform(circle, square))
		self.wait()
		self.play(ShrinkToCenter(square))
		self.play(SpinInFromNothing(triangle))
		self.wait()
		self.play(FadeOut(triangle))
		self.wait()