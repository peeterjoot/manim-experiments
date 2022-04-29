# for Callable:
from __future__ import annotations
import typing

from helper import *

class Circular_015( Scene ):
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

        rv = lambda t: e1dir * np.cos( t * 0.5 * PI ) + e2dir * np.sin( t * 0.5 * PI )
        tv = lambda t: - e1dir * np.sin( t * 0.5 * PI ) + e2dir * np.cos( t * 0.5 * PI )

        def omega( t ):
            #return 2 * PI * (t/4)^2
            return 2 * PI * (t+1)/4
            #return 1

        def omegaprime( t ):
            #return 4 * PI * (t/4)
            return PI/4
            #return 0

        om = omega
        omp = omegaprime

        t_parameter = ValueTracker(0)

        scale = 0.25
        # v = r \omega \thetacap
        def velocity(t, omegaf: Callable[[float], float]):
            # logically, we are treating r = 1, but we have a scale factor for the rendering.
            p = origin + radius * rv( t )
            d = scale * omegaf( t ) * tv( t )
            return [p, d]

        def uv( mob ):
            t = t_parameter.get_value()
            x = velocity( t, om )
            mob.put_start_and_end_on( x[0], x[0] + x[1] )

        # a = -r \omega^2 \rcap + r \omega' \thetacap
        def acceleration( t, omegaf: Callable[[float], float], omegapf: Callable[[float], float] ):
            rt = rv( t )
            tt = tv( t )
            p = origin + radius * rt
            o = omegaf( t )
            d = scale * (- o * o * rt + omegapf( t ) * tt)
            return [p, d]

        def ua( mob ):
            t = t_parameter.get_value()
            x = acceleration( t, om, omp )
            mob.put_start_and_end_on( x[0], x[0] + x[1] )

        v1_i = velocity( 0, om )
        a1_i = acceleration( 0, om, omp )
        v1 = Arrow( start = v1_i[0], end = v1_i[0] + v1_i[1], color = RED, stroke_width=20, max_stroke_width_to_length_ratio=10, max_tip_length_to_length_ratio=0.5, buff = 0 ).add_updater(uv).update()
        a1 = Arrow( start = a1_i[0], end = a1_i[0] + a1_i[1], color = RED, buff = 0 ).add_updater(ua).update()
        #vtex = AcolorsMathTex( vec_v ).add_updater(uvt).update()
        #atex = AcolorsMathTex( vec_a ).add_updater(uat).update()

        g1 = ParametricFunction( lambda t: origin + radius * rv( t ),
                                 t_range=[0, 1],
                                 scaling=axes.x_axis.scaling, color=YELLOW )
        #self.add( VGroup( axes, g1, e1, e2, rtex, ttex, line ) )
        self.play( AnimationGroup( Write( axes ), Write( g1 ), Write( v1 ), Write( a1 ) ) )
        self.wait( 4 )

        self.play( UpdateFromAlphaFunc( t_parameter,
                                        lambda mob, alpha: mob.set_value( alpha ) ),
                                        run_time=6 )
        self.wait( 4 )

        om = lambda t: 1
        omp = lambda t: 0
        scale = 1
        t_parameter = ValueTracker(0)
        v1_i = velocity( 0, om )
        a1_i = acceleration( 0, om, omp )

        eq3 = AcolorsMathTex( concat( vec_v, " = ", r" r \omega", hat_theta, r",\quad", vec_a, " = - r \omega^2", hat_r ) )
        eq3.move_to( eq2 )

        v1p = Arrow( start = v1_i[0], end = v1_i[0] + v1_i[1], color = RED, buff = 0 ).add_updater(uv).update()
        a1p = Arrow( start = a1_i[0], end = a1_i[0] + a1_i[1], color = RED, buff = 0 ).add_updater(ua).update()
        self.play( AnimationGroup( 
            Transform( v1, v1p ),
            Transform( a1, a1p ),
            TransformMatchingTex( eq2, eq3 )
            ) )

        self.play( UpdateFromAlphaFunc( t_parameter,
                                        lambda mob, alpha: mob.set_value( alpha ) ),
                                        run_time=6 )
        self.wait( 4 )


# vim: et sw=4 ts=4
