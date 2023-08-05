from helper import *

class m60_azimuthal_expansion( Scene ):
    def construct( self ):

        title = Text( 'Azimuthal unit vector: conventional form.' )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.play( FadeIn( title ) )
        self.wait( 5 )

        eq = [ MathTex( concat( r'\hat{\boldsymbol{\phi}} =', vec_e2, r'e^{i\phi}' ) ),
               MathTex( concat(                         ' = ', vec_e2, l.lr( r'\cos\phi + i \sin\phi' ) ) ),
               MathTex( concat(                         ' = ', vec_e2, l.lr( r'\cos\phi + ', vec_e1, vec_e2, ' \sin\phi' ) ) ),
               MathTex( concat(                         ' = -', vec_e1, r'\sin\phi + ', vec_e2, r'\cos\phi' ) ) ]

        eq[0].shift( 2 * UP + 2 * LEFT )
        self.play( Write( eq[0] ) )
        self.wait( 5 )

        for i in range(3):
            sh = 0.75 * DOWN + 0.0 * RIGHT
            if i == 0:
                sh += 0.50 * RIGHT
            write_aligned( self, eq[i], eq[i+1], sh, None )
            self.wait( 3 )
        self.wait( 5 )

        fadeall( self )

# vim: et sw=4 ts=4
