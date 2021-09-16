
# https://talkingphysics.wordpress.com/2018/06/21/aligning-text-manim-series-part-6/

from manim import *
import numpy as np

class UsingBraces(Scene):
    #Using braces to group text together
    def construct(self):
        eq1A = Tex("$4x + 3y$")
        eq1B = Tex("$=$")
        eq1C = Tex("$0$")
        eq2A = Tex("$5x - 2y$")
        eq2B = Tex("$=$")
        eq2C = Tex("$3$")
        eq1B.next_to(eq1A,RIGHT)
        eq1C.next_to(eq1B,RIGHT)
        eq2A.shift(DOWN)
        eq2B.shift(DOWN)
        eq2C.shift(DOWN)
        eq2A.align_to(eq1A,LEFT)
        eq2B.align_to(eq1B,LEFT)
        eq2C.align_to(eq1C,LEFT)
         
        #eq_group=VGroup(eq1A,eq2A)
        #braces=Brace(eq_group,LEFT)
        #eq_text = braces.get_text("A pair of equations")
         
        self.add(eq1A, eq1B, eq1C)
        self.add(eq2A, eq2B, eq2C)
        #self.play(GrowFromCenter(braces),Write(eq_text))
