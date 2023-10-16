from mycolors import *

class m050_recover( Scene ):
    def construct( self ):

        title = Text( "Check: Recovering Maxwell's equations" )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.play( FadeIn( title ) )
        self.wait( 5 )

        eq = [  MathTex( r"\Bigl( \boldsymbol{\nabla} + { 1 \over c } { \partial \over { \partial t } }\Bigr) (\mathbf{E} + I \eta \mathbf{H}) = \eta ( c \rho - \mathbf{J} ) + I (c \rho_{ \mathrm{m} } - \mathbf{M} )" ) ]
        eq[0].shift( 2.00 * UP )
        self.play( Write( eq[0] ) )
        self.wait( 5 )

        fadeall( self )

# vim: et sw=4 ts=4
