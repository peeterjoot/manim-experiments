from mycolors import *

class m010_Intro( Scene ):
    def construct( self ):

        title = Text( "Maxwell's equation in geometric algebra." )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.play( FadeIn( title ) )
        self.wait( 5 )

        eq = [ cMathTex( r"{{ \boldsymbol{\nabla} }} \times {{ \mathbf{E} }} = -{{ \mathbf{M} }} - { \partial {{ \mathbf{B} }} \over \partial t } " ),
               cMathTex( r"{{ \boldsymbol{\nabla} }} \times {{ \mathbf{H} }} = {{ \mathbf{J} }} + { \partial {{ \mathbf{D} }} \over \partial t } " ),
               cMathTex( r"{{ \boldsymbol{\nabla} }} \cdot {{ \mathbf{D} }} = \rho" ),
               cMathTex( r"{{ \boldsymbol{\nabla} }} \cdot {{ \mathbf{B} }} = \rho_{\mathrm{m}}" ) ]
        eq[0].shift( 1.50 * UP + 0 * RIGHT )
        self.play( Write( eq[0] ) )
        self.wait( 5 )

        for i in range(3):
            sh = 1.00 * DOWN
            if i == 0:
                sh += 0.00 * DOWN + 1.70 * LEFT
            if i == 1:
                sh += 0.00 * DOWN + 1.40 * LEFT
            if i == 2:
                sh += 0.00 * DOWN + 1.40 * LEFT
            write_aligned( self, eq[i], eq[i+1], sh, None )
            self.wait( 5 )
        self.play( FadeOut( VGroup( *eq ) ) )
        self.wait( 5 )

        eq2 = [ cMathTex( r"\Bigl( \boldsymbol{\nabla} + { 1 \over c } { \partial \over \partial t } \Bigr) F = J" ),
                cMathTex( r"F = {{ \mathbf{E} }} + I \eta {{ \mathbf{H} }}" ),
                # = {{ \mathbf{E} }} + I c {{ \mathbf{B} }}" ),
                cMathTex( r"J = \eta( c \rho - {{ \mathbf{J} }} ) + I ( c \rho_{\mathrm{m}} - {{ \mathbf{M} }} )" ) ]
        eq2[0].move_to( eq[0] )
        self.play( Write( eq2[0] ) )
        self.wait( 5 )
        for i in range(2):
            sh = 1.50 * DOWN
            if i == 0:
                sh += 0.00 * DOWN + 1.70 * LEFT
            write_aligned( self, eq2[i], eq2[i+1], sh, None )
            self.wait( 5 )

        fadeall( self )

# vim: et sw=4 ts=4
