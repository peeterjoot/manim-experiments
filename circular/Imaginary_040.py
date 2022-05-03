from helper import *

class Imaginary_040( Scene ):
    def construct( self ):

        title = Text( '2D Geometric algebra: the imaginary.' )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.play( FadeIn( title ) )
        self.wait( 5 )

        eq = [ MathTex( concat( l.sq(vec_e1), ' = ', l.sq( vec_e2 ), ' = 1' ) ),
               MathTex( concat( vec_e2, vec_e1, ' = -', vec_e1, vec_e2 ) ),
               MathTex( concat( l.text('Let'), r'\quad i = ', vec_e1, vec_e2 ) ) ]
        eq[0].shift( 2 * UP )

        self.play( Write( eq[0] ) )
        self.wait( 5 )
        for i in range(2):
            write_aligned( self, eq[i], eq[i+1], 0.75 * DOWN + 0.0 * LEFT, None )
            self.wait( 3 )

        eq2 = [ MathTex( concat( vec_e1, 'i = ', vec_e1, l.lr( vec_e1, vec_e2 ) ) ),
                MathTex( concat(           '= ', l.lr( vec_e1, vec_e1 ), vec_e2 ) ),
                MathTex( concat(           '= ', vec_e2 ) ) ]

        eq3 = [ MathTex( concat( vec_e2, 'i = ', vec_e2, l.lr( vec_e1, vec_e2 ) ) ),
                MathTex( concat(           '= ', l.lr( vec_e2, vec_e1 ), vec_e2 ) ),
                MathTex( concat(           '= ', l.lr( '-', vec_e1, vec_e2 ), vec_e2 ) ),
                MathTex( concat(           '= -', vec_e1, l.lr( vec_e2, vec_e2 ) ) ),
                MathTex( concat(           '= -', vec_e1 ) ) ]

        eq4 = [ MathTex( concat( 'i^2 = ', l.lr( vec_e1, vec_e2 ), l.lr( vec_e1, vec_e2 ) ) ),
                MathTex( concat(     '= ', vec_e1, l.lr( vec_e2, vec_e1 ), vec_e2 ) ),
                MathTex( concat(     '= ', vec_e1, l.lr( '-', vec_e1, vec_e2 ), vec_e2 ) ),
                MathTex( concat(     '= -', l.sq( vec_e1 ), l.sq( vec_e2 ) ) ),
                MathTex( concat(           '= -1' ) ) ]

        g = VGroup( *eq )
        eq2[0].move_to( eq[0] )
        eq3[0].move_to( eq[0] )
        eq4[0].move_to( eq[0] )
        eq2[0].shift( 2 * RIGHT )
        eq3[0].shift( 2 * RIGHT )
        eq4[0].shift( 2 * RIGHT )
        self.play( g.animate.shift(4.5 * LEFT + 0 * DOWN), run_time=1, rate_func=linear )
        self.wait( 3 )

        self.play( Write( eq4[0] ) )
        self.wait( 3 )
        for i in range(4):
            write_aligned( self, eq4[i], eq4[i+1], 0.75 * DOWN + 0.0 * LEFT, m = None )
            self.wait( 3 )

        eq4a = MathTex( 'i^2 = -1' )
        align_it( self, eq[2], eq4a, 0.75 * DOWN + 0.0 * LEFT, m = None, what = '=' )
        self.play( AnimationGroup( FadeOut( *eq4 ), Write( eq4a ) ) )
        self.wait( 3 )

        self.play( Write( eq2[0] ) )
        self.wait( 3 )
        for i in range(2):
            write_aligned( self, eq2[i], eq2[i+1], 0.75 * DOWN + 0.0 * LEFT, m = None )
            self.wait( 3 )

        eq2a = MathTex( concat( vec_e1, ' i = ', vec_e2 ) )
        align_it( self, eq4a, eq2a, 0.75 * DOWN + 0.0 * LEFT, m = None, what = '=' )
        self.play( AnimationGroup( FadeOut( *eq2 ), Write( eq2a ) ) )
        self.wait( 3 )

        self.play( Write( eq3[0] ) )
        self.wait( 3 )
        for i in range(4):
            write_aligned( self, eq3[i], eq3[i+1], 0.75 * DOWN + 0.0 * LEFT, m = None )
            self.wait( 3 )

        eq3a = MathTex( concat( vec_e2, ' i = -', vec_e1 ) )
        align_it( self, eq2a, eq3a, 0.75 * DOWN + 0.0 * LEFT, m = None, what = '=' )
        self.play( AnimationGroup( FadeOut( *eq3 ), Write( eq3a ) ) )
        self.wait( 3 )

        # axes, vector and rotated vector, with labels.  Animate the rotation.

        radius = 4
        axes = Axes( x_range = [-0.5, 1, 1], y_range = [0, 1, 1], x_length = 1.5 * radius, y_length = radius,
                     axis_config = {"include_tip": True, "numbers_to_exclude": [-1, 0, 1]} ).add_coordinates()

        axes.shift( DOWN + 2 * RIGHT )
        origin = axes.coords_to_point( 0, 0 )
        self.play( FadeIn( axes ) )
        self.wait( 3 )

        #origin = 4 * LEFT
        s = 2
        e1 = Arrow( start = origin, end = origin + s * h_r( 0 ), color = GREEN, buff = 0 )
        e1Tex = MathTex( vec_e1 )
        e1Tex.set_color( GREEN )
        e1Tex.move_to( origin + (s + 0.3) * h_r( 0 ) + 0.3 * UP )
        e2 = Arrow( start = origin, end = origin + s * h_r( PI/2 ), color = RED, buff = 0 )
        e2Tex = MathTex( concat( vec_e1, 'i' ) )
        e2Tex.set_color( RED )
        e2Tex.move_to( origin + (s + 0.3) * h_r( PI/2 ) + 0.3 * RIGHT )

        self.play( AnimationGroup( Write( e1 ), Write( e1Tex ) ) )
        self.wait( 4 )
        self.play( AnimationGroup( Write( e2 ), Write( e2Tex ) ) )
        self.wait( 4 )
        self.play( FadeOut( VGroup( e1, e2, e1Tex, e2Tex ) ) )
        self.wait( 4 )


        e1 = Arrow( start = origin, end = origin + s * h_r( PI/2 ), color = GREEN, buff = 0 )
        e1Tex = MathTex( vec_e2 )
        e1Tex.set_color( GREEN )
        e1Tex.move_to( origin + (s + 0.3) * h_r( PI/2 ) + 0.3 * RIGHT )
        e2 = Arrow( start = origin, end = origin + s * h_r( PI ), color = RED, buff = 0 )
        e2Tex = MathTex( concat( vec_e2, 'i' ) )
        e2Tex.set_color( RED )
        e2Tex.move_to( origin + (s + 0.3) * h_r( PI ) + 0.3 * UP )

        self.play( AnimationGroup( Write( e1 ), Write( e1Tex ) ) )
        self.wait( 4 )
        self.play( AnimationGroup( Write( e2 ), Write( e2Tex ) ) )
        self.wait( 4 )
        self.play( FadeOut( VGroup( e1, e2, e1Tex, e2Tex ) ) )
        self.wait( 4 )



        th1 = PI/6
        th2 = PI * ( 1/2 + 1/6 )
        #origin = 4 * LEFT
        v1 = Arrow( start = origin, end = origin + radius * h_r( th1 ), color = GREEN, buff = 0 )
        v1Tex = MathTex( vec_x )
        v1Tex.set_color( GREEN )
        v1Tex.move_to( origin + (radius + 0.3) * h_r( th1 ) )
        v2 = Arrow( start = origin, end = origin + radius * h_r( th2 ), color = RED, buff = 0 )
        v2Tex = MathTex( concat( vec_x, 'i' ) )
        v2Tex.set_color( RED )
        v2Tex.move_to( origin + (radius + 0.3) * h_r( th2 ) )

        self.play( AnimationGroup( Write( v1 ), Write( v1Tex ) ) )
        self.wait( 4 )
        self.play( AnimationGroup( Write( v2 ), Write( v2Tex ) ) )
        self.wait( 4 )

        fadeall( self )

# vim: et sw=4 ts=4
