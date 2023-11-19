from mycolors import *

class m050_graddot( Scene ):
    def construct( self ):

        title = Text( "Gradient of a dot product (Jackson)" )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.play( FadeIn( title ) )
        self.wait( 1 )

        eq = [ [ cMathTex( r"\boldsymbol{\nabla} ({{ \mathbf{a} }} \cdot {{ \mathbf{b} }})" ),
                 cMathTex( r"=" ),
                 cMathTex( r"({{ \mathbf{a} }} \cdot \boldsymbol{\nabla}) {{ \mathbf{b} }} + ({{ \mathbf{b} }} \cdot \boldsymbol{\nabla}) {{ \mathbf{a} }} + {{ \mathbf{b} }} \times (\boldsymbol{\nabla} \times {{ \mathbf{a} }}) + {{ \mathbf{a} }} \times (\boldsymbol{\nabla} \times {{ \mathbf{b} }})" ) ] ]

        eq[0][1].next_to( title, DOWN ).shift( 4.0 * LEFT + 0.2 * DOWN )
        eq[0][0].next_to( eq[0][1], LEFT )
        eq[0][2].next_to( eq[0][1], RIGHT )
        for i in range(3):
            self.play( Write( eq[0][i] ) )
        self.wait( 1 )
        self.play( FadeOut( *eq[0] ) )
        self.wait( 1 )

        eq2 = [ [ cMathTex( r"\boldsymbol{\nabla} ({{ \mathbf{a} }} \cdot {{ \mathbf{b} }})" ),
                  cMathTex( r"=" ),
                  cMathTex( r"\langle \spacegrad (\Ba \Bb - \Ba \wedge \Bb) \rangle {}_1" ) ],
                [ cMathTex( r"=" ),
                  cMathTex( r"\langle \spacegrad \Ba \Bb \rangle {}_1 - \spacegrad \cdot (\Ba \wedge \Bb)" ) ] ]
        eq2[0][1].next_to( title, DOWN ).shift( 4.0 * LEFT + 0.2 * DOWN )
        eq2[0][0].next_to( eq2[0][1], LEFT )
        eq2[0][2].next_to( eq2[0][1], RIGHT )
        for i in range(3):
            self.play( Write( eq2[0][i] ) )
        self.wait( 1 )
        eq2[1][0].next_to( eq2[0][1], DOWN ).shift( 0.2 * DOWN )
        eq2[1][1].next_to( eq2[0][1], RIGHT )
        for i in range(2):
            self.play( Write( eq2[1][i] ) )
        self.wait( 1 )




        self.wait( 5 )
        fadeall( self )

# vim: et sw=4 ts=4
