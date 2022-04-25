from manim import *

# https://gist.github.com/Adirockzz95/06649145d7e6c4c147c02459fd2bc5af
class MoveVector(Scene):
    def construct(self):
        #vector = Vector(direction=RIGHT)
        #end_point = (4,0,0)
        #animation = ApplyMethod(vector.shift,end_point)
        #self.play(animation)

        def rf(t: float) -> float:
            #return 1 - np.cos((t * np.pi) / 2)
            return 1 - np.cos((t * np.pi) / 2)

        d1 = Dot().set_color(ORANGE)
        l1 = Line(LEFT, RIGHT)
        l2 = VMobject()
        self.add(d1, l1, l2)
        l2.add_updater( lambda x: x.become(Line(LEFT, d1.get_center()).set_color(ORANGE)) )
        #self.play( MoveAlongPath(d1, l1), rate_func=lambda t: rf(1 - t) )
        self.play( MoveAlongPath(d1, l1), rate_func=rf )
