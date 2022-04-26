from manim import *
import numpy as np
import math

class basis( Scene ):
    def construct( self ):

        axes = Axes( x_range = [0, 1, 1], y_range = [0, 1, 1], x_length = 4, y_length = 4,
                     axis_config = {"include_tip": True, "numbers_to_exclude": [0]} ).add_coordinates()

        pc = lambda t: axes.coords_to_point( np.cos( t * 0.5 * PI ), np.sin( t * 0.5 * PI ) )
        xone = pc(0)
        t_parameter = ValueTracker(0)

        #l.put_start_and_end_on(d[1].get_center(), d[2].get_center())

        def u(mob):
            v = t_parameter.get_value()
            p = pc( t_parameter.get_value() )
            mob.put_start_and_end_on( p, (5/4) * p )

        e1 = Arrow( start = xone, end = xone + RIGHT, color = GREEN, buff = 0 ).add_updater( u ).update()
        #lambda mob: mob.put_start_and_end_on( pc( t_parameter.get_value() ), 1.25 * pc( t_parameter.get_value() ) )
        #e2 = Arrow( start = xone, end = xone + UP, color = GREEN, buff = 0 ).add_updater(
        #    lambda mob: mob.move_to( pc( t_parameter.get_value() ) )
        #).update()
        g1 = ParametricFunction( pc,
                                 t_range=[0, 1],
                                 scaling=axes.x_axis.scaling, color=YELLOW )

        #self.add( VGroup( axes, g1, e1, e2 ) )
        self.add( VGroup( axes, g1, e1 ) )
        self.wait( 1 )
        #self.play( UpdateFromAlphaFunc( t_parameter, 
        #                                lambda mob, alpha: mob.set_value( alpha ) ),
        #                                run_time=6 )
        #x = e1.copy()
        e1.set_value( 0.5 )
        u(e1)
        self.wait( 1 )
