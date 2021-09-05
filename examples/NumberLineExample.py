from manim import *

class NumberLineExample(Scene):
    def construct(self):
        #dot = Dot(ORIGIN)
        ##arrow = Point(ORIGIN, [2, 2, 0], buff=0)
        #numberline = NumberLine()
        #origin_text = Text('0').next_to(dot, DOWN)
        ##tip_text = Text('2').next_to(arrow.get_end(), RIGHT)
        ##self.add(numberplane, dot, arrow, origin_text, tip_text)
        #self.add(numberline, dot, origin_text)

        l0 = NumberLine(
            x_range=[-10, 10, 2],
            length=10,
            color=BLUE,
            include_numbers=True,
            label_direction=UP,
        )

        line_group = VGroup(l0).arrange(DOWN, buff=1)
        self.add(line_group)
