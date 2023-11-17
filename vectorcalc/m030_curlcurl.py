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

        g1 = VGroup( *eq[0] )
        g2 = VGroup( *eq[1] )
        g3 = VGroup( *eq[2] )
        self.play( AnimationGroup( g1.animate.shift(5.0 * LEFT + 0 * DOWN),
                                   g2.animate.shift(5.0 * LEFT + 0 * DOWN),
                                   g3.animate.shift(5.0 * LEFT + 0 * DOWN) ), run_time=3, rate_func=linear )

        eq2m = [ cMathTex( r"f \in \mathbb{R}" ),
                 cMathTex( r"0" ),
                 cMathTex( r"=" ), cMathTex( r"\boldsymbol{\nabla} \wedge ( \boldsymbol{\nabla} \wedge f )" ),
                 cMathTex( r"=" ), cMathTex( r"\boldsymbol{\nabla} \wedge ( \boldsymbol{\nabla} f )" ),
                 cMathTex( r"=" ), cMathTex( r"I (\boldsymbol{\nabla} \times ( \boldsymbol{\nabla} f ))" ) ]

        eq2m[0].next_to( title, DOWN )
        eq2m[1].next_to( eq2m[0], DOWN )
        eq2m[2].next_to( eq2m[1], RIGHT )
        eq2m[3].next_to( eq2m[2], RIGHT )
        self.play( Write( eq2m[0] ) )
        self.wait( 1 )
        self.play( Write( eq2m[1] ) )
        self.play( Write( eq2m[2] ) )
        self.play( Write( eq2m[3] ) )
        self.wait( 1 )
        ref = eq2m[2]
        j = 4
        for i in range(2):
            eq2m[j].next_to( ref, DOWN ).shift( 0.3 * DOWN )
            eq2m[j+1].next_to( eq2m[j], RIGHT )
            for k in range(2):
                self.play( Write( eq2m[j+k] ) )
            ref = eq2m[j]
            self.wait( 1 )
            j += 2
        self.play( Indicate( g1 ) )
        self.wait( 5 )
        self.play( FadeOut( VGroup( *eq2m ) ) )
        self.wait( 1 )

        eq3m = [ cMathTex( r"{{ \mathbf{f} }} \in \mathbb{R}^N" ),
                 cMathTex( r"0" ),
                 cMathTex( r"=" ), cMathTex( r"\boldsymbol{\nabla} \wedge ( \boldsymbol{\nabla} \wedge {{ \mathbf{f} }})" ),
                 cMathTex( r"=" ), cMathTex( r"I (\boldsymbol{\nabla} \cdot ( \boldsymbol{\nabla} \times {{ \mathbf{f} }}))" ) ]

        eq3m[0].next_to( title, DOWN )
        eq3m[1].next_to( eq3m[0], DOWN )
        eq3m[2].next_to( eq3m[1], RIGHT )
        eq3m[3].next_to( eq3m[2], RIGHT )
        self.play( Write( eq3m[0] ) )
        self.wait( 1 )
        self.play( Write( eq3m[1] ) )
        self.play( Write( eq3m[2] ) )
        self.play( Write( eq3m[3] ) )
        self.wait( 1 )
        ref = eq3m[2]
        j = 4
        for i in range(1):
            eq3m[j].next_to( ref, DOWN ).shift( 0.3 * DOWN )
            eq3m[j+1].next_to( eq3m[j], RIGHT )
            for k in range(2):
                self.play( Write( eq3m[j+k] ) )
            ref = eq3m[j]
            self.wait( 1 )
            j += 2
        self.play( Indicate( g2 ) )
        self.wait( 5 )
        self.play( FadeOut( VGroup( *eq3m ) ) )
        self.wait( 1 )

        eq2 = [ cMathTex( r"f \in \mathbb{R}" ),
                cMathTex( r"\boldsymbol{\nabla} \wedge ( \boldsymbol{\nabla} \wedge f )" ),
                cMathTex( r"=" ), cMathTex( r"\boldsymbol{\nabla} \wedge ( \boldsymbol{\nabla} f )" ),
                cMathTex( r"=" ), cMathTex( r"\sum_{ij} ({{ \mathbf{e} }}_{i} \wedge {{ \mathbf{e} }}_{j}) { \partial^2 f \over { \partial x_i \partial x_j} }" ),
                cMathTex( r"=" ), cMathTex( r"0" ) ]

        eq2[0].next_to( title, DOWN )
        eq2[1].next_to( eq2[0], DOWN )
        eq2[2].next_to( eq2[1], RIGHT )
        eq2[3].next_to( eq2[2], RIGHT )
        self.play( Write( eq2[0] ) )
        self.wait( 1 )
        self.play( Write( eq2[1] ) )
        self.play( Write( eq2[2] ) )
        self.play( Write( eq2[3] ) )
        self.wait( 1 )
        ref = eq2[2]
        j = 4
        for i in range(2):
            eq2[j].next_to( ref, DOWN ).shift( 0.5 * DOWN )
            eq2[j+1].next_to( eq2[j], RIGHT )
            for k in range(2):
                self.play( Write( eq2[j+k] ) )
            ref = eq2[j]
            self.wait( 1 )
            j += 2
        self.play( Indicate( g3 ) )
        self.wait( 5 )
        self.play( FadeOut( VGroup( *eq2 ) ) )
        self.wait( 1 )

        eq3 = [ cMathTex( r"{{ \mathbf{f} }} \in \mathbb{R}^N" ),
                cMathTex( r"\boldsymbol{\nabla} \wedge ( \boldsymbol{\nabla} \wedge {{ \mathbf{f} }} )" ),
                cMathTex( r"=" ), cMathTex( r"\sum_{ij} ({{ \mathbf{e} }}_{i} \wedge {{ \mathbf{e} }}_{j} \wedge {{ \mathbf{e} }}_{k}) { \partial^2 f_k \over { \partial x_i \partial x_j} }" ),
                cMathTex( r"=" ), cMathTex( r"0" ) ]

        eq3[0].next_to( title, DOWN )
        eq3[1].next_to( eq3[0], DOWN )
        eq3[2].next_to( eq3[1], RIGHT )
        eq3[3].next_to( eq3[2], RIGHT )
        self.play( Write( eq3[0] ) )
        self.wait( 1 )
        self.play( Write( eq3[1] ) )
        self.play( Write( eq3[2] ) )
        self.play( Write( eq3[3] ) )
        self.wait( 1 )
        ref = eq3[2]
        j = 4
        for i in range(1):
            eq3[j].next_to( ref, DOWN ).shift( 0.5 * DOWN )
            eq3[j+1].next_to( eq3[j], RIGHT )
            for k in range(2):
                self.play( Write( eq3[j+k] ) )
            ref = eq3[j]
            self.wait( 1 )
            j += 2
        self.play( Indicate( g3 ) )
        self.wait( 5 )
        self.play( FadeOut( VGroup( *eq3 ) ) )
        self.wait( 1 )


        self.wait( 5 )
        fadeall( self )

# vim: et sw=4 ts=4
