from helper import *

class m70_summary( Scene ):
    def construct( self ):

        title = Text( 'Summary' )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.play( FadeIn( title ) )
        self.wait( 5 )

        eq = [ MathTex( concat( r'i = ', vec_e1, vec_e2, ',\quad j = ', vec_e3, vec_e1, r'e^{i\phi}' ) ),
               MathTex( concat( r'\hat{\mathbf{r}} =', vec_e3, r'e^{j\theta}' ) ),
               MathTex( concat( ' = ', vec_e1, r'\sin\theta \cos\phi + ', vec_e2, r'\sin\theta \sin\phi + ', vec_e3, r'\cos\theta' ) ),
               MathTex( concat( r'\hat{\boldsymbol{\theta}} =', vec_e3, r"e^{j(\theta + \pi/2)}" ) ),
               MathTex( concat( ' = ', vec_e1, r'\cos\theta \cos\phi + ', vec_e2, r'\cos\theta \sin\phi -', vec_e3, r'\sin\theta' ) ),
               MathTex( concat( r'\hat{\boldsymbol{\phi}} =', vec_e2, r'e^{i\phi}' ) ),
               MathTex( concat( ' = -', vec_e1, r'\sin\phi + ', vec_e2, r'\cos\phi' ) ) ]

        eq[0].shift( 2 * UP + 2 * LEFT )
        self.play( Write( eq[0] ) )
        self.wait( 5 )

        for i in range(6):
            sh = 0.75 * DOWN + 0.0 * RIGHT
            if i == 0:
                sh += 0.50 * RIGHT
            write_aligned( self, eq[i], eq[i+1], sh, None )
            self.wait( 3 )
        self.wait( 5 )

        fadeall( self )

# vim: et sw=4 ts=4
