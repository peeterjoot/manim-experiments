from helper import *

class m10_spherical( Scene ):
    def construct( self ):

        title = Text( 'Spherical position vector.' )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.play( FadeIn( title ) )
        self.wait( 5 )

        eq = [ MathTex( concat( r'\mathrm{Let}\, i = ', vec_e1, vec_e2 ) ),
               #MathTex( concat( r'j = ', vec_e3, vec_e1, r'e^{i\phi}' ) ), 
               MathTex( concat( l.vec( 'x' ), ' = r', hat_r, r' = r', vec_e3, r'e^{j\theta}' ) ) ]

        eq[0].shift( 2 * UP + 0 * LEFT )
        self.play( Write( eq[0] ) )
        self.wait( 5 )
        self.wait( 5 )

        for i in range(1):
            sh = 0.75 * DOWN + 0.0 * RIGHT
            if i == 0:
                sh += 0.00 * RIGHT
            write_aligned( self, eq[i], eq[i+1], sh, None )
            self.wait( 3 )
        self.wait( 5 )

        fadeall( self )

# vim: et sw=4 ts=4
