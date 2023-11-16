from mycolors import *
import random

class m010_intro( Scene ):
    def construct( self ):

        title = Text( "Geometric algebra and calculus identities." )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.play( FadeIn( title ) )
        self.wait( 1 )

        eq = [ cMathTex( r" \boldsymbol{\nabla} \times ( \boldsymbol{\nabla} f ) = 0 " ),
               cMathTex( r" \boldsymbol{\nabla} \cdot ( \boldsymbol{\nabla} \times {{ \mathbf{f} }} ) = 0" ),
               cMathTex( r" \boldsymbol{\nabla} \wedge ( \boldsymbol{\nabla} \wedge A ) = 0" ),
               cMathTex( r" \boldsymbol{\nabla} \cdot ( f {{ \mathbf{f} }} ) = ( \boldsymbol{\nabla} f ) \cdot {{ \mathbf{f} }} + f ( \boldsymbol{\nabla} \cdot {{ \mathbf{f} }} )" ),
               cMathTex( r" \boldsymbol{\nabla} \times ( f {{ \mathbf{f} }} ) = ( \boldsymbol{\nabla} f ) \times {{ \mathbf{f} }} + f ( \boldsymbol{\nabla} \times {{ \mathbf{f} }} )" ),
               cMathTex( r" \boldsymbol{\nabla} \wedge ( f A ) = ( \boldsymbol{\nabla} f ) \wedge A + f ( \boldsymbol{\nabla} \wedge A )" ),
               MathTex( r"  \mathbf{a}  \times (  \mathbf{b}  \times  \mathbf{c}  ) = -  \mathbf{a}  \cdot (  \mathbf{b}  \wedge  \mathbf{c}  ) " ),
               cMathTex( r" ( {{ \mathbf{a} }} \times {{ \mathbf{b} }} ) \times {{ \mathbf{c} }} = - ( {{ \mathbf{a} }} \wedge {{ \mathbf{b} }} ) \cdot {{ \mathbf{c} }}" ),
               cMathTex( r" \boldsymbol{\nabla} ( {{ \mathbf{a} }} \cdot {{ \mathbf{b} }} ) = ( {{ \mathbf{a} }} \cdot \boldsymbol{\nabla} ) {{ \mathbf{b} }} + ( {{ \mathbf{b} }} \cdot \boldsymbol{\nabla} ) {{ \mathbf{a} }} + ( \boldsymbol{\nabla} \wedge {{ \mathbf{b} }} ) \cdot {{ \mathbf{a} }} + ( \boldsymbol{\nabla} \wedge {{ \mathbf{a} }} ) \cdot {{ \mathbf{b} }}" ),
               cMathTex( r" \boldsymbol{\nabla} ( {{ \mathbf{a} }} \cdot {{ \mathbf{b} }} ) = ( {{ \mathbf{a} }} \cdot \boldsymbol{\nabla} ) {{ \mathbf{b} }} + ( {{ \mathbf{b} }} \cdot \boldsymbol{\nabla} ) {{ \mathbf{a} }} + {{ \mathbf{a} }} \times ( \boldsymbol{\nabla} \times {{ \mathbf{b} }} ) + {{ \mathbf{b} }} \times ( \boldsymbol{\nabla} \times {{ \mathbf{a} }} )" ),
               cMathTex( r" \boldsymbol{\nabla} \times ( {{ \mathbf{a} }} \times {{ \mathbf{b} }} ) = -\boldsymbol{\nabla} \cdot ( {{ \mathbf{a} }} \wedge {{ \mathbf{b} }} )" ),
               MathTex( r"  \mathbf{a}  \cdot (  \mathbf{b}  \times  \mathbf{c}  ) = -I (  \mathbf{a}  \wedge  \mathbf{b}  \wedge  \mathbf{c}  )" ),
               cMathTex( r" \boldsymbol{\nabla} \cdot ( f ( \boldsymbol{\nabla} g \times \boldsymbol{\nabla} h } ) = \boldsymbol{\nabla} f \cdot ( \boldsymbol{\nabla} g \times \boldsymbol{\nabla} h )" ),
               cMathTex( r" \boldsymbol{\nabla} \wedge ( f ( \boldsymbol{\nabla} g \wedge \boldsymbol{\nabla} h } ) = \boldsymbol{\nabla} f \wedge \boldsymbol{\nabla} g \wedge \boldsymbol{\nabla} h" ),
               cMathTex( r" \boldsymbol{\nabla} \cdot ( {{ \mathbf{a} }} \times {{ \mathbf{b} }} ) = {{ \mathbf{b} }} \cdot ( \boldsymbol{\nabla} \times {{ \mathbf{a} }} ) - {{ \mathbf{a} }} \cdot ( \boldsymbol{\nabla} \times {{ \mathbf{b} }} )" ),
               cMathTex( r" \boldsymbol{\nabla} \wedge ( {{ \mathbf{a} }} \wedge {{ \mathbf{b} }} ) = {{ \mathbf{b} }} \wedge ( \boldsymbol{\nabla} \wedge {{ \mathbf{a} }} ) - {{ \mathbf{a} }} \wedge ( \boldsymbol{\nabla} \wedge {{ \mathbf{b} }} )" ) ]

        for i in range(16):
            xrand = random.uniform( -1, 1 )
            yrand = random.uniform( 1.8, 5 )
            eq[i].move_to( title ).shift( xrand * RIGHT + (yrand + 0.5 ) * DOWN )
            if i > 0:
                self.play( AnimationGroup( FadeOut( eq[i-1] ), Write( eq[i] ) ) )
            else:
                self.play( Write( eq[i] ) )
            self.wait( 0.25 )

        fadeall( self )

# vim: et sw=4 ts=4
