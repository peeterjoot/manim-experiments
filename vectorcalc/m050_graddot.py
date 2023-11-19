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
                [ #cMathTex( r"=" ),
                  #cMathTex( r"(\boldsymbol{\nabla} \wedge {{ \mathbf{a} }}) \cdot {{ \mathbf{b} }}" ],
                  cMathTex( r"+ (\boldsymbol{\nabla} \wedge {{ \mathbf{b} }}) \cdot {{ \mathbf{a} }}" ) ],
                  #cMathTex( r"+ ({{ \mathbf{a} }} \cdot \boldsymbol{\nabla}) {{ \mathbf{b} }}" ),
                  #cMathTex( r"+ ({{ \mathbf{b} }} \cdot \boldsymbol{\nabla}) {{ \mathbf{a} }}" ),
                [ cMathTex( r"=" ),
                  cMathTex( r"{{ \mathbf{b} }} \times (\boldsymbol{\nabla} \times {{ \mathbf{a} }})" ),
                  cMathTex( r"+ {{ \mathbf{a} }} \times (\boldsymbol{\nabla} \times {{ \mathbf{b} }})" ),
                  cMathTex( r"+ ({{ \mathbf{a} }} \cdot \boldsymbol{\nabla}) {{ \mathbf{b} }}" ),
                  cMathTex( r"+ ({{ \mathbf{b} }} \cdot \boldsymbol{\nabla}) {{ \mathbf{a} }}" ) ] ]

        aligned1( self, eq5[0], eq2[1][0], 0.3 * DOWN, 1 )
        self.wait( 1 )
        eq5[1][0].move_to( eq5[0][2] )
        self.play( ReplacementTransform( eq5[0][2], eq5[1][0] ) )
        #aligned1( self, eq5[1], eq5[0][0], 0.3 * DOWN, 1 )
        self.wait( 1 )
        self.play( AnimationGroup( Indicate( eq5[0][1] ), Indicate( eq5[1][0] ) ) )
        self.wait( 5 )
        aligned1( self, eq5[2], eq5[0][0], 0.3 * DOWN, 1 )
        self.wait( 1 )

        self.wait( 5 )
        fadeall( self )

# vim: et sw=4 ts=4
