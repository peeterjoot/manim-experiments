from mycolors import *

class m070_gradientexamples( Scene ):
    def construct( self ):

        title = Text( "Vector derivative examples." )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.play( FadeIn( title ) )
        self.wait( 1 )

        eq = [ cMathTex( r"{{ \mathbf{x} }}(u,v) = (u + v) {{ \mathbf{e} }}_1 + v {{ \mathbf{e} }}_3" ),
               cMathTex( r"{{ \mathbf{x} }}_1 = {{ \mathbf{e} }}_1, \quad {{ \mathbf{x} }}_2 = {{ \mathbf{e} }}_1 + {{ \mathbf{e} }}_3, \quad {{ \mathbf{x} }}_1 \wedge {{ \mathbf{x} }}_2 = {{ \mathbf{e} }}_{13}" ) ]
        eq2 = [ cMathTex( r"{{ \mathbf{x} }}^1 = {{ \mathbf{x} }}_2 \cdot {{ \mathbf{e} }}_{31}" ),
                cMathTex( r"= ({{ \mathbf{e} }}_1 + {{ \mathbf{e} }}_3) \cdot {{ \mathbf{e} }}_{31}" ),
                cMathTex( r"= -{{ \mathbf{e} }}_3 + {{ \mathbf{e} }}_1" ) ]
        eq3 = [ cMathTex( r"{{ \mathbf{x} }}^2 = - {{ \mathbf{x} }}_1 \cdot {{ \mathbf{e} }}_{31}" ),
                cMathTex( r"= - {{ \mathbf{e} }}_1 \cdot {{ \mathbf{e} }}_{31}" ),
                cMathTex( r"= {{ \mathbf{e} }}_3" ) ]
        eq4 = cMathTex( r"\boldsymbol{\partial} = ({{ \mathbf{e} }}_1 -{{ \mathbf{e} }}_3) { \partial \over { \partial u } } + {{ \mathbf{e} }}_3 { \partial \over { \partial v } }" )

        eq[0].shift( 2.00 * UP + 0.00 * RIGHT )
        self.play( Write( eq[0] ) )
        self.wait( 1 )
        for i in range(1):
            sh = 0.80 * DOWN
            if i == 0:
                sh += 0.00 * DOWN + 2.00 * LEFT
            write_aligned( self, eq[i], eq[i+1], sh, None )
            self.wait( 1 )

        eq2[0].move_to( eq[1] ).shift( 1.00 * DOWN + 4.00 * LEFT )
        self.play( Write( eq2[0] ) )
        self.wait( 1 )
        for i in range(2):
            sh = 1.00 * DOWN
            if i == 0:
                sh += 0.00 * DOWN + 0.32 * RIGHT
            write_aligned( self, eq2[i], eq2[i+1], sh, None )
            self.wait( 1 )

        eq3[0].move_to( eq2[0], RIGHT ).shift( 6.00 * RIGHT )
        self.play( Write( eq3[0] ) )
        self.wait( 1 )
        for i in range(2):
            sh = 1.00 * DOWN
            if i == 0:
                sh += 0.00 * DOWN + 0.32 * RIGHT
            write_aligned( self, eq3[i], eq3[i+1], sh, None )
            self.wait( 1 )

        eq4.move_to( eq3[2], RIGHT ).shift( 1.00 * DOWN )
        self.play( Write( eq4 ) )
        self.wait( 1 )
        self.play( AnimationGroup( FadeOut( VGroup( *eq ) ),
                                   FadeOut( VGroup( *eq2 ) ),
                                   FadeOut( VGroup( *eq3 ) ),
                                   FadeOut( eq4 ) ) )


        ceq = [ cMathTex( r"{{ \mathbf{x} }}(r, \theta) = r {{ \mathbf{e} }}_1 e^{j \theta}, \quad j = {{ \mathbf{e} }}_{13}" ),
                cMathTex( r"{{ \mathbf{x} }}_1 = {{ \mathbf{e} }}_1 e^{j \theta}, \quad {{ \mathbf{x} }}_2 = r {{ \mathbf{e} }}_3 e^{j \theta}, \quad {{ \mathbf{x} }}_1 \cdot {{ \mathbf{x} }}_2 = 0" ) ]
        ceq2 = [ cMathTex( r"{{ \mathbf{x} }}^1 = { 1 \over {{ \mathbf{x} }}_1" ),
                 cMathTex( r"= e^{-j \theta} {{ \mathbf{e} }}_1" ) ]
        ceq3 = [ cMathTex( r"{{ \mathbf{x} }}^2 = { 1 \over {{ \mathbf{x} }}_2" ),
                 cMathTex( r"= { 1 \over r } e^{-j \theta} {{ \mathbf{e} }}_3" ) ]
        ceq4 = [ cMathTex( r"\boldsymbol{\partial} = e^{-j \theta} \Bigl( {{ \mathbf{e} }}_1 { \partial \over { \partial r } } + { {{ \mathbf{e} }}_3 \over r } { \partial \over { \partial \theta } } \Bigr)" ) ]

        ceq[0].shift( 2.00 * UP + 0.00 * RIGHT )
        self.play( Write( ceq[0] ) )
        self.wait( 1 )
        for i in range(1):
            sh = 0.80 * DOWN
            if i == 0:
                sh += 0.00 * DOWN + 2.00 * LEFT
            write_aligned( self, ceq[i], ceq[i+1], sh, None )
            self.wait( 1 )

        ceq2[0].move_to( ceq[1] ).shift( 1.00 * DOWN + 4.00 * LEFT )
        self.play( Write( ceq2[0] ) )
        self.wait( 1 )
        for i in range(1):
            sh = 1.50 * DOWN
            if i == 0:
                sh += 0.00 * DOWN + 0.32 * RIGHT
            write_aligned( self, ceq2[i], ceq2[i+1], sh, None )
            self.wait( 1 )

        ceq3[0].move_to( ceq2[0], RIGHT ).shift( 6.00 * RIGHT )
        self.play( Write( ceq3[0] ) )
        self.wait( 1 )
        for i in range(1):
            sh = 1.50 * DOWN
            if i == 0:
                sh += 0.00 * DOWN + 0.32 * RIGHT
            write_aligned( self, ceq3[i], ceq3[i+1], sh, None )
            self.wait( 1 )

        ceq4[0].move_to( ceq3[1], RIGHT ).shift( 1.30 * DOWN + 1.00 * LEFT )
        self.play( Write( ceq4[0] ) )
        self.wait( 1 )

        self.wait( 5 )
        fadeall( self )

# vim: et sw=4 ts=4
