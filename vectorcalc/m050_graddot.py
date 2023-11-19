from mycolors import *

class m050_graddot( Scene ):
    def construct( self ):

        title = Text( "Curl of a bivector (divergence of a cross.)" )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.play( FadeIn( title ) )
        self.wait( 1 )

        eq = [ [ cMathTex( r"\boldsymbol{\nabla} ({{ \mathbf{a} }} \cdot {{ \mathbf{b} }})" ),
                 cMathTex( r"=" ),
                 cMathTex( r"(\Ba \cdot \spacegrad) \Bb + (\Bb \cdot \spacegrad) \Ba + \Bb \times (\spacegrad \times \Ba) + \Ba \times (\spacegrad \times \Bb)" ) ] ]

        eq[0][1].next_to( title, DOWN ).shift( 0.0 * LEFT )
        eq[0][0].next_to( eq[0][1], LEFT )
        eq[0][2].next_to( eq[0][1], RIGHT )
        self.play( Write( *eq[0] ) )
        self.wait( 1 )

        self.wait( 5 )
        fadeall( self )

# vim: et sw=4 ts=4
