from mycolors import *

class m040_curlbivector( Scene ):
    def construct( self ):

        title = Text( "Curl of a bivector (divergence of a cross.)" )
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

        eqb = eq[7].copy().next_to( eq[2], RIGHT )
        #self.play( AnimationGroup( FadeOut( eq[0] ), ReplacementTransform( VGroup( eq[3], eq[4], eq[5] ), eqb ) ) )
        self.play( ReplacementTransform( VGroup( eq[3], eq[4], eq[5], eq[6], eq[7] ), eqb ) )
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
        self.wait( 2 )

        eq4 = [ [ eq[1].copy(), eq[2].copy(), eqb.copy() ],
                [ eq3[2][0].copy(), eq3[0][1].copy(), eq3[2][2].copy() ] ]
        eq4[0][1].next_to( title, DOWN ).shift( 0.5 * DOWN + 1.5 * LEFT )
        eq4[0][0].next_to( eq4[0][1], LEFT )
        eq4[0][2].next_to( eq4[0][1], RIGHT )
        eq4[1][1].next_to( eq4[0][1], DOWN ).shift( 0.25 * DOWN )
        eq4[1][0].next_to( eq4[1][1], LEFT )
        eq4[1][2].next_to( eq4[1][1], RIGHT )
        self.play( AnimationGroup( FadeOut( eq[0], *eq2 ) ) )
        self.play( AnimationGroup( ReplacementTransform( VGroup( eq[1], eq[2], eq3[0][1], eq3[2][0], eq3[2][2], eqb ),
                                                         VGroup( *eq4[0], *eq4[1] ) ) ) )
        self.wait( 2 )

        eq5 = [ [ cMathTex( r"\mathrm{Example}:\, {{ \mathbf{a} }} = f \boldsymbol{\nabla} g,\quad {{ \mathbf{b} }} = \boldsymbol{\nabla} h" ) ],
                [ cMathTex( r"\boldsymbol{\nabla} \wedge ( f \boldsymbol{\nabla} g \wedge \boldsymbol{\nabla} h )"),
                  cMathTex( "=" ),
                  cMathTex( r"\boldsymbol{\nabla} h \wedge (\boldsymbol{\nabla} \wedge (f \boldsymbol{\nabla} g)) - f \boldsymbol{\nabla} g \wedge (\boldsymbol{\nabla} \wedge \boldsymbol{\nabla} h)" ) ],
                [ cMathTex( "=" ),
                  cMathTex( r"f\boldsymbol{\nabla} h \wedge (\boldsymbol{\nabla} \wedge \boldsymbol{\nabla} g)"
                            r"+ \boldsymbol{\nabla} h \wedge \boldsymbol{\nabla} f \wedge \boldsymbol{\nabla} g" ) ],
                [ cMathTex( "=" ),
                  cMathTex( r"\boldsymbol{\nabla} h \wedge \boldsymbol{\nabla} f \wedge \boldsymbol{\nabla} g" ) ] ]
        eq5[0][0].next_to( eq4[1][1], DOWN ).shift( 0.3 * DOWN )
        ref = eq5[0][0]
        self.play( Write( eq5[0][0] ) )
        self.wait( 1 )
        for i in range(3):
            if i == 0:
                eq5[i+1][1].next_to( ref, DOWN ).shift( 0.3 * DOWN )
                eq5[i+1][0].next_to( eq5[i+1][1], LEFT )
                eq5[i+1][2].next_to( eq5[i+1][1], RIGHT )
                ref = eq5[i+1][1]
                for j in range(3):
                    self.play( Write( eq5[i+1][j] ) )
            else:
                eq5[i+1][0].next_to( ref, DOWN ).shift( 0.3 * DOWN )
                eq5[i+1][1].next_to( eq5[i+1][0], RIGHT )
                ref = eq5[i+1][0]
                for j in range(2):
                    self.play( Write( eq5[i+1][j] ) )
            self.wait( 1 )
        self.play( FadeOut( VGroup( *eq5[1], *eq5[2], *eq5[3] ) ) )
        self.wait( 1 )

        eq6 = [ [ cMathTex( r"\boldsymbol{\nabla} \cdot ( f \boldsymbol{\nabla} g \times \boldsymbol{\nabla} h )"),
                  cMathTex( "=" ),
                  cMathTex( r"\boldsymbol{\nabla} h \cdot (\boldsymbol{\nabla} \times (f \boldsymbol{\nabla} g)) - f \boldsymbol{\nabla} g \times (\boldsymbol{\nabla} \times \boldsymbol{\nabla} h)" ) ],
                [ cMathTex( "=" ),
                  cMathTex( r"f\boldsymbol{\nabla} h \cdot (\boldsymbol{\nabla} \times \boldsymbol{\nabla} g)"
                            r"+ \boldsymbol{\nabla} h \cdot (\boldsymbol{\nabla} f \times \boldsymbol{\nabla} g)" ) ],
                [ cMathTex( "=" ),
                  cMathTex( r"\boldsymbol{\nabla} h \cdot (\boldsymbol{\nabla} f \times \boldsymbol{\nabla} g)" ) ] ]
        ref = eq5[0][0]
        self.wait( 1 )
        for i in range(3):
            if i == 0:
                eq6[i][1].next_to( ref, DOWN ).shift( 0.3 * DOWN )
                eq6[i][0].next_to( eq6[i][1], LEFT )
                eq6[i][2].next_to( eq6[i][1], RIGHT )
                ref = eq6[i][1]
                for j in range(3):
                    self.play( Write( eq6[i][j] ) )
            else:
                eq6[i][0].next_to( ref, DOWN ).shift( 0.3 * DOWN )
                eq6[i][1].next_to( eq6[i][0], RIGHT )
                ref = eq6[i][0]
                for j in range(2):
                    self.play( Write( eq6[i][j] ) )
            self.wait( 1 )
        self.play( FadeOut( VGroup( *eq6[0], *eq6[1], *eq6[2] ) ) )
        self.wait( 1 )

        eq7 = [ [ cMathTex( r"\boldsymbol{\nabla} \wedge ( f (\boldsymbol{\nabla} g \wedge \boldsymbol{\nabla} h) )"),
                  cMathTex( "=" ),
                  cMathTex( r"\boldsymbol{\nabla} h \wedge \boldsymbol{\nabla} f \wedge \boldsymbol{\nabla} g" ) ] ]
        eq8 = [ [ cMathTex( r"\boldsymbol{\nabla} \cdot ( f (\boldsymbol{\nabla} g \times \boldsymbol{\nabla} h) )"),
                  cMathTex( "=" ),
                  cMathTex( r"\boldsymbol{\nabla} h \cdot (\boldsymbol{\nabla} f \times \boldsymbol{\nabla} g)" ) ] ]

        aligned( self, eq7, eq5[0][0], 1.5 * RIGHT + 0.2 * DOWN, 0.3 * DOWN, 1, 1 )
        self.wait( 1 )
        aligned( self, eq8, eq7[0][1], 0.0 * LEFT + 0.2 * DOWN, 0.3 * DOWN, 1, 1 )
        self.wait( 1 )

        self.wait( 5 )
        fadeall( self )

# vim: et sw=4 ts=4
