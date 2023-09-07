from helper import *

class m025_Lemma( Scene ):
    def construct( self ):

        title = MathTex( concat( r"\mathrm{Lemma}: r' = ", l.dot( prime(vec_x), hat_r ) ) )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.play( FadeIn( title ) )
        self.wait( 5 )

        eq = [ MathTex( concat( l.frac( 'd', 'dt' ), 'r^2 = ', l.frac( 'd', 'dt' ), l.dot( vec_x, vec_x ) ) ),
               MathTex( concat( "2 r r' = 2", l.dot( prime(vec_x), vec_x ) ) ),
               MathTex( concat( "r' = ", l.dot( prime(vec_x), hat_r ) ) ) ]
        eq[0].shift( UP )
        self.play( Write( eq[0] ) )
        self.wait( 5 )

        for i in range(2):
            sh = 0.90 * DOWN + 0.0 * RIGHT
            #if i == 0:
            #    sh += 0.00 * RIGHT
            write_aligned( self, eq[i], eq[i+1], sh, None )
            self.wait( 3 )
        self.wait( 5 )

        fadeall( self )

# vim: et sw=4 ts=4
