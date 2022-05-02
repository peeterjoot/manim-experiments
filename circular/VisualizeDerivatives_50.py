from helper import *

class VisualizeDerivatives_50( Scene ):
    def construct( self ):
        title = Text( 'Tangential vector derivative.' )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.play( FadeIn( title ) )
        #self.wait( 5 )

        radius = 4
        axes = Axes( x_range = [0, 1, 1], y_range = [0, 1, 1], x_length = radius, y_length = radius,
                     axis_config = {"include_tip": True, "numbers_to_exclude": [0]} ).add_coordinates()

        axes.shift( DOWN + 3 * LEFT )
        origin = axes.coords_to_point( 0, 0 )

        e1dir = RIGHT
        e2dir = UP
        f_r = lambda th: e1dir * np.cos( th ) + e2dir * np.sin( th )
        f_th = lambda th: - e1dir * np.sin( th ) + e2dir * np.cos( th )

        x1dir = f_r((PI/16)/(PI/2))
        x2dir = f_r((3 * PI/16)/(PI/2))
        t1dir = f_th((PI/16)/(PI/2))
        t2dir = f_th((3 * PI/16)/(PI/2))
        x1 = origin + radius * x1dir
        x2 = origin + radius * x2dir

        e1 = Arrow( start = x1, end = x1 + t1dir, color = GREEN, buff = 0 )
        e1p = Arrow( start = x2, end = x2 + t2dir, color = RED, buff = 0 )
        line = Line( start = origin, end = x1, color = BLUE, buff = 0 )
        linep = Line( start = origin, end = x2, color = BLUE, buff = 0 )
        ttex = MathTex( concat( hat_theta, r'(\theta)' ) )
        ttex.move_to( x1 + 0.45 * t1dir + 0.75 * x1dir )
        ttex.set_color( GREEN )
        ttexp = MathTex( concat( hat_theta, r'(\theta + \Delta\theta)' ) )
        ttexp.move_to( x2 + 0.25 * t2dir + 1.20 * x2dir )
        ttexp.set_color( RED )
        dtex = MathTex( r'\Delta \theta' )
        dtex.move_to( origin + ((x1 + x2)/2 - origin) * 0.7 )
        dtex.set_color( BLUE )

        g1 = ParametricFunction( lambda t: origin + radius * f_r( 0.5 * PI * t ),
                                 t_range=[0, 1],
                                 scaling=axes.x_axis.scaling, color=YELLOW )

        self.play( AnimationGroup( Write( axes ), Write( g1 ) ) )
        self.wait( 4 )
        self.play( AnimationGroup( Write( e1 ), Write( ttex ), Write( line ) ) )
        self.wait( 4 )
        self.play( AnimationGroup( Write( e1p ), Write( ttexp ), Write( linep ), Write( dtex ) ) )
        self.wait( 4 )

        self.play( FadeOut( axes, g1, line, linep, dtex ) )
        self.wait( 4 )

        all2 = VGroup( e1, e1p, ttex, ttexp )
        origin2 = origin + 2 * RIGHT + 0.5 * DOWN
        slen = 5 # scale factor length
        e1b = origin2
        e1e = origin2 + slen * t1dir
        e2b = origin2
        e2e = origin2 + slen * t2dir
        e3b = e1e
        e3e = e1e + slen * (t2dir - t1dir)
        r1  = Arrow( start = e1b, end = e1e, color = GREEN, buff = 0 )
        r1p = Arrow( start = e2b, end = e2e, color = RED, buff = 0 )
        t1  = Arrow( start = e3b, end = e3e, color = YELLOW, buff = 0 )
        sttex = ttex.copy().move_to( origin2 + t1dir * slen/2 + 0.7 * RIGHT )
        sttexp = ttexp.copy().move_to( origin2 + t2dir * slen/2 + 1.2 * LEFT + 0.5 * DOWN )
        t1tex = MathTex( concat( hat_theta, r'(\theta + \Delta \theta) - ', hat_r, r'(\theta) \approx', that_prime, r'\Delta\theta' ) )
        t1tex.move_to( origin2 + 1.2 * slen * (t1dir + t2dir)/2 + 1.0 * RIGHT + 0.5 * DOWN ) 
        t1tex.set_color( YELLOW )

        #all3 = VGroup( r1, r1p )
        all3 = VGroup( r1, r1p, sttex, sttexp )
        self.play( Transform( all2, all3 ) )
        self.wait( 4 )

        tangent = VGroup( t1, t1tex )
        self.play( AnimationGroup( Write( t1 ), Write( t1tex ) ) )

        tprime = prime(r'\theta')

        eq2 = [ AcolorsMathTex( concat( prime(hat_theta), r' = ', l.frac('d', 'dt'), vec_e1, r'e^{i\theta} i') ),
                AcolorsMathTex( concat(                    ' = ', vec_e1, r'e^{i\theta} i^2', tprime ) ),
                AcolorsMathTex( concat(                    ' = - ', hat_r, tprime ) ),
                AcolorsMathTex( concat(                   r' = - \omega', hat_r, r',\quad \omega = ', l.frac(r'd\theta', 'dt') ) ) ]

        eq2[0].shift( 1.5 * UP + 2 * RIGHT )
        self.play( Write( eq2[0] ) )
        self.wait( 5 )

        i = 0
        write_aligned( self, eq2[i], eq2[i+1], 1.15 * DOWN + 0.30 * RIGHT, None )
        self.wait( 5 )
        i = 1
        write_aligned( self, eq2[i], eq2[i+1], 0.75 * DOWN + 0.0 * LEFT, None )
        self.wait( 5 )
        i = 2
        write_aligned( self, eq2[i], eq2[i+1], 0.75 * DOWN + 0.0 * LEFT, None )
        self.wait( 5 )

        fadeall(self)

# vim: et sw=4 ts=4
