from helper import *

class Position_010( Scene ):
    def construct( self ):

        #title = Text( 'Circular velocity and acceleration.' )
        title = Text( 'Circular coordinates.' )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.add( title )
        self.wait( 5 )

        if 0:
            eq = [ AcolorsMathTex( concat( vec_x, ' = x_r ', hat_r, r' + x_\theta', hat_theta ) ),
                   AcolorsMathTex( concat( hat_r, ' = ', vec_e1, r'e^{i\theta}' ) ),
                   AcolorsMathTex( concat( hat_theta, ' = ', vec_e2, r'e^{i\theta}' ) ),
                   AcolorsMathTex( concat( 'i = ', vec_e1, vec_e2 ) ),
                   AcolorsMathTex( concat( vec_e1, vec_e1, ' = ', vec_e2, vec_e2, '= 1' ) ),
                   AcolorsMathTex( concat( vec_e1, vec_e2, ' = -', vec_e2, vec_e1 ) ) ]

            eq[0].shift( 1.5 * UP )
            self.play( Write( eq[0] ) )
            self.wait( 5 )

            i = 0
            write_aligned( self, eq[i], eq[i+1], 0.75 * DOWN + 0.40 * LEFT, None )
            self.wait( 5 )
            i = 1
            write_aligned( self, eq[i], eq[i+1], 0.75 * DOWN + 0.40 * LEFT, None )
            self.wait( 5 )
            i = 2
            write_aligned( self, eq[i], eq[i+1], 0.75 * DOWN + 0.35 * LEFT, None )
            self.wait( 5 )
            i = 3
            write_aligned( self, eq[i], eq[i+1], 0.75 * DOWN + 0.80 * LEFT, None )
            self.wait( 5 )
            i = 4
            write_aligned( self, eq[i], eq[i+1], 0.75 * DOWN + 0.00 * LEFT, None )
            self.wait( 5 )



        axes = Axes( x_range = [-1, 4, 1], y_range = [-1, 4, 1], x_length = 4, y_length = 4,
                     axis_config = {"include_tip": True, "numbers_to_exclude": [0]} ).add_coordinates()
        axes.to_edge( DOWN + LEFT )

        function = lambda theta: 2 * np.sin(theta * 5)

        rline = NumberLine(
            x_range=[0, 4, 1],
            length=4,
            color=BLUE,
            include_numbers=True,
            label_direction=DOWN,
        )
        rline.shift( 4 * LEFT + 2 * UP )
        rtex = MathTex( 'r' )
        rtex.move_to( rline, LEFT )
        rtex.shift( 0.5 * LEFT )

        tline = NumberLine(
            x_range=[ 0, 0.5 * PI, 0.25 * PI ],
            length=4,
            color=BLUE,
            include_numbers=False,
            label_direction=DOWN,
        )
        #tline.add_labels( {0: MathTex('0'), 0.5: MathTex(r'\pi/4'), 1: MathTex(r'\pi/2')} )
        tline.move_to( rline, DOWN )
        tline.shift( 0.5 * DOWN )
        ttex = MathTex( r'\theta' )
        ttex.move_to( tline, LEFT )
        ttex.shift( 0.5 * LEFT )

        g1 = ParametricFunction( lambda t: axes.coords_to_point(np.cos(t * 0.25 * PI), np.sin(t * 0.25 * PI)),
                                 t_range=[0, 1],
                                 scaling=axes.x_axis.scaling, color=YELLOW )

        r1 = ParametricFunction( lambda t: rline.number_to_point(1),
                                 t_range=[0, 1],
                                 scaling=rline.scaling, color=RED )

        t1 = ParametricFunction( lambda t: tline.number_to_point(t * 0.25 * PI),
                                 t_range=[0, 1],
                                 scaling=tline.scaling, color=YELLOW )



        p = np.array( [ np.cos( 0.25 * PI ), np.sin( 0.25 * PI ) ] )
        g2 = ParametricFunction( lambda t: axes.coords_to_point( (t+1) * p[0], (t+1) * p[1] ),
                                 t_range=[0, 1],
                                 scaling=axes.x_axis.scaling, color=RED )

        r2 = ParametricFunction( lambda t: rline.number_to_point(1 + t),
                                 t_range=[0, 1],
                                 scaling=rline.scaling, color=RED )

        t2 = ParametricFunction( lambda t: tline.number_to_point(0.25 * PI),
                                 t_range=[0, 1],
                                 scaling=tline.scaling, color=YELLOW )

        def radius(x, y):
            r = np.sqrt( x*x + y*y )
            return r

        def angle(x, y):
            a = np.arctan2( x, y )
            return a


        p2 = 2 * p
        f = lambda t: axes.coords_to_point( p2[0] + np.sin(10 * t), p2[1] + 1.0 * (np.exp(t)-1) )
        g3 = ParametricFunction( f,
                                 t_range=[0, 1],
                                 scaling=axes.x_axis.scaling, color=GREEN )

        r3 = ParametricFunction( lambda t: rline.number_to_point( radius( p2[0] + np.sin(10 * t), p2[1] + 1.0 * ( np.exp(t)-1 ) ) ),
                                 t_range=[0, 1],
                                 scaling=rline.scaling, color=RED )

        t3 = ParametricFunction( lambda t: tline.number_to_point( angle(p2[0] + np.sin(10 * t), p2[1] + 1.0 * ( np.exp(t)-1 ) ) ),
                                 t_range=[0, 1],
                                 scaling=tline.scaling, color=YELLOW )



        self.play( DrawBorderThenFill( VGroup( axes, rline, rtex, tline, ttex ) ), run_time = 2 )
        self.wait( )

        self.play( AnimationGroup(Create(t1), Create(r1), Create(g1)), run_time = 6 )
        self.wait( )
        self.play( AnimationGroup(Create(t2), Create(r2), Create(g2)), run_time = 6 )
        self.wait( )
        self.play( AnimationGroup(Create(g3), Create(r3), Create(t3)), run_time = 6 )
        self.wait( )


        if 0:

            graphs = VGroup( g1, g2, g3 )

            #r = lambda u: np.array([ np.cos(u), np.sin(u), 0 ])
            #graph = ParametricFunction( r, color=RED, t_range=[0, 0.5 * PI] )
            #graph.underlying_function = r

            #graphing_stuff = VGroup( axes, g1, g2 )
            #graphing_stuff += axis_labels

            #self.play(DrawBorderThenFill(axes), Write(axis_labels), run_time = 2)
            self.wait()
            self.play(Create(graphs), run_time = 6)
            self.wait()

# vim: et sw=4 ts=4
