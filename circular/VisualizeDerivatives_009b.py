from helper import *

class Basis_008( Scene ):
    def construct( self ):
        title = Text( 'Tangential vector derivative.' )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.add( title )
        #self.wait( 5 )

        radius = 4
        axes = Axes( x_range = [0, 1, 1], y_range = [0, 1, 1], x_length = radius, y_length = radius,
                     axis_config = {"include_tip": True, "numbers_to_exclude": [0]} ).add_coordinates()

        axes.shift( DOWN + 3 * LEFT )
        origin = axes.coords_to_point( 0, 0 )

        e1dir = RIGHT
        e2dir = UP
        r = lambda t: origin + radius * e1dir * np.cos( t * 0.5 * PI ) + radius * e2dir * np.sin( t * 0.5 * PI )
        tv = lambda t: - e1dir * np.sin( t * 0.5 * PI ) + e2dir * np.cos( t * 0.5 * PI )

        x1 = origin + radius * e1dir
        x2 = r(PI/16)
        x1dir = e1dir
        x2dir = (x2 - origin)/radius

        e1 = Arrow( start = x1, end = x1 + x1dir, color = GREEN, buff = 0 )
        e1p = Arrow( start = x2, end = x2 + x2dir, color = GREEN, buff = 0 )
        line = Line( start = origin, end = x1, color = RED, buff = 0 )
        linep = Line( start = origin, end = x2, color = RED, buff = 0 )
        rtex = AcolorsMathTex( hat_r, r'(\theta)' )
        rtex.move_to( x1 + 1.5 * x1dir )
        rtexp = AcolorsMathTex( hat_r, r'(\theta + \Delta\theta)' )
        rtexp.move_to( x2 + 1.75 * x2dir )

        g1 = ParametricFunction( r,
                                 t_range=[0, 1],
                                 scaling=axes.x_axis.scaling, color=YELLOW )

        all1 = VGroup( axes, g1, e1, e1p, rtex, rtexp, line, linep )
        self.add( all1 )
        self.wait( 1 )

        self.play( FadeOut( axes, g1, line, linep ) )
        self.wait( 4 )

        all2 = VGroup( e1, e1p, rtex, rtexp )
        origin2 = 6 * LEFT + 0.75 * UP
        slen = 5 # scale factor length
        e1b = origin2
        e1e = origin2 + slen * x1dir
        e2b = origin2
        e2e = origin2 + slen * x2dir
        e3b = e1e
        e3e = e1e + slen * (x2dir - x1dir)
        r1  = Arrow( start = e1b, end = e1e, color = GREEN, buff = 0 )
        r1p = Arrow( start = e2b, end = e2e, color = GREEN, buff = 0 )
        t1  = Arrow( start = e3b, end = e3e, color = YELLOW, buff = 0 )
        srtex = rtex.copy().move_to( origin2 + x1dir * slen/2 + 0.5 * DOWN )
        srtexp = rtexp.copy().move_to( origin2 + x2dir * slen/2 + 1.0 * LEFT + 0.5 * UP )
        t1tex = AcolorsMathTex( hat_r, r'(\theta + \Delta \theta) - ', hat_r, r'(\theta) \approx', rhat_prime, r'\Delta\theta' )
        t1tex.move_to( origin2 + 1.2 * slen * (x1dir + x2dir)/2 + 2.0 * RIGHT + 0.2 * DOWN ) 

        all3 = VGroup( r1, r1p, srtex, srtexp )
        self.play( Transform( all2, all3 ) )
        self.wait( 4 )

        tangent = VGroup( t1, t1tex )
        self.play( AnimationGroup( Write( t1 ), Write( t1tex ) ) )

#        def moveit(mob):
#            mob.shift(3 * UP + LEFT)
#            return mob
#
#        all4 = VGroup( r1, r1p, srtex, srtexp, t1, t1tex )
#        self.play( ApplyFunction( moveit, all4 ) )

        tprime = prime(r'\theta')

        eq = [ AcolorsMathTex( concat( prime(hat_r), r' = ', l.frac('d', 'dt'), vec_e1, r'e^{i\theta}') ),
               AcolorsMathTex( concat(               ' = ', vec_e1, r'e^{i\theta} i', tprime ) ),
               AcolorsMathTex( concat(               ' = ', hat_r, 'i', tprime ) ),
               AcolorsMathTex( concat(               r' = \omega', hat_theta, r',\qquad \omega = ', l.frac(r'd\theta', 'dt') ) ) ]

        eq[0].shift( 0.00 * UP + 0.00 * LEFT )
        self.play( Write( eq[0] ) )
        self.wait( 5 )

        i = 0
        write_aligned( self, eq[i], eq[i+1], 1.15 * DOWN + 0.30 * RIGHT, None )
        self.wait( 5 )
        i = 1
        write_aligned( self, eq[i], eq[i+1], 0.75 * DOWN + 0.0 * LEFT, None )
        self.wait( 5 )
        i = 2
        write_aligned( self, eq[i], eq[i+1], 0.75 * DOWN + 0.0 * LEFT, None )
        self.wait( 5 )

#
## vim: et sw=4 ts=4
