from mycolors import *

class m030_divcurl( Scene ):
    def construct( self ):

        title = Text( "Maxwell's equation" )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.play( FadeIn( title ) )
        self.wait( 5 )

        eq = [ MathTex( r"\boldsymbol{\nabla} \mathbf{E} + {1 \over c } { { \partial (I \eta \mathbf{H}) } \over { \partial t } } = { \rho \over \epsilon } - I  \mathbf{M}" ),
               MathTex( r"\boldsymbol{\nabla} (I \eta \mathbf{H}) + { 1 \over c } { \partial  \mathbf{E}  \over \partial t } = I c \rho_{ \mathrm{m} } - \eta \mathbf{J}" ) ]
        #eq[0].shift( 1.00 * DOWN )
        self.play( Write( eq[0] ) )
        for i in range(1):
            sh = 1.00 * DOWN + 0.00 * RIGHT
            #if i == 0:
            #    sh += 0.20 * DOWN + 1.70 * RIGHT
            #if i == 1:
            #    sh += 0.20 * DOWN + 2.00 * LEFT
            write_aligned( self, eq[i], eq[i+1], sh, None )
            self.wait( 5 )

        fadeall( self )

# vim: et sw=4 ts=4
