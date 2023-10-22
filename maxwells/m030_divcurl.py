from mycolors import *
class m030_divcurl( Scene ):
    def construct( self ):

        title = Text( "Grouping Divs and Curls" )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.play( FadeIn( title ) )
        self.wait( 5 )

        eq0 = [ MathTex( r" \mathbf{X} \mathbf{Y} = \mathbf{X} \cdot \mathbf{Y} + \mathbf{X} \wedge \mathbf{Y}" ),
                MathTex( r"                       = \mathbf{X} \cdot \mathbf{Y} + I ( \mathbf{X} \times \mathbf{Y} )" ),
                MathTex( r" \boldsymbol{\nabla} {{ \mathbf{Y} }} = \boldsymbol{\nabla} \cdot {{ \mathbf{Y} }}  + I (  \boldsymbol{\nabla} \times {{ \mathbf{Y} }} )" ) ]
        eq0[0].shift( 1.50 * UP + 0 * LEFT )
        self.play( Write( eq0[0] ) )
        self.wait( 5 )
        i = 0
        sh = 1.00 * DOWN + 1.00 * RIGHT
        write_aligned( self, eq0[i], eq0[i+1], sh, None )
        self.wait( 5 )
        i = 1
        sh = 1.00 * DOWN + 1.10 * LEFT
        write_aligned( self, eq0[i], eq0[i+1], sh, None )
        self.wait( 5 )
        self.play( FadeOut( VGroup(*eq0) ) )
        self.wait( 5 )

        eq = [ cMathTex( r" \boldsymbol{\nabla} \cdot {{ \mathbf{E} }}  = { \rho \over \epsilon }" ),
               cMathTex( r" \boldsymbol{\nabla} \times {{ \mathbf{E} }}  = - {{ \mathbf{M} }}  - \mu { \partial {{ \mathbf{H} }}  \over \partial t } " ),
               cMathTex( r" \boldsymbol{\nabla} {{ \mathbf{E} }}  = { \rho \over \epsilon } - I {{ \mathbf{M} }} - I \mu { { \partial {{ \mathbf{H} }} } \over { \partial t } }" ),
               cMathTex( r" \boldsymbol{\nabla} \cdot {{ \mathbf{H} }} = { \rho_{ \mathrm{m} } \over \mu }" ),
               cMathTex( r" \boldsymbol{\nabla} \times {{ \mathbf{H} }} = {{ \mathbf{J} }}  + \epsilon { \partial {{ \mathbf{E} }}  \over \partial t } " ),
               cMathTex( r" \boldsymbol{\nabla} {{ \mathbf{H} }}  = { \rho_{ \mathrm{m} } \over \mu } +  I {{ \mathbf{J} }}  + I \epsilon { \partial {{ \mathbf{E} }}  \over \partial t } " ) ]
        eq[0].shift( 1.50 * UP + 5.25 * LEFT )
        self.play( Write( eq[0] ) )
        self.wait( 5 )

        for i in range(2):
            sh = 1.00 * DOWN
            if i == 0:
                sh += 0.40 * DOWN + 1.60 * LEFT
            if i == 1:
                sh += 0.40 * DOWN + 1.00 * LEFT
            write_aligned( self, eq[i], eq[i+1], sh, None )
            self.wait( 5 )

        i=3
        eq[i].move_to( eq[0] ).shift( 7.25 * RIGHT )
        self.play( Write( eq[i] ) )
        self.wait( 5 )

        for i in range(3,5):
            sh = 1.00 * DOWN
            if i == 3:
                sh += 0.40 * DOWN + 1.60 * LEFT
            if i == 4:
                sh += 0.40 * DOWN + 1.10 * LEFT
            write_aligned( self, eq[i], eq[i+1], sh, None )
            self.wait( 5 )

        eqE = eq[2].copy().move_to( eq[0] ).shift( 1.00 * RIGHT )
        eqH = eq[5].copy().move_to( eq[3] ).shift( 1.00 * RIGHT )

        self.play( ReplacementTransform( VGroup( *eq ), VGroup( eqE, eqH ) ) )
        self.wait( 5 )

        eqD = [ cMathTex( r"[ {{ \mathbf{E} }} / {{ \mathbf{H} }} ] = { V \over m } { m \over A } = \Omega = [ \eta ],\quad \eta = \sqrt{ \mu \over \epsilon }, \quad c = { 1 \over \sqrt{ \mu \epsilon } }" ),
                cMathTex( r"[ {{ \mathbf{E} }} ] = [ \eta {{ \mathbf{H} }} ]" ) ]
        eqD[0].move_to( eqE ).shift( 1.50 * DOWN + 3.5 * RIGHT )
        self.play( Write( eqD[0] ) )
        self.wait( 5 )

        for i in range(1):
            sh = 1.50 * DOWN + 3.00 * RIGHT
            write_aligned( self, eqD[i], eqD[i+1], sh, None )
            self.wait( 5 )

        self.play( FadeOut( VGroup( *eqD ) ) )
        self.wait( 5 )

        eq2 = [ cMathTex( r"= { \rho \over \epsilon } - I {{ \mathbf{M} }} - I \sqrt{ \mu \over \epsilon } \sqrt{ \mu \epsilon } { { \partial {{ \mathbf{H} }} } \over { \partial t } }" ),
                cMathTex( r"= { \rho \over \epsilon } - I {{ \mathbf{M} }} - I {1 \over c } { { \partial (\eta {{ \mathbf{H} }}) } \over { \partial t } }" ),
                cMathTex( r"= { \rho \over \epsilon } - I {{ \mathbf{M} }} - {1 \over c } { { \partial (I \eta {{ \mathbf{H} }}) } \over { \partial t } }" ) ]

        sh = 1.30 * DOWN + 0.00 * LEFT
        write_aligned( self, eqE, eq2[0], sh, None )
        self.wait( 5 )
        #sh = 1.30 * DOWN
        #write_aligned( self, eq2[0], eq2[1], sh, None )
        eq2[1].move_to( eq2[0] ).shift( 0.40 * LEFT )
        self.play( ReplacementTransform( eq2[0], eq2[1] ) )
        self.wait( 5 )
        eq2[2].move_to( eq2[1] ).shift( 0.00 * LEFT )
        self.play( ReplacementTransform( eq2[1], eq2[2] ) )
        self.wait( 5 )

        eq3 = [ cMathTex( r" \boldsymbol{\nabla} (\eta {{ \mathbf{H} }}) = \eta { \rho_{ \mathrm{m} } \over \mu } +  I \eta {{ \mathbf{J} }}  + I \eta \epsilon { \partial {{ \mathbf{E} }}  \over \partial t } " ),
                cMathTex( r"= c \rho_{ \mathrm{m} } +  I \eta {{ \mathbf{J} }}  + I { 1 \over c } { \partial {{ \mathbf{E} }}  \over \partial t } " ),
                cMathTex( r"\boldsymbol{\nabla} (I \eta {{ \mathbf{H} }}) = I c \rho_{ \mathrm{m} } - \eta {{ \mathbf{J} }}  - { 1 \over c } { \partial {{ \mathbf{E} }}  \over \partial t } " ) ]
        eq3[0].move_to( eqH ).shift( 1.30 * DOWN + 0.20 * RIGHT )
        self.play( Write( eq3[0] ) )
        for i in range(2):
            sh = 1.00 * DOWN + 0.00 * RIGHT
            if i == 0:
                sh += 0.20 * DOWN + 0.40 * RIGHT
            if i == 1:
                sh += 0.20 * DOWN + 2.00 * LEFT
            write_aligned( self, eq3[i], eq3[i+1], sh, None )
            self.wait( 5 )

        fadeall( self )

# vim: et sw=4 ts=4
