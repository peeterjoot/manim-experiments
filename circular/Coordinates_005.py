from helper import *

class Coordinates_005( Scene ):
    def construct( self ):

        title = Text( 'Circular coordinates.' )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.play( FadeIn( title ) )
        self.wait( 5 )

        axes = Axes( x_range = [-1, 4, 1], y_range = [-1, 4, 1], x_length = 4, y_length = 4,
                     axis_config = {"include_tip": True, "numbers_to_exclude": [0]} ).add_coordinates()
        axes.to_edge( LEFT )
        axes.shift( RIGHT + DOWN )

        rline = NumberLine(
            x_range=[0, 4, 1],
            length=4,
            color=BLUE,
            include_numbers=True,
            label_direction=DOWN,
        )
        rline.to_edge( RIGHT )
        rline.shift( 1.0 * LEFT )
        rtex = MathTex( 'r' )
        rtex.move_to( rline, LEFT )
        rtex.shift( 0.5 * LEFT )

        tline = NumberLine(
            x_range=[ 0, 4 ],
            length=4,
            color=BLUE,
            include_numbers=False,
            label_direction=DOWN,
        )
        tline.add_labels( {
            0: MathTex('0'),
            1: MathTex(r'\pi/4'),
            2: MathTex(r'\pi/2'),
            3: MathTex(r'3\pi/4'),
            4: MathTex(r'\pi/2')
            } )
        tline.move_to( rline, DOWN )
        tline.shift( 1.0 * DOWN )
        ttex = MathTex( r'\theta' )
        ttex.move_to( tline, LEFT )
        ttex.shift( 0.5 * LEFT )

        g1 = ParametricFunction( lambda t: axes.coords_to_point(np.cos(t * 0.25 * PI), np.sin(t * 0.25 * PI)),
                                 t_range=[0, 1],
                                 scaling=axes.x_axis.scaling, color=YELLOW )

        r1p = ValueTracker(0)
        r1u = lambda mob: mob.move_to(rline.number_to_point(1 + r1p.get_value()))
        r1d = Dot(color=RED).add_updater(r1u).update()

        t1p = ValueTracker(0)
        t1u = lambda mob: mob.move_to(tline.number_to_point(2 * t1p.get_value()))
        t1d = Dot(color=YELLOW).add_updater(t1u).update()

        self.play( DrawBorderThenFill( VGroup( axes, r1d, rline, rtex, t1d, tline, ttex ) ), run_time = 2 )
        self.wait( )

        self.play( AnimationGroup( Create( g1, run_time=6 ),
                                   UpdateFromAlphaFunc( t1p, 
                                                        lambda mob, alpha: mob.set_value(alpha),
                                                        run_time=6 ),
                                   ) )
        self.wait( 4 )

        p = np.array( [ np.cos( 0.25 * PI ), np.sin( 0.25 * PI ) ] )
        g2 = ParametricFunction( lambda t: axes.coords_to_point( (t+1) * p[0], (t+1) * p[1] ),
                                 t_range=[0, 1],
                                 scaling=axes.x_axis.scaling, color=RED )

        self.play( AnimationGroup( Create( g2, run_time=6 ),
                                   UpdateFromAlphaFunc( r1p, 
                                                        lambda mob, alpha: mob.set_value(alpha),
                                                        run_time=6 ),
                                   ) )
        self.wait( 4 )

        def radius(x, y):
            r = np.sqrt( x*x + y*y )
            return r

        def angle(x, y):
            a = np.arctan2( y, x )
            return a

        p2 = 2 * p
        f = lambda t: axes.coords_to_point( p2[0] + np.sin(10 * t), p2[1] + 1.0 * (np.exp(t)-1) )
        g3 = ParametricFunction( f,
                                 t_range=[0, 1],
                                 scaling=axes.x_axis.scaling, color=GREEN )

        # PI/4 => 2
        # PI   => 8
        # 2 PI => 16
        t3a = lambda t: (8 / math.pi) * angle( p2[0] + np.sin(10 * t), p2[1] + 1.0 * ( np.exp(t)-1 ) )
        t3r = lambda t: radius( p2[0] + np.sin(10 * t), p2[1] + 1.0 * ( np.exp(t)-1 ) )
        t3u = lambda mob: mob.move_to(tline.number_to_point(t3a(t1p.get_value())))
        r3u = lambda mob: mob.move_to(rline.number_to_point(t3r(r1p.get_value())))
        t1d.remove_updater(t1u)
        r1d.remove_updater(r1u)
        t1d.add_updater(t3u).update()
        r1d.add_updater(r3u).update()


        self.play( AnimationGroup( Create( g3, run_time=6 ),
                                   UpdateFromAlphaFunc( r1p, 
                                                        lambda mob, alpha: mob.set_value(alpha),
                                                        run_time=6 ),
                                   UpdateFromAlphaFunc( t1p, 
                                                        lambda mob, alpha: mob.set_value(alpha),
                                                        run_time=6 ),
                                   ) )
        self.wait( 4 )

        fadeall(self)

# vim: et sw=4 ts=4
