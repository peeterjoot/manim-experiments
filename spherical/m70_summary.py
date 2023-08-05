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

        eq[0].shift( 2 * UP + 0.5 * LEFT )
        self.play( Write( eq[0] ) )
        self.wait( 5 )

        eq[1].move_to( eq[0] ).shift( 1.00 * DOWN + 3.0 * LEFT )
        self.play( Write( eq[1] ) )
        self.wait( 5 )
    
        i = 1
        write_aligned( self, eq[i], eq[i+1], 0.75 * DOWN + 0.37 * RIGHT, None )
        self.wait( 5 )

        eq[3].move_to( eq[1] ).shift( 1.7 * DOWN + 0.57 * RIGHT )
        self.play( Write( eq[3] ) )
        self.wait( 5 )

        i = 3
        write_aligned( self, eq[i], eq[i+1], 0.75 * DOWN + 0.42 * RIGHT, None )
        self.wait( 5 )

        eq[5].move_to( eq[3] ).shift( 1.7 * DOWN + 0.65 * LEFT )
        self.play( Write( eq[5] ) )
        self.wait( 5 )

        i = 5
        write_aligned( self, eq[i], eq[i+1], 0.75 * DOWN + 0.48 * RIGHT, None )
        self.wait( 5 )

        #for i in range(6):
        #    sh = 0.75 * DOWN + 0.0 * RIGHT
        #    if i % 2 == 0:
        #        sh += 0.50 * RIGHT
        #    write_aligned( self, eq[i], eq[i+1], sh, None )
        #    self.wait( 3 )
        #self.wait( 5 )

        fadeall( self )

# vim: et sw=4 ts=4
