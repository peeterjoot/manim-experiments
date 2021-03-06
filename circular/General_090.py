# for Callable:
#from __future__ import annotations
#import typing

from helper import *

class General_090( Scene ):
    def construct( self ):
        title = Text( 'Velocity and acceleration.' )
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

        radius = 4
        axes = Axes( x_range = [-1, 1, 1], y_range = [0, 1, 1], x_length = 2 * radius, y_length = radius,
                     axis_config = {"include_tip": True, "numbers_to_exclude": [-1, 0, 1]} ).add_coordinates()

        axes.shift( DOWN + 0 * LEFT )
        origin = axes.coords_to_point( 0, 0 )

        fr = PI
        f_theta = lambda t: 0.5 * PI * ( t + t * np.sin( fr * t ) )
        f_omega = lambda t: 0.5 * PI * ( 1 + np.sin( fr * t ) + fr * t * np.cos( fr * t ) )
        f_omegap = lambda t: 0.5 * PI * ( 2 * fr * np.cos( fr * t ) - t * fr * fr * np.sin( fr * t ) )
        f_r = lambda t: (2.5 * t + 4 + t * t/2)/2
        f_rp = lambda t: (2.5 + 1 * t)/2
        f_rpp = lambda t: 1/2
        #f_r = lambda t: 2.0 * (2 + ((t-1)**2) * np.cos(8 * t)  ) - 2
        #f_rp = lambda t: 2.0 * (2 * (t-1) * np.cos(8 * t) - 8 * ((t-1)**2) * np.sin( 8 * t ) )
        #f_rpp = lambda t: 2.0 * (2 * np.cos(8 * t) - 16 * (t-1) * np.sin( 8 * t ) - 16 * (t-1) * np.sin( 8 * t ) - 64 * ((t-1)**2) * np.cos( 8 * t ) )

        t_parameter = ValueTracker(0)

        def position(t):
            r = f_r( t )
            th = f_theta( t )
            rh = h_r( th )
            p = r * rh
            return p

        # v = r' \hat{\Br} + r \omega \hat{\Btheta}
        def velocity(t):
            r = f_r( t )
            th = f_theta( t )
            rh = h_r( th )
            thh = h_th( th )
            p = origin + r * rh
            d = f_rp( t ) * rh + f_r( t ) * f_omega( t ) * thh
            return [ p, d/4 ]

        # a = (r'' -r \omega^2) \rcap + (2 r' \omega + r \omega' ) \thetacap
        def acceleration( t ):
            r = f_r( t )
            th = f_theta( t )
            rh = h_r( th )
            thh = h_th( th )
            om = f_omega( t )
            p = origin + r * rh
            d = (f_rpp( t ) - r * om * om ) * rh + ( 2 * f_rp(t) * om + r * f_omegap(t) ) * thh
            return [ p, d/16 ]

        def ud( mob ):
            t = t_parameter.get_value()
            x = velocity( t )
            mob.move_to( x[0] )

        def uv( mob ):
            t = t_parameter.get_value()
            x = velocity( t )
            mob.put_start_and_end_on( x[0], x[0] + x[1] )

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

        s2 = 0.75
        def ur1( mob ):
            t = t_parameter.get_value()
            th = f_theta( t )
            s = origin + s2 * h_r( th )
            e = origin + 2 * s2 * h_r( th )
            mob.put_start_and_end_on( s, e )

        def ut1( mob ):
            t = t_parameter.get_value()
            th = f_theta( t )
            s = origin + s2 * h_r( th )
            e = s + s2 * h_th( th )
            mob.put_start_and_end_on( s, e )

        uhr = lambda mob: mob.move_to( origin + 2.2 * s2 * h_r( f_theta( t_parameter.get_value() ) ) )

        def uht( mob ):
            th = f_theta( t_parameter.get_value() )
            e = origin + s2 * h_r( th ) + 1.2 * s2 * h_th( th )
            mob.move_to( e )

        v1_i = velocity( 0 )
        a1_i = acceleration( 0 )
        d1 = Dot( v1_i[0], color = GREEN ).add_updater(ud).update()
        v1 = Arrow( start = v1_i[0], end = v1_i[0] + v1_i[1], color = RED, buff = 0 ).add_updater(uv).update()
        a1 = Arrow( start = a1_i[0], end = a1_i[0] + a1_i[1], color = BLUE, buff = 0 ).add_updater(ua).update()
        r1 = Arrow( start = origin + h_r( f_theta( 0 ) ), end = origin + 2 * h_r( f_theta( 0 ) ), color = RED, buff = 0 ).add_updater(ur1).update()
        t1 = Arrow( start = origin + h_r( f_theta( 0 ) ), end = origin + h_th( f_theta( 0 ) ), color = RED, buff = 0 ).add_updater(ut1).update()
        vtex = AcolorsMathTex( vec_v ).add_updater(uvt).update()
        atex = AcolorsMathTex( vec_a ).add_updater(uat).update()
        rtex = AcolorsMathTex( hat_r ).add_updater(uhr).update()
        thtex = AcolorsMathTex( hat_theta ).add_updater(uht).update()

        g1 = ParametricFunction( lambda t: origin + position( t ),
                                 t_range=[0, 1],
                                 scaling=axes.x_axis.scaling, color=YELLOW )

        g2 = ParametricFunction( lambda t: origin + s2 * h_r( f_theta( t ) ),
                                 t_range=[0, 1],
                                 scaling=axes.x_axis.scaling, color=YELLOW )
        self.play( AnimationGroup( Write( axes ),
                                   Write( g1 ),
                                   Write( v1 ),
                                   Write( a1 ),
                                   Write( vtex ),
                                   Write( atex ),
                                   Write( g2 ),
                                   Write( r1 ),
                                   Write( t1 ),
                                   Write( rtex ),
                                   Write( thtex ),
                                   Write( d1 ) ) )
        self.wait( 4 )

        self.play( UpdateFromAlphaFunc( t_parameter,
                                        lambda mob, alpha: mob.set_value( alpha ) ),
                                        run_time=6 )
        self.wait( 4 )

        fadeall( self )

# vim: et sw=4 ts=4
