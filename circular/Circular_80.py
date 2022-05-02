from helper import *

class Circular_80( Scene ):
    def construct( self ):
        title = Text( 'Circular velocity and acceleration.' )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.play( FadeIn( title ) )
        self.wait( 1 )

        eq = AcolorsMathTex( concat( vec_v, " = ", r_prime, hat_r, r' + r \omega', hat_theta, r',\quad',
            vec_a,
            " = ", l.lr( dr_prime, r" - r \omega^2" ), hat_r, '+', l.frac('1', 'r'), prime( l.lr( r'r^2 \omega' ) ), hat_theta ) )
        eq.shift( 2 * UP )

        self.play( Write( eq ) )
        self.wait( 5 )

        eq2 = AcolorsMathTex( concat( vec_v, " = ", r" r \omega", hat_theta, r",\quad",
            vec_a,
            " = - r \omega^2", hat_r, "+ r", prime(r"\omega"), hat_theta ) )
        eq2.move_to( eq )
        self.play( TransformMatchingTex( eq, eq2 ) )
        self.wait( 5 )

        radius = 4
        axes = Axes( x_range = [0, 1, 1], y_range = [0, 1, 1], x_length = radius, y_length = radius,
                     axis_config = {"include_tip": True, "numbers_to_exclude": [0]} ).add_coordinates()

        axes.shift( DOWN + 3 * LEFT )
        origin = axes.coords_to_point( 0, 0 )
        e1dir = RIGHT
        e2dir = UP

        h_r = lambda th: e1dir * np.cos( th ) + e2dir * np.sin( th )
        h_th = lambda th: - e1dir * np.sin( th ) + e2dir * np.cos( th )

        # \theta = (t + t^2/2) pi/3
        # \omega = (1 + t) pi/3
        # \omega' = pi/3
        def theta( t ):
            return 0.5 * PI * t * (1 + t/2) * (2/3)

        def omega( t ):
            return PI * (1 + t) / 3

        def omegaprime( t ):
            return PI / 3

        om = omega
        omp = omegaprime

        t_parameter = ValueTracker(0)

        scale = 0.25
        def velocity(t):
            # logically, we are treating r = 1, but we have a scale factor for the rendering.
            th = theta( t )
            p = origin + radius * h_r( th )
            d = scale * om( t ) * h_th( th )
            return [ p, d ]

        def uv( mob ):
            t = t_parameter.get_value()
            x = velocity( t )
            mob.put_start_and_end_on( x[0], x[0] + x[1] )

        # a = -r \omega^2 \rcap + r \omega' \thetacap
        def acceleration( t ):
            th = theta( t )
            rt = h_r( th )
            tt = h_th( th )
            p = origin + radius * rt
            o = om( t )
            d = scale * (- o * o * rt + omp( t ) * tt)
            return [ p, d ]

        def ua( mob ):
            t = t_parameter.get_value()
            x = acceleration( t )
            mob.put_start_and_end_on( x[0], x[0] + x[1] )

        def uvt( mob ):
            t = t_parameter.get_value()
            x = velocity( t )
            dir = x[1]/np.linalg.norm( x[1] )
            mob.move_to( x[0] + x[1] + 0.2 * dir )

        def uat( mob ):
            t = t_parameter.get_value()
            x = acceleration( t )
            dir = x[1]/np.linalg.norm( x[1] )
            mob.move_to( x[0] + x[1] + 0.2 * dir )

        otex1 = Text( 'Non-constant angular frequency' ).scale( 0.7 )
        otex1.set_color( BLUE )
        otex2 = MathTex( r'\omega = \omega_0 + t\, \alpha' )
        otex1.shift( 2 * RIGHT + 0 * UP )
        otex2.move_to( otex1, DOWN )
        otex2.shift( 1.00 * DOWN )

        v1_i = velocity( 0 )
        a1_i = acceleration( 0 )
        v1 = Arrow( start = v1_i[0], end = v1_i[0] + v1_i[1], color = RED, stroke_width=20, max_stroke_width_to_length_ratio=10, max_tip_length_to_length_ratio=0.5, buff = 0 ).add_updater(uv).update()
        #v1 = Arrow( start = v1_i[0], end = v1_i[0] + v1_i[1], color = RED, buff = 0 ).add_updater(uv).update()
        a1 = Arrow( start = a1_i[0], end = a1_i[0] + a1_i[1], color = RED, buff = 0 ).add_updater(ua).update()
        vtex = AcolorsMathTex( vec_v ).add_updater(uvt).update()
        atex = AcolorsMathTex( vec_a ).add_updater(uat).update()

        g1 = ParametricFunction( lambda t: origin + radius * h_r( theta(t) ),
                                 t_range=[0, 1],
                                 scaling=axes.x_axis.scaling, color=YELLOW )
        self.play( AnimationGroup(
            Write( axes ), Write( g1 ), Write( v1 ), Write( a1 ), Write( vtex ), Write( atex ), Write( otex1 ), Write( otex2 ) ) )
        self.wait( 4 )

        self.play( UpdateFromAlphaFunc( t_parameter,
                                        lambda mob, alpha: mob.set_value( alpha ) ),
                                        run_time=6 )
        self.wait( 4 )

        theta = lambda t: 0.5 * PI * t
        om = lambda t: 0.5 * PI
        omp = lambda t: 0
        scale = 0.5
        t_parameter = ValueTracker(0)
        v1_i = velocity( 0 )
        a1_i = acceleration( 0 )

        otex1p = Text( 'Constant angular frequency' ).scale( 0.7 )
        otex1p.set_color( BLUE )
        otex2p = MathTex( r'\omega = \omega_0' )
        otex1p.shift( 2 * RIGHT + 0 * UP )
        otex2p.move_to( otex1, DOWN )
        otex2p.shift( 1.00 * DOWN )
        otex3 = MathTex( r'v = r \omega' )
        otex3.move_to( otex2p, DOWN )
        otex3.shift( 0.5 * DOWN )
        otex4 = MathTex( concat( r'a = -r \omega^2 = -', l.frac('v^2', 'r') ) )
        otex4.move_to( otex3, DOWN )
        otex4.shift( DOWN )

        eq3 = AcolorsMathTex( concat( vec_v, " = ", r" r \omega", hat_theta, r",\quad", vec_a, " = - r \omega^2", hat_r ) )
        eq3.move_to( eq2 )

        v1p = Arrow( start = v1_i[0], end = v1_i[0] + v1_i[1], color = RED, buff = 0 ).add_updater(uv).update()
        #v1p = Arrow( start = v1_i[0], end = v1_i[0] + v1_i[1], color = RED, stroke_width=2, max_stroke_width_to_length_ratio=4, max_tip_length_to_length_ratio=0.5, buff = 0 ).add_updater(uv).update()
        a1p = Arrow( start = a1_i[0], end = a1_i[0] + a1_i[1], color = RED, buff = 0 ).add_updater(ua).update()
        vtexp = vtex.copy().update()
        atexp = atex.copy().update()
        self.play( AnimationGroup(
            Transform( v1, v1p ),
            Transform( a1, a1p ),
            Transform( vtex, vtexp ),
            Transform( atex, atexp ),
            Transform( otex1, otex1p ),
            Transform( otex2, otex2p ),
            Write( otex3 ),
            Write( otex4 ),
            TransformMatchingTex( eq2, eq3 )
            ) )

        self.play( UpdateFromAlphaFunc( t_parameter,
                                        lambda mob, alpha: mob.set_value( alpha ) ),
                                        run_time=6 )
        self.wait( 4 )

        fadeall(self)

# vim: et sw=4 ts=4
