from mycolors import *

# write just the "&= foo \\" line for aligned:
def aligned1( self, eq, ref, sh, w ):
    eq[0].next_to( ref, DOWN ).shift( sh )
    elen = len(eq)
    for i in range(elen):
        if i + 1 < elen:
            eq[i+1].next_to( eq[i], RIGHT )
        self.play( Write( eq[i] ) )
    self.wait( w )

# Model this common aligned construct:
#
# \begin{aligned}
# a &= b0 + b1 \\
#   &= c0 + c1 + c2
#   &= d0 + d1 + d2 + d3
# \end{aligned}
#
# The input would look like:
#
# eq = [ [ MathTex( r"a" )
#          MathTex( r"=" )
#          MathTex( r"b0" ), MathTex( r"+ b1" ) ],
#        [ MathTex( r"=" )
#          MathTex( r"c0" ), MathTex( r"+ c1" ), MathTex( r"+ c2" ) ],
#        [ MathTex( r"=" )
#          MathTex( r"d0" ), MathTex( r"+ d1" ), MathTex( r"+ d2" ), MathTex( r"+ d3" ) ] ]
#
# The stuff after the = sign doesn't have to be split up, but it can be (to allow for easy Indicate() or transformation if desired.)
#
def aligned( self, eq, ref, ish, sh, w1, w2 ):
    eq[0][1].next_to( ref, DOWN ).shift( ish )
    eq[0][0].next_to( eq[0][1], LEFT )
    eq[0][2].next_to( eq[0][1], RIGHT )
    elen = len(eq[0])
    for i in range(elen):
        self.play( Write( eq[0][i] ) )
    ref = eq[0][1]
    self.wait( w1 )
    alen = len(eq)
    for j in range(alen-1):
        #eq[j+1][0].next_to( ref, DOWN ).shift( sh )
        #elen = len(eq[j+1])
        #for i in range(elen):
        #    if i + 1 < elen:
        #        eq[j+1][i+1].next_to( eq[j+1][i], RIGHT )
        #    self.play( Write( eq[j+1][i] ) )
        #self.wait( w2 )
        aligned1( self, eq[j+1], ref, sh, w2 )
        ref = eq[j+1][0]


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

        aligned( self, eq, title, 4.0 * LEFT + 0.2 * DOWN, 0.3 * DOWN, 1, 1 )

        self.play( FadeOut( *eq[0] ) )
        self.wait( 1 )

        eq2 = [ [ cMathTex( r"\boldsymbol{\nabla} ({{ \mathbf{a} }} \cdot {{ \mathbf{b} }})" ),
                  cMathTex( r"=" ),
                  cMathTex( r"\langle \boldsymbol{\nabla} ({{ \mathbf{a} }} {{ \mathbf{b} }} - {{ \mathbf{a} }} \wedge {{ \mathbf{b} }}) \rangle {}_1" ) ],
                [ cMathTex( r"=" ),
                  cMathTex( r"\langle \boldsymbol{\nabla} {{ \mathbf{a} }} {{ \mathbf{b} }} \rangle {}_1 - \boldsymbol{\nabla} \cdot ({{ \mathbf{a} }} \wedge {{ \mathbf{b} }})" ) ] ]

        aligned( self, eq2, title, 4.0 * LEFT + 0.2 * DOWN, 0.3 * DOWN, 1, 1 )

        eq3 = [ [ cMathTex( r"\langle \boldsymbol{\nabla} {{ \mathbf{a} }} {{ \mathbf{b} }} \rangle {}_1" ),
                  cMathTex( r"=" ),
                  cMathTex( r"\langle \boldsymbol{\nabla}' {{ \mathbf{a} }}' {{ \mathbf{b} }}"
                            r"+ \boldsymbol{\nabla}' {{ \mathbf{a} }} {{ \mathbf{b} }}' \rangle {}_1" ) ],
                [ cMathTex( r"=" ),
                  cMathTex( r"\langle (\boldsymbol{\nabla} \cdot {{ \mathbf{a} }} + \boldsymbol{\nabla} \wedge {{ \mathbf{a} }}) {{ \mathbf{b} }}"
                            r"- {{ \mathbf{a} }} \boldsymbol{\nabla}' {{ \mathbf{b} }}' + 2 ({{ \mathbf{a} }} \cdot \boldsymbol{\nabla}) {{ \mathbf{b} }} \rangle {}_1" ) ],
                [ cMathTex( r"=" ),
                  cMathTex( r"(\boldsymbol{\nabla} \cdot {{ \mathbf{a} }}) {{ \mathbf{b} }}" ), # I1
                  cMathTex( r" + (\boldsymbol{\nabla} \wedge {{ \mathbf{a} }}) \cdot {{ \mathbf{b} }}" ),
                  cMathTex( r"- {{ \mathbf{a} }}(\boldsymbol{\nabla} \cdot {{ \mathbf{b} }})" ), # I1
                  cMathTex( r"- {{ \mathbf{a} }} \cdot (\boldsymbol{\nabla} \wedge {{ \mathbf{b} }})" ) ],
                [ cMathTex( r"+" ),
                  cMathTex( r"2 ({{ \mathbf{a} }} \cdot \boldsymbol{\nabla}) {{ \mathbf{b} }}" ) ] ] # I2

        aligned( self, eq3, eq2[1][0], 0.0 * LEFT + 0.2 * DOWN, 0.3 * DOWN, 1, 1 )

        eq4 = [ [ cMathTex( r"\boldsymbol{\nabla} \cdot ({{ \mathbf{a} }} \wedge {{ \mathbf{b} }})" ),
                  cMathTex( r"=" ),
                  cMathTex( r"\boldsymbol{\nabla}' \cdot ({{ \mathbf{a} }}' \wedge {{ \mathbf{b} }})"
                            r"+\boldsymbol{\nabla}' \cdot ({{ \mathbf{a} }} \wedge {{ \mathbf{b} }}')" ) ],
                [ cMathTex( r"=" ),
                  cMathTex( r"(\boldsymbol{\nabla} \cdot {{ \mathbf{a} }}) {{ \mathbf{b} }}" ), # I1
                  cMathTex( r"- ({{ \mathbf{b} }} \cdot \boldsymbol{\nabla}) {{ \mathbf{a} }}" ),
                  cMathTex( r"-(\boldsymbol{\nabla} \cdot {{ \mathbf{b} }}) {{ \mathbf{a} }}" ), # I1
                  cMathTex( r"+ ({{ \mathbf{a} }} \cdot \boldsymbol{\nabla}) {{ \mathbf{b} }}" ) ] ] # I2

        aligned( self, eq4, eq3[3][0], 0.0 * LEFT + 0.2 * DOWN, 0.3 * DOWN, 1, 1 )

        self.play( Indicate( VGroup( eq3[2][1], eq3[2][3], eq4[1][1], eq4[1][3] ) ) )
        self.wait( 5 )

        self.play( Indicate( VGroup( eq3[3][1], eq4[1][4] ) ) )
        self.wait( 5 )
        self.play( FadeOut( *eq3[0], *eq3[1], *eq3[2], *eq3[3], *eq4[0], *eq4[1] ) )
        self.wait( 1 )

        eq5 = [ [ cMathTex( r"=" ),
                  cMathTex( r"(\boldsymbol{\nabla} \wedge {{ \mathbf{a} }}) \cdot {{ \mathbf{b} }}" ),
                  cMathTex( r"- {{ \mathbf{a} }} \cdot (\boldsymbol{\nabla} \wedge {{ \mathbf{b} }})" ),
                  cMathTex( r"+ ({{ \mathbf{a} }} \cdot \boldsymbol{\nabla}) {{ \mathbf{b} }}" ),
                  cMathTex( r"+ ({{ \mathbf{b} }} \cdot \boldsymbol{\nabla}) {{ \mathbf{a} }}" ) ],
                [ cMathTex( r"=" ),
                  cMathTex( r"(\boldsymbol{\nabla} \wedge {{ \mathbf{a} }}) \cdot {{ \mathbf{b} }}" ),
                  cMathTex( r"+ (\boldsymbol{\nabla} \wedge {{ \mathbf{b} }}) \cdot \Ba" ),
                  cMathTex( r"+ ({{ \mathbf{a} }} \cdot \boldsymbol{\nabla}) {{ \mathbf{b} }}" ),
                  cMathTex( r"+ ({{ \mathbf{b} }} \cdot \boldsymbol{\nabla}) {{ \mathbf{a} }}" ) ] ],
                [ cMathTex( r"=" ),
                  cMathTex( r"\Bb \cross (\boldsymbol{\nabla} \cross {{ \mathbf{a} }})" ),
                  cMathTex( r"+ \Ba \cross (\boldsymbol{\nabla} \cross {{ \mathbf{b} }})" ),
                  cMathTex( r"+ ({{ \mathbf{a} }} \cdot \boldsymbol{\nabla}) {{ \mathbf{b} }}" ),
                  cMathTex( r"+ ({{ \mathbf{b} }} \cdot \boldsymbol{\nabla}) {{ \mathbf{a} }}" ) ] ]

        aligned1( self, eq5[0], eq2[1][0], 0.3 * DOWN, 1 )
        self.wait( 1 )

        self.wait( 5 )
        fadeall( self )

# vim: et sw=4 ts=4
