from helper import *

class m10_spherical( Scene ):
    def construct( self ):

        title = Text( 'Spherical basis with Geometric algebra.' )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.play( FadeIn( title ) )
        self.wait( 5 )

        eq = [ MathTex( concat( r'\mathrm{Let}\, i = ', vec_e1, vec_e2, r',\quad j = ', vec_e3, vec_e1, r'e^{i\phi}'  ) ), 
               MathTex( concat( l.vec( 'x' ), ' = r', hat_r, r' = r', vec_e3, r'e^{j\theta}' ) ) ]

        eq[0].shift( 2 * UP + 3 * LEFT )
        self.play( Write( eq[0] ) )
        self.wait( 5 )

        eq[1].move_to( eq[0] )
        eq[1].shift( 1 * DOWN )
        self.play( Write( eq[1] ) )
        self.wait( 5 )

        fadeall( self )

# vim: et sw=4 ts=4
