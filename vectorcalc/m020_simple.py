from mycolors import *

class m020_simple( Scene ):
    def construct( self ):

        title = Text( "Some useful vector identities." )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.play( FadeIn( title ) )
        self.wait( 1 )

        eq = [ cMathTex( r"{{ \mathbf{a} }} \cdot ({{ \mathbf{b} }} \times {{ \mathbf{c} }})" ),
               cMathTex( r"=" ), cMathTex( r" \langle {{ \mathbf{a} }} ({{ \mathbf{b} }} \times {{ \mathbf{c} }}) \rangle" ),
               cMathTex( r"=" ), cMathTex( r"\langle -I {{ \mathbf{a} }} ({{ \mathbf{b} }} \wedge {{ \mathbf{c} }}) \rangle" ),
               cMathTex( r"=" ), cMathTex( r"\langle "
                                           r"-I({{ \mathbf{a} }} \cdot ({{ \mathbf{b} }} \wedge {{ \mathbf{c} }}))"
                                           r"-I({{ \mathbf{a} }} \wedge ({{ \mathbf{b} }} \wedge {{ \mathbf{c} }}))"
                                           r"\rangle" ),
               cMathTex( r"=" ), cMathTex( r"-I({{ \mathbf{a} }} \wedge {{ \mathbf{b} }} \wedge {{ \mathbf{c} }})" ) ]

        eq2 = [ cMathTex( r"{{  \mathbf{a} }} \times ( {{ \mathbf{b} }} \times {{ \mathbf{c} }} )" ),
                cMathTex( r"=" ), cMathTex( r"-I ({{  \mathbf{a} }} \wedge ( {{ \mathbf{b} }} \times {{ \mathbf{c} }} ))" ),
                cMathTex( r"=" ), cMathTex( r"\langle "
                                            r"-I {{  \mathbf{a} }} ( {{ \mathbf{b} }} \times {{ \mathbf{c} }} )"
                                            r"\rangle {}_1" ),
                cMathTex( r"=" ), cMathTex( r"\langle "
                                            r"(-I)^2 {{  \mathbf{a} }} ( {{ \mathbf{b} }} \wedge {{ \mathbf{c} }} )"
                                            r"\rangle {}_1" ),
                cMathTex( r"=" ), cMathTex( r"-\langle "
                                            r"{{  \mathbf{a} }} \cdot ( {{ \mathbf{b} }} \wedge {{ \mathbf{c} }} )"
                                            r"+ {{  \mathbf{a} }} \wedge ( {{ \mathbf{b} }} \wedge {{ \mathbf{c} }} )"
                                            r"\rangle {}_1" ),
                cMathTex( r"=" ), cMathTex( r" - {{ \mathbf{a} }}  \cdot ( {{ \mathbf{b} }} \wedge {{ \mathbf{c} }} ) " ) ]

        eq3 = [ cMathTex( r"({{  \mathbf{a} }} \times {{ \mathbf{b} }} ) \times {{ \mathbf{c} }}" ),
                cMathTex( r"=" ), cMathTex( r"-I (({{  \mathbf{a} }} \times {{ \mathbf{b} }}) \wedge {{ \mathbf{c} }})" ),
                cMathTex( r"=" ), cMathTex( r"\langle "
                                            r"-I ({{  \mathbf{a} }} \times {{ \mathbf{b} }}) {{ \mathbf{c} }}"
                                            r"\rangle {}_1" ),
                cMathTex( r"=" ), cMathTex( r"\langle "
                                            r"(-I)^2 ({{  \mathbf{a} }} \wedge {{ \mathbf{b} }} ) {{ \mathbf{c} }}"
                                            r"\rangle {}_1" ),
                cMathTex( r"=" ), cMathTex( r"-\langle "
                                            r"({{  \mathbf{a} }} \wedge {{ \mathbf{b} }}) \cdot {{ \mathbf{c} }}"
                                            r"+ ({{  \mathbf{a} }} \wedge {{ \mathbf{b} }}) \wedge {{ \mathbf{c} }}"
                                            r"\rangle {}_1" ),
                cMathTex( r"=" ), cMathTex( r" - ({{ \mathbf{a} }} \wedge {{ \mathbf{b} }}) \cdot {{ \mathbf{c} }} " ) ]

        eq[0].shift( 2.00 * UP + 2.00 * LEFT )
        self.play( Write( eq[0] ) )
        self.wait( 1 )
        i=1
        eq[i].next_to( eq[i-1], RIGHT )
        eq[i+1].next_to( eq[i], RIGHT )
        self.play( AnimationGroup( Write( eq[i] ), Write( eq[i+1] ) ) )
        self.wait( 1 )
        i=3
        for j in range(3):
            eq[i].next_to( eq[i-2], DOWN ).shift( 0.3 * DOWN )
            eq[i+1].next_to( eq[i], RIGHT )
            self.play( AnimationGroup( Write( eq[i] ), Write( eq[i+1] ) ) )
            self.wait( 1 )
            i += 2
        eqm = [ eq[7].copy().move_to( eq[1] ), eq[8].copy().next_to( eq[1], RIGHT ) ]
        self.play( AnimationGroup( ReplacementTransform( VGroup( eq[1], eq[2], eq[3], eq[4], eq[5], eq[6], eq[7], eq[8] ), VGroup( *eqm ) ) ) )
        self.wait( 1 )

        eq2[0].next_to( eq[0], DOWN ) #.shift( 0.50 * DOWN )
        self.play( Write( eq2[0] ) )
        self.wait( 1 )
        i=1
        eq2[i].next_to( eq2[i-1], RIGHT )
        eq2[i+1].next_to( eq2[i], RIGHT )
        self.play( AnimationGroup( Write( eq2[i] ), Write( eq2[i+1] ) ) )
        self.wait( 1 )
        i=3
        for j in range(4):
            eq2[i].next_to( eq2[i-2], DOWN ).shift( 0.3 * DOWN )
            eq2[i+1].next_to( eq2[i], RIGHT )
            self.play( AnimationGroup( Write( eq2[i] ), Write( eq2[i+1] ) ) )
            self.wait( 1 )
            i += 2
        eq2m = [ eq2[9].copy().move_to( eq2[1] ), eq2[10].copy().next_to( eq2[1], RIGHT ) ]
        self.play( AnimationGroup( ReplacementTransform( VGroup( eq2[1], eq2[2], eq2[3], eq2[4], eq2[5], eq2[6], eq2[7], eq2[8], eq2[9], eq2[10] ), VGroup( *eq2m ) ) ) )
        self.wait( 1 )

        eq3[0].next_to( eq2[0], DOWN ) #.shift( 0.50 * DOWN )
        self.play( Write( eq3[0] ) )
        self.wait( 1 )
        i=1
        eq3[i].next_to( eq3[i-1], RIGHT )
        eq3[i+1].next_to( eq3[i], RIGHT )
        self.play( AnimationGroup( Write( eq3[i] ), Write( eq3[i+1] ) ) )
        self.wait( 1 )
        i=3
        for j in range(4):
            eq3[i].next_to( eq3[i-2], DOWN ).shift( 0.3 * DOWN )
            eq3[i+1].next_to( eq3[i], RIGHT )
            self.play( AnimationGroup( Write( eq3[i] ), Write( eq3[i+1] ) ) )
            self.wait( 1 )
            i += 2
        eq3m = [ eq3[9].copy().move_to( eq3[1] ), eq3[10].copy().next_to( eq3[1], RIGHT ) ]
        self.play( AnimationGroup( ReplacementTransform( VGroup( eq3[1], eq3[2], eq3[3], eq3[4], eq3[5], eq3[6], eq3[7], eq3[8], eq3[9], eq3[10] ), VGroup( *eq3m ) ) ) )
        self.wait( 1 )



        self.wait( 5 )
        fadeall( self )

# vim: et sw=4 ts=4
