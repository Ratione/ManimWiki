from manimlib.imports import *

class PlaceHolder(Scene):
    def construct(self):
        placeholderText = TextMobject("This is a Placeholder")

        self.play(Write(placeholderText))
        self.wait(2)
        self.play(FadeOut(placeholderText))
