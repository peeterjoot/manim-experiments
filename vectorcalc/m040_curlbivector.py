from mycolors import *

class m040_curlbivector( Scene ):
    def construct( self ):

        title = Text( "Curl of a bivector." )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.play( FadeIn( title ) )
        self.wait( 1 )

        eq = [ cMathTex( r"{{ \mathbf{a} }}, {{ \mathbf{b} }} \in \mathbb{R}^N" ),
               cMathTex( r"\boldsymbol{\nabla} \wedge ( {{ \mathbf{a} }} \wedge {{ \mathbf{b} }} )"),
               cMathTex( "=" ), cMathTex( r"\boldsymbol{\nabla}' \wedge ( {{ \mathbf{a} }}' \wedge {{ \mathbf{b} }} )"
                                          r"+ \boldsymbol{\nabla}' \wedge ( {{ \mathbf{a} }} \wedge {{ \mathbf{b} }}' )" ),
               cMathTex( "=" ), cMathTex( r"(\boldsymbol{\nabla} \wedge {{ \mathbf{a} }}) \wedge {{ \mathbf{b} }}"
                                          r"- (\boldsymbol{\nabla} \wedge {{ \mathbf{b} }}) \wedge {{ \mathbf{a} }}" ),
               cMathTex( "=" ), cMathTex( r"{{ \mathbf{b} }} \wedge (\boldsymbol{\nabla} \wedge {{ \mathbf{a} }})"
                                          r"- {{ \mathbf{a} }} \wedge (\boldsymbol{\nabla} \wedge {{ \mathbf{b} }})" ) ]

        eq[0].next_to( title, DOWN ).shift( 2.0 * LEFT + 2.0 * RIGHT )
        eq[1].next_to( eq[0], DOWN ).shift( 0.5 * DOWN - 3.0 * RIGHT )
        eq[2].next_to( eq[1], RIGHT )
        eq[3].next_to( eq[2], RIGHT )
        self.play( Write( eq[0] ) )
        self.wait( 1 )
        self.play( Write( eq[1] ) )
        self.play( Write( eq[2] ) )
        self.play( Write( eq[3] ) )
        self.wait( 1 )
        ref = eq[2]
        j = 4
        for i in range(2):
            eq[j].next_to( ref, DOWN ).shift( 0.5 * DOWN )
            eq[j+1].next_to( eq[j], RIGHT )
            for k in range(2):
                self.play( Write( eq[j+k] ) )
            ref = eq[j]
            self.wait( 1 )
            j += 2
        #self.play( FadeOut( VGroup( *eq ) ) )
        self.wait( 5 )

        eq5p = eq[7].copy().next_to( eq[2], RIGHT )
        #self.play( AnimationGroup( FadeOut( eq[0] ), ReplacementTransform( VGroup( eq[3], eq[4], eq[5] ), eq5p ) ) )
        self.play( ReplacementTransform( VGroup( eq[3], eq[4], eq[5], eq[6], eq[7] ), eq5p ) )
        self.wait( 5 )

        eq2 = [ cMathTex( r"{{ \mathbf{a} }}, {{ \mathbf{b} }} \in \mathbb{R}^3" ),
                cMathTex( r"{{ \mathbf{a} }} \cdot ({{ \mathbf{b} }} \times {{ \mathbf{c} }})" ),
                cMathTex( r"=" ), cMathTex( r"-I({{ \mathbf{a} }} \wedge ({{ \mathbf{b} }} \wedge {{ \mathbf{c} }}))" ) ]
        eq2[0].next_to( eq[0], DOWN ).shift( 2.0 * LEFT + 2.0 * RIGHT + 1.5 * DOWN )
        eq2[1].next_to( eq2[0], DOWN ).shift( 0.5 * DOWN + 2.0 * LEFT )
        eq2[2].next_to( eq2[1], RIGHT )
        eq2[3].next_to( eq2[2], RIGHT )
        self.play( Write( eq2[0] ) )
        self.wait( 1 )
        self.play( Write( eq2[1] ) )
        self.play( Write( eq2[2] ) )
        self.play( Write( eq2[3] ) )
        self.wait( 1 )

        eq3 = [ [ cMathTex( r"\boldsymbol{\nabla} \wedge ( {{ \mathbf{a} }} \wedge {{ \mathbf{b} }} )"), cMathTex( "=" ), cMathTex( r"{{ \mathbf{b} }} \wedge (\boldsymbol{\nabla} \wedge {{ \mathbf{a} }}) - {{ \mathbf{a} }} \wedge (\boldsymbol{\nabla} \wedge {{ \mathbf{b} }})" ) ],
                [ cMathTex( r"-I(\boldsymbol{\nabla} \wedge ( {{ \mathbf{a} }} \wedge {{ \mathbf{b} }} ))"), cMathTex( "=" ), cMathTex( r"-I({{ \mathbf{b} }} \wedge (\boldsymbol{\nabla} \wedge {{ \mathbf{a} }})) + I({{ \mathbf{a} }} \wedge (\boldsymbol{\nabla} \wedge {{ \mathbf{b} }}))" ) ],
                [ cMathTex( r"\boldsymbol{\nabla} \cdot ( {{ \mathbf{a} }} \times {{ \mathbf{b} }} )"), cMathTex( "=" ), cMathTex( r"{{ \mathbf{b} }} \cdot (\boldsymbol{\nabla} \times {{ \mathbf{a} }}) - {{ \mathbf{a} }} \cdot (\boldsymbol{\nabla} \times {{ \mathbf{b} }})" ) ] ]
        eq3[0][0].next_to( eq2[1], DOWN ).shift( 1.0 * LEFT + 0.5 * DOWN )
        eq3[0][1].next_to( eq3[0][0], RIGHT )
        eq3[0][2].next_to( eq3[0][1], RIGHT )
        self.play( Write( eq3[0][0] ) )
        self.play( Write( eq3[0][1] ) )
        self.play( Write( eq3[0][2] ) )
        self.wait( 1 )

        # replace aligned:
        for i in range(2):
            eq3[i+1][0].next_to( eq3[0][1], LEFT )
            eq3[i+1][2].next_to( eq3[0][1], RIGHT )
            self.play( AnimationGroup( ReplacementTransform( eq3[i][0], eq3[i+1][0] ),
                                       ReplacementTransform( eq3[i][2], eq3[i+1][2] ) ) )
            self.wait( 1 )

        self.wait( 5 )
        fadeall( self )

# vim: et sw=4 ts=4
