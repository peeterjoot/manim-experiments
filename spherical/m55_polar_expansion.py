from helper import *

class m55_polar_expansion( Scene ):
    def construct( self ):

        title = Text( 'Polar unit vector: conventional form.' )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.play( FadeIn( title ) )
        self.wait( 5 )

        eq = [ MathTex( concat( r'\hat{\boldsymbol{\theta}} =', vec_e1, r"e^{i\phi} e^{j\theta}" ) ),
               MathTex( concat(                           ' = ', vec_e1, r"e^{i\phi}", l.lr( r'\cos\theta + j \sin\theta' ) ) ),
               MathTex( concat(                           ' = ', vec_e1, r"e^{i\phi}", l.lr( r'\cos\theta + ', vec_e3, vec_e1, r'e^{i\phi} \sin\theta' ) ) ),
               MathTex( concat(                           ' = ', vec_e1, l.lr( r'\cos\theta e^{i\phi} + ', vec_e3, r'e^{i\phi}', vec_e1, r'e^{i\phi} \sin\theta' ) ) ),
               MathTex( concat(                           ' = ', vec_e1, l.lr( r'\cos\theta e^{i\phi} + ', vec_e3, vec_e1, r'e^{-i\phi} e^{i\phi} \sin\theta' ) ) ),
               MathTex( concat(                           ' = ', vec_e1, l.lr( r'\cos\theta e^{i\phi} + ', vec_e3, vec_e1, r'\sin\theta' ) ) ),
               MathTex( concat(                           ' = ', vec_e1, r'\cos\theta \cos\phi + ', vec_e2, r'\cos\theta \sin\phi -', vec_e3, r'\sin\theta' ) ) ]

        eq[0].shift( 2 * UP + 3 * LEFT )
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
