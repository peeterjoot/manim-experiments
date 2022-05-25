from helper import *

class GAIntro_030( Scene ):
    def construct( self ):

        title = Text( '2D Geometric algebra.' )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.play( FadeIn( title ) )
        self.wait( 4 )

        eq = MathTex( concat( l.sq(vec_x), ' = ', l.dot( vec_x, vec_x ) ) )
        eq.shift( 2 * RIGHT + 2 * UP )

        origin = 6 * LEFT + 2 * DOWN
        s = 3
        a1 = Arrow( start = origin, end = origin + s * RIGHT, color = GREEN, buff = 0 )
        e1tex = MathTex( vec_e1 )
        e1tex.move_to( origin + s * RIGHT/2 + 0.40 * DOWN )
        e1tex.set_color( GREEN )
        a2 = Arrow( start = origin, end = origin + s * UP, color = RED, buff = 0 )
        e2tex = MathTex( vec_e2 )
        e2tex.move_to( origin + s * UP/2 + 0.40 * RIGHT )
        e2tex.set_color( RED )
        self.play( AnimationGroup( Write( a1 ), Write( e1tex ), Write( a2 ), Write( e2tex ) ) )
        self.wait( 4 )

        self.play( Write( eq ) )
        self.wait( 1 )
        self.play( Indicate( VGroup( a1, e1tex ) ) )
        self.wait( 4 )
        eq1 = MathTex( concat( l.sq( vec_e1 ), ' = 1' ) )
        eq1.move_to( eq, DOWN )
        eq1.shift( DOWN + 1.0 * LEFT )
        eq1.set_color( GREEN )
        self.play( Write( eq1 ) )
        self.wait( 4 )

        self.play( Indicate( VGroup( a2, e2tex ) ) )
        self.wait( 4 )
        eq2 = MathTex( concat( r'\quad, ', l.sq( vec_e2 ), ' = 1' ) )
        eq2.move_to( eq1, RIGHT )
        eq2.shift( 2.0 * RIGHT )
        eq2.set_color( RED )
        self.play( AnimationGroup( Write( a2 ), Write( e2tex ) ) )
        self.wait( 4 )
        self.play( Write( eq2 ) )
        self.wait( 4 )

        a2g = VGroup( a2, e2tex )
        self.play( a2g.animate.shift(s * RIGHT), run_time=1, rate_func=linear )
        self.wait( 2 )
        e1e2p = origin + s * (RIGHT + UP)
        e1e2 = Arrow( start = origin, end = e1e2p, color = BLUE, buff = 0 )
        e1e2tex = MathTex( concat( l.add( vec_e1, vec_e2 ) ) )
        e1e2tex.move_to( origin + s * (RIGHT + UP)/2 + 1.0 * LEFT + 0.2 * UP )
        e1e2tex.set_color( BLUE )
        self.play( AnimationGroup( Write( e1e2 ), Write( e1e2tex ) ) )
        self.wait( 4 )


        eq3b = [ MathTex( concat( '2 = ', l.sq( l.lr( l.add( vec_e1, vec_e2 ) ) ) ) ),
                 MathTex( concat( '= ', l.lr( l.add( vec_e1, vec_e2 ) ), l.lr( l.add( vec_e1, vec_e2 ) ) ) ),
                 MathTex( concat( '= ', l.sq( vec_e1 ), '+', l.sq( vec_e2 ), '+', vec_e1, vec_e2, '+', vec_e2, vec_e1 ) ),
                 MathTex( concat( '= 2 + ', vec_e1, vec_e2, '+', vec_e2, vec_e1 ) ),
               ]
        eq3b[0].move_to( eq1 )
        eq3b[0].shift( DOWN )
        eq3b[0].set_color( BLUE )
        self.play( Write( eq3b[0] ) )
        self.wait( 4 )
        shifts = [ 0.38 * RIGHT, 0 * UP, 0 * UP, 0 * UP ]

        for i in range(3):
            eq3b[i+1].set_color( BLUE )
            write_aligned( self, eq3b[i], eq3b[i+1], 0.75 * DOWN + shifts[i], None )
            self.wait( 4 )
        self.wait( 4 )


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
        self.wait( 10 )

        fadeall( self )

# vim: et sw=4 ts=4
