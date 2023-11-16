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

        #MathTex( r"  \mathbf{a}  \times (  \mathbf{b}  \times  \mathbf{c}  ) = -  \mathbf{a}  \cdot (  \mathbf{b}  \wedge  \mathbf{c}  ) " ),
        #cMathTex( r" ( {{ \mathbf{a} }} \times {{ \mathbf{b} }} ) \times {{ \mathbf{c} }} = - ( {{ \mathbf{a} }} \wedge {{ \mathbf{b} }} ) \cdot {{ \mathbf{c} }}" ),

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

        self.wait( 5 )
        fadeall( self )

# vim: et sw=4 ts=4
