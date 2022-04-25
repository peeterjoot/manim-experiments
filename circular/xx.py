from manim import *
import numpy as np
import math

class line( Scene ):
    def construct( self ):

        tline = NumberLine(
            x_range=[ 0, 1 ],
            length=4,
            color=BLUE,
            include_numbers=False )

        t1 = ParametricFunction( lambda t: tline.number_to_point(np.sin(t * PI)),
                                 t_range=[0, 1],
                                 scaling=tline.scaling, color=YELLOW )

        self.play( DrawBorderThenFill( VGroup( tline ) ), run_time = 2 )
        #trace = TracedPath(t1.get_start)
        #dot = Dot(color=RED).move_to(t1.get_start())
        dot = Dot(color=RED).move_to(tline.get_start())
        #dot.add_updater(lambda m: m.shift( RIGHT/10 ))
        #self.play( AnimationGroup(Create(t1)), run_time = 6 )
        self.add( dot )
        #self.add( trace, dot, t1 )
        self.play( dot.animate.shift(4 * RIGHT), run_time=6, rate_func=linear )


        #self.add(trace, dot)
        #self.play(dot.animate.shift(8*RIGHT), run_time=4, rate_func=linear)


# vim: et sw=4 ts=4
