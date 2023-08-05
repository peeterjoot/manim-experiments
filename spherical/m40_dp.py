from helper import *

class m20_dt( Scene ):
    def construct( self ):

        title = Text( 'Azimuthal unit vector' )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.play( FadeIn( title ) )
        self.wait( 5 )

        eq = [ MathTex( concat( r'\hat{\boldsymbol{\phi}} \propto', l.frac( r'\partial \mathbf{x}', r'\partial \phi') ) ) ]
        eq[0].shift( 1 * UP + 5.00 * LEFT )
        self.play( Write( eq[0] ) )
        self.wait( 5 )

        eq2 = [ MathTex( concat( l.frac( r'\partial \mathbf{x}', r'\partial \phi'), ' = ', vec_e3, l.frac( r'\partial ', r'\partial \phi'), l.lr( r'\cos\theta + j \sin\theta' ) ) ),
                MathTex( concat( ' = ', vec_e3, r'\sin\theta', l.frac( r'\partial j', r'\partial \phi') ) ),
                MathTex( concat( ' = ', vec_e3, r'\sin\theta', vec_e3, vec_e1, r'i e^{i\phi}' ) ),
                MathTex( concat( ' = ', r'\sin\theta', vec_e1, vec_e1, vec_e2, r'e^{i\phi}' ) ),
                MathTex( concat( ' = ', r'\sin\theta', vec_e2, r'e^{i\phi}' ) ) ]
        eq2[0].move_to( eq[0] ).shift( 0.00 * DOWN + 6.00 * RIGHT )
        self.play( Write( eq2[0] ) )
        self.wait( 5 )
        for i in range(4):
            sh = 1.0 * DOWN + 0.0 * RIGHT
            if i == 0:
                #print("sh")
                sh += 0.80 * RIGHT
            write_aligned( self, eq2[i], eq2[i+1], sh, None )
            self.wait( 3 )
        self.wait( 5 )

        eq2p = [ MathTex( concat( l.frac( r'\partial \mathbf{x}', r'\partial \phi'), ' = ', r'\sin\theta', vec_e2, r'e^{i\phi}' ) ) ]
        eq2p[0].move_to( eq2[0] ).shift( 1.20 * LEFT )
        self.play( ReplacementTransform( VGroup(*eq2), VGroup(*eq2p) ) )
        self.wait( 5 )

        eq3 = [ MathTex( concat( r'\hat{\boldsymbol{\phi}} =', vec_e2, r'e^{i\phi}' ) ) ]
        eq3[0].move_to( eq2p[0] ).shift( 1.50 * DOWN + 0.35 * LEFT )
        self.play( Write( eq3[0] ) )
        self.wait( 5 )

        fadeall( self )

# vim: et sw=4 ts=4
