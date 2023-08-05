from helper import *

class m30_dt( Scene ):
    def construct( self ):

        title = Text( 'Polar unit vector' )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.play( FadeIn( title ) )
        self.wait( 5 )

        eq = [ MathTex( concat( r'\hat{\boldsymbol{\theta}} \propto', l.frac( r'\partial \mathbf{x}', r'\partial \theta') ) ) ]
        eq[0].shift( 1 * UP + 5.00 * LEFT )
        self.play( Write( eq[0] ) )
        self.wait( 5 )

        eq2 = [ MathTex( concat( l.frac( r'\partial \mathbf{x}', r'\partial \theta'), ' = r', vec_e3, r' j e^{j\theta}' ) ),
                #MathTex( concat(  ' = r', vec_e3, vec_e3, vec_e1, r" e^{i\phi} e^{j\theta}" ) ),
                #MathTex( concat(  ' = r', vec_e3, r" j e^{j\theta}" ) ),
                MathTex( concat(  ' = r', vec_e3, r" e^{j(\theta + \pi/2)}" ) ) ]
                #MathTex( concat(  ' = r', vec_e1, r" e^{i\phi} e^{j\theta}" ) ) 
        eq2[0].move_to( eq[0] ).shift( 0.00 * DOWN + 4.00 * RIGHT )
        self.play( Write( eq2[0] ) )
        self.wait( 5 )
        for i in range(1):
            sh = 1.0 * DOWN + 0.0 * RIGHT
            if i == 0:
                #print("sh")
                sh += 0.80 * RIGHT
            write_aligned( self, eq2[i], eq2[i+1], sh, None )
            self.wait( 3 )
        self.wait( 5 )

        #eq3 = [ MathTex( concat( r'\hat{\boldsymbol{\theta}} =', vec_e1, r"e^{i\phi} e^{j\theta}" ) ) ]
        eq3 = [ MathTex( concat( r'\hat{\boldsymbol{\theta}} =', vec_e3, r"e^{j(\theta + \pi/2)}" ) ) ]
        eq3[0].move_to( eq2[1] ).shift( 1.50 * DOWN + 0.35 * LEFT )
        self.play( Write( eq3[0] ) )
        self.wait( 5 )

        fadeall( self )

# vim: et sw=4 ts=4
