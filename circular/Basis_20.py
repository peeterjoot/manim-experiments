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

        axes.shift( DOWN + 3 * LEFT )
        origin = axes.coords_to_point( 0, 0 )
        e1dir = RIGHT
        e2dir = UP

        x1 = origin + radius * e1dir
        x2 = origin + radius * e2dir

        h_r = lambda th: origin + radius * e1dir * np.cos( th ) + radius * e2dir * np.sin( th )
        h_th = lambda th: - e1dir * np.sin( th ) + e2dir * np.cos( th )

        f_th = lambda t: 0.4 * PI * t

        def rmove(a, t):
            th = f_th(t)
            p = h_r(th)
            d = (p - origin)/radius
            a.put_start_and_end_on( p, p + d )

        def tmove(a, t):
            th = f_th(t)
            p = h_r(th)
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
            p = h_r(th)
            d = 1.25 * (p - origin)/radius
            mob.move_to( p + d )

        def ut(mob):
            t = t_parameter.get_value()
            th = f_th(t)
            p = h_r(th)
            d2 = h_th(th)
            d1 = 0.35 * (p - origin)/radius
            mob.move_to( p + d1 + d2 )

        def ul(mob):
            t = t_parameter.get_value()
            th = f_th(t)
            p = h_r(th)
            mob.put_start_and_end_on( origin, p )

        t_parameter = ValueTracker(0)
        e1 = Arrow( start = x1, end = x1 + e1dir, color = GREEN, buff = 0 ).add_updater(u1).update()
        e2 = Arrow( start = x1, end = x1 + e2dir, color = GREEN, buff = 0 ).add_updater(u2).update()
        line = Line( start = origin, end = x1, color = RED, buff = 0 ).add_updater(ul).update()
        rtex = AcolorsMathTex( hat_r ).add_updater(ur).update()
        ttex = AcolorsMathTex( hat_theta ).add_updater(ut).update()

        eq = [ AcolorsMathTex( hat_r, ' = ', vec_e1, r'e^{i\theta}' ),
               AcolorsMathTex( hat_theta, ' = ', vec_e2, r'e^{i\theta} = ', hat_r, ' i' ),
               AcolorsMathTex( 'i = ', vec_e1, vec_e2 ) ]
        eq[0].move_to( 2 * RIGHT )

        f_arc = lambda t: h_r(0.5 * PI * t)

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


        self.play( Write( eq[0] ) )
        i = 0
        # Fixme: write_aligned works for aligning to ' = ', but only when it starts a line.
        write_aligned( self, eq[i], eq[i+1], 0.75 * DOWN + 0.45 * LEFT, None )
        self.wait( 4 )
        i = 1
        write_aligned( self, eq[i], eq[i+1], 0.75 * DOWN + 0.33 * LEFT, None )
        self.wait( 4 )


        fadeall(self)

# vim: et sw=4 ts=4
