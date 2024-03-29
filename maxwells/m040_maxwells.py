from mycolors import *

class m040_maxwells( Scene ):
    def construct( self ):

        title = Text( "Maxwell's equation" )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.play( FadeIn( title ) )
        self.wait( 1 )

        eq = [ cMathTex( r"\boldsymbol{\nabla} {{ \mathbf{E} }} + {1 \over c } { { \partial (I \eta {{ \mathbf{H} }}) } \over { \partial t } } = { \rho \over \epsilon } - I  {{ \mathbf{M} }}" ),
               cMathTex( r"\boldsymbol{\nabla} (I \eta {{ \mathbf{H} }}) + { 1 \over c } { \partial  {{ \mathbf{E} }}  \over \partial t } = I c \rho_{ \mathrm{m} } - \eta {{ \mathbf{J} }}" ),
               cMathTex( r"\boldsymbol{\nabla} ({{ \mathbf{E} }} + I \eta {{ \mathbf{H} }}) + { 1 \over c } { \partial ({{ \mathbf{E} }} + I \eta {{ \mathbf{H} }}) \over \partial t } = { \rho \over \epsilon } - I  {{ \mathbf{M} }} + I c \rho_{ \mathrm{m} } - \eta {{ \mathbf{J} }}"),
               cMathTex( r"\Bigl( \boldsymbol{\nabla} + { 1 \over c } { \partial \over { \partial t } }\Bigr) ({{ \mathbf{E} }} + I \eta {{ \mathbf{H} }}) = \eta ( c \rho - {{ \mathbf{J} }} ) + I (c \rho_{ \mathrm{m} } - {{ \mathbf{M} }} )" ) ]
        eq[0].shift( 2.00 * UP )
        self.play( Write( eq[0] ) )
        self.wait( 12 )
        for i in range(3):
            sh = 1.00 * DOWN + 0.00 * RIGHT
            if i == 0:
                sh += 0.50 * DOWN + 1.90 * LEFT
            if i == 1:
                sh += 0.70 * DOWN + 5.60 * LEFT
            if i == 2:
                sh += 0.50 * DOWN + 2.20 * LEFT
            write_aligned( self, eq[i], eq[i+1], sh, None )
            self.wait( 12 )

        eq2 = [  cMathTex( r"\Bigl( \boldsymbol{\nabla} + { 1 \over c } { \partial \over { \partial t } }\Bigr) F = J" ),
                 cMathTex( r"F = {{ \mathbf{E} }} + I \eta {{ \mathbf{H} }}" ),
                 cMathTex( r"J = \eta ( c \rho - {{ \mathbf{J} }} ) + I (c \rho_{ \mathrm{m} } - {{ \mathbf{M} }} )" ) ]
        self.play( FadeOut( VGroup( *eq ) ) )
        self.wait( 12 )
        eq2[0].move_to( eq[0] ).shift( 1.00 * DOWN )
        self.play( Write( eq2[0] ) )
        for i in range(2):
            sh = 1.00 * DOWN + 0.00 * RIGHT
            if i == 0:
                sh += 0.50 * DOWN + 0.00 * RIGHT
            write_aligned( self, eq2[i], eq2[i+1], sh, None )
            self.wait( 12 )

        fadeall( self )

# vim: et sw=4 ts=4
