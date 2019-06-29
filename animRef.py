from manimlib.imports import *

class circleControl(Scene):
	def construct(self):
		circle = Circle()
		circle.set_fill(PINK, opacity=0.5)

		self.add(circle)
		self.wait(5)

class circleShowCreation(Scene):
	def construct(self):
		circle = Circle()
		circle.set_fill(PINK, opacity=0.5)

		self.play(ShowCreation(circle))
		self.wait(5)

class circleShowCreation(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        square.flip(RIGHT)
        square.rotate(-3 * TAU / 8)
        circle.set_fill(PINK, opacity=0.5)

        self.play(ShowCreation(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))

class squareShowUncreateA(Scene):
    def construct(self):
        square = Square()
        square.flip(RIGHT)
        square.rotate(-3 * TAU / 8)

        self.wait()
        self.play(ShowCreation(square))
        self.wait()
        self.play(Uncreate(square))
        self.wait()

class squareShowUncreateB(Scene):
    def construct(self):
        square = Square()
        square.flip(RIGHT)
        square.rotate(-3 * TAU / 8)
        square.set_fill(BLUE, opacity=0.5)

        self.wait()
        self.play(ShowCreation(square))
        self.wait()
        self.play(Uncreate(square))
        self.wait()

class circleBorderFill(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(PINK, opacity=0.5)

        self.play(DrawBorderThenFill(circle))
        self.wait(5)       

class textWrite(Scene):
    def construct(self):
        text = TextMobject("This is some \\LaTeX")

        self.play(Write(text))
        self.wait(2)
        self.play(Uncreate(text))
        self.wait(2)       