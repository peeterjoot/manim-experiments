from mycolors import *
import random

class m090_oneparameter( Scene ):
    def construct( self ):

        title = Text( "Fundamental theorem of GC: 1 parameter." )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.play( FadeIn( title ) )
        self.wait( 1 )

        eq = [ cMathTex( r"\int_V F d^1 {{ \mathbf{x} }} {\stackrel{ \leftrightarrow }{ \boldsymbol{\partial} } G = F G {\vert}_{\Delta V}" ) ]
        eq[0].shift( 2 * UP )
        self.play( Write( eq[0] ) )
        self.wait( 1 )

        fadeall( self )

# vim: et sw=4 ts=4
