from helper import *

class Basis_20( Scene ):
    def construct( self ):
        title = Text( 'Circular basis vectors.' )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.play( FadeIn( title ) )
        #self.wait( 5 )

        radius = 4
        axes = Axes( x_range = [0, 1, 1], y_range = [0, 1, 1], x_length = radius, y_length = radius,
                     axis_config = {"include_tip": True, "numbers_to_exclude": [0]} ).add_coordinates()

        axes.shift( DOWN + 0 * LEFT )
        origin = axes.coords_to_point( 0, 0 )
        e1dir = RIGHT
        e2dir = UP

        x1 = origin + radius * e1dir
        x2 = origin + radius * e2dir

        h_r = lambda th: e1dir * np.cos( th ) + e2dir * np.sin( th )
        h_th = lambda th: - e1dir * np.sin( th ) + e2dir * np.cos( th )

        f_th = lambda t: (PI/6) * t

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
            d = 1.25 * (p - origin)/radius
            mob.move_to( p + d )

        def ut(mob):
            t = t_parameter.get_value()
            th = f_th(t)
            p = origin + radius * h_r(th)
            d2 = h_th(th)
            d1 = 0.35 * (p - origin)/radius
            mob.move_to( p + d1 + d2 )

        def ul(mob):
            t = t_parameter.get_value()
            th = f_th(t)
            p = origin + radius * h_r(th)
            mob.put_start_and_end_on( origin, p )

        t_parameter = ValueTracker(0)
        e1 = Arrow( start = x1, end = x1 + e1dir, color = GREEN, buff = 0 ).add_updater(u1).update()
        e2 = Arrow( start = x1, end = x1 + e2dir, color = GREEN, buff = 0 ).add_updater(u2).update()
        line = Line( start = origin, end = x1, color = RED, buff = 0 ).add_updater(ul).update()
        rtex = AcolorsMathTex( hat_r ).add_updater(ur).update()
        ttex = AcolorsMathTex( hat_theta ).add_updater(ut).update()

        f_arc = lambda t: origin + radius * h_r(0.5 * PI * t)

        g1 = ParametricFunction( f_arc,
                                 t_range=[0, 1],
                                 scaling=axes.x_axis.scaling, color=YELLOW )

        self.play( FadeIn( VGroup( axes, g1, line ) ) )
        self.wait( 4 )

        self.play( AnimationGroup( Write( e1 ), Write( rtex ) ) )
        self.wait( 4 )

        self.play( AnimationGroup( Write( e2 ), Write( ttex ) ) )
        self.wait( 4 )


        self.play( UpdateFromAlphaFunc( t_parameter,
                                        lambda mob, alpha: mob.set_value( alpha ) ),
                                        run_time=6 )
        self.wait( 4 )

        self.play( FadeOut( axes, g1, line ) )
        self.wait( 4 )

        t = t_parameter.get_value()
        th = f_th(t)
        r3 = h_r( th )
        t3 = radius * h_th( th )
        x3 = origin + radius * r3

        aR = Arrow( start = origin, end = x3, color = GREEN, buff = 0 )
        aT = Arrow( start = x3, end = x3 + t3, color = GREEN, buff = 0 )
        rtex3 = AcolorsMathTex( hat_r )
        ttex3 = AcolorsMathTex( hat_theta )

        #rtex3.move_to( x3 + 0.3 * r3 )
        #ttex3.move_to( x3 + t3 + 0.3 * t3 )
        rtex3.move_to( origin + (x3 - origin)/2 + t3/radius/3 )
        ttex3.move_to( x3 + t3/2 - h_r( th )/3 )

        self.play( AnimationGroup(
                ReplacementTransform( e1, aR ),
                ReplacementTransform( e2, aT ),
                ReplacementTransform( rtex, rtex3 ),
                ReplacementTransform( ttex, ttex3 ),
                ) )
        self.wait( 4 )

        Rcos = Arrow( start = origin, end = origin + e1dir * radius * np.cos(th), color = RED, buff = 0 )
        Rsin = Arrow( start = origin + radius * e1dir * np.cos(th), end = origin + radius * r3, color = RED, buff = 0 )
        Rth = MathTex( r'\theta' )
        Rcost = MathTex( concat( vec_e1, r'\cos\theta' ) )
        Rsint = MathTex( concat( vec_e2, r'\sin\theta' ) )
        Rth.move_to( origin + 1.5 * (e1dir + r3)/2 )
        Rcost.move_to( origin + 1.7 * e1dir - e2dir/2 )
        Rsint.move_to( origin + radius * e1dir * np.cos(th) + 1.0 * e1dir + e2dir )
        Rcost.set_color( RED )
        Rsint.set_color( RED )
        Rhattex = MathTex( concat( hat_r, ' = ', vec_e1, r'\cos\theta + ', vec_e2, r'\sin\theta' ) )
        Rhattex.move_to( 4 * LEFT + 2 * DOWN )

        self.play( AnimationGroup( Write( Rcos ),
                                   Write( Rsin ),
                                   Write( Rth ),
                                   Write( Rcost ),
                                   Write( Rsint ) ) )
        self.wait( 4 )

        Rhattex.set_color( RED )
        self.play( Write( Rhattex ) )
        self.wait( 4 )

        x4 = origin + radius * r3 + radius * e2dir * np.cos(th)
        Tcos = Arrow( start = origin + radius * r3,
                      end = x4,
                      color = BLUE, buff = 0 )
        Tsin = Arrow( start = x4,
                      end = x4 - e1dir * radius * np.sin(th),
                      color = BLUE, buff = 0 )
        Tth = MathTex( r'\theta' )
        Tcost = MathTex( concat( vec_e2, r'\cos\theta' ) )
        Tcost.move_to( x3 + radius * e2dir/2 + e1dir )
        Tcost.set_color( BLUE )

        Tsint = MathTex( concat( '-', vec_e1, r'\sin\theta' ) )
        Tsint.move_to( x3 + radius * e2dir - 1.00 * e1dir )
        Tsint.set_color( BLUE )
        Thattex = MathTex( concat( hat_theta, ' = -', vec_e1, r'\sin\theta + ', vec_e2, r'\cos\theta' ) )
        Thattex.move_to( 4 * LEFT + 2 * UP )

        Tth.move_to( x3 + 1.5 * (e2dir * np.cos(th) + t3/radius)/2 )
        self.play( AnimationGroup( FadeOut( title ),
                                   Write( Tcos ),
                                   Write( Tsin ),
                                   Write( Tth ),
                                   Write( Tsint ),
                                   Write( Tcost ) ) )
        self.wait( 4 )
        Thattex.set_color( BLUE )
        self.play( Write( Thattex ) )
        self.wait( 4 )

        #eq = [ AcolorsMathTex( hat_r, ' = ', vec_e1, r'e^{i\theta}' ),
        #       AcolorsMathTex( hat_theta, ' = ', vec_e2, r'e^{i\theta} = ', hat_r, ' i' ),
        #       AcolorsMathTex( 'i = ', vec_e1, vec_e2 ) ]
        #eq[0].move_to( 2 * RIGHT )
        #self.play( Write( eq[0] ) )
        #i = 0
        ## Fixme: write_aligned works for aligning to ' = ', but only when it starts a line.
        #write_aligned( self, eq[i], eq[i+1], 0.75 * DOWN + 0.45 * LEFT, None )
        #self.wait( 4 )
        #i = 1
        #write_aligned( self, eq[i], eq[i+1], 0.75 * DOWN + 0.33 * LEFT, None )
        #self.wait( 4 )


        fadeall(self)

# vim: et sw=4 ts=4
