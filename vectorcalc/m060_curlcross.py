from mycolors import *

class m060_curlcross( Scene ):
    def construct( self ):

        title = Text( "Curl of a cross product (Jackson)" )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.play( FadeIn( title ) )
        self.wait( 1 )

        eq = [ [ cMathTex( r"\boldsymbol{\nabla} \times ({{ \mathbf{a} }} \times {{ \mathbf{b} }})" ),
                 cMathTex( r"=" ),
                 cMathTex( r"-I(\boldsymbol{\nabla} \wedge ({{ \mathbf{a} }} \times {{ \mathbf{b} }}))" ) ],
               [ cMathTex( r"=" ),
                 cMathTex( r"\langle -I(\boldsymbol{\nabla} \wedge ({{ \mathbf{a} }} \times {{ \mathbf{b} }})) \rangle {}_1" ) ],
               [ cMathTex( r"=" ),
                 cMathTex( r"\langle -I(\boldsymbol{\nabla} ({{ \mathbf{a} }} \times {{ \mathbf{b} }})) \rangle {}_1" ) ],
               [ cMathTex( r"=" ),
                 cMathTex( r"\langle (-I)^2(\boldsymbol{\nabla} ({{ \mathbf{a} }} \wedge {{ \mathbf{b} }})) \rangle {}_1" ) ],
               [ cMathTex( r"=" ),
                 cMathTex( r"-\boldsymbol{\nabla} \cdot ({{ \mathbf{a} }} \wedge {{ \mathbf{b} }})" ) ] ]

        aligned( self, eq, title, 0.0 * LEFT + 0.2 * DOWN, 0.3 * DOWN, 1, 1 )
        self.wait( 5 )
        eqg = eq[4][1].copy().next_to( eq[0][1], RIGHT )
        self.play( AnimationGroup( FadeOut( *eq[1], *eq[2], *eq[3], *eq[4] ), ReplacementTransform( eq[0][2], eqg ) ) )
        #self.play( FadeOut( *eq[0] ) )
        self.wait( 1 )

        eq2 = [ [ cMathTex( r"\boldsymbol{\nabla} \cdot ({{ \mathbf{a} }} \wedge {{ \mathbf{b} }})" ),
                  cMathTex( r"=" ),
                  cMathTex( r"\boldsymbol{\nabla}' \cdot ({{ \mathbf{a} }}' \wedge {{ \mathbf{b} }})" ),
                  cMathTex( r"+\boldsymbol{\nabla}' \cdot ({{ \mathbf{a} }} \wedge {{ \mathbf{b} }}')" ) ],
                [ cMathTex( r"=" ),
                  cMathTex( r"(\boldsymbol{\nabla} \cdot {{ \mathbf{a} }}) {{ \mathbf{b} }}" ),
                  cMathTex( r"-({{ \mathbf{b} }} \cdot \boldsymbol{\nabla}) {{ \mathbf{a} }}" ),
                  cMathTex( r"+({{ \mathbf{a} }} \cdot \boldsymbol{\nabla}) {{ \mathbf{b} }}" ),
                  cMathTex( r"-(\boldsymbol{\nabla} \cdot {{ \mathbf{b} }}) {{ \mathbf{a} }}" ) ] ]
        aligned( self, eq2, eq[0][1], 3.0 * LEFT + 0.6 * DOWN, 0.3 * DOWN, 1, 1 )

        self.wait( 5 )
        fadeall( self )

# vim: et sw=4 ts=4
