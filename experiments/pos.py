from manim import *

class pos( Scene ):
    def construct( self ):

        axes = Axes( x_range = [-1, 4, 1], y_range = [-1, 4, 1], x_length = 4, y_length = 4,
                     axis_config = {"include_tip": True, "numbers_to_exclude": [0]} ).add_coordinates()
        axes.to_edge( DOWN + LEFT )

        tline = NumberLine(
            x_range=[ 0, 4 ],
            length=4,
            color=BLUE,
            include_numbers=False,
            label_direction=DOWN,
        )
        tline.add_labels( {0: MathTex('0'), 0.25: MathTex(r'\pi/4'), 0.5: MathTex(r'\pi/2'), 0.75: MathTex(r'3\pi/4'), 1: MathTex(r'2 \pi')} )
        tline.to_edge( UP + LEFT )
        tline.shift( 2.0 * DOWN + 1.0 * RIGHT )
        ttex = MathTex( r'\theta' )
        ttex.move_to( tline, LEFT )
        ttex.shift( 0.5 * LEFT )

        g1 = ParametricFunction( lambda t: axes.coords_to_point(np.cos(t * 0.25 * PI), np.sin(t * 0.25 * PI)),
                                 t_range=[0, 1],
                                 scaling=axes.x_axis.scaling, color=YELLOW )

        t1p = ValueTracker(0)
        t1d = Dot(color=YELLOW).add_updater(
            lambda mob: mob.move_to(tline.number_to_point(1 * t1p.get_value())),
        ).update()

        self.add( VGroup( axes, g1, t1d, tline, ttex ) )
        self.play( AnimationGroup( Create(g1, run_time=6),
                                   UpdateFromAlphaFunc( t1p, 
                                                        lambda mob, alpha: mob.set_value(alpha),
                                                        run_time=6 ),
                                   ) )
        self.wait( )

# vim: et sw=4 ts=4
