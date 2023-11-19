from mycolors import *

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
        eq[j+1][0].next_to( ref, DOWN ).shift( sh )
        elen = len(eq[j+1])
        for i in range(elen):
            if i + 1 < elen:
                eq[j+1][i+1].next_to( eq[j+1][i], RIGHT )
            self.play( Write( eq[j+1][i] ) )
        self.wait( w2 )
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
                            r"- {{ \mathbf{a} }} \boldsymbol{\nabla}' {{ \mathbf{b} }}' + 2 ({{ \mathbf{a} }} \cdot \boldsymbol{\nabla}) {{ \mathbf{b} }} \rangle {}_1" ) ],
                [ cMathTex( r"=" ),
                  cMathTex( r"(\boldsymbol{\nabla} \cdot {{ \mathbf{a} }}) {{ \mathbf{b} }} + (\boldsymbol{\nabla} \wedge {{ \mathbf{a} }}) \cdot {{ \mathbf{b} }}"
                            r"- {{ \mathbf{a} }}(\boldsymbol{\nabla} \cdot {{ \mathbf{b} }})"
                            r"- {{ \mathbf{a} }} \cdot (\boldsymbol{\nabla} \wedge {{ \mathbf{b} }})" ) ],
                [ cMathTex( r"\quad+" ),
                  cMathTex( r"2 ({{ \mathbf{a} }} \cdot \boldsymbol{\nabla}) {{ \mathbf{b} }}" ) ] ]
        eq3[0][1].next_to( eq2[1][0], DOWN ).shift( 0.0 * LEFT + 0.2 * DOWN )
        eq3[0][0].next_to( eq3[0][1], LEFT )
        eq3[0][2].next_to( eq3[0][1], RIGHT )
        for i in range(3):
            self.play( Write( eq3[0][i] ) )
        ref = eq3[0][1]
        self.wait( 1 )
        for j in range(3):
            eq3[j+1][0].next_to( ref, DOWN ).shift( 0.3 * DOWN )
            eq3[j+1][1].next_to( eq3[j+1][0], RIGHT )
            for i in range(2):
                self.play( Write( eq3[j+1][i] ) )
            self.wait( 1 )
            ref = eq3[j+1][0]

        eq4 = [ [ cMathTex( r"\boldsymbol{\nabla} \cdot ({{ \mathbf{a} }} \wedge {{ \mathbf{b} }})" ),
                  cMathTex( r"=" ),
                  cMathTex( r"\boldsymbol{\nabla}' \cdot ({{ \mathbf{a} }}' \wedge {{ \mathbf{b} }})"
                            r"+\boldsymbol{\nabla}' \cdot ({{ \mathbf{a} }} \wedge {{ \mathbf{b} }}')" ) ],
                [ cMathTex( r"=" ),
                  cMathTex( r"(\boldsymbol{\nabla} \cdot {{ \mathbf{a} }}) {{ \mathbf{b} }}" ),
                  cMathTex( r"- ({{ \mathbf{b} }} \cdot \boldsymbol{\nabla}) {{ \mathbf{a} }}" ),
                  cMathTex( r"-(\boldsymbol{\nabla} \cdot {{ \mathbf{b} }}) {{ \mathbf{a} }}" ),
                  cMathTex( r"+ ({{ \mathbf{a} }} \cdot \boldsymbol{\nabla}) {{ \mathbf{b} }}" ) ] ]

        aligned( self, eq4, eq3[3][0], 0.0 * LEFT + 0.2 * DOWN, 0.3 * DOWN, 1, 1 )
        #ref = eq3[3][0]
        #eq4[0][1].next_to( ref, DOWN ).shift( 0.0 * LEFT + 0.2 * DOWN )
        #eq4[0][0].next_to( eq4[0][1], LEFT )
        #eq4[0][2].next_to( eq4[0][1], RIGHT )
        #for i in range(3):
        #    self.play( Write( eq4[0][i] ) )
        #ref = eq4[0][1]
        #self.wait( 1 )
        #alen = len(eq4):
        #for j in range(alen-1):
        #    eq4[j+1][0].next_to( ref, DOWN ).shift( 0.3 * DOWN )
        #    elen = len(eq4[j+1])
        #    for i in range(elen):
        #        if i + 1 < elen:
        #            eq4[j+1][i+1].next_to( eq4[j+1][i], RIGHT )
        #        self.play( Write( eq4[j+1][i] ) )
        #    self.wait( 1 )
        #    ref = eq4[j+1][0]


        self.wait( 5 )
        fadeall( self )

# vim: et sw=4 ts=4
