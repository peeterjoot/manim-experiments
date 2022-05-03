from helper import *

class GADecoding_30( Scene ):
    def construct( self ):

        title = Text( 'Exponential unit vector representation.' )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.play( FadeIn( title ) )
        self.wait( 5 )

        req = [ MathTex( concat( hat_r, ' = ', vec_e1, r'\cos\theta + ', vec_e2, r'\sin\theta' ) ),
                MathTex( concat(        ' = ', vec_e1, r'\cos\theta + ', vec_e1, vec_e1, vec_e2, r'\sin\theta' ) ),
                MathTex( concat(        ' = ', vec_e1, l.lr( r'\cos\theta + ', vec_e1, vec_e2, r'\sin\theta' ) ) ),
                MathTex( concat(        ' = ', vec_e1, l.lr( r'\cos\theta + i \sin\theta' ) ) ),
                MathTex( concat(        ' = ', vec_e1, r'e^{i\theta}' ) ) ]

        teq = [ MathTex( concat( hat_theta, ' = ', vec_e2, r'\cos\theta - ', vec_e1, r'\sin\theta' ) ),
                MathTex( concat(            ' = ', vec_e2, r'\cos\theta - ', vec_e2, vec_e2, vec_e1, r'\sin\theta' ) ),
                MathTex( concat(            ' = ', vec_e2, l.lr( r'\cos\theta - ', vec_e2, vec_e1, r'\sin\theta' ) ) ),
                MathTex( concat(            ' = ', vec_e2, l.lr( r'\cos\theta + ', vec_e1, vec_e2, r'\sin\theta' ) ) ),
                MathTex( concat(            ' = ', vec_e2, l.lr( r'\cos\theta + i \sin\theta' ) ) ),
                MathTex( concat(            ' = ', vec_e2, r'e^{i\theta}' ) ) ]

        teq2 = [ MathTex( concat( hat_theta, ' = ', hat_r, 'i' ) ),
                 MathTex( concat(            ' = ', vec_e1, r'e^{i\theta} i' ) ),
                 MathTex( concat(            ' = ', vec_e1, r'i e^{i\theta}' ) ),
                 MathTex( concat(            ' = ', vec_e2, r'e^{i\theta}' ) ) ]

        req[0].shift( UP )
        self.play( Write( req[0] ) )
        self.wait( 4 )
        for i in range(4):
            write_aligned( self, req[i], req[i+1], 0.75 * DOWN + 0.00 * LEFT, m = None )
            self.wait( 4 )

        req2 = MathTex( concat( hat_r, ' = ', vec_e1, r'e^{i\theta}' ) )
        req2.move_to( 5 * LEFT + 1 * UP )
        self.play( Transform( VGroup(*req), req2 ) )
        self.wait( 4 )

        teq[0].shift( UP )
        self.play( Write( teq[0] ) )
        self.wait( 5 )
        for i in range(5):
            write_aligned( self, teq[i], teq[i+1], 0.75 * DOWN + 0.00 * LEFT, m = None )
            self.wait( 4 )

        teq3 = MathTex( concat( hat_theta, ' = ', vec_e2, r'e^{i\theta}' ) )
        teq3.move_to( 5 * LEFT + 0 * UP )
        self.play( Transform( VGroup(*teq), teq3 ) )
        self.wait( 4 )

        teq2[0].shift( UP )
        self.play( Write( teq2[0] ) )
        self.wait( 5 )
        for i in range(3):
            write_aligned( self, teq2[i], teq2[i+1], 0.75 * DOWN + 0.00 * LEFT, m = None )
            self.wait( 4 )

        teq4 = MathTex( concat( ' =',  hat_r, 'i' ) )
        teq4.move_to( teq3, RIGHT )
        teq4.shift( RIGHT )
        self.play( AnimationGroup( FadeOut( *teq2 ),
                                   Write( teq4 ) ) )
        self.wait( 4 )


        radius = 4
        axes = Axes( x_range = [0, 1, 1], y_range = [0, 1, 1], x_length = radius, y_length = radius,
                     axis_config = {"include_tip": True, "numbers_to_exclude": [0]} ).add_coordinates()

        axes.shift( DOWN + 0 * LEFT )
        origin = axes.coords_to_point( 0, 0 )

        x1 = origin + radius * e1dir
        x2 = origin + radius * e2dir

        f_th = lambda t: PI/20 + t * PI/6

        def rmove(a, t):
            th = f_th(t)
            p = origin + radius * h_r(th)
            d = (p - origin)/radius
            a.put_start_and_end_on( p, p + d )

        def tmove(a, t):
            th = f_th(t)
            p = origin + radius * h_r(th)
            d = h_th(th)
            a.put_start_and_end_on( p, p + d )

        def u1(mob):
            t = t_parameter.get_value()
            rmove( mob, t )

        def u2(mob):
            t = t_parameter.get_value()
            tmove( mob, t )

        def ur(mob):
            t = t_parameter.get_value()
            th = f_th(t)
            p = origin + radius * h_r(th)
            d = 1.65 * (p - origin)/radius
            mob.move_to( p + d )

        def ut(mob):
            t = t_parameter.get_value()
            th = f_th(t)
            p = origin + radius * h_r(th)
            d2 = h_th(th)
            d1 = 0.65 * (p - origin)/radius
            mob.move_to( p + d1 + d2 )

        def ul(mob):
            t = t_parameter.get_value()
            th = f_th(t)
            p = origin + radius * h_r(th)
            mob.put_start_and_end_on( origin, p )

        def uth(mob):
            t = t_parameter.get_value()
            th = f_th(t)/2
            p = origin + (radius -1 + t * (radius/3 - radius + 1) ) * h_r(th)
            mob.move_to( p )

        t_parameter = ValueTracker(0)
        e1 = Arrow( start = origin, end = origin + e1dir, color = GREEN, buff = 0 )
        e2 = Arrow( start = origin, end = origin + e2dir, color = GREEN, buff = 0 )
        v1 = Arrow( start = x1, end = x1 + e1dir, color = GREEN, buff = 0 ).add_updater(u1).update()
        v2 = Arrow( start = x1, end = x1 + e2dir, color = GREEN, buff = 0 ).add_updater(u2).update()
        line = Line( start = origin, end = x1, color = RED, buff = 0 ).add_updater(ul).update()
        rtex = AcolorsMathTex( concat( vec_e1, r'e^{i\theta}' ) ).add_updater(ur).update()
        ttex = AcolorsMathTex( concat( vec_e2, r'e^{i\theta}' ) ).add_updater(ut).update()
        e1tex = AcolorsMathTex( vec_e1 )
        e2tex = AcolorsMathTex( vec_e2 )
        thtex = AcolorsMathTex( r'\theta' ).add_updater(uth).update()
        e1tex.move_to( origin + e1dir + 0.4 * DOWN )
        e2tex.move_to( origin + e2dir + 0.4 * LEFT )

        f_arc = lambda t: origin + radius * h_r(0.5 * PI * t)

        g1 = ParametricFunction( f_arc,
                                 t_range=[0, 1],
                                 scaling=axes.x_axis.scaling, color=YELLOW )

        self.play( FadeIn( VGroup( axes, g1, line, e1, e2, e1tex, e2tex, thtex ) ) )
        self.wait( 4 )

        self.play( AnimationGroup( Write( v1 ), Write( rtex ), Write( v2 ), Write( ttex ) ) )
        self.wait( 4 )

        self.play( UpdateFromAlphaFunc( t_parameter,
                                        lambda mob, alpha: mob.set_value( alpha ) ),
                                        run_time=6 )
        self.wait( 4 )

        fadeall( self )

# vim: et sw=4 ts=4
