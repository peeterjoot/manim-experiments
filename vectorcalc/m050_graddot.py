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
                  cMathTex( r"\langle \boldsymbol{\nabla} ({{ \mathbf{a} }} {{ \mathbf{b} }} - {{ \mathbf{a} }} \wedge {{ \mathbf{b} }}) \rangle {}_1" ) ],
                [ cMathTex( r"=" ),
                  cMathTex( r"\langle \boldsymbol{\nabla} {{ \mathbf{a} }} {{ \mathbf{b} }} \rangle {}_1 - \boldsymbol{\nabla} \cdot ({{ \mathbf{a} }} \wedge {{ \mathbf{b} }})" ) ] ]
        eq2[0][1].next_to( title, DOWN ).shift( 4.0 * LEFT + 0.2 * DOWN )
        eq2[0][0].next_to( eq2[0][1], LEFT )
        eq2[0][2].next_to( eq2[0][1], RIGHT )
        for i in range(3):
            self.play( Write( eq2[0][i] ) )
        self.wait( 1 )
        eq2[1][0].next_to( eq2[0][1], DOWN ).shift( 0.3 * DOWN )
        eq2[1][1].next_to( eq2[1][0], RIGHT )
        for i in range(2):
            self.play( Write( eq2[1][i] ) )
        self.wait( 1 )

        eq3 = [ [ cMathTex( r"\langle \boldsymbol{\nabla} {{ \mathbf{a} }} {{ \mathbf{b} }} \rangle {}_1" ),
                  cMathTex( r"=" ),
                  cMathTex( r"\langle \boldsymbol{\nabla}' {{ \mathbf{a} }}' {{ \mathbf{b} }}"
                            r"+ \boldsymbol{\nabla}' {{ \mathbf{a} }} {{ \mathbf{b} }}' \rangle {}_1" ) ],
                [ cMathTex( r"=" ),
                  cMathTex( r"\langle (\boldsymbol{\nabla} \cdot {{ \mathbf{a} }} + \boldsymbol{\nabla} \wedge {{ \mathbf{a} }}) {{ \mathbf{b} }}"
                            r"- {{ \mathbf{a} }} \boldsymbol{\nabla}' {{ \mathbf{b} }}' + 2 (\Ba \cdot \spacegrad) \Bb \rangle {}_1" ) ],
                [ cMathTex( r"=" ),
                  cMathTex( r"(\boldsymbol{\nabla} \cdot {{ \mathbf{a} }} \Bb + (\boldsymbol{\nabla} \wedge {{ \mathbf{a} }}) \cdot {{ \mathbf{b} }}"
                            r"- {{ \mathbf{a} }}(\boldsymbol{\nabla} \cdot {{ \mathbf{b} }})"
                            r"- {{ \mathbf{a} }} \cdot (\boldsymbol{\nabla} \wedge {{ \mathbf{b} }}) + 2 (\Ba \cdot \spacegrad) \Bb" ) ]
        eq3[0][1].next_to( eq2[1][0], DOWN ).shift( 0.0 * LEFT + 0.2 * DOWN )
        eq3[0][0].next_to( eq3[0][1], LEFT )
        eq3[0][2].next_to( eq3[0][1], RIGHT )
        for i in range(3):
            self.play( Write( eq3[0][i] ) )
        self.wait( 1 )
        for j in range(2):
            eq3[j+1][0].next_to( eq3[j+0][1], DOWN ).shift( 0.3 * DOWN )
            eq3[j+1][1].next_to( eq3[j+1][0], RIGHT )
            for i in range(2):
                self.play( Write( eq3[j+1][i] ) )
            self.wait( 1 )

        self.wait( 5 )
        fadeall( self )

# vim: et sw=4 ts=4
