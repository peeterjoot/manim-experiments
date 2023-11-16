from mycolors import *
import random

class m010_intro( Scene ):
    def construct( self ):

        title = Text( "Geometric algebra and calculus identities." )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.play( FadeIn( title ) )
        self.wait( 1 )

        eq = [ [ cMathTex( r"\boldsymbol{\nabla} \times ( \boldsymbol{\nabla} f )"), cMathTex( " = "), cMathTex(" 0 " ) ],
               [ cMathTex( r"\boldsymbol{\nabla} \cdot ( \boldsymbol{\nabla} \times {{ \mathbf{f} }} )"), cMathTex( "=" ), cMathTex( r"0" ) ],
               [ cMathTex( r"\boldsymbol{\nabla} \wedge ( \boldsymbol{\nabla} \wedge A )"), cMathTex( "=" ), cMathTex( r"0" ) ],
               [ cMathTex( r"\boldsymbol{\nabla} \cdot ( f {{ \mathbf{f} }} )"), cMathTex( "=" ), cMathTex( r"( \boldsymbol{\nabla} f ) \cdot {{ \mathbf{f} }} + f ( \boldsymbol{\nabla} \cdot {{ \mathbf{f} }} )" ) ],
               [ cMathTex( r"\boldsymbol{\nabla} \times ( f {{ \mathbf{f} }} )"), cMathTex( "=" ), cMathTex( r"( \boldsymbol{\nabla} f ) \times {{ \mathbf{f} }} + f ( \boldsymbol{\nabla} \times {{ \mathbf{f} }} )" ) ],
               [ cMathTex( r"\boldsymbol{\nabla} \wedge ( f A )"), cMathTex( "=" ), cMathTex( r"( \boldsymbol{\nabla} f ) \wedge A + f ( \boldsymbol{\nabla} \wedge A )" ) ],
               [ cMathTex( r"{{ \mathbf{a} }} \times ( {{ \mathbf{b} }} \times {{  \mathbf{c} }} )"), cMathTex( "=" ), cMathTex( r"- {{ \mathbf{a} }} \cdot ( {{ \mathbf{b} }}  \wedge  \mathbf{c} }} ) " ) ],
               [ cMathTex( r"( {{ \mathbf{a} }} \times {{ \mathbf{b} }} ) \times {{ \mathbf{c} }}"), cMathTex( "=" ), cMathTex( r"- ( {{ \mathbf{a} }} \wedge {{ \mathbf{b} }} ) \cdot {{ \mathbf{c} }}" ) ],
               [ cMathTex( r"\boldsymbol{\nabla} ( {{ \mathbf{a} }} \cdot {{ \mathbf{b} }} )"), cMathTex( "=" ), cMathTex( r"( {{ \mathbf{a} }} \cdot \boldsymbol{\nabla} ) {{ \mathbf{b} }} + ( {{ \mathbf{b} }} \cdot \boldsymbol{\nabla} ) {{ \mathbf{a} }} + ( \boldsymbol{\nabla} \wedge {{ \mathbf{b} }} ) \cdot {{ \mathbf{a} }} + ( \boldsymbol{\nabla} \wedge {{ \mathbf{a} }} ) \cdot {{ \mathbf{b} }}" ) ],
               [ cMathTex( r"\boldsymbol{\nabla} ( {{ \mathbf{a} }} \cdot {{ \mathbf{b} }} )"), cMathTex( "=" ), cMathTex( r"( {{ \mathbf{a} }} \cdot \boldsymbol{\nabla} ) {{ \mathbf{b} }} + ( {{ \mathbf{b} }} \cdot \boldsymbol{\nabla} ) {{ \mathbf{a} }} + {{ \mathbf{a} }} \times ( \boldsymbol{\nabla} \times {{ \mathbf{b} }} ) + {{ \mathbf{b} }} \times ( \boldsymbol{\nabla} \times {{ \mathbf{a} }} )" ) ],
               [ cMathTex( r"\boldsymbol{\nabla} \times ( {{ \mathbf{a} }} \times {{ \mathbf{b} }} )"), cMathTex( "=" ), cMathTex( r"-\boldsymbol{\nabla} \cdot ( {{ \mathbf{a} }} \wedge {{ \mathbf{b} }} )" ) ],
               [ cMathTex( r"{{ \mathbf{a} }} \cdot ( {{ \mathbf{b} }} \times {{ \mathbf{c} }} )"), cMathTex( "=" ), cMathTex( r"-I ( {{ \mathbf{a} }} \wedge {{ \mathbf{b} }} \wedge {{  \mathbf{c} }}  )" ) ],
               [ cMathTex( r"\boldsymbol{\nabla} \cdot ( f ( \boldsymbol{\nabla} g \times \boldsymbol{\nabla} h } )"), cMathTex( "=" ), cMathTex( r"\boldsymbol{\nabla} f \cdot ( \boldsymbol{\nabla} g \times \boldsymbol{\nabla} h )" ) ],
               [ cMathTex( r"\boldsymbol{\nabla} \wedge ( f ( \boldsymbol{\nabla} g \wedge \boldsymbol{\nabla} h } )"), cMathTex( "=" ), cMathTex( r"\boldsymbol{\nabla} f \wedge \boldsymbol{\nabla} g \wedge \boldsymbol{\nabla} h" ) ],
               [ cMathTex( r"\boldsymbol{\nabla} \cdot ( {{ \mathbf{a} }} \times {{ \mathbf{b} }} )"), cMathTex( "=" ), cMathTex( r"{{ \mathbf{b} }} \cdot ( \boldsymbol{\nabla} \times {{ \mathbf{a} }} ) - {{ \mathbf{a} }} \cdot ( \boldsymbol{\nabla} \times {{ \mathbf{b} }} )" ) ],
               [ cMathTex( r"\boldsymbol{\nabla} \wedge ( {{ \mathbf{a} }} \wedge {{ \mathbf{b} }} )"), cMathTex( "=" ), cMathTex( r"{{ \mathbf{b} }} \wedge ( \boldsymbol{\nabla} \wedge {{ \mathbf{a} }} ) - {{ \mathbf{a} }} \wedge ( \boldsymbol{\nabla} \wedge {{ \mathbf{b} }} )" ) ] ]

        for i in range(16):
            xrand = random.uniform( -1, 1 )
            yrand = random.uniform( 1.8, 5 )
            eq[i][0].move_to( title ).shift( xrand * RIGHT + 4.5 * LEFT + (yrand + 0.5 ) * DOWN )
            eq[i][1].next_to( eq[i][0], RIGHT )
            eq[i][2].next_to( eq[i][1], RIGHT )
            if i > 0:
                self.play( FadeOut( VGroup( *eq[i-1] ) ) )
            for j in range(3):
                self.play( Write( eq[i][j] ) )
            self.wait( 0.25 )

        fadeall( self )

# vim: et sw=4 ts=4
