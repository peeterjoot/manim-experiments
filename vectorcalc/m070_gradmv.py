from mycolors import *

class m070_gradmv( Scene ):
    def construct( self ):

        title = Text( "Gradient of products." )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.play( FadeIn( title ) )
        self.wait( 1 )

        eq = [ [ cMathTex( r"\boldsymbol{\nabla} \times ({{ \mathbf{a} }} \times {{ \mathbf{b} }})" ),
                 cMathTex( r"=" ),
                 cMathTex( r"-I(\boldsymbol{\nabla} \wedge ({{ \mathbf{a} }} \times {{ \mathbf{b} }}))" ) ],
               [ cMathTex( r"=" ),
                 cMathTex( r"-\boldsymbol{\nabla} \cdot ({{ \mathbf{a} }} \wedge {{ \mathbf{b} }})" ) ] ]

        aligned( self, eq, title, 0.0 * LEFT + 0.2 * DOWN, 0.3 * DOWN, 1, 1 )

        self.wait( 5 )
        fadeall( self )

# vim: et sw=4 ts=4
