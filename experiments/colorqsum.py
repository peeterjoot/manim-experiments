# https://stackoverflow.com/questions/69408013/colorize-parts-of-a-complex-equation-manim
from manim import *

class Find_Path(Scene):
    def construct(self):
        obj1 = MathTex(r"\text{minimize}", r"\quad \sum_{\text{start}}^{\text{end}}")
        obj2 = MathTex(r"d_{i,i+1}", r"\over", r"v_{i,i+1}")
        obj1.set_color_by_tex("start", GREEN)
        obj1.set_color_by_tex("end", GREEN)
        obj2.move_to(obj1, RIGHT)
        obj2.shift(1.5 * RIGHT)
        obj2[0].set_color(YELLOW)
        obj2[2].set_color(RED)
        self.play(AnimationGroup(Write(obj1), Write(obj2)))
        self.wait(3)
