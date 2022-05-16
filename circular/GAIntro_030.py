from helper import *

class GAIntro_030( Scene ):
    def construct( self ):

        title = Text( '2D Geometric algebra: fundamentals.' )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.play( FadeIn( title ) )
        self.wait( 5 )

        eq = AcolorsMathTex( concat( l.sq(vec_x), ' = ', l.dot( vec_x, vec_x ) ) )
        eq.shift( 2 * RIGHT )

        self.play( Write( eq ) )
        self.wait( 5 )

        origin = 6 * LEFT + 2 * DOWN
        s = 3
        e1p = origin + s * RIGHT
        e1e2p = origin + s * (RIGHT + UP)
        e1 = Arrow( start = origin, end = e1p, color = GREEN, buff = 0 )
        e2 = Arrow( start = e1p, end = e1p + s * UP, color = RED, buff = 0 )
        e1e2 = Arrow( start = origin, end = e1e2p, color = BLUE, buff = 0 )
        e1tex = MathTex( vec_e1 )
        e1tex.move_to( origin + s * RIGHT/2 + 0.40 * DOWN )
        e1tex.set_color( GREEN )
        e2tex = MathTex( vec_e2 )
        e2tex.move_to( origin + s * (RIGHT + UP/2) + 0.40 * RIGHT )
        e2tex.set_color( RED )
        e1e2tex = MathTex( concat( l.add( vec_e1, vec_e2 ) ) )
        e1e2tex.move_to( origin + s * (RIGHT + UP)/2 + 1.0 * LEFT + 0.2 * UP )
        e1e2tex.set_color( BLUE )

        self.play( AnimationGroup( Write( e1 ), Write( e1tex ),
                                   Write( e2 ), Write( e2tex ),
                                   Write( e1e2 ), Write( e1e2tex )
                                   ) )
        self.wait( 5 )

        self.play( eq.animate.shift(2 * UP), run_time=1, rate_func=linear )
        self.wait( 5 )

        eq1 = MathTex( concat( l.sq( vec_e1 ), ' = 1' ) )
        eq1.move_to( eq, DOWN )
        eq1.shift( DOWN + 1.0 * LEFT )
        eq1.set_color( GREEN )

        eq2 = MathTex( concat( l.sq( vec_e2 ), ' = 1' ) )
        eq2.move_to( eq1, RIGHT )
        eq2.shift( 2.0 * RIGHT )
        eq2.set_color( RED )

        eq3 = MathTex( concat( l.sq( l.lr( l.add( vec_e1, vec_e2 ) ) ), ' = 2' ) )
        eq3.move_to( eq1, DOWN )
        eq3.shift( DOWN )
        eq3.set_color( BLUE )

        self.play( Write( eq1 ) )
        self.wait( 3 )
        self.play( Write( eq2 ) )
        self.wait( 3 )
        self.play( Write( eq3 ) )
        self.wait( 3 )

        eq3b = [ MathTex( concat( '2 = ', l.sq( l.lr( l.add( vec_e1, vec_e2 ) ) ) ) ),
                 MathTex( concat( '= ', l.lr( l.add( vec_e1, vec_e2 ) ), l.lr( l.add( vec_e1, vec_e2 ) ) ) ),
                 MathTex( concat( '= ', l.sq( vec_e1 ), '+', l.sq( vec_e2 ), '+', vec_e1, vec_e2, '+', vec_e2, vec_e1 ) ),
                 MathTex( concat( '= 2 + ', vec_e1, vec_e2, '+', vec_e2, vec_e1 ) ),
               ]
        eq3b[0].move_to( eq3 )
        eq3b[0].set_color( BLUE )
        self.play( TransformMatchingTex( eq3, eq3b[0] ) )
        self.wait( 2 )
        last = eq3b[0]

        for i in range(3):
            eq3b[i+1].set_color( BLUE )
            write_aligned( self, eq3b[i], eq3b[i+1], 0.75 * DOWN + 0.0 * LEFT, None )
            self.wait( 3 )

        eq4 = MathTex( concat( '0 = ', vec_e1, vec_e2, '+', vec_e2, vec_e1 ) )
        eq4.set_color( BLUE )
        write_aligned( self, eq3b[3], eq4, 0.75 * DOWN + 0.0 * LEFT, None )
        self.wait( 4 )

        self.play( FadeOut( VGroup(*eq3b) ) )
        self.wait( 4 )

        eq5 = MathTex( concat( vec_e2, vec_e1, ' = - ', vec_e1, vec_e2 ) )
        eq5.move_to( eq1, DOWN )
        eq5.shift( DOWN + RIGHT )
        eq5.set_color( BLUE )
        self.play( TransformMatchingTex( eq4, eq5 ) )
        self.wait( 4 )

        fadeall( self )

# vim: et sw=4 ts=4
