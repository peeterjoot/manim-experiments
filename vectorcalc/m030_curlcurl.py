from mycolors import *

class m030_curlcurl( Scene ):
    def construct( self ):

        title = Text( "Repeated curl." )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.play( FadeIn( title ) )
        self.wait( 1 )

        eq = [ [ cMathTex( r"\boldsymbol{\nabla} \times ( \boldsymbol{\nabla} f )"), cMathTex( " = "), cMathTex(" 0 " ) ],
               [ cMathTex( r"\boldsymbol{\nabla} \cdot ( \boldsymbol{\nabla} \times {{ \mathbf{f} }} )"), cMathTex( "=" ), cMathTex( r"0" ) ],
               [ cMathTex( r"\boldsymbol{\nabla} \wedge ( \boldsymbol{\nabla} \wedge A )"), cMathTex( "=" ), cMathTex( r"0" ) ] ]

        ref = title
        for i in range(3):
            eq[i][0].next_to( ref, DOWN )
            eq[i][1].next_to( eq[i][0], RIGHT )
            eq[i][2].next_to( eq[i][1], RIGHT )
            for j in range(3):
                self.play( Write( eq[i][j] ) )
            ref = eq[i][0]
            self.wait( 1 )

        g = VGroup( *eq[0] )
        g += VGroup( *eq[1] )
        g += VGroup( *eq[2] )
        self.play( g.animate.shift(5.0 * LEFT + 0 * DOWN), run_time=3, rate_func=linear ) 

        eq2m = [ cMathTex( r"0" ),
                 cMathTex( r"=" ), cMathTex( r"\boldsymbol{\nabla} \wedge ( \boldsymbol{\nabla} \wedge f )" ),
                 cMathTex( r"=" ), cMathTex( r"\boldsymbol{\nabla} \wedge ( \boldsymbol{\nabla} f )" ),
                 cMathTex( r"=" ), cMathTex( r"I (\boldsymbol{\nabla} \times ( \boldsymbol{\nabla} f ))" ) ]

        eq3m = [ cMathTex( r"0" ),
                 cMathTex( r"=" ), cMathTex( r"\boldsymbol{\nabla} \wedge ( \boldsymbol{\nabla} \wedge {{ \mathbf{f} }})" ),
                 cMathTex( r"=" ), cMathTex( r"I (\boldsymbol{\nabla} \cdot ( \boldsymbol{\nabla} \times {{ \mathbf{f} }}))" ) ]

        eq2 = [ cMathTex( r"f \in \mathbb{R}" ),
                cMathTex( r"\boldsymbol{\nabla} \wedge ( \boldsymbol{\nabla} \wedge f )" ),
                cMathTex( r"=" ), cMathTex( r"\boldsymbol{\nabla} \wedge ( \boldsymbol{\nabla} f )" ),
                cMathTex( r"=" ), cMathTex( r"\sum_{ij} ({{ \mathbf{e} }}_{i} \wedge {{ \mathbf{e} }}_{j}) { \partial^2 f \over { \partial x_i \partial x_j} }" ),
                cMathTex( r"=" ), cMathTex( r"0" ) ]

        eq3 = [ cMathTex( r"{{ \mathbf{f} }} \in \mathbb{R}^N" ),
                cMathTex( r"\boldsymbol{\nabla} \wedge ( \boldsymbol{\nabla} \wedge {{ \mathbf{f} }} )" ),
                cMathTex( r"=" ), cMathTex( r"\sum_{ij} ({{ \mathbf{e} }}_{i} \wedge {{ \mathbf{e} }}_{j}) { \partial^2 f_j \over { \partial x_i \partial x_j} }" ),
                cMathTex( r"=" ), cMathTex( r"0" ) ]

        self.wait( 5 )
        fadeall( self )

# vim: et sw=4 ts=4
