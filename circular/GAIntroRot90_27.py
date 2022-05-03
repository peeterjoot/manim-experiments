from helper import *

class GAIntro_26( Scene ):
    def construct( self ):

        title = Text( 'Geometric algebra: the imaginary.' )
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

        #origin = 4 * LEFT
        #e1 = Arrow( start = origin, end = origin + LEFT, color = GREEN, buff = 0 )
        #e1p = Arrow( start = origin, end = origin + UP, color = RED, buff = 0 )

        fadeall( self )

# vim: et sw=4 ts=4
